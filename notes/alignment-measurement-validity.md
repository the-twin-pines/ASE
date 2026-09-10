# Alignment measurement validity

Alignment diagnosis begins with whether the geometry was measured validly. A number can be precise and still answer the wrong geometric question.

Source details and status are in `../sources/reviewed/alignment-measurement-sources.md`. The video corpus and its unresolved spoken-content work are in `../sources/alignment-video-audit.md`.

## 1. Separate observations from conclusions

Every recorded value belongs to one of these classes.

| Class | Meaning |
| --- | --- |
| **RAW** | Direct instrument/physical observation under a recorded setup. |
| **REFERENCE-CORRECTED** | Arithmetic reference correction under stated geometric assumptions. |
| **DERIVED** | Computed from valid prerequisite measurements. |
| **SPEC** | Source-backed vehicle/instrument target or procedure. |
| **UNKNOWN** | Missing, illegible, unsupported, or invalidated. |

Examples:

- `RF camber = +1.0°` from a wheel-mounted inclinometer is **RAW**.
- `RF camber ≈ +1.18° on a horizontal reference` after adding a measured 0.18° transverse slope is **REFERENCE-CORRECTED**, and only under the stated rigid-body/reference assumption.
- `RF caster = +3.2°` from a valid symmetric per-wheel sweep is **DERIVED** unless the instrument reports it directly from its own validated caster mode.
- subtracting two invalid caster estimates produces **UNKNOWN**, not cross-caster.

## 2. Preconditions before interpreting alignment angles

The 2005 Dakota service procedure itself begins downstream of a pre-alignment inspection and requires suspension height before alignment. ASE's A4 task list likewise treats ride height, camber, caster, toe, SAI/KPI, included angle, thrust angle, wheel/tire condition, pressure, runout, and tire pull as distinct diagnostic tasks.

Record before adjustment:

- vehicle year/model/drivetrain/suspension variant and the service information being used;
- tire size, model/construction/application, pressure, tread/wear, obvious damage, and whether a tire-pull test is still needed;
- wheel/rim damage and radial/lateral runout where relevant;
- vehicle load/cargo/fuel state required by the procedure;
- bearing, ball-joint, tie-rod, control-arm-bushing, steering-gear/rack/shaft looseness or binding;
- spring/shock/strut condition and OEM ride height at the specified datum;
- whether the suspension was rolled/jounced/settled;
- whether turn/slip plates are free and their bridges/working surfaces are flush;
- wheel-sensor/gauge mounting, zero/reference method, runout compensation, and resolution;
- steering straight-ahead reference and rear thrust reference where the method needs them.

An unstable bushing or joint can make “alignment” change with load. An incorrect ride height can place the control arms and tie rods at the wrong operating point. Neither is repaired by tuning a static number around the defect.

## 3. Four wheel pads are a geometry problem

Let the wheel-contact/turn-plate elevations be:

`z_LF`, `z_RF`, `z_LR`, `z_RR`.

Record all four values from one common elevation datum. From them, calculate and retain all six pairwise differences:

- LF ↔ RF — front transverse relationship;
- LR ↔ RR — rear transverse relationship;
- LF ↔ LR — left longitudinal relationship;
- RF ↔ RR — right longitudinal relationship;
- LF ↔ RR — one diagonal;
- RF ↔ LR — the other diagonal.

There are only three independent height degrees of freedom after choosing a common zero, so the redundant pairs are useful: they expose survey inconsistency and corner twist instead of hiding it behind a single “level” statement.

### Plane and twist

With measured wheel-contact coordinates `(x_i, y_i)` and heights `z_i`, fit or construct the plane

`z = a x + b y + c`

and inspect each corner's residual. If one plane cannot describe all four contacts within measurement uncertainty, the setup has twist/non-coplanarity. A single transverse or longitudinal correction is then not enough.

For a rectangular approximation with equal front/rear half-track, the simple twist indicator

`tau = z_LF + z_RR - z_RF - z_LR`

is zero for a perfect plane. For unequal front/rear track or asymmetric actual contact coordinates, use the coordinate-based plane instead of relying on `tau`.

### Front transverse slope and apparent camber

For front contact width `W_F`,

`rho_F = atan((z_RF - z_LF) / W_F)`.

