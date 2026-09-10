# Alignment video corpus audit

Audit date: 2026-09-10

This file accounts for the alignment-related video targets currently present on the A4 suspension/steering branch and the larger Hunter alignment sets discovered while following those targets.

Status language is strict:

- **transcript reviewed end to end** — the spoken material was available in a published transcript and was actually reviewed;
- **video page reviewed** — the video page/title/description was inspected, but the spoken material was not available here;
- **catalog entry reviewed** — the title is present in an alignment-video catalog, but that is not evidence for the spoken technical content;
- **unresolved** — the old queue identity was retained, but a current indexed page was not recovered in this pass.

A title or description is never promoted into a technical note as though the spoken video had been reviewed.

## Every video in the branch's existing acquisition queue

### 1. OldSchoolNoe — ASE A4 Test Prep #1 - Alignment Angles

Video id: `eHG1gDpVpoE`  
Status: **video page reviewed; spoken material pending**

The page description says the scope includes camber, caster, front/rear toe, toe-out-on-turns, thrust line, thrust angle, geometric centerline, SAI, and included angle. This is the most direct OldSchoolNoe alignment target and remains a high-priority transcript acquisition.

Do not use the description as the source for definitions or diagnostic rules; those are cross-checked against Hunter material in `notes/alignment-diagnostic-patterns.md`.

### 2. OldSchoolNoe — ASE A4 Test Prep #2 - Tires

Video id: `UjvpfP8wE_s`  
Status: **video page reviewed; spoken material pending**

The page is alignment-adjacent because its advertised scope includes tire wear patterns, tire pull, and runout checks. It matters to alignment diagnosis chiefly as a competing-cause source: a vehicle can pull or wear tires for reasons that are not a simple caster/camber/toe adjustment.

### 3. OldSchoolNoe — ASE A4 Test Prep #3 - Steering Linkage, Bump Steer, and Memory Steer

Video id: `brgWEHip1_c`  
Status: **video page reviewed; spoken material pending**

The page identifies parallelogram and rack-and-pinion linkage, worn/bent component symptoms, bump steer, and memory steer. It is retained as alignment material because bump steer is dynamic steering/toe geometry and memory steer must be distinguished from poor returnability caused by caster alone.

### 4. OldSchoolNoe — ASE A4 Test Prep #4 - Front Suspension & Angles Changes

Video id: `uSyLmYMX2D0`  
Status: **video page reviewed; spoken material pending**

The description explicitly says the video shows front-suspension components and which alignment angles change when parts wear, including control-arm and strut-rod bushings and load-carrying ball-joint identification/testing. This is one of the highest-value pending sources because it connects mechanical movement to alignment readings.

### 5. OldSchoolNoe — 3 ASE A4 Topics That Seem Difficult At First

Video id: `bFOy-_jgfnI`  
Status: **video page identity recovered; spoken material pending**

The title alone does not establish which alignment topics are spoken about. Keep it in the queue until the spoken material can be inspected; do not infer content from the channel's neighboring A4 videos.

### 6. Driver's Therapy — ASE A4 Suspension & Steering - Test & Study Advice

Video id: `8Y-Z63vXg7w`  
Status: **video identity/page reference verified; spoken material pending**

This is a broad A4 review rather than a dedicated alignment demonstration. Keep it as a secondary source. If transcript acquisition becomes available, extract only the material that improves diagnosis rather than copying exam-prep mnemonics into the corpus.

### 7. McCuistian — Steering and Suspension Pop Test

Video id: `ZGjzZG5uOkE`  
Status: **video page reviewed; spoken material pending**

The indexed page exposes too little description to establish the alignment content safely. Retain as a broad A4 target rather than pretending the title proves a particular lesson.

### 8. Auto Pro Teacher — ASE A4 steering and suspension (Tire Size)

Video id: `7OByzAQw2yo`  
Status: **unresolved in this pass**

The old queue identity remains, but a current indexed video page was not recovered. Tire size is relevant to alignment measurement and pull diagnosis, but no technical claim from this target is promoted until the source page/spoken material is recovered.

