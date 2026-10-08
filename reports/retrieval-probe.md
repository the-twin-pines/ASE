# Deterministic retrieval probe

Source head: `7433a551e744b8551a54311951a10ac6344c7115`; initial worktree: CLEAN. Questions SHA256: `9bbb7c87bde0ebd8c8e4c200912bcde9ca0bbdfb86692886d428b12e08d2a3db`.
BM25-style k1=1.2, b=0.75, top3, fixed stopwords, ID ties; no synonym expansion,
model reranking or question-tuned threshold. Approved corpus: 12 passages, 10268 UTF-8
bytes. Total probe time including validation/context writing: 1010.164 ms on this
disposable host, not a phone timing or stable performance guarantee.

Same-author expected-ID overlap: 14/14 in-corpus top3; out-of-corpus abstention
0/1. These are measured retrieval overlaps, not independently adjudicated
answer-quality or safety scores. Questions are not independent/blinded holdouts.

Concrete limits:
H14 out-of-corpus: unrelated hits steering-aeration-noise,steering-ehps-noise,steering-eps-intermittent

45 fixed three-condition contexts are prepared; all raw answers and ratings are
NOT_RUN. Endpoint configured: no. No fixed callable model comparison or independent
review was performed. No wins/regressions or diagnostic-accuracy gain is claimed.

Decision: NO-GO for expansion pending paired model evidence. Model-benefit decision
is BLOCKED, not proof that retrieval cannot help. The original lost-head results
are not reused for this reconstruction. See tests/retrieval-experiment.md.
