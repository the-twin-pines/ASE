# A4 — suspension and steering

This branch is part of the automotive diagnosis corpus. It is not an ASE study guide.

The useful material here should make an assistant better at answering real suspension and steering questions: noises over bumps, looseness, pull/wander, tire wear, poor return-to-center, wheel-bearing noise, ride-height problems, alignment geometry, and deciding which joint or component to inspect next.

## Current reviewed material

- `sources/reviewed/1a-auto-front-end-diagnosis.md` — transcript-reviewed videos covering ball-joint play, tie-rod play, wheel-bearing play/noise, sway-bar links, and shocks/struts.
- `sources/reviewed/1a-auto-tires-alignment.md` — full transcript review of the 1A Auto tire video, including tire-pull and four-wheel-measurement material.
- `notes/front-end-diagnostic-patterns.md` — reusable diagnostic lessons distilled from reviewed sources and cross-checks.
- `notes/alignment-diagnostic-patterns.md` — detailed alignment reasoning: measurement conditions, frame angle, caster/camber/toe order, thrust line, SAI/included angle, ride height, bump steer, memory steer, tire pull, torque steer, DIY measurement limits, and diagnostic sequence.
- `sources/alignment-video-audit.md` — accounting of every old branch video target plus the complete Hunter Alignment Angles catalog and additional Hunter procedure-video set found during the audit.
- `sources/cross-checks.md` — inspectable manufacturer/training sources used to keep source demonstrations from turning into universal rules.

## Acquisition queue

- `sources/video-queue.md` — remaining OldSchoolNoe, Hunter, and other suspension/steering videos whose spoken material still needs acquisition. Video-page inspection is kept separate from transcript/spoken-content review.

## Working rule

A wheel that moves when shaken is not yet a diagnosis. Watch the relevant parts while the load is applied and identify the **relative motion**: knuckle versus control arm, tie-rod stud/socket versus knuckle, rotor/hub versus knuckle, and so on.

Likewise, do not turn a generic inspection trick into a universal procedure. Ball-joint loading and acceptable play depend on suspension design and service information; a light oil film on a shock/strut is not automatically the same thing as a failed leaking unit.

For alignment, establish tires, mechanical condition, ride height, load, and the relevant vehicle/frame reference before interpreting the numbers. On a total four-wheel alignment, rear geometry establishes the thrust reference; at the front, the working order is **caster → camber → toe**, subject to the vehicle-specific procedure and any coupled adjustments.
