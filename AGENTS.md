# A4 suspension/steering agent guidance

This branch is a diagnosis corpus. Do not turn an alignment number, a photograph, or a memorized rule into a repair prescription before establishing that the measurement means what you say it means.

## Alignment inference gate

Before recommending an alignment adjustment, answer these questions from evidence:

1. What vehicle, suspension design, and vehicle-specific service procedure apply?
2. Are the tires equivalent in size/application and correctly inflated? Are left/right pressures equal where they should be? Are wear, damage, conicity/lead, and wheel runout still competing causes?
3. Has mechanical looseness or binding been checked at the correct loaded/unloaded condition for this suspension?
4. Is ride height valid at the OEM datum, with the vehicle in the required load state and the suspension settled?
5. What are the elevations of **LF, RF, LR, and RR wheel contact/turn-plate locations**? Do not accept “the floor is level” or one bubble-level reading as a four-corner survey.
6. What are all six pairwise height relationships: LF↔RF, LR↔RR, LF↔LR, RF↔RR, LF↔RR, and RF↔LR? Is there twist/non-coplanarity?
7. Which readings are direct instrument observations, which are reference corrections, and which are derived quantities?
8. Was caster actually measured with a valid steering sweep using the required **actual road-wheel angle for each wheel**, or was a steering-wheel turn/ratio merely assumed?
9. Does the caster procedure use the instrument's required sweep and sign convention? Are the two positions symmetric about the required reference, and were hysteresis and turn-plate freedom controlled?
10. Has every derived result passed the result-integrity gate: arithmetic, input transcription, geometry, vehicle plausibility, and independent cross-check?
11. What does the actual suspension let you adjust, and which other angles move when that adjustment is made?
12. What must be remeasured after the adjustment?

If any prerequisite for a claimed quantity is missing, mark that quantity **UNKNOWN**. Do not fill a gap with a nominal specification, steering ratio, generic alignment lore, or a value from the other side.

## Alignment data vocabulary

Use these labels explicitly:

- **RAW** — a direct observation from a named instrument, image, or measurement, with setup metadata.
- **REFERENCE-CORRECTED** — an arithmetic correction to a reference under stated assumptions. This is not automatically the value the suspension would have on a physically level rack.
- **DERIVED** — a computed quantity whose prerequisites were actually measured and validated.
- **SPEC** — a vehicle/instrument specification from an identified source.
- **UNKNOWN** — unavailable, illegible, unsupported, or invalidated by the setup.

Do not call all five categories “measurements.”

## Result-integrity gate

A numerically calculable result is not automatically a mechanically credible result. Before reporting a derived alignment value as usable, apply `notes/alignment-result-plausibility.md`.

Every result must pass, in order:

1. **Arithmetic consistency** — recompute from preserved raw observations.
2. **Input consistency** — verify decimal point, sign, units, wheel, sweep position/direction, and transcription against the original record.
3. **Geometric consistency** — verify that the formula, actual sweep, reference, and instrument procedure match the physical measurement.
4. **Vehicle plausibility** — compare with exact service information and the scale of the real suspension/adjuster.
5. **Cross-check consistency** — compare with the opposite side, repeat measurements, ride height, toe/thrust, SAI/included angle, or other independent constraints that actually apply.

Use these control states: **IN-SPEC**, **OUT-OF-SPEC / BELIEVABLE**, **SUSPECT**, **INVALID**, **UNKNOWN**.

`SUSPECT`, `INVALID`, and `UNKNOWN` stop adjustment advice. Do not soften them into “very out of spec.”

Preserve every raw observation separately from corrected or derived values. Never overwrite a handwritten/photo reading with an inferred correction. Ambiguous source material remains ambiguous until re-read or remeasured.

For the current Dakota corpus, a result around `+12°` caster is not accepted as an ordinary adjustment value merely because a formula generated it: it is many degrees outside the normal service/adjustment scale and must trigger the failed-result diagnostic tree. A tens-of-degrees result such as `+50°` must be rejected by the absurd-result tripwire.

Run both alignment check scripts after changing equations, examples, thresholds, or result states:

- `python3 scripts/check_alignment_math.py`
- `python3 scripts/check_alignment_plausibility.py`

## Forbidden alignment shortcuts

Do not:

- prescribe an eccentric/cam/tie-rod movement from a photograph before validating the setup;
- omit tire pressure, tire equivalence, ride height, wheel/runout, or mechanical inspection from the validity check;
- infer four-corner level from a level across the hood, frame, bumper, one axle, or one pair of pads;
- use a straight-ahead inclinometer reading as absolute camber when transverse pad slope is unknown;
- insert a straight-ahead camber reading into the branch's two-position caster calculation;
- call the difference of two unsupported caster estimates “cross-caster”;
- convert steering-wheel degrees to individual road-wheel degrees with the nominal steering ratio and treat that as a caster sweep;
- assume both front wheels turned the same angle; toe-out-on-turns/Ackermann and total toe make that unsafe;
- use a memorized caster multiplier such as `1.5` without proving the sweep angle and the instrument convention;
- mix a digital gauge's 15° procedure with a vial gauge's 20° procedure;
- claim physical floor slope “cancels” in caster merely because a constant camber-sensor zero cancels from a symmetric camber-difference formula;
- treat a PSI-to-camber number as universal;
- accept an arithmetically correct result that fails a vehicle-plausibility or cross-check gate;
- infer a bent, worn, or adjustable component until setup error and unstable geometry have been separated from a real angle error;
- replace vehicle-specific adjustment geometry with “always caster first” or “always camber first”;
- finish toe before a coupled caster/camber adjustment is complete;
- quote an OCR-derived specification or a conflicting torque value as settled fact.

## 2005 Dodge Dakota rule

For the 2005 Dakota suspension represented in the current case, the service procedure uses slotted lower-control-arm frame brackets and adjustable front and rear lower-control-arm cam bolts; the upper arm is not the camber/caster adjuster.

Treat the two lower-arm pivots as a coupled adjustment:

- rear-pivot movement changes caster strongly and camber somewhat; a small opposite front-pivot movement is used to preserve camber while changing caster;
- moving front and rear pivots together changes camber strongly and caster somewhat;
- after a meaningful cam movement, settle the suspension and remeasure **both caster and camber**;
- iterate to the vehicle specification;
- set toe last.

That is not a universal front-end sequence. It is the adjustment geometry of this suspension. Verify current service information and the exact vehicle variant before using specifications or torques.

## Source discipline

`sources/alignment-video-audit.md` distinguishes transcript-reviewed spoken material from page/catalog inspection. A title, description, chapter list, search snippet, or neighboring video is not the video's spoken technical content.

If spoken content is unavailable, say it is unavailable and use an inspectable authoritative source for the rule. Never change a source status to “reviewed” just to complete a checklist.

For alignment work, read:

- `notes/alignment-measurement-validity.md`
- `notes/alignment-result-plausibility.md`
- `notes/alignment-measurement-checklist.md`
- `sources/reviewed/alignment-measurement-sources.md`
- `sources/reviewed/alignment-plausibility-sources.md`
- the applicable vehicle service procedure
