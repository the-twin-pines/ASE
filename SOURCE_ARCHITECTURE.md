# Source identity, review and retrieval

sources/videos owns 195 canonical atomic video IDs; playlist manifests own their
positions. The unchanged check_sources.py checks topology and blocks playlist-
wide synthesis. A5 partial review notes retain their cited identities and original
states; they are neither additional reviewed video records nor indexed evidence.

catalog.tsv is explicit eligibility. acquisitions.tsv records a separate pinned
pass: 26 A1 targets, 14 captions acquired, 12 unavailable, reviewed=false. No raw
captions/bootstrap chunks are copied. Title material stays in _legacy/.

Only individually inspected page/scoped-extract/transcript/video states with
eligible=true, matching receipts and digests can support approved passages. This
pass admits ten document/incident/historical-note scopes and twelve passages.
No video is upgraded. Future video admission requires actual review and a deliberate
validator change. Partial/metadata-only sources remain ineligible. A reviewed
companion document does not upgrade a video.

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
