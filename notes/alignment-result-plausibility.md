# Alignment result plausibility gate

A formula producing a number is not enough. Every alignment result must survive this gate before it is reported as a usable vehicle angle or used for adjustment advice.

This file is the result-integrity layer for `alignment-measurement-validity.md` and `alignment-measurement-checklist.md`. It does not replace the setup and measurement requirements in those files.

## Result states

Use one of these states explicitly.

| state | meaning | action |
| --- | --- | --- |
| **IN-SPEC** | Valid measurement and verified vehicle-specific specification agree. | May be used with the rest of the alignment evidence. |
| **OUT-OF-SPEC / BELIEVABLE** | Measurement is valid and outside specification, but the magnitude is mechanically credible for this vehicle/setup. | Diagnose causes; do not skip setup checks merely because the number is believable. |
| **SUSPECT** | Arithmetic may be correct, but the magnitude or cross-checks are abnormal enough that transcription, sweep, setup, or damaged geometry is more likely than an ordinary adjustment error. | Stop. Audit the raw observations and repeat the measurement before adjustment advice. |
| **INVALID** | A required input is missing/wrong, the geometry does not match the formula, or the result is physically absurd for the vehicle. | Do not report it as an alignment value. Preserve the raw observations and find the failed prerequisite. |
| **UNKNOWN** | Required evidence is absent or ambiguous. | Obtain the missing measurement; do not infer it. |

`SUSPECT` and `INVALID` are control-flow states, not adjectives. They stop the adjustment pipeline.

## Five mandatory gates

Apply these in order to every derived caster/camber/toe/cross result.

### 1. Arithmetic consistency

Recompute from the recorded raw observations. The recalculation must be reproducible without consulting the previously reported answer.

For a caster calculation, retain `C1`, `C2`, `T1`, `T2`, units, formula/version, and the exact result. A copied result with no reconstructable inputs is **UNKNOWN**.

### 2. Input consistency

Compare the calculation inputs to the original source record, not to a cleaned transcription.

Check:

- decimal point;
- plus/minus sign;
- degrees versus another unit;
- LF versus RF;
- first versus second sweep position;
- left-turn versus right-turn label;
- instrument mode and zero/reference;
- copied digits and handwriting ambiguity.

Never repair a raw observation in place. If a notebook mark could be `+0.5°` or `+5°`, retain the literal ambiguity and mark the dependent result **UNKNOWN** until resolved.

### 3. Geometric consistency

Verify that the formula describes the measurement actually taken.

For the symmetric two-position caster method described by SAE 850219:

- `C1` and `C2` are camber observations at the two actual road-wheel steer/toe angles `T1` and `T2`;
- the individual wheel angles are measured relative to the required reference, not inferred from steering-wheel rotation;
- the sweep is symmetric about that reference within the measurement method's tolerance;
- the wheel whose caster is being calculated is the wheel whose actual angles were measured;
- the instrument-specific sweep is used;
- the turn/slip surfaces are free enough that tire scrub and suspension wind-up do not substitute for steering angle.

A nominal steering ratio does not fill a missing `T1` or `T2`. Ackermann/toe-out-on-turns and total toe are enough to make the two front road-wheel angles differ even when the steering wheel made one repeatable rotation.

### 4. Vehicle plausibility

Compare a valid calculation with an exact service specification and with the scale of the vehicle's actual suspension geometry.

For the 2005 Dakota branch case:

- the accessible 2005 service-manual table gives a nominal caster value near `+3.5°`; the table's tolerance is text-extracted ambiguously and must be verified from an authoritative exact-variant source before an **IN-SPEC** decision is automated;
- an OE-replacement Dakota lower-control-arm cam kit is published with about `±2°` camber/caster adjustment range. This is a useful *scale check*, not an OEM specification.

Use that distinction:

- a valid value just outside a verified service envelope can be mechanically believable;
- once a value lies more than roughly one normal adjustment-scale (`~2°` for this Dakota cam hardware) beyond the verified envelope, require a repeat measurement and setup audit before treating it as ordinary misalignment;
- a value several adjustment-scales away is **SUSPECT** even if the arithmetic is flawless;
- for an assembled stock Dakota, `|caster| >= 45°` is an automatic **INVALID** data-integrity tripwire. Forty-five degrees is not a service limit: it means the steering axis is tilted as much fore/aft as it rises vertically (`tan 45° = 1`), radically unlike the service geometry and adjustment scale. Such a result must not be described as merely “very out of spec.”

The `45°` tripwire is deliberately conservative and specific to rejecting absurd data in this corpus. It is not a universal alignment threshold and must not be reused as a vehicle specification.

### 5. Cross-check consistency

Compare the result with independent constraints:

- opposite-side value, but only if that side is independently valid;
- verified maximum left/right difference where the vehicle service data supplies one;
- straight-ahead camber, ride height, SAI/included angle, toe/thrust, and visible geometry where they constrain the hypothesis;
- repeat sweep in the same setup;
- before/after response to a known controlled adjustment, if one has actually been made and remeasured.

A cross value inherits the weakest operand. If either individual caster is `UNKNOWN`, `SUSPECT`, or `INVALID`, cross-caster is not a valid derived result.

## Caster calculation and sweep uncertainty

