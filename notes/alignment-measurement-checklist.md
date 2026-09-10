# Alignment measurement-validity checklist

Use this before giving an adjustment prescription. Blank means unknown; do not silently substitute a nominal value.

The result gate in `alignment-result-plausibility.md` is mandatory. A computed number is not usable until it passes arithmetic, input, geometry, vehicle-plausibility, and cross-check review.

## Vehicle and source

- vehicle / year:
- drivetrain / suspension variant:
- VIN/build information needed to choose specifications:
- service procedure / revision:
- exact specification source and page/table:
- alignment instrument or DIY gauge:
- instrument caster mode and required sweep:
- load / cargo / fuel state:

## Immutable RAW observation ledger

Transcribe what was observed before doing arithmetic. Never overwrite a raw entry with a corrected/inferred value.

| observation id | source artifact / photo / instrument | wheel | position / steering direction | literal signed reading | units | reference / zero | ambiguity / legibility |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | |

Rules:

- keep the original photograph/notebook/instrument record when available;
- preserve decimal points and signs exactly;
- if `0.5` versus `5`, `+` versus `-`, LF/RF, or sweep direction is ambiguous, record the alternatives and mark dependent results **UNKNOWN**;
- corrected values go in a separate derived table and cite the observation ids they came from;
- never choose the transcription that merely makes the result look reasonable.

## Tires, wheels, and mechanical condition

| item | LF | RF | LR | RR |
| --- | --- | --- | --- | --- |
| tire size | | | | |
| tire model / construction / load application | | | | |
| cold pressure | | | | |
| placard/spec pressure | | | | |
| tread / abnormal wear | | | | |
| damage / suspected tire lead | | | | |
| wheel/tire runout checked | | | | |
| wheel-contact / pad elevation | | | | |
| OEM ride-height datum | | | | |

Mechanical inspection:

- wheel bearings:
- ball joints with correct suspension loading:
- tie rods / linkage:
- control-arm bushings:
- steering gear/rack / intermediate shaft:
- binding / memory steer:
- spring/shock/strut:
- brake pull:
- relevant recent repairs:

## Four-corner level survey

Record every pad elevation from the **same datum**.

- `z_LF =`
- `z_RF =`
- `z_LR =`
- `z_RR =`

Calculate all six pairs:

- `RF - LF =` — front transverse
- `RR - LR =` — rear transverse
- `LR - LF =` — left front-to-rear
- `RR - RF =` — right front-to-rear
- `RR - LF =` — LF↔RR diagonal
- `LR - RF =` — RF↔LR diagonal

Then record:

- actual wheel-contact coordinates / track / wheelbase used:
- best-fit/constructed plane:
- fourth-corner residual or other twist check:
- physically shimmed/leveled?:
- uncertainty of height survey:
- suspension rolled/jounced/settled after setup?:
- front turn plates and rear slip plates free / flush?:

Do not replace this section with “floor level,” “hood level,” or one axle-level measurement.

## Straight-ahead RAW readings

Record the reference/zero procedure and whether runout compensation was done.

| quantity | LF | RF | LR | RR |
| --- | --- | --- | --- | --- |
| RAW camber | | | | |
| RAW individual toe | | | | |
| other direct angle | | | | |

- rear total toe:
- rear thrust angle:
- front total toe:
- steering wheel centered/secured:
- gauge/sensor zero reference:
- wheel/runout compensation:
- resolution / repeatability:

If transverse slope is unknown, straight-ahead camber stays **RAW** and must not be called true/level camber. Straight-ahead camber is not an extra input to the branch's two-position caster formula.

## Caster sweep — each front wheel separately

### LF

- instrument/mode:
- prescribed wheel sweep:
- thrust/steer reference:
- first **actual LF road-wheel** angle `T1 =`
- source observation id for `T1`:
- first camber `C1 =`
- source observation id for `C1`:
- second **actual LF road-wheel** angle `T2 =`
- source observation id for `T2`:
- second camber `C2 =`
- source observation id for `C2`:
- symmetric about required reference?:
- both target positions approached from same steering direction?:
- turn plate free?:
- formula/instrument result:
- recomputed result from raw ids:
- status: IN-SPEC / OUT-OF-SPEC-BELIEVABLE / SUSPECT / INVALID / UNKNOWN
- reason:

### RF

- instrument/mode:
- prescribed wheel sweep:
- thrust/steer reference:
- first **actual RF road-wheel** angle `T1 =`
- source observation id for `T1`:
- first camber `C1 =`
- source observation id for `C1`:
- second **actual RF road-wheel** angle `T2 =`
- source observation id for `T2`:
- second camber `C2 =`
- source observation id for `C2`:
- symmetric about required reference?:
- both target positions approached from same steering direction?:
- turn plate free?:
- formula/instrument result:
- recomputed result from raw ids:
- status: IN-SPEC / OUT-OF-SPEC-BELIEVABLE / SUSPECT / INVALID / UNKNOWN
- reason:

A steering-wheel revolution or nominal steering ratio does not fill `T1`/`T2`. The other front wheel's angle does not fill them either.

## Corrected and derived values

For each correction/derivation, write the input observation ids and formula. Derived values never replace raw rows.

| value | class/status | source observation ids | formula / assumption | uncertainty / validity |
| --- | --- | --- | --- | --- |
| | RAW / REFERENCE-CORRECTED / DERIVED / SPEC / UNKNOWN | | | |

## Mandatory result gate

For every value that may influence diagnosis or adjustment, answer all five.

1. **Arithmetic:** recomputed from the raw ids and matches the reported result?
2. **Input:** decimal, sign, units, wheel, sweep direction/position, and transcription verified against the source artifact?
3. **Geometry:** formula, actual road-wheel sweep, reference plane/line, and instrument procedure match what was physically measured?
4. **Vehicle plausibility:** exact vehicle spec identified; magnitude credible for the suspension/adjustment scale?
5. **Cross-check:** opposite side/repeat/cross/ride-height/toe/SAI or other independent constraints do not contradict it?

Final state:

- `IN-SPEC` / `OUT-OF-SPEC-BELIEVABLE` / `SUSPECT` / `INVALID` / `UNKNOWN`
- reason:
- next smallest measurement needed if not usable:

Before using cross-caster:

- LF caster valid and not suspect?:
- RF caster valid and not suspect?:
- same setup/reference?:
- cross-caster sign convention stated?:
- exact cross specification/source verified?:
- if any prerequisite fails: **cross-caster = UNKNOWN/INVALID**, not an adjustment input.

## Failed-result diagnostic tree

If caster is `SUSPECT` or `INVALID`, inspect in this order:

1. original handwritten/raw observations;
2. decimal-place transcription;
3. positive/negative sign;
4. LF/RF wheel assignment;
5. first/second and left-turn/right-turn assignment;
6. inclinometer zero/reference/mode;
7. actual individual road-wheel sweep;
8. degrees of road-wheel angle versus steering-wheel rotation/turns;
9. formula/multiplier/units;
10. wheel movement, scrub, roll, and settling;
11. floor/rack/gravel four-corner geometry;
12. tire pressure, tire equivalence, and tire condition;
13. OEM ride height/load state;
14. looseness, damage, binding, or genuinely abnormal suspension geometry.

## Adjustment plan

This section remains blank until all values used by the plan are usable.

- actual adjustable mechanism on this suspension:
- movement chosen:
- angle primarily targeted:
- other angles expected to change:
- evidence/calibration for predicted response:
- measurements to repeat immediately after movement:
- toe finalized only after coupled geometry is stable?:
- torque source verified for this exact fastener/variant?:

Do not extrapolate an eccentric-position photograph or one previous cam movement into a large predicted angle change unless before/after measurements establish the local response.

## Stop rule

No adjustment prescription when any controlling value is `SUSPECT`, `INVALID`, or `UNKNOWN`, or when a setup uncertainty is large enough to change the diagnosis.

A result several times larger than the vehicle's ordinary service/adjustment scale is a request to audit the measurement, not a request to move the adjuster farther.
