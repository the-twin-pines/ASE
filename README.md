# A4 — suspension and steering

This branch is part of the automotive diagnosis corpus. It is not an ASE study guide.

The useful material here should make an assistant better at answering real suspension and steering questions: noises over bumps, looseness, pull/wander, tire wear, poor return-to-center, wheel-bearing noise, ride-height problems, alignment geometry, and deciding which joint or component to inspect next.

## Current reviewed material

- `sources/reviewed/1a-auto-front-end-diagnosis.md` — transcript-reviewed videos covering ball-joint play, tie-rod play, wheel-bearing play/noise, sway-bar links, and shocks/struts.
- `sources/reviewed/1a-auto-tires-alignment.md` — full transcript review of the 1A Auto tire video, including tire-pull and four-wheel-measurement material.
- `sources/reviewed/alignment-measurement-sources.md` — inspected ASE, Dakota service, SAE caster, instrument, rack-setup, and tire-stiffness sources with source-status boundaries.
- `sources/reviewed/alignment-plausibility-sources.md` — sources used for the explicit result-integrity repair, including the 2005 Dakota alignment procedure/table, SAE caster geometry, Longacre sweep requirements, and the Dakota lower-control-arm adjustment scale.
- `notes/front-end-diagnostic-patterns.md` — reusable front-end diagnostic lessons.
- `notes/alignment-diagnostic-patterns.md` — pull/SAI/thrust/bump-steer/memory-steer interpretation after the measurement gate; no generic camber/caster ordering rule.
- `notes/alignment-measurement-validity.md` — validity-first alignment procedure, four-corner level model, caster derivation, quantitative tire-pressure sensitivity, and Dakota coupled adjustment geometry.
- `notes/alignment-result-plausibility.md` — mandatory arithmetic/input/geometry/vehicle/cross-check gate, failed-result diagnostic tree, sweep uncertainty, and deliberate bad-data regression examples.
- `notes/alignment-measurement-checklist.md` — field worksheet that preserves immutable raw observations and forces every derived value through the result-integrity gate.
- `notes/dakota-alignment-case.md` — application of the repaired method to the currently recovered 2005 Dakota notebook data without manufacturing caster/cross-caster.
- `sources/alignment-video-audit.md` — accounting of every old branch video target plus the Hunter alignment catalogs found during the audit.
- `sources/cross-checks.md` — source hierarchy and cross-checks that keep generic demonstrations from becoming universal rules.
- `AGENTS.md` — alignment inference gate and diagnostic anti-patterns.
- `scripts/check_alignment_math.py` — reproducible checks for the geometry and tire-pressure sensitivity numbers used in the notes.
- `scripts/check_alignment_plausibility.py` — regression checks proving decimal, sign, direction, sweep, missing-spec, and absurd-result failures stop before adjustment advice.

## Acquisition queue

- `sources/video-queue.md` — OldSchoolNoe, Hunter, and other suspension/steering videos whose spoken material still needs acquisition. Video-page inspection is kept separate from transcript/spoken-content review.

## Working rules

A wheel that moves when shaken is not yet a diagnosis. Watch the relevant parts while the load is applied and identify the **relative motion**: knuckle versus control arm, tie-rod stud/socket versus knuckle, rotor/hub versus knuckle, and so on.

An alignment number is also not yet a diagnosis. Before an adjustment prescription, establish tire/wheel condition and pressure, stable mechanical geometry, OEM ride height, four wheel-contact elevations, gauge/runout/turn-plate references, and the validity of every derived quantity.

A derived angle must also be mechanically credible. Recompute it from preserved raw observations, audit decimal/sign/wheel/direction/units, prove the geometry and actual road-wheel sweep, compare with exact service data and the vehicle's adjustment scale, then cross-check it. `SUSPECT`, `INVALID`, or `UNKNOWN` results do not become adjustment inputs.

Do not call a straight-ahead inclinometer reading “true camber” on an unknown transverse slope. Do not call anything “cross-caster” unless both individual caster values came from valid per-wheel sweeps and passed the plausibility gate.

Do not hard-code a generic caster-versus-camber order. On the 2005 Dakota represented by the current case, both lower-control-arm pivots participate in a **coupled** caster/camber adjustment: rear-pivot motion is primarily a caster control, common front/rear motion is primarily a camber control, both angles must be remeasured as the cams are iterated, and toe is final.
