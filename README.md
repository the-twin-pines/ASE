# Automotive diagnosis corpus

This repository exists to make an AI assistant materially better at diagnosing and explaining vehicle problems. It is **not** an ASE test-prep guide for people.

ASE A1–A9 remain useful as broad coverage buckets because they give the corpus a familiar automotive taxonomy. Problem-, component-, and symptom-focused branches are equally important when they are better retrieval keys.

## ASE coverage buckets

- [A1 — Engine Repair](https://github.com/isomorphisms/ASE/tree/a1-engine-repair)
- [A2 — Automatic Transmission/Transaxle](https://github.com/isomorphisms/ASE/tree/a2-automatic-transmission-transaxle)
- [A3 — Manual Drivetrain & Axles](https://github.com/isomorphisms/ASE/tree/a3-manual-drivetrain-axles)
- [A4 — Suspension & Steering](https://github.com/isomorphisms/ASE/tree/a4-suspension-steering)
- [A5 — Brakes](https://github.com/isomorphisms/ASE/tree/a5-brakes)
- [A6 — Electrical/Electronic Systems](https://github.com/isomorphisms/ASE/tree/a6-electrical-electronic-systems)
- [A7 — Heating & Air Conditioning](https://github.com/isomorphisms/ASE/tree/a7-heating-air-conditioning)
- [A8 — Engine Performance](https://github.com/isomorphisms/ASE/tree/a8-engine-performance)
- [A9 — Light Vehicle Diesel Engines](https://github.com/isomorphisms/ASE/tree/a9-light-vehicle-diesel-engines)

## Problem and component retrieval branches

- [Large EVAP leak](https://github.com/isomorphisms/ASE/tree/large-evap-leak) — EVAP system operation, leak diagnosis, purge/vent valves, filler-neck faults
- [Engine sensors](https://github.com/isomorphisms/ASE/tree/engine-sensors) — crankshaft position, MAF, TPS, MAP, ECU communication, and CAN diagnosis

## What belongs in the corpus

The valuable unit is not a link. Prefer a chain like:

`source → transcript/captions → source-grounded summary → diagnostic lessons → reusable failure pattern`

For a diagnostic source, preserve especially:

- complaint and repair history;
- measurements and observations in the order they occurred;
- what each observation establishes and what it does not establish;
- the next discriminating test and why it was chosen;
- confirmed fault versus suspicion;
- repair and post-repair verification when available;
- lessons that transfer to a different vehicle without pretending all systems are identical.

Keep full transcripts or captions when obtainable and appropriate to store. Summaries and lessons are derived artifacts, not replacements for source review.

Raw URL/title/playlist metadata may be kept for acquisition, but it is low-maturity material and must never be presented as though the source itself was reviewed.

<!-- atomic-video-sources:start -->
## Atomic video sources

Canonical video records live in [`sources/videos/`](sources/videos/), one file per platform video ID. Playlist order and duplicates live separately in [`sources/playlists/`](sources/playlists/). Title-grouped import notes are legacy acquisition material, not reviewed source evidence.

Current imported corpus:

- A1 Engine Repair: 26 unique videos from 26 playlist positions;
- Brakes: 169 unique videos from 175 playlist positions;
- individual source passes complete: 0;
- playlist/series synthesis: blocked.

See [`SOURCE_ARCHITECTURE.md`](SOURCE_ARCHITECTURE.md) and run `python3 check_sources.py` before committing source changes.
<!-- atomic-video-sources:end -->

## Tests

- [`tests/`](https://github.com/isomorphisms/ASE/tree/main/tests) — a lightweight place to preserve an occasional before/after check when one is worth keeping.

`tests/` is not a training gym or benchmark project and must be excluded from retrieval indexes.

## Working rule

Optimize for the questions a mechanic, owner, or technician might actually ask an assistant: *What does this measurement rule out? What should I test next? Why did the new part not fix it? Is this electrical, hydraulic, mechanical, control-side, or load-side?*

Generic prose that does not improve those answers is low value. Concrete source-backed diagnostic traces are high value.