For the SAE symmetric-turn approximation used in this branch, with consistent signs and radians inside trigonometric functions:

`K ≈ atan((sin(C1) - sin(C2)) / (sin(T2) - sin(T1)))`

For small angles and a symmetric sweep `T1=-theta`, `T2=+theta`:

`K ≈ (180/pi) * (C1 - C2) / (2 theta)`.

The straight-ahead camber reading is not an input to this two-position caster calculation. It is separately useful as camber evidence. Adding a straight-ahead reading to the caster formula is a different, unsupported procedure unless the instrument's own documented method requires it.

Approximate sweep produces scale uncertainty. In the small-angle form, caster is inversely proportional to total sweep, so approximately:

`delta K / K ≈ - delta(total sweep) / total sweep`.

For a nominal `±15°` sweep, an actual `±14°` sweep changes the sine-form scale factor by about `+7.0%`; an actual `±16°` sweep changes it by about `-6.1%`. Longacre explicitly warns that even `1°` or `2°` turn-angle error causes caster error. If actual wheel angle was not measured, this is not merely an uncertainty bar: the geometric prerequisite is missing and caster is **UNKNOWN/INVALID** for adjustment purposes.

## What sensor zero can cancel — and what it cannot

A constant camber-sensor zero offset cancels from a camber-difference caster calculation. That does **not** mean the physical surface cancels.

An unlevel or twisted setup can change chassis pitch, cross-load the suspension, alter the wheel path, and create hysteresis. Gravel can also let the tire sink or move while adding scrub resistance. Tire pressure, tire construction, ride height, looseness, bushing compliance, steering play, and settling can therefore contaminate the raw geometry even when a constant electronic zero error would algebraically cancel.

## Failed-result diagnostic tree

When a caster result is `SUSPECT` or `INVALID`, inspect in this order and stop when a cause is found:

1. original handwritten/photo/instrument **RAW** observations;
2. decimal-place transcription (`0.5` versus `5`);
3. positive/negative sign;
4. LF/RF wheel assignment;
5. first/second or left-turn/right-turn sweep assignment;
6. inclinometer zero/reference and instrument mode;
7. actual individual road-wheel sweep angles;
8. degrees of road-wheel angle versus steering-wheel rotation/turns;
9. formula, units, and multiplier for the actual sweep;
10. wheel movement, tire scrub, vehicle roll, and suspension settling between observations;
11. floor/rack/gravel level, four-corner pad elevations, and twist;
12. tire pressure, tire equivalence, wear, and damage;
13. OEM ride height and load state;
14. looseness, binding, bent/damaged parts, or genuinely abnormal suspension geometry.

Do not jump to item 14 merely because it would make the calculation possible.

## Worked regression cases

These are data-integrity examples, not measurements of the current truck. The exact calculation uses a symmetric `±15°` measured road-wheel sweep unless stated otherwise.

| case | raw inputs | calculation result | gate result | why |
| --- | --- | ---: | --- | --- |
| normal synthetic caster | `C1=+0.5°`, `C2=-1.3°`, `T1=-15°`, `T2=+15°` | about `+3.47°` | plausible; compare to verified spec | Reconstructable inputs and proper measured sweep. |
| decimal transcription | same except `C1` copied as `+5°` | about `+11.98°` | **SUSPECT** | Many degrees away from the Dakota's normal service/adjustment scale; return to the raw note and decimal point before advice. |
| sign error | both camber signs reversed | about `-3.47°` | **SUSPECT** | Grossly inconsistent with the positive-caster service geometry; audit source signs and cross-check the other side. |
| sweep-direction swap | `T1=+15°`, `T2=-15°` under the declared formula convention | would reverse the sign | **INVALID before reporting** | The input labels violate the declared sweep convention; do not let arithmetic hide a direction swap. |
| assumed steering ratio | `C1=+0.5°`, `C2=-1.3°`, but `T1/T2` filled from one steering-wheel revolution and `17.4:1` | a precise-looking number can be produced | **INVALID/UNKNOWN** | Road-wheel angles were not measured; Ackermann, toe, linkage geometry, and compliance defeat the shortcut. |
| absurd raw pair | `C1=+20°`, `C2=-20°`, `T1=-15°`, `T2=+15°` | about `+52.88°` | **INVALID** | The result trips the absurd-axis gate and must trigger the diagnostic tree, not adjustment advice. |

The decimal-error case is intentional: the calculation is arithmetically correct for the *wrong transcription*. That is exactly why arithmetic checking alone is insufficient.

## Broader alignment use

Apply the same pattern to camber, toe, cross-camber, cross-caster, ride height, SAI/included angle, and adjustment predictions:

- verify raw inputs and units;
- compare with the exact service envelope when available;
- compare with visible/physical geometry and known adjustment authority;
- compare left/right and repeat observations;
- treat values far outside the mechanism's ordinary scale as measurement/setup questions before adjustment questions.

Do not invent universal hard cutoffs for every angle. A static toe value can be mechanically enormous after steering/linkage work, for example, while the same number might be impossible for another stated setup. Where the repository lacks a defensible vehicle-specific threshold, the correct state is **UNKNOWN** or **SUSPECT pending repeat**, not a fabricated limit.
