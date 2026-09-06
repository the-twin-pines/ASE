# Source architecture

The atomic unit is one source, not one playlist and not one topic note.

## Canonical layout

- `sources/videos/youtube-<video-id>.md` — one canonical record per YouTube video.
- `sources/playlists/youtube-<playlist-id>.md` — membership, order, duplicate positions, and review progress only.
- `brakes/` and `engine-repair/` — coverage maps, cases, checked references, and eventual synthesis; they do not own duplicate copies of video records.
- `_legacy/title-grouping/` — preserved title-based grouping from the initial import. It is excluded from source evidence and synthesis.

## Required video pass

A video record begins as `metadata-only`. That state may contain title, channel, duration, URL, playlist position, and tentative topic hints, but no claims about what the video says.

A record can become `transcript-reviewed` only after a complete transcript or caption pass. It can become `video-reviewed` only after a pass over the audiovisual source. A partial clip, search snippet, title, description, chapter list, or another person's summary is not a complete pass.

An individual-pass summary should preserve:

1. what the source actually demonstrates or argues;
2. complaint, conditions, measurements, and observations in order when the source is diagnostic;
3. what each observation establishes and what it does not;
4. the discriminating tests and why they were chosen;
5. confirmed fault, repair, and post-repair verification when present;
6. vehicle-specific limits, questionable claims, and facts requiring service-information checks.

## Synthesis gate

Playlist, series, channel, and topic synthesis is blocked while any relevant member is `metadata-only`, `partial`, or still awaiting a relevance decision. Synthesis must link back to the individual records it combines. It may resolve disagreements between sources, but it may not erase them.

Run `python3 check_sources.py` before committing source changes.
