# Source identity, review and retrieval

sources/videos owns 195 canonical atomic video IDs; playlist manifests own their
positions. The unchanged check_sources.py checks topology and blocks playlist-
wide synthesis. A5 partial review notes retain their cited identities and original
states; they are neither additional reviewed video records nor indexed evidence.

catalog.tsv is explicit eligibility. acquisitions.tsv records a separate pinned
pass: 26 A1 targets, 14 captions acquired, 12 unavailable, reviewed=false. No raw
captions/bootstrap chunks are copied. Title material stays in _legacy/.

Only individually inspected page/scoped-extract/transcript/video states with
eligible=true, matching receipts and digests can support approved passages. The
2026-10-08 pass admitted ten document/incident/historical-note scopes and twelve
passages. The 2026-10-12 HVAC/wheel pass adds four scopes and seven passages:
fourteen admitted scopes and nineteen passages at that stage. A7 branch notes are
preserved in hvac/history; their original review states remain historical.
The subsequent A1 pass reviews fourteen stored caption tracks: thirteen full-
acquired-text passes and one partial pass. Twelve videos are explicitly eligible;
the transmission-support demonstration and partial engine-size track are excluded.
Two maker-text scopes and thirteen new passages bring totals to twenty-eight
admitted scopes and thirty-two passages. Partial/metadata-only sources remain
ineligible. A reviewed companion document does not upgrade a video.

reviews.tsv binds ID, local reviewed-artifact digest, scope, edition, location,
citation, date/basis and digested review note. Digests bind local paraphrase and
attestation bytes, not immutable remote webpage snapshots. passages.tsv binds
approved source IDs, content digest, status/scope and citations. Reading an old
review note is not a new video replay. Review is an attestation, not cryptographic
proof of reading; an editor of data and receipts can forge it. Review is still needed.

Retrieval validates atomic topology plus admission and indexes only listed
passages. tests/, _legacy/, _work/, examples/, reports/, .git/ and _ithon/ are
excluded, including resolved symlink targets and outside-root paths. Verification
is read-only. admit.pi is explicit author attestation after inspection, not an
ingestion/review algorithm. reconcile.pi is a one-time pinned import, not a service.

Specification approval is separate: exact procedure/context, current OEM/licensed
authority and receipt, no conflict and independent unit check. Real approvals are
empty. Qualitative source approval supplies no service numbers. Controlled answer
composition is not a general free-prose safety filter. See specifications/README.md.

The admissions.tsv inputs and admit.pi describe the pinned 2026-10-08 one-time
attestation. They are not a current ingestion service: running that old writer
would replace later receipts/passages. The 2026-10-12 pass explicitly appends to
catalog.tsv, reviews.tsv and passages.tsv after inspection, preserving older
receipts. Validation and retrieval remain read-only. New component-maker extracts
are qualitative guidance; no OEM/current-service authority is assigned to them.

For canonical videos, catalog status must equal the record's metadata status.
transcript-reviews.tsv binds per-ID reading to the pinned acquisition object and
artifact/caption digests, language, generation metadata and review note. The
validator reads archived captions only for provenance; raw text never enters the
index. Caption digests include one appended LF after UTF-8 encoding of stored text.
Unknown timed coverage cannot be relabeled complete; playlist synthesis remains
blocked. The unchanged atomic validator still owns membership/metadata checks.