Define positive camber as top of wheel outward, and define `rho_F > 0` when the surface rises toward the vehicle's right. Under a **rigid-body reference approximation** with no suspension articulation/cross-load camber gain:

`C_LF_RAW ≈ C_LF_LEVEL + rho_F`

`C_RF_RAW ≈ C_RF_LEVEL - rho_F`

so the reference corrections are

`C_LF_LEVEL ≈ C_LF_RAW - rho_F`

`C_RF_LEVEL ≈ C_RF_RAW + rho_F`.

If cross-camber is defined here as `LF - RF`,

`cross_RAW ≈ cross_LEVEL + 2 rho_F`.

These are reference corrections, not proof of what the wheels would read after physically leveling the truck. Real tires, springs, bushings, stabilizer bars, and suspension camber gain redistribute load when a corner is raised. The preferred correction is therefore to make the four working pads physically coplanar/level, roll/jounce the vehicle, and remeasure.

### Quantitative surface sensitivity for a 2005 Dakota-sized footprint

Using the published 2005 Dakota front track `W_F ≈ 1594.5 mm` only as a scale:

| LF↔RF height difference | front transverse slope | possible `LF-RF` reference bias under the rigid-body model |
| ---: | ---: | ---: |
| 1 mm | 0.0359° | 0.0719° |
| 5 mm | 0.1797° | 0.3593° |
| 10 mm | 0.3593° | 0.7187° |
| 14 mm | 0.5031° | 1.0061° |

Equivalently, an apparent cross-camber difference of 0.1°, 0.5°, or 1.0° needs only about 1.39 mm, 6.96 mm, or 13.91 mm of front left-right height difference in this simplified model.

That is why a straight-ahead camber pair on an unknown transverse slope must remain **RAW**, not be treated as true absolute camber.

### Longitudinal and diagonal relationships

With wheelbase `L`,

`theta_L = atan((z_LR - z_LF) / L)`

`theta_R = atan((z_RR - z_RF) / L)`.

The two values should agree for a simple planar pitch. A disagreement is another twist/cross-load warning.

For the 2005 Dakota wheelbase `L ≈ 3335.3 mm`, a 1, 5, 10, or 14 mm front-to-rear difference corresponds to about 0.0172°, 0.0859°, 0.1718°, or 0.2405° of reference pitch.

Diagonals do not create two additional independent slopes; they are important consistency checks. A setup can have front and rear pairs that look modest while still containing corner twist that changes chassis load distribution.

## 4. Tire pressure can imitate alignment geometry

“Check tire pressure” is not enough. Pressure changes loaded tire radius, so one side can sit lower even before the suspension geometry is considered.

There is no universal PSI-to-degrees conversion. Loaded radius depends on load, tire dimensions, footprint width, construction, temperature, and nonlinear sidewall/contact behavior.

### A transparent light-truck example

Use a representative `245/70R16` tire only as an **illustration**, not as a claim about the tire currently installed on the truck.

Assume:

- outside diameter `OD = 749.4 mm`;
- footprint width `W = 183.75 mm` (75% of nominal 245 mm section width, an explicit illustrative assumption);
- wheel load `F_z = 5.0 kN`;
- baseline pressure `35 psi = 241.3 kPa`;
- the semi-empirical Rhyne vertical-stiffness relation, expressed in N/mm:

`K_z = 0.00028 * P_kPa * g * sqrt(W * OD) + 33.84`.

Then `K_z ≈ 279.8 N/mm` at 35 psi and the simple spring deflection `F_z/K_z ≈ 17.87 mm`.

Holding the assumed wheel load fixed:

| Pressure | model `K_z` | model deflection | center drop from 35 psi |
| ---: | ---: | ---: | ---: |
| 35 psi | 279.8 N/mm | 17.87 mm | 0 |
| 30 psi | 244.7 N/mm | 20.44 mm | 2.57 mm |
| 25 psi | 209.5 N/mm | 23.86 mm | 5.99 mm |
| 20 psi | 174.4 N/mm | 28.67 mm | 10.80 mm |

If, very conservatively, that one-tire center drop were allowed to become a one-for-one front left-right chassis height difference, the Dakota-track rigid-body model above would require approximately:

| apparent `LF-RF` cross-camber bias | required height difference | pressure deficit from 35 psi in this example |
| ---: | ---: | ---: |
| 0.1° | 1.39 mm | 2.9 psi |
| 0.5° | 6.96 mm | 11.2 psi |
| 1.0° | 13.91 mm | 17.4 psi |