### 9. Master Automotive Training — ASE A-4 Steering and Suspension [Easy Study Guide]

Video id: `eUnPiN6aico`  
Status: **video identity/page reference verified; spoken material pending**

This is a broad A4 study guide. The provider's current course material includes wheel-alignment coverage, but that does not substitute for the video's spoken content. Retain as secondary review material.

### 10. Suspensions Explained — Torque Steer: What it is and how it works.

Video id: `gc2blDwAJBk`  
Status: **video page reviewed; spoken material pending**

This is not a static wheel-alignment lesson. It is kept because throttle-dependent pull must not be misdiagnosed as caster/camber. The indexed page chapters identify unequal drive forces, suspension design, differential design, CV-joint angles, and cornering as topics. Treat it as a competing-cause source for pull diagnosis.

### 11. 1A Auto — Everything You Need to Know About Tires on Your Car, Truck or SUV

Video id: `yMPR8-MKKEw`  
Status: **transcript reviewed end to end**

Full review: `sources/reviewed/1a-auto-tires-alignment.md`

Useful alignment material includes tire identity/pressure/condition, the fact that abnormal wear can come from front-end condition as well as alignment, and the diagnostic value of four-wheel readings even where the rear has no ordinary adjustment.

The transcript's blanket alignment-interval claims are explicitly not adopted as universal rules.

### 12. Donut — Alignment Explained (+ DIY Guide)

Video id: `NZUgNJjUQLY`  
Status: **video page reviewed; spoken material pending**

The page identifies a lowered Miata, alignment explanation, and a home procedure using string, calipers, camber/caster/toe plates, and a bubble gauge. This is a useful future practical-measurement source, especially for understanding what DIY tools do and do not reference.

Do not copy the procedure into the corpus from the tool list or description. The current reusable DIY notes are instead cross-checked against QuickTrick's published written instructions.

### 13. Fast Monty's Garage — How to Measure Caster, Camber, and Toe, at home. Quick Trick Alignment

Video id: `oAxqgnd26nI`  
Status: **video page reviewed; spoken material pending**

The indexed page identifies QuickTrick alignment tools and home/track measurement of caster, camber, and toe. The exact spoken procedure remains pending.

The manufacturer's current written Alignment 101 procedure was reviewed separately because it supplies an inspectable source for pressure/suspension settling, caster sweep, camber reference, toe measurement, and the caster → camber → toe order.

### 14. Hunter Learning Channel — SAI-Included Angle - Hunter Engineering

Video id: `qoQwvJnk4Z0`  
Status: **video page reviewed; spoken material pending**

This target led to the larger Hunter alignment-video catalog below. SAI/included-angle diagnostic notes are cross-checked against Hunter's alignment training supplement rather than inferred from this video's description.

## Hunter Learning Channel: complete Alignment Angles catalog found during audit

Catalog page: https://phoenixtireequipment.com/all-videos/alignment-angles/

The catalog currently lists all of the following alignment videos. Every title below was inspected in the catalog; where an exact indexed YouTube page was recovered, that is noted. Catalog presence is not treated as transcript review.

