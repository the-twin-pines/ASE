# Diagnostic fieldbook — gaps in A2, A3, A6, A8 and A9

2026-10-22. **Working diagnostic notes, not approved retrieval passages or accepted repairs.**

The purpose is to improve explanations and choice of the *next discriminating test*, not
to generate ASE examination questions. See the root [source architecture](../SOURCE_ARCHITECTURE.md)
and [exact-specification authority](../specifications/README.md).

| Bucket | Note | Central distinction |
| --- | --- | --- |
| A2 automatic transmission | [Delayed engagement](A2-automatic-transmission/delayed-engagement.md) | Driver's range request vs electrical command vs hydraulic application vs torque transfer |
| A3 manual driveline | [Clutch drag versus slip](A3-manual-drivetrain/clutch-drag-versus-slip.md) | Incomplete release vs insufficient torque capacity vs gear selection fault |
| A6 electricity | [Loaded-circuit testing](A6-electrical/loaded-circuit-testing.md) | Voltage presence vs ability to carry current; feed vs return |
| A6 actual case | [2002 CR-V driver's power window](A6-electrical/2002-crv-driver-window.md) | Ignition feed vs integrated master/controller vs motor/door mechanism; recall inspection |
| A8 engine performance | [Lean-idle/misfire](A8-engine-performance/lean-idle-misfire.md) | Oxygen/mixture signal vs the reason for it; fuel, air, ignition, compression |
| A9 diesel | [Common-rail crank/no-start](A9-light-diesel/common-rail-no-start.md) | Low-pressure supply vs rail generation/retention vs authorization/timing |

[Evidence-trace format](method/evidence-trace.md) describes how to reuse these notes.
Existing reviewed [A4 steering](../steering/), [A5 brakes](../brakes/),
and the separately developed [HVAC/engine/wheel PR](https://github.com/the-twin-pines/ASE/pull/13)
are deliberately not recreated here.

## Source and admission boundary

These documents are *research/diagnostic synthesis* with linked external references,
bounded hypotheses and incomplete-case labels. Their presence here does not turn
a webpage, quoted bulletin, service-manual mirror, or a field observation into an
approved source. Nothing in this addition changes `sources/catalog.tsv`,
`sources/reviews.tsv`, `sources/passages.tsv`, the receipt validator, or service
approval in `specifications/reviews.tsv`. **None of these fieldbook notes is
retrieval-eligible.** Any proposed passage must later undergo individual source
review, scoped citations, digests, explicit admission and negative eligibility tests.

The [2026 ASE A1–A9 task lists](https://www.ase.com/uploads/ASE_Automobile_Study_Guide_2026.pdf)
are a *coverage map*, not a source of vehicle-specific service limits or proof
of any diagnosis. Component-maker articles describe mechanisms within their
own stated applications. Historical service-manual mirrors require exact
vehicle/variant and current-source verification before use for repair.

Evidence levels used throughout:
- **SOURCE** — named external text consulted, with its actual scope.
- **REPORTED** — an observation as described, not reproduced independently.
- **HYPOTHESIS** — an explanation compatible with observations.
- **TEST PLAN** — what could distinguish hypotheses, with conditional outcomes.
- **UNKNOWN / NOT_RUN** — unresolved facts or missing verification.
- **VERIFIED REPAIR** — requires actual before/after evidence; none here.

The number of notes, links or worked cases is **not evidence** of better model answers.
The paired model comparison in [the retrieval experiment](../tests/retrieval-experiment.md)
remains NOT_RUN. Do not leak these notes into that experiment as answer keys.

## Next source-work gaps

1. A2: pick a real, identified transmission and obtain its range-state, pressure-port,
   temperature, fluid and command-to-application procedure, not a generic pressure value.
2. A3: obtain exact clutch hydraulic/release travel test instructions for a named vehicle;
   resolve engine-off / engine-running tests against that vehicle's safety instructions.
3. A6: obtain the exact 2002 CR-V EX power-window wiring/connector view, verify any
   proposed pin using the right connector-side orientation, and check actual recall
   completion by VIN.
4. A8: compare fuel trims at recorded operating conditions with independent fuel,
   air and mechanical evidence; avoid assuming an oxygen-sensor DTC is the cause.
5. A9: select a real diesel architecture (common rail, HEUI, unit injector, etc.)
   before prescribing an instrument, pressure target or isolation procedure.

Nothing here supplies safety-critical torque, hydraulic pressure, fluid type,
vehicle-dependent voltage-drop limit, SRS work, transmission stand/stall tests,
or diesel high-pressure opening instructions.
