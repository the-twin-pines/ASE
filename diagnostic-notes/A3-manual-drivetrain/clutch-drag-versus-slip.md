# A3 — distinguish clutch drag, clutch slip and gear-selection faults

**Status:** source-informed diagnostic notes; no vehicle-specific service
procedure or physical test run.

Sources: [ZF/SACHS, Clutch Doesn't Disengage](https://aftermarket.zf.com/en/aftermarket-portal/knowledge-hub/clutch-does-not-disengage/);
[ZF/SACHS, Clutch Slipping](https://aftermarket.zf.com/en/aftermarket-portal/for-workshops/useful-tips/clutches/clutch-slipping/);
[2026 ASE A3 task list](https://www.ase.com/uploads/ASE_Automobile_Study_Guide_2026.pdf).
The ZF articles describe failure mechanisms, not a procedure or adjustment
for a particular car.

## Three distinct fault classes

- **Drag:** engine torque still reaches the gearbox input with clutch pedal
  fully depressed when the clutch ought to be disengaged. A dragging input
  can make a stationary reverse/first selection difficult or noisy.
- **Slip:** clutch is nominally engaged, but its torque capacity is insufficient,
  so engine speed and output acceleration disagree under load.
- **Selection/synchronizer/linkage fault:** lever or gearbox cannot select or
  synchronize a gear even if the clutch correctly releases.

A dragging clutch can originate in hydraulic actuation (fluid/air/leak/master/
slave), cable/pivot geometry, release bearing/fork, disc sticking on splines,
pilot bearing, wrong components or assembly error. ZF explicitly warns
against automatically blaming the friction disc.

## Stationary diagnostic reasoning

| Observation to collect, safely | More likely direction | What it does not prove |
| --- | --- | --- |
| Gear selects engine OFF but resists engine RUNNING, at a safe idle and stationary | Incomplete release / spinning input | Exact cause; engine-off linkage drag remains possible |
| Pedal travel/feel changes; external release motion absent or inconsistent | Actuation/hydraulic/linkage path | Internal gearbox fault excluded |
| One gear alone resists in multiple states | Specific selection/synchronizer/linkage path | All clutch faults ruled out |
| Engine speed rises while wheel torque is insufficient during existing driving symptoms | Clutch slip or another torque-path problem | Worn disc specifically |
| Engine-off selection also consistently fails | Shift linkage or internal selector becomes important | No clutch-related secondary problem |

Never force a gear, repeatedly grind teeth, or run wheels on an improvised stand.
A vehicle that can lurch should not be subjected to stationary engine-running
gear tests without exact approved precautions.

## Source-mechanism map

ZF identifies incomplete disengagement from release system faults, disc
runout/hub spline binding, installation errors and pilot-bearing problems.
ZF lists slip candidates including contaminated friction surfaces, release
preload/actuation problems and incorrect parts/flywheel work. These mechanisms
have **different observable consequences** and different confirmation steps.
Symptoms alone are not a parts order.

## Next discriminators

1. Capture engine-off versus engine-running behavior only if safe to observe;
   record cold/hot, which gear, clutch pedal travel/feel, and history.
2. Inspect accessible linkage, visible hydraulic level/leaks and external
   release action according to the installed clutch architecture.
3. For an unresolved issue, obtain exact master/slave stroke, release travel,
   clutch free-play, fluid, and gearbox test procedures; do not invent numbers.
4. After repair, confirm quiet, repeatable selection and correct take-up under
   safe ordinary operation, then check for leaks and recurrence.

Outcome `NOT_RUN`. No exact travel, torque or fluid is approved by this note.