1. **ADAS requires wheel alignment to work properly: What vehicle owners should know** — exact indexed video page recovered, id `zauOjoh7tBI`; page description connects four-wheel mechanical alignment to the vehicle direction used by radar/camera ADAS.
2. **ADAS calibration post-alignment: The importance of service providers** — catalog entry reviewed; spoken material pending.
3. **Why Do Cars Need Wheel Alignment?** — catalog entry reviewed; Hunter's current written material separately lists irregular tire wear, handling problems, and crooked steering wheel as reasons to check alignment.
4. **Toe Measurement – Hunter Engineering Company** — catalog entry reviewed; spoken material pending.
5. **Caster Measurement – Hunter Engineering Company** — catalog entry reviewed; spoken material pending.
6. **Camber Measurement – Hunter Engineering** — exact indexed video page recovered, id `mJSc_f5jOCs`; page description only says camber measurement is described.
7. **Four Wheel Alignment (Thrustline) – Hunter Engineering** — exact indexed video page recovered, id `E6If8r6Bdcg`; the page identifies four-wheel alignment and rear adjustment points, while detailed sequence notes are taken from Hunter's training supplement.
8. **Hunter Collision Alignment – Understanding Advanced Diagnostic Alignment Angles** — catalog entry and Hunter collision page reviewed; current written Hunter material identifies ride height, toe-out-on-turns, maximum steering angle, symmetry/setback, and suspension-body-dimension audit as diagnostic measurements.
9. **Hunter Collision Alignment – Blueprint a Car for the Collision Repair Industry** — catalog entry and collision page reviewed; spoken material pending.
10. **Turning Angle - Hunter Engineering Company** — catalog entry reviewed; spoken material pending.
11. **SAI-Included Angle – Hunter Engineering** — exact branch target `qoQwvJnk4Z0`; spoken material pending.
12. **Frame Angle – Hunter Engineering** — catalog entry reviewed; frame-angle notes are cross-checked against the Hunter training supplement.
13. **Dog Tracking – Hunter Engineering** — catalog entry reviewed; thrust-line/dog-tracking notes are cross-checked against the Hunter training supplement.
14. **What Causes Alignment To Change? – Hunter Engineering** — exact indexed video page recovered, id `41_cH4WojZA`; its description contains no useful technical detail, so the spoken material remains pending.

## Additional Hunter alignment-procedure catalog found during the same pass

A separate Hunter wheel-alignment-procedure catalog exposes another set of alignment-specific targets:

- Why Do Cars Need Wheel Alignment?
- ADAS calibration post-alignment: The importance of service providers
- Four Wheel Alignment (Thrustline) - Hunter Engineering
- Wheel Alignment Is Not Elective - Hunter Engineering
- QuickGrip Adaptor Proper & Secure Mounting
- What Causes Alignment To Change? - Hunter Engineering
- WinAlign Software - Hunter Engineering Company
- Hunter's WinAlign Spec Update with TPMSpecs
- Doug Woolverton's Two-Minute Drill - Hunter Engineering
- Wheel Alignment for Performance Vehicles - Hunter Engineering
- Performance Wheel Alignment Guidelines - Hunter Engineering
- WinAlign Tuner Hunter Engineering
- Measuring Vehicle Ride Height - Hunter Engineering
- Measuring Bump Steer - Hunter Engineering

The duplicate titles are already accounted for in the Alignment Angles list. Of the new titles, **Measuring Vehicle Ride Height** and **Measuring Bump Steer** are the highest-value future transcript targets for this diagnostic corpus. The adapter/software/speed-demo videos are lower priority unless they contain measurement-error or setup information that changes diagnostic interpretation.

## What this pass establishes

The old branch queue was too narrow in two ways:

1. it had only one Hunter alignment video even though Hunter's alignment-angle catalog contains a complete 14-video set;
2. it did not distinguish enough between a page being found and the spoken technical content actually being reviewed.

The branch now has an explicit accounting of every old queue target plus the complete discovered Hunter alignment-angle set, and a second procedure set for future transcript acquisition.

## Remaining acquisition work

The only source in this audit whose spoken material was actually available and reviewed end to end is the 1A Auto tire video. Most YouTube-only sources remain **spoken material pending** rather than being falsely promoted from their descriptions.

When transcript access is available, process the remaining sources in this order:

1. OldSchoolNoe #1 — complete angle relationships;
2. OldSchoolNoe #4 — worn suspension parts versus angle change;
3. Hunter Frame Angle — especially truck caster/reference geometry;
4. Hunter SAI/Included Angle — bent-part localization;
5. Hunter Four Wheel Alignment/Thrustline and Dog Tracking — rear geometry;
6. Hunter Measuring Vehicle Ride Height;
7. Hunter Measuring Bump Steer and OldSchoolNoe #3;
8. tire pull/conicity sources;
9. DIY measurement videos;
10. broad A4 review videos last.

For each future review, preserve the source status and add notes from the spoken material, not from the title or description.
