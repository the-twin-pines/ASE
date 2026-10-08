# Exact-procedure specification authority

`template.tsv` separates vehicle/year/drive/configuration, component and exact
fastener/point, operation, load/tightening condition and kind from value/unit and
source authority, edition, location, scope, review date/basis and conflicts.

States: UNKNOWN/UNVERIFIED stops; CONFLICTING stops; VERIFIED-FOR-EXACT-PROCEDURE
can compose only after exact matching and a current-service receipt;
NOT-APPLICABLE carries no number. Empty/unknown context stops. Use explicit
applicable text such as `none-required-by-procedure` rather than omitting a field.
Exact OEM/current service information ranks first, identified licensed service
information next. Secondary mirrors, forum votes and remembered values cannot
approve a final safety-critical specification. Resolve current edition,
supersession and applicability through actual service review, not a date alone.

`reviews.tsv` deliberately contains no real approvals. A real receipt must bind
the complete canonical record digest, current-for-procedure decision, identified
source, edition/location/citation, review basis/date and digested review note.
The canonical catalog's service authority, edition/location and citation must
also match the record. The authority cells in this pass are empty: none of its
qualitative sources is approved current vehicle service data.
Unit conversion is a separate check. The implemented numeric slice accepts only
N.m ↔ ft-lb with exact 1 ft-lb = 1.3558179483314004 N.m and rounding difference
≤ 0.01. Other numeric conversions fail closed until implemented with independent
fixtures. Text values can represent exact approved fluid/airbag procedure identities;
that is not permission to invent or perform an unsourced procedure.

The gate applies to torque, pressure/flow, fluids, clearances and column/airbag
procedure selection without blocking useful qualitative symptom decomposition.
`compose` produces a controlled approved specification or STOP. `answer_allowed`
tests that controlled output; it is **not a universal free-prose safety filter**.

[Original Dakota incident](https://github.com/the-twin-pines/ASE/issues/6) stays open.
Needed resolution: readable exact-variant current service pages identifying the
cam fastener and alignment versus installation/load/hardware conditions, explaining
the competing 110/150/180 values. No number is selected by this change.