The one-for-one mapping is intentionally an upper-sensitivity assumption. A real four-tire suspension redistributes load through springs, anti-roll bars, bushings, the opposite axle, and tire compliance, so the actual body/pad attitude change can be smaller and the required pressure difference larger.

A published 235/55R19 study also shows why the model must not be universalized: manufacturer vertical stiffness was about 181 N/mm while one validated finite-element condition near 228 kPa/5 kN produced about 236 N/mm, and stiffness changed with inflation pressure.

Practical conclusion:

- a few PSI can contaminate small/tenths-of-a-degree comparisons in a sensitive setup;
- an apparent 0.5° cross difference from pressure alone would require a substantial mismatch in this example;
- a full 1° apparent cross error from pressure alone is not a plausible explanation for an ordinary small pressure mismatch; in this deliberately favorable model it takes roughly a 17 psi deficit;
- measure pressure anyway, because the cost of eliminating this confounder is trivial.

For the current truck case, equal pressures have already been reported, so unequal pressure is **not** being proposed as its actual cause.

## 5. Caster is a derived sweep measurement

Caster is not the straight-ahead angle shown by a wheel-mounted inclinometer. It is the fore/aft inclination of the steering axis and is normally inferred from how camber changes while the wheel is steered.

SAE Technical Paper 850219 derives the relationship. In its sign/reference convention, make two camber observations `C1`, `C2` at actual individual wheel toe/steer angles `T1`, `T2` measured relative to the rear thrust line. With a symmetric turn `T2 = -T1`, the small-angle approximation becomes:

`K ≈ (180/pi) * (C1 - C2) / (T2 - T1)`.

A more exact symmetric-turn approximation after eliminating SAI is:

`K ≈ atan((sin(C1) - sin(C2)) / (sin(T2) - sin(T1)))`

with the trigonometric inputs converted consistently to radians and the result converted to degrees.

The exact sign depends on using the same `T` and camber sign convention as the formula. Do not paste readings into a memorized multiplier without first proving that convention.

### What a valid caster record needs

For **each front wheel independently**, record:

- the instrument and caster mode/procedure;
- required sweep angle for that instrument;
- actual first road-wheel angle `T1`;
- camber `C1`;
- actual second road-wheel angle `T2`;
- camber `C2`;
- the reference for road-wheel angle (preferably thrust line where the method requires it);
- whether both target positions were approached from the same steering direction to reduce hysteresis;
- whether the turn/slip plates moved freely;
- the calculation or instrument-reported result.

The SAE paper explicitly warns that one wheel being at the correct angle does not establish that the other wheel is: toe-out-on-turns/Ackermann and total toe make their turn angles differ. Each wheel must reach its own valid symmetric pair.

### Instrument-specific sweep angles are not interchangeable

One current Longacre digital gauge requires exactly ±15° road-wheel positions (30° total), and its instructions explicitly distinguish this from vial gauges that use 20°. A 1–2° steering-angle error is enough for Longacre to warn of caster error.

Therefore:

- do not infer road-wheel angle from steering-wheel revolutions;
- do not use `360° / 17.4 = 20.69°` as though a 17.4:1 overall steering ratio were a measured wheel angle;
- do not assume a “1.5× camber change” caster factor.

For intuition only, the further small-angle SAE factor for a symmetric `±theta` sweep is `57.2958/(2 theta)`:

| actual symmetric sweep | small-angle multiplier |
| ---: | ---: |
| ±10° | 2.8648 |
| ±15° | 1.9099 |
| ±20° | 1.4324 |

A nominal one-turn steering-ratio conversion to ±20.69° would imply about 1.3846 in that approximation, but it is **not a valid caster measurement** because the individual road-wheel angles were not measured.

### What cancels and what does not

A constant camber-sensor zero offset cancels from a camber-difference caster calculation; the SAE paper notes that range calibration matters more than absolute camber zero for this reason.

Do not generalize that into “floor slope cancels.”

- longitudinal rack/floor slope changes the physical pitch of the chassis/steering axis relative to gravity;
- transverse slope can cross-load/articulate the suspension and alter the wheel path;
- twist means the four contacts do not even share one plane;
- tire/turn-plate/bushing compliance produces hysteresis.

