# 2005 Dakota alignment case — current evidence

Case review date: 2026-09-10

This applies `alignment-measurement-validity.md` to the truck measurements recovered from the current working context and the photographed notebook. It deliberately does not fill missing measurements.

## Evidence presently available

- Vehicle: 2005 Dodge Dakota.
- Tire pressure: the owner reports the pressures were checked equal. Exact cold PSI and placard comparison are not preserved in the notebook image.
- Handwritten notebook: a straight-ahead row is legible as approximately:
  - driver/LF: `-1/4°` (`-0.25°`);
  - passenger/RF: `+1°` (`+1.0°`).
- The notebook also contains left/right-steered inclinometer readings, but some handwritten numerals are not clear enough to promote into exact repository data.
- The steering input used in the discussion was one full steering-wheel revolution from center. Actual individual LF and RF road-wheel steering angles were not measured/recorded.
- A nominal 2005 Dakota overall steering ratio of `17.4:1` was found in Chrysler product specifications. `360° / 17.4 ≈ 20.69°` is therefore a nominal steering-ratio calculation, **not a measured wheel angle**.
- Exact LF/RF/LR/RR wheel-pad elevations have not been recovered.
- A level placed across the truck body/hood does not establish the four contact patches are coplanar and does not provide a pad correction.
- OEM ride-height measurements at the spindle/lower-control-arm-pivot datums have not been recovered.

## Classification

### Directly supported / RAW

- equal tire pressure was checked, according to the owner;
- LF straight-ahead inclinometer reading: about `-0.25°`;
- RF straight-ahead inclinometer reading: about `+1.0°`;
- the raw straight-ahead difference, defining cross here as `LF - RF`, is therefore about `-1.25°`;
- left/right-steered inclinometer observations were taken;
- steering-wheel input was one full revolution.

The `-1.25°` difference is a **RAW difference**, not yet true cross-camber.

### REFERENCE-CORRECTED

None.

No common-datum wheel-pad elevations are available, so a transverse floor/reference correction cannot be calculated. Even if a simple slope were known, it would be labeled a rigid-body reference correction rather than a guaranteed level-rack suspension result.

### DERIVED

None for caster.

The available sweep does not record the actual individual road-wheel angles required by the caster derivation. The nominal steering ratio does not repair that missing input, because LF and RF road-wheel angles can differ through toe-out-on-turns/Ackermann and total toe, and the actual instrument procedure/sweep angle also matters.

Therefore:

- LF caster = **UNKNOWN**
- RF caster = **UNKNOWN**
- cross-caster = **UNKNOWN**

A subtraction of two estimates made from the same unvalidated steering-wheel-turn assumption would still be an unsupported cross-caster.

### Other UNKNOWN quantities that matter

- true/level LF camber;
- true/level RF camber;
- true cross-camber;
- all four pad elevations and setup twist;
- front/rear/diagonal level relationships;
- OEM ride-height values;
- actual LF and RF road-wheel sweep angles;
- rear toe/thrust reference;
- wheel/runout compensation;
- exact installed tire size/model equivalence and placard PSI in the preserved case evidence;
- current vehicle-specific caster/camber specifications for the exact variant.

## What equal tire pressure does and does not establish

Equal pressure removes one obvious left/right setup asymmetry from the present diagnosis. It does not prove equal loaded radius if tire size/construction/wear/load differ, and it does not establish the floor/pads are level.

The general procedure still must ask about pressure before diagnosis; the fact that the owner already checked it means it should now be marked checked, not repeatedly proposed as the cause.

## Plausible cause classes still open

Because the measurement reference is incomplete, preserve these as hypotheses rather than diagnoses:

- real lower-control-arm cam position/alignment error;
- ride-height or load asymmetry;
- tire/wheel loaded-radius or construction differences other than pressure;
- loose/bound control-arm, ball-joint, tie-rod, bearing, rack/steering or suspension geometry;
- bent/shifted suspension or mounting structure;
- nonlevel/twisted measurement surface contaminating the raw straight readings.

No component is justified as “the” cause from the current notebook alone.

## Smallest measurements needed next

1. Record LF/RF/LR/RR pad elevations from one common datum, including all six pairwise differences.
2. Verify installed tire size/model/application at all four corners and exact cold placard pressure; pressure equality itself is already checked.
3. Measure 2005 Dakota ride height by the service-manual spindle/lower-control-arm-pivot method on both sides.
4. Roll/jounce/settle the truck on free turn/slip surfaces.
5. Repeat straight-ahead camber with the gauge reference documented.
6. For caster, measure **actual LF and actual RF road-wheel angles independently** at the instrument-prescribed symmetric sweep and record camber at each position. Do not substitute one steering-wheel revolution.
7. Record rear toe/thrust or otherwise state the reference used by the caster/toe method.

Only then can the raw camber be corrected/qualified, individual caster be derived, and cross-caster become a meaningful quantity.

## Adjustment justified now

None.

The 2005 Dakota does have real caster/camber adjustment at the lower-control-arm cams, but adjustability is not evidence that the current raw readings are valid enough to prescribe cam movement.

Once valid values exist, use the Dakota's coupled geometry:

- rear-pivot movement primarily for caster, with compensating opposite front-pivot movement when maintaining camber;
- both pivots together primarily for camber;
- settle and remeasure both caster and camber after meaningful movement;
- iterate;
- toe last.

The accessible service-manual sources disagree on a lower-control-arm fastener torque (`203 N·m / 150 ft-lb` in the alignment-adjustment text versus `244 N·m / 180 ft-lb` in another torque/installation context). Do not resolve that by guessing.
