# Alignment plausibility sources

Review date: 2026-09-10

This file records the sources used specifically for the physical-plausibility repair. It supplements `alignment-measurement-sources.md`.

## 2005 Dodge Dakota service manual — wheel alignment

Inspectable HTML mirror:

- https://manualmachine.com/dodge/dakota2005/3868971-workshop-manual/

Corroborating public manual extraction:

- https://www.scribd.com/document/393774961/Dodge-Dakota-2005-Service-Repair-Manual-FREE-PDF-DOWNLOAD

Status: **2005 service-manual alignment procedure/table inspected through public mirrors.**

Useful facts:

- suspension height is measured before alignment;
- tires/pressure, looseness/binding, runout, suspension condition, ride-height variation, and road behavior belong in pre-alignment inspection;
- front camber/caster are adjusted at the slotted lower-control-arm frame brackets using both front and rear cam bolts;
- rear-pivot movement strongly changes caster and slightly changes camber;
- common front/rear pivot movement strongly changes camber and slightly changes caster;
- toe is final;
- the 131-inch-wheelbase 2005 alignment table renders nominal caster as `3.5°` in the accessible text.

### Specification-table caution

The same text extraction renders the caster tolerance as `± .05°`. That may be an exact table value or a formatting/OCR defect; it is unusual enough that this repair does **not** hard-code it as the pass/fail service envelope. `IN-SPEC` classification therefore requires the exact-variant specification to be verified from an authoritative readable table before use.

This caution is deliberate: a plausibility guardrail must not cure one transcription failure by institutionalizing another.

## SAE 850219 — Steering Geometry and Caster Measurement

Official metadata:

- https://saemobilus.sae.org/papers/steering-geometry-caster-measurement-850219

Inspectible reprint:

- https://studylib.net/doc/8280217/steering-geometry-and-caster-measurement

Author: Daniel B. January, Hunter Engineering Co., 1985.

Status: **derivation and practical procedure inspected; official SAE metadata cross-checked.**

Useful results:

- caster is inferred from camber at two road-wheel steer/toe positions;
- the simplified method restricts the two positions to a symmetric sweep about the thrust line (`T2 = -T1`);
- the practical procedure requires the actual toe/steer angles for the wheel being calculated;
- the other front wheel cannot be assumed to have the same symmetric turn because toe-out-on-turns/Ackermann and total toe change the relationship;
- hysteresis matters; approaching the measurement positions consistently reduces it;
- constant camber-sensor zero can cancel from the difference, but that is not a statement that physical rack/floor slope cancels.

The branch uses the symmetric approximation:

`K ≈ atan((sin(C1) - sin(C2)) / (sin(T2) - sin(T1)))`.

## Longacre digital caster/camber procedure

Current manufacturer instructions:

- https://longacreracing.com/pages/digital-caster-camber-gauge-with-acculevel%E2%84%A2-and-quickset%E2%84%A2-adapter
- https://longacreracing.com/pages/digital-caster-camber-gauge-with-acculevel%E2%84%A2

Status: **manufacturer HTML instructions inspected.**

Useful facts:

- the digital procedure uses an exact `15°` road-wheel turn one way and `15°` the other (`30°` total);
- the manufacturer warns that a `1°` or `2°` turn error causes caster error;
- its vial gauges use a different `20°` procedure;
- unlevel ground affects accuracy;
- after caster/camber change, bounce/settle and recheck because the adjustments interact.

Use: instrument procedure controls the sweep. There is no universal multiplier.

## Dakota lower-control-arm adjustment scale

Specialty Products Company part 82400 as published by NAPA:

- https://www.napaonline.com/en/p/SAP82400

Corroborating current fitment pages:

- https://www.tirerack.com/suspension/results.jsp?autoMake=Dodge&autoModel=Dakota+Quad+Cab+4wd&autoYear=2005
- https://www.suspension.com/spc-82400

Status: **current product/fitment descriptions inspected.**

The 82400 kit replaces the OE lower-control-arm cams on 2005-11 Dakota applications and publishes approximately `±2°` camber/caster change.

Use: `±2°` is an *ordinary adjustment-scale plausibility reference*, not an OEM alignment specification. A calculated Dakota caster many degrees beyond the verified service envelope should be remeasured before it is interpreted as an eccentric adjustment problem.

## Why the branch does not convert steering-wheel turns to road-wheel angle

The branch's existing Chrysler 2005 Dakota product-specification source records a published overall steering ratio around `17.4:1` and about `3.18` turns lock-to-lock. Those are steering-system descriptors, not measurements of either front road wheel at a caster sweep position.

SAE 850219 supplies the decisive geometric reason: caster calculation depends on each wheel's actual turn angles, and the two front wheels differ through toe-out-on-turns/Ackermann and total toe. Linkage/compliance and effective ratio across travel add more uncertainty. Therefore `360° / 17.4` is not accepted as `T1` or `T2`.
