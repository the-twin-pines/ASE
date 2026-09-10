# Alignment diagnostic patterns

Use this file only **after** the measurement-validity gate in `alignment-measurement-validity.md` and the result-integrity gate in `alignment-result-plausibility.md`.

An alignment display is evidence about geometry under a particular setup. It is not, by itself, evidence that an adjuster should be moved or that a particular component is bent/worn.

## Numeric plausibility is part of diagnosis

Do not interpret every formula output as an angle the vehicle actually has.

Before any diagnostic use:

1. recompute from preserved raw observations;
2. verify decimal/sign/units/wheel/position against the source record;
3. prove the formula and reference match the physical measurement;
4. compare with exact vehicle specifications and the scale of the actual suspension/adjuster;
5. compare with independent measurements and the other side.

A result can be arithmetically correct and still be **SUSPECT** or **INVALID**. This is especially important for OCR, handwriting, phone photos, copied alignment screens, and DIY caster calculations.

The same rule applies to predictions: do not extrapolate eccentric position into a large angle correction without before/after measurements showing the local response.

## Start with the complaint condition

Classify when the problem occurs:

- steady cruise on a known road;
- acceleration versus coast;
- light versus hard braking;
- immediately after a left/right turn;
- over a bump/dip;
- with a changed load;
- after tire rotation or suspension work.

The condition selects the competing mechanisms. A static printout cannot reproduce every road load.

## Camber

After setup/reference validity is established:

- an individual camber error can contribute to edge loading/wear;
- a real side-to-side camber difference can contribute to drift/pull;
- camber that changes when the joint/bushing is loaded is evidence of moving geometry, not merely a static adjustment;
- ride-height changes can alter camber on independent suspensions;
- SAI/included-angle information can help distinguish ordinary adjustment from displaced structure, but only when SAI/IA were validly measured.

A camber result grossly inconsistent with the visibly near-vertical wheel, the service range, and the adjuster's available motion is a measurement/transcription problem until repeated. Do not infer a bent arm, knuckle, frame, or adjuster from camber alone.

## Caster

Caster contributes to directional stability and steering return, but it is a **derived sweep quantity** unless a validated aligner reports it from a proper sweep.

Before using an individual caster or cross-caster value, verify the per-wheel sweep requirements in `alignment-measurement-validity.md`, then pass the explicit severity gate in `alignment-result-plausibility.md`.

Poor return-to-center also has mechanical competitors:

- binding ball joints;
- strut/mount bearings where applicable;
- steering gear/rack or shaft binding;
- tie-rod/linkage binding;
- bushings tightened/bound at the wrong suspension position.

Do not tune caster to hide binding. Do not accept a multi-adjustment-scale or tens-of-degrees caster result as ordinary misalignment without auditing the raw observations and sweep.

## Toe and steering center

Keep separate:

- total toe — relationship between the two wheels on the axle;
- individual toe — each wheel relative to the chosen vehicle/thrust reference;
- steering-wheel center — rack/steering position relative to the vehicle's actual travel direction;
- rear thrust angle — rear axle/wheel direction relative to vehicle centerline.

Correct total toe does not prove correct individual toe or a centered steering wheel. Rear thrust geometry can make a front-only correction misleading.

A toe value being calculable from tape/string distances does not prove the reference strings, wheel diameter, wheel runout, or unit conversion were correct. Very large toe values should be compared with visible wheel direction and repeated before they become tie-rod advice.

Whether toe is the last adjustment is a **vehicle-procedure question**. For the 2005 Dakota case on this branch, the service procedure explicitly makes toe final after its coupled lower-control-arm caster/camber adjustment.

## Rear geometry and thrust

Measure rear toe/thrust even if the rear has no convenient ordinary adjuster. Nonadjustable geometry is still diagnostic evidence.

An abnormal thrust angle can point toward:

- axle or suspension displacement;
- spring/locating hardware problems;
- cradle/subframe or frame/body displacement;
- damaged structure.

Do not center the steering wheel around an unexamined rear thrust direction.

## SAI and included angle

SAI/KPI and included angle are diagnostic geometry, not ordinary “green box” adjustments.

Use them only after:

1. validating the camber/reference setup;
2. performing the specified steering measurement without wheel/turn-plate slip;
3. checking the applicable vehicle specification or side-to-side diagnostic rule;
4. combining the result with physical geometry;
5. checking that the magnitude itself is credible before using it to localize a bent/displaced part.

Do not turn a training example threshold into a universal bent-part threshold.

## Ride height

Ride height establishes the suspension operating point. A sagged or incorrectly loaded corner changes control-arm, tie-rod, and steering-axis relationships.

Use the OEM datum. Hood/fender/body heights are not substitutes unless the vehicle procedure explicitly uses them.

On the 2005 Dakota in the current case, the service procedure uses spindle center and lower-control-arm pivot-bolt centers for the front ride-height calculation.

A surprising ride-height result must be checked for datum selection, units, tape/reference position, tire loaded radius, floor height, and left/right assignment before being converted into an alignment prediction.

## Tire pull and pressure

A vehicle can pull with valid alignment because a tire generates lateral force. Preserve:

- pressure/loaded-radius difference;
- size/construction mismatch;
- conicity/ply steer/tire lead;
- wear/damage;
- circumference difference.

Equal pressure removes one confounder but does not prove the tires are geometrically or force-equivalent.

The quantitative pressure sensitivity calculation in `alignment-measurement-validity.md` is an assumption-based example, not a PSI→degrees conversion.

## Surface level is part of the model

Do not treat “level floor” as one Boolean.

Record four contact elevations and inspect:

- front transverse;
- rear transverse;
- left longitudinal;
- right longitudinal;
- both diagonals;
- twist/non-coplanarity.

A known simple slope may support a **REFERENCE-CORRECTED** sensitivity calculation. Physically leveling/shimming the four working pads and resettling the suspension is stronger evidence because suspension cross-loading and camber gain are real.

## Bump steer

Bump steer is a toe/direction change caused by suspension travel. Separate it from free play:

1. Is there lost motion in joints/rack/linkage?
2. With joints tight, does toe/direction change systematically through jounce/rebound?
3. Is the road simply deflecting the tire/steering through crown/ruts/compliance?

Inspect ride height, steering-link and control-arm geometry, rack/gear mounting, bent parts, and modifications that changed relative pivot heights.

## Memory steer

Memory steer is a tendency to retain the last steering direction. Check binding and hysteresis before blaming caster.

A valid caster number does not prove free return motion; an invalid caster number proves even less.

## Adjustment logic

Never begin with an angle-order slogan.

Instead:

1. establish valid **RAW**, **REFERENCE-CORRECTED**, **DERIVED**, **SPEC**, and **UNKNOWN** data;
2. pass every derived value through **IN-SPEC / OUT-OF-SPEC-BELIEVABLE / SUSPECT / INVALID / UNKNOWN** result integrity;
3. identify the actual adjustable mechanism;
4. determine mechanically which other angles that movement changes;
5. make one controlled movement;
6. settle the suspension;
7. remeasure every coupled angle;
8. iterate using the vehicle procedure;
9. finalize the remaining independent settings when the procedure directs.

For the Dakota-specific lower-control-arm cam geometry, see the dedicated section in `alignment-measurement-validity.md`, the plausibility gate, and the current case in `dakota-alignment-case.md`.
