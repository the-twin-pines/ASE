# Alignment measurement-validity checklist

Use this before giving an adjustment prescription. Blank means unknown; do not silently substitute a nominal value.

## Vehicle and source

- vehicle / year:
- drivetrain / suspension variant:
- VIN/build information needed to choose specifications:
- service procedure / revision:
- alignment instrument or DIY gauge:
- instrument caster mode and required sweep:
- load / cargo / fuel state:

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

If transverse slope is unknown, straight-ahead camber stays **RAW** and must not be called true/level camber.

## Caster sweep — each front wheel separately

### LF

- instrument/mode:
- prescribed wheel sweep:
- thrust/steer reference:
- first **actual LF road-wheel** angle `T1 =`
- first camber `C1 =`
- second **actual LF road-wheel** angle `T2 =`
- second camber `C2 =`
- symmetric about required reference?:
- both target positions approached from same steering direction?:
- turn plate free?:
- formula/instrument result:
- status: RAW / DERIVED / UNKNOWN
- reason:

### RF

- instrument/mode:
- prescribed wheel sweep:
- thrust/steer reference:
- first **actual RF road-wheel** angle `T1 =`
- first camber `C1 =`
- second **actual RF road-wheel** angle `T2 =`
- second camber `C2 =`
- symmetric about required reference?:
- both target positions approached from same steering direction?:
- turn plate free?:
- formula/instrument result:
- status: RAW / DERIVED / UNKNOWN
- reason:

A steering-wheel revolution or nominal steering ratio does not fill `T1`/`T2`. The other front wheel's angle does not fill them either.

## Corrected and derived values

For each correction/derivation, write the input values and formula.

| value | class | inputs | formula / assumption | uncertainty / validity |
| --- | --- | --- | --- | --- |
| | RAW / REFERENCE-CORRECTED / DERIVED / SPEC / UNKNOWN | | | |

Before using cross-caster:

- LF caster valid?:
- RF caster valid?:
- same setup/reference?:
- cross-caster sign convention stated?:
- if any answer is no: **cross-caster = UNKNOWN**.

## Adjustment plan

- actual adjustable mechanism on this suspension:
- movement chosen:
- angle primarily targeted:
- other angles expected to change:
- measurements to repeat immediately after movement:
- toe finalized only after coupled geometry is stable?:
- torque source verified for this exact fastener/variant?:

## Stop rule

No adjustment prescription if the answer depends on an unknown setup variable that is large enough to change the diagnosis. Report what is **RAW**, what can be **REFERENCE-CORRECTED**, what can be **DERIVED**, and what remains **UNKNOWN**, then ask for the smallest missing measurement that resolves it.