Known pad heights can therefore **qualify** caster and can bound the attitude error, but a generic arithmetic subtraction is not a substitute for a level/coplanar setup or a vehicle-specific frame-angle correction. Use the OEM/reference-frame procedure when one exists.

### When cross-caster exists as evidence

Cross-caster is meaningful only after both left and right individual caster values are valid under the same reference/setup. If either side's caster is unsupported, cross-caster is **UNKNOWN**.

## 6. 2005 Dodge Dakota: coupled lower-control-arm adjustment

The 2005 Dakota service procedure is explicit:

- suspension height is measured before alignment;
- both front and rear lower-control-arm cam bolts are adjustable;
- camber and caster adjustments are made at the lower control arm; the upper arm is not the adjustment;
- moving the rear lower-control-arm pivot in/out changes caster significantly and camber slightly; move the front pivot slightly opposite if preserving camber while changing caster;
- moving both front and rear pivots together changes camber significantly and caster slightly;
- toe is the final adjustment.

This is a two-control, coupled problem rather than two independent knobs.

A defensible adjustment loop is:

1. validate tires, mechanical condition, OEM ride height, four-pad geometry, gauge setup, and the caster sweep;
2. compare valid caster and camber to the exact vehicle specification;
3. use primarily differential front/rear pivot movement to change caster while managing camber;
4. use primarily common-mode front/rear pivot movement to change camber while managing caster;
5. settle/roll/jounce as required;
6. **remeasure both caster and camber** after every meaningful cam movement;
7. iterate until both are acceptable;
8. set toe last and verify steering center;
9. road-test the original complaint.

Generic training material often presents a working sequence such as caster → camber → toe. That is not permission to ignore coupling. On this Dakota, the service-manual movement rules are the reasoned procedure; the final toe rule is explicit.

### Torque-source conflict

The accessible 2005 service-manual mirror gives `203 N·m (150 ft-lb)` immediately after the camber/caster adjustment procedure, while another suspension torque chart/manual extraction gives `244 N·m (180 ft-lb)` for lower suspension-arm frame nuts. This branch does **not** resolve that conflict by choosing one. Verify the exact vehicle/fastener procedure in authoritative service information before using a torque.

## 7. Diagnostic interpretation after validity

Only after the measurement gate is satisfied should an angle pattern be used to choose physical checks.

Examples:

- real camber error with normal/stable ride height may justify cam adjustment if the vehicle provides it;
- camber that changes under load points toward moving/loose geometry, not merely a static setting;
- abnormal SAI/included-angle relationships can help localize bent/displaced structure, but only if those measurements are themselves valid;
- pull can come from tire lead/conicity, pressure, brake drag, steering assist/binding, cross-camber/caster, rear thrust, road crown, or compliance under load;
- bump steer is dynamic toe/steering geometry and should not be collapsed into generic looseness;
- memory steer requires checking binding and returnability, not merely increasing caster.

Do not name the failed component from one red box. Use valid geometry to decide which boundary to inspect.

## 8. Compact measurement-to-adjustment sequence

1. Identify the exact vehicle/suspension/service procedure.
2. Verify tire application, cold placard pressure, left/right equivalence, wear/damage, and wheel/runout concerns.
3. Establish the required vehicle load state.
4. Inspect bearings, joints, bushings, steering gear/rack/shaft, and binding/play using the correct loading method.
5. Measure OEM ride height at the specified datum; correct it first if required.
6. Survey LF/RF/LR/RR pad elevations and all six pairwise relationships; physically level/shim the working pads when possible.
7. Confirm turn/slip plates are free/flush and perform required runout/rolling compensation.
8. Roll/jounce/settle and establish steering/thrust references.
9. Record **RAW** straight-ahead camber/toe/rear-thrust data.
10. Measure caster with a valid instrument-specific, actual-per-wheel symmetric sweep.
11. Create **REFERENCE-CORRECTED** values only where the correction model and assumptions are explicit.
12. Create **DERIVED** quantities only when every prerequisite is valid.
13. Diagnose the geometry; do not infer a part prematurely.
14. Adjust using the vehicle's actual coupled/independent mechanisms.
15. Set toe after caster/camber geometry is stable when the vehicle procedure says toe is final.
16. Settle and remeasure everything changed by the adjustment.
17. Verify steering center/electronic resets if applicable and road-test the original condition.
