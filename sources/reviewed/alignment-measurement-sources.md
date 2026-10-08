# Reviewed alignment measurement sources

Review date: 2026-09-10

This file records sources actually inspected for the measurement-validity repair. It is separate from `../alignment-video-audit.md`, whose status labels must remain strict.

## Official ASE A4 task list

Source: https://www.ase.com/uploads/ASE_Automobile_Study_Guide_2025_V2.pdf  
Status: **official PDF task list inspected**

Relevant A4 tasks separately require:

- diagnosing wander/drift/pull, bump steer, memory steer, torque steer, and return concerns;
- measuring ride height;
- measuring and adjusting camber where adjustable;
- measuring and adjusting caster where adjustable;
- measuring/adjusting toe and centering steering;
- measuring toe-out-on-turns, SAI/KPI, included angle, rear toe, thrust angle, setback, and subframe/cradle alignment;
- diagnosing damaged mounting locations;
- inspecting tire condition/size/application, measuring pressure, diagnosing runout, and diagnosing tire pull.

Use: this supports treating tire/wheel condition, ride height, steering geometry, and alignment as separate measurements/diagnostic tasks rather than assuming an out-of-spec display identifies the repair.

## 2005 Dodge Dakota service procedure

Public service-manual mirror, 2005 Dakota 2WD V8-4.7L VIN J:

- https://workshop-manuals.com/dodge/dakota_2wd/v8-4.7l_vin_j/maintenance/alignment/system_information/specifications/page_867/
- https://workshop-manuals.com/dodge/dakota_2wd/v8-4.7l_vin_j/maintenance/alignment/system_information/specifications/page_868/
- preceding description: https://workshop-manuals.com/dodge/dakota_2wd/v8-4.7l_vin_j/maintenance/alignment/system_information/specifications/page_866/

Status: **service-manual text inspected through a public mirror; verify exact variant/VIN against current authoritative service information before using specifications or torques**

Useful procedure:

- suspension height must be measured/adjusted before wheel alignment;
- front ride height is a geometry datum, not hood/fender height: spindle center-to-ground minus the average of front and rear lower-control-arm pivot-bolt center heights to ground; the mirrored procedure gives `71 mm ± 6 mm`;
- roll/jounce and remeasure after ride-height adjustment;
- both front and rear lower-control-arm cam bolts are adjustable;
- camber/caster adjustment is at the lower control arm, not the upper arm;
- rear lower-arm pivot movement changes caster strongly and camber slightly; front pivot can be moved slightly opposite to preserve camber;
- moving both pivots together changes camber strongly and caster slightly;
- toe is final.

The same manual material's pre-alignment logic calls for tire size/pressure/tread, wheel-bearing condition, wheel radial/lateral runout/balance, ball studs/linkage/steering gear and intermediate-shaft looseness/binding, suspension condition, ride-height variation, and a road test.

### Unresolved torque discrepancy

The alignment-adjustment page states `203 N·m (150 ft-lb)` after camber/caster adjustment. Another 2005 lower-control-arm installation/torque extraction lists lower suspension-arm frame fasteners at `244 N·m (180 ft-lb)`. This audit does not choose between them. Treat alignment geometry as established but torque as unresolved until exact authoritative procedure/fastener applicability is checked.

## Chrysler 2005 Dakota product specifications

Source: https://s3.amazonaws.com/chryslermedia.iconicweb.com/mediasite/attachments/05DakotaSpecs.pdf  
Status: **manufacturer product-specification PDF inspected**

Useful geometry:

- front suspension: upper and lower A-arms;
- power rack-and-pinion steering;
- published overall steering ratio `17.4:1`;
- published `3.18` steering-wheel turns lock-to-lock.

The ratio is descriptive vehicle data, **not** a substitute for actual individual road-wheel angles during a caster sweep. Steering geometry, toe-out-on-turns, total toe, compliance, and variable effective ratio across travel prevent that shortcut from validating caster.

Published dimensions used only for scale calculations in the notes are approximately:

- wheelbase `131.3 in = 3335.3 mm`;
- front track `62.8 in = 1594.5 mm`;
- rear track `62.9 in = 1598 mm`.

Do not infer the current truck's tire option or alignment specification from the general product sheet.

## SAE 850219 — Steering Geometry and Caster Measurement

Official metadata/abstract: https://saemobilus.sae.org/papers/steering-geometry-caster-measurement-850219  
Accessible reprint inspected: https://studylib.net/doc/8280217/steering-geometry-and-caster-measurement  
Author: Daniel B. January, Hunter Engineering Co.; 1985.  
Status: **derivation and practical-procedure text inspected; official SAE metadata cross-checked**

Core results:

