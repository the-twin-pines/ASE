#!/usr/bin/env python3
"""Validate ASE atomic video records and playlist synthesis gates."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VIDEOS = ROOT / "sources" / "videos"
PLAYLISTS = ROOT / "sources" / "playlists"
REVIEWED = {"transcript-reviewed", "video-reviewed"}
PLACEHOLDER = "Not yet written. This record currently contains playlist metadata only."


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def metadata_from_record(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"## Source metadata\s*```json\s*(\{.*?\})\s*```", text, re.S)
    if not match:
        raise ValueError("missing JSON source metadata block")
    return json.loads(match.group(1)), text


def summary_from_record(text: str) -> str:
    match = re.search(r"## Individual-pass summary\s*(.*?)(?=\n## |\Z)", text, re.S)
    return match.group(1).strip() if match else ""


def main() -> int:
    errors: list[str] = []
    records: dict[str, tuple[Path, dict, str]] = {}

    for path in sorted(VIDEOS.glob("youtube-*.md")):
        try:
            metadata, text = metadata_from_record(path)
        except Exception as exc:
            fail(f"{path.relative_to(ROOT)}: {exc}", errors)
            continue
        video_id = metadata.get("video_id")
        expected_name = f"youtube-{video_id}.md"
        if path.name != expected_name:
            fail(f"{path.relative_to(ROOT)}: filename should be {expected_name}", errors)
        if metadata.get("source_kind") != "video" or metadata.get("platform") != "youtube":
            fail(f"{path.relative_to(ROOT)}: bad source_kind/platform", errors)
        if metadata.get("url") != f"https://www.youtube.com/watch?v={video_id}":
            fail(f"{path.relative_to(ROOT)}: URL does not match video ID", errors)
        if video_id in records:
            fail(f"duplicate canonical record for YouTube ID {video_id}", errors)
        records[video_id] = (path, metadata, text)

        status = metadata.get("review_status")
        if status in REVIEWED:
            summary = summary_from_record(text)
            if not metadata.get("review_basis") or not metadata.get("reviewed_at"):
                fail(f"{path.relative_to(ROOT)}: reviewed record lacks basis/date", errors)
            if not summary or PLACEHOLDER in summary:
                fail(f"{path.relative_to(ROOT)}: reviewed record lacks individual-pass summary", errors)
        elif status == "metadata-only":
            if PLACEHOLDER not in text:
                fail(f"{path.relative_to(ROOT)}: metadata-only record lost its warning", errors)
        elif status == "partial":
            if not metadata.get("review_basis"):
                fail(f"{path.relative_to(ROOT)}: partial record lacks review_basis", errors)
        else:
            fail(f"{path.relative_to(ROOT)}: unknown review_status {status!r}", errors)

    manifest_video_ids: set[str] = set()
    blocked_coverages: set[str] = set()
    for path in sorted(PLAYLISTS.glob("youtube-*.json")):
        manifest = json.loads(path.read_text(encoding="utf-8"))
        entries = manifest.get("entries", [])
        declared_unique = manifest["snapshot"]["unique_video_count"]
        if declared_unique != len(entries):
            fail(f"{path.relative_to(ROOT)}: unique count mismatch", errors)

        declared_positions = manifest["snapshot"]["entry_count"]
        positions = [position for entry in entries for position in entry["positions"]]
        if sorted(positions) != list(range(1, declared_positions + 1)):
            fail(f"{path.relative_to(ROOT)}: positions are missing or duplicated incorrectly", errors)

        for entry in entries:
            video_id = entry["video_id"]
            manifest_video_ids.add(video_id)
            if video_id not in records:
                fail(f"{path.relative_to(ROOT)}: missing atomic record {video_id}", errors)
                continue
            _, metadata, _ = records[video_id]
            memberships = metadata.get("playlist_memberships", [])
            matching = [item for item in memberships if item.get("playlist_id") == manifest["playlist_id"]]
            if len(matching) != 1 or matching[0].get("positions") != entry["positions"]:
                fail(f"{video_id}: playlist membership/positions disagree with manifest", errors)
            for field in ("title", "channel", "duration", "relevance_status"):
                if metadata.get(field) != entry.get(field):
                    fail(f"{video_id}: {field} disagrees with playlist manifest", errors)
            if metadata.get("coverage") != [entry.get("coverage")]:
                fail(f"{video_id}: coverage disagrees with playlist manifest", errors)
            if metadata.get("title_based_topic_hints") != entry.get("title_based_topic_hints"):
                fail(f"{video_id}: title-based topic hints disagree with playlist manifest", errors)
            if metadata.get("review_status") not in REVIEWED or metadata.get("relevance_status") == "boundary-review":
                blocked_coverages.update(metadata.get("coverage", []))

    missing_from_manifests = set(records) - manifest_video_ids
    if missing_from_manifests:
        fail(f"atomic records missing from playlist manifests: {sorted(missing_from_manifests)}", errors)

    for stale in (ROOT / "brakes" / "sources" / "notes", ROOT / "engine-repair" / "sources" / "notes"):
        if stale.exists() and any(stale.glob("*.md")):
            fail(f"{stale.relative_to(ROOT)}: title-grouped notes remain in the active source tree", errors)

    for coverage in sorted(blocked_coverages):
        synthesis = ROOT / coverage.replace("a1-", "") / "synthesis" / "README.md"
        if coverage == "a1-engine-repair":
            synthesis = ROOT / "engine-repair" / "synthesis" / "README.md"
        elif coverage == "brakes":
            synthesis = ROOT / "brakes" / "synthesis" / "README.md"
        if not synthesis.exists() or "status: blocked" not in synthesis.read_text(encoding="utf-8"):
            fail(f"{coverage}: synthesis must remain blocked", errors)

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        print(f"FAIL: {len(errors)} error(s)")
        return 1

    status_counts: dict[str, int] = {}
    for _, metadata, _ in records.values():
        status = metadata.get("review_status", "missing")
        status_counts[status] = status_counts.get(status, 0) + 1
    rendered = ", ".join(f"{key}={value}" for key, value in sorted(status_counts.items()))
    print(f"PASS: {len(records)} canonical video records; {rendered}; playlist positions complete; synthesis gates enforced")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
