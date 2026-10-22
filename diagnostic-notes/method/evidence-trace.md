# A diagnostic trace is a sequence of conditional eliminations

Scope: shared writing method for A1–A9. An engine, transmission, window motor or
power-steering pump is not a diagnosis simply because it is named in a symptom.

## Trace record

1. **Identity:** exact vehicle/engine/transmission, installed architecture,
   year and relevant option codes. Otherwise `UNKNOWN`.
2. **Complaint in time:** cold/hot, when it began, what changes the symptom,
   whether it appeared after service, and which operations still work.
3. **Raw observations:** exact test instrument, hookup and reference point;
   ignition and load state; measured unit; error/uncertainty if meaningful.
   Preserve words such as “reported,” “suspected,” or “appears” when appropriate.
4. **Functional boundary:** separate the command, energy supply, power conversion,
   mechanical load and observed result. For example, lighting a tester at a
   window-switch feed does not show that motor current crosses the switch.
5. **Competing causes:** list only hypotheses with distinct predictions. Do not
   stack parts names without identifying a way to test them.
6. **Next discriminator:** choose the least invasive safe test whose possible
   results actually change the ranking of causes.
7. **Interpretation:** for each result, state what it establishes and what it
   leaves open. A test that does not recreate the complaint may be inconclusive.
8. **After-action verification:** reproduce original conditions safely and
   demonstrate symptom correction, not merely clearing codes or obtaining
   a plausible resistance/voltage at rest.

## Sample discriminators

| Observable | Stronger inference | Still unproved |
| --- | --- | --- |
| Feed voltage with circuit disconnected | Potential exists at the measured point | Enough voltage/current **under load**, ground return, controller or motor |
| Large loaded drop across one connection | That connection is resisting current in this test state | Why it failed, or whether it is the only fault |
| Engine starts normally with clutch engaged, but a manual gear is difficult to select with engine running | Clutch release/drag becomes a candidate | Failed gearbox or specific hydraulic component |
| Rail pressure actual differs from requested during diesel cranking | A control/pressure discrepancy exists, subject to sensor validity | Bad high-pressure pump specifically |
| One wheel is hot and a brake pedal pumps up | Heat/drag and excess hydraulic travel may be related | One single fault, exact wheel, or master cylinder failure |

## Negative controls

For every working hypothesis include a plausible result that would lower its
ranking. Example: if a door-window motor sees a correct *loaded* drive
supply/return in both command directions yet cannot move, upstream power-feed
absence loses plausibility and motor/mechanism testing becomes more valuable.
The correct condition must be defined by exact wiring, not an assumed
reversing-motor diagram.

Do not turn “fuse has power” into “fuse is good,” or “battery reads 12.6 V” into
“the circuit carries the commanded motor current.” Keep test lights, digital
meters and loaded voltage-drop tests separate. Reference:
[Fluke, Diagnosing Voltage Drops](https://www.fluke.com/en/learn/blog/automotive/electrical-automotive-troubleshooting).

## Stop states

- Safety-critical operation or limit without exact authorized service information
  → `STOP: SPEC_UNKNOWN`.
- Source record is a title, playlist position, partial video or unreviewed quotation
  → `STOP: SOURCE_NOT_ADMITTED`.
- Measurement setup invalid, unidentified pin, or result fails plausibility
  → `STOP: MEASUREMENT_INVALID`.
- No before/after repair observation
  → `NOT_RUN`, not “fixed.”

This method is a writing aid; it does not implement an automated content safety gate.
