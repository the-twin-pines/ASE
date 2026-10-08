# A4 cross-check sources

These sources are not interchangeable. Manufacturer/service procedures control vehicle-specific work; training material is used for geometry and diagnostic relationships; video descriptions are acquisition metadata, not spoken technical evidence.

## Ball-joint inspection loading

MOOG — Signs of Loose Ball Joints  
https://www.moogparts.com/technical/bulletins/tech-tips/how-to-inspect-ball-joints-for-looseness.html

Useful correction: inspection depends on whether the joint is load-carrying, follower/non-load-carrying, or part of a MacPherson-strut arrangement. The page gives different unloading and pry/dial-indicator procedures rather than one universal wheel-shake rule.

Keep from this: identify the suspension design or consult its service procedure before saying exactly where to jack or how much play is allowed.

## Shock/strut weepage versus leakage

Monroe — Shock Weepage vs Leakage  
https://www.monroe.com/technical-resources/servicegrams/weepage-vs-leakage-shocks-struts.html

Useful correction: a light film/weepage can be acceptable. Broad wetness or fluid dripping from the unit is treated as leakage and a replacement condition.

Keep from this: do not diagnose a failed strut solely from “there is some oil on it.”

## Shock/strut inspection as a whole-system check

Monroe — How to Conduct a Shock or Strut Inspection  
https://www.monroe.com/technical-resources/tech-tips/how-to-conduct-a-shock-strut-inspection.html

The useful order is customer/repair history → road evaluation → physical inspection. The bounce test is one clue inside a larger inspection, not a definitive oracle.

## Alignment measurement sources

Detailed source/status notes are in `reviewed/alignment-measurement-sources.md`.

The important hierarchy is:

1. exact vehicle service information for ride-height datum, adjustment hardware, specifications, and torque;
2. instrument manufacturer procedure for required caster sweep/zero/reference;
3. geometric derivations such as SAE 850219 for what the sweep mathematically requires;
4. alignment training material for general relationships;
5. videos only when their spoken content is actually available and reviewed.

### 2005 Dakota service geometry

The 2005 Dakota service-manual material says ride height comes before alignment; both lower-control-arm cams are adjustable; rear-pivot motion mainly changes caster, both pivots together mainly change camber; and toe is final.

Keep from this: **do not preserve a generic “caster first” or “camber first” slogan**. On this design, caster and camber are coupled and must be iterated/rechecked according to the actual cam movements.

### SAE 850219 caster measurement

Daniel B. January, Hunter Engineering — *Steering Geometry and Caster Measurement*  
Official metadata: https://saemobilus.sae.org/papers/steering-geometry-caster-measurement-850219

Keep from this:

- caster is inferred from camber change during a steering sweep;
- symmetric actual per-wheel steer/toe angles are a prerequisite for the simplified derivation;
- road-wheel angle is referenced to thrust line in the paper's definition;
- one front wheel's turn does not establish the other's because toe-out-on-turns/total toe create asymmetry;
- hysteresis and turn-angle error matter;
- a constant camber-sensor zero offset cancelling from the difference is not evidence that physical rack slope/cross-loading cancels.

### Longacre caster/camber gauge instructions

https://longacreracing.com/pages/digital-caster-camber-gauge-with-acculevel%E2%84%A2

Keep from this:

- unlevel ground affects the reading;
- straight-ahead is required for direct camber;
- the specific digital gauge uses exactly ±15° while vial gauges use 20°;
- caster/camber adjustments interact and must be rechecked.

Keep the lesson instrument-specific. There is no universal sweep angle or multiplier.

### Four-corner surface validity

NHTSA-hosted OEM/Hunter rack example:  
https://static.nhtsa.gov/odi/tsbs/2013/SB-10090443-5448.pdf

It explicitly treats tire pressure, excess load, rack level, target level, rolling compensation, and turn/slip plate setup as prerequisites to accurate readings.

Keep from this: “the rack/floor is level” is a measured setup condition, not an assumption. For DIY work, survey LF/RF/LR/RR contact heights and check twist.

### Tire-pressure sensitivity

Rhyne-relation source used for the worked sensitivity calculation:  
https://pmc.ncbi.nlm.nih.gov/articles/PMC8537413/

Real-tire stiffness variability example:  
https://www.mdpi.com/2624-8921/6/1/16

Keep from this: pressure changes loaded radius, but pressure-to-height and pressure-to-camber depend on tire/load/geometry. Never create a universal PSI→degrees rule.

## Hunter vehicle-alignment training supplement

Hunter Engineering — Vehicle Alignment Seminar, Technician Reference Guide, 2008–2011  
https://bccskillsusa.weebly.com/uploads/4/3/3/2/43327659/hec_alignment_manual_edu_2.pdf

Useful general geometry:

- spring sag/load/worn or damaged parts can change alignment;
- frame angle and vehicle attitude can matter;
- caster is a steering-sweep quantity, not a straight-ahead snapshot;
- rear thrust geometry remains diagnostic even if not adjustable;
- SAI/included angle can help localize displaced structure.

The supplement's generic total-alignment workflow is **not** a vehicle-specific camber/caster adjustment law. Use exact service information for the actual mechanism.

## Hunter current alignment and collision material

https://www.hunter.com/alignment-machines/hawkeye-elite/  
https://www.hunter.com/collision  
https://www.hunter.com/cs/media-center/industry-insight/benefits-of-wheel-alignment/

Use current Hunter material to preserve ride height, toe-out-on-turns, setback/symmetry, rear thrust, and electronic calibration as parts of a complete alignment picture. Do not turn product features into vehicle specifications.

## QuickTrick written home-alignment procedure

https://quicktrickalignment.com/alignment-101/

This is useful as a practical portable-tool cross-check: pressure, settling, a caster sweep, and an external/string reference for individual toe matter.

Its suggested workflow does not override vehicle-specific coupled adjustment geometry or the sweep requirements of a different instrument.

## Video evidence boundary

See `alignment-video-audit.md` and `video-queue.md`.

Most alignment videos in the branch remain **spoken material pending** because only page/catalog metadata was obtainable. Do not quote or summarize their technical claims from titles/descriptions. The 1A Auto tire source is separately marked transcript-reviewed.