- caster is not directly sensed on the invisible steering axis; it can be inferred from camber change as the wheel's toe/steer angle changes;
- the full camber relation contains caster, SAI, zero-toe camber, and toe;
- after the stated approximation and the critical restriction that the two steering positions be symmetric about the thrust line (`T2 = -T1`), the SAI term is eliminated to first order;
- small-angle form, using the paper's sign convention:

  `K ≈ (180/pi) * (C1 - C2) / (T2 - T1)`;

- the toe/steer angles must be measured relative to the rear thrust line for the paper's total-alignment caster definition;
- one front wheel being at the required turn angle does not prove the other is; toe-out-on-turns and total toe can make the second wheel's turn asymmetric;
- each wheel therefore needs its own valid turn positions;
- suspension/tire/turn-plate hysteresis contaminates camber change; the paper recommends approaching both measurement positions from the same steering direction;
- at a symmetric ±10° sweep, the small-angle multiplier is about `2.8648`;
- the paper's worked example shows only `0.05°` of camber hysteresis can create about `0.14°` caster error at ±10°;
- absolute camber sensor zero can cancel from the change measurement, but this is not a claim that physical rack slope/cross-loading cancels.

Use: this is the primary basis for refusing to derive caster from one steering-wheel revolution and unmeasured road-wheel angles.

## Longacre digital caster/camber instructions

Source: https://longacreracing.com/pages/digital-caster-camber-gauge-with-acculevel%E2%84%A2  
PDF: https://www.longacreracing.com/Userfiles/Docs/LIT-5059-REV-A.pdf  
Status: **manufacturer instructions inspected**

Useful instrument-specific rules:

- unlevel ground affects accuracy;
- wheels are straight ahead for direct camber;
- this digital gauge requires exactly `15°` one way then `15°` the other way for caster;
- its instructions explicitly say that vial gauges use a different `20°` procedure and that 1–2° turn error causes caster error;
- after caster/camber changes, bounce/settle and recheck because the two interact;
- for camber on nonlevel ground, its removable level can be zeroed on the ground parallel to the axle centerline on each side.

Use: there is no universal sweep angle or universal caster multiplier. The instrument procedure controls.

## NHTSA-hosted Hunter rack setup example

Source: https://static.nhtsa.gov/odi/tsbs/2013/SB-10090443-5448.pdf  
Status: **OEM TSB hosted by NHTSA inspected; not a Dakota specification**

The Kia/Hunter rack procedure is useful as an equipment-validity example:

- rolling compensation is critical;
- set tire pressure to factory specification;
- remove excessive load;
- ensure the lift is level so suspension/steering are neutral;
- set target levels as prescribed;
- keep slip-plate pins/turn-plate bridges in the required state and the bridge flush during compensation.

Use: alignment equipment setup is part of measurement validity, not a cosmetic shop detail.

## Tire vertical stiffness and pressure

### Semi-empirical Rhyne relation

Inspectible secondary source reproducing the relation and definitions:  
https://pmc.ncbi.nlm.nih.gov/articles/PMC8537413/

Status: **peer-reviewed article inspected**

The article gives tire vertical load as `F_z = K_z d` and a semi-empirical pressure/geometry stiffness form equivalent to:

`K_z = 0.00028 * P_kPa * g * sqrt(W * OD) + 33.84 N/mm`

where `W` is footprint width in mm and `OD` is outside diameter in mm. It also states vertical stiffness depends on pressure and sidewall structure.

Use: this supports a transparent sensitivity calculation, not a universal PSI-to-camber conversion.

### Real-tire stiffness variation example

Source: https://www.mdpi.com/2624-8921/6/1/16  
Status: **peer-reviewed article inspected**

For a 235/55R19 Continental CrossContact LX Sport example, the paper reports manufacturer vertical stiffness around `181.1 N/mm` while a finite-element condition near `228 kPa` and `5 kN` gives about `235.86 N/mm`; the modeled stiffness changes with pressure.

Use: construction/load/model matter enough that a single PSI→height→angle conversion must be labeled as an assumption-based sensitivity example.

## 1A Auto tire video

Review file: `1a-auto-tires-alignment.md`  
Video/page: https://www.1aauto.com/everything-you-need-to-know-about-tires-on-your-car-truck-or-suv/video/49957  
YouTube id: `yMPR8-MKKEw`  
Status: **full published page transcript reviewed end to end**

Useful material: placard tire identity/pressure, wear/damage, tires as a competing source of pull, and diagnostic value of four-wheel measurement even where an axle lacks ordinary adjustment.

## Alignment video corpus status

See `../alignment-video-audit.md`.

During this audit every video target already present in the branch queue was individually accounted for/retrieval-attempted. Most YouTube pages did not expose usable spoken transcripts in the available source path. Those entries remain **spoken material pending**. The only queued alignment-adjacent video with a full published transcript available here is the 1A Auto tire video above.

This is intentional. Page titles/descriptions are useful for acquisition planning but are not promoted into technical rules as though the video itself had been reviewed.
