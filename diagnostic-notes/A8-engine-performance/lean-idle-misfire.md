# A8 — lean at idle and misfire: oxygen is not a parts diagnosis

**Status:** synthetic symptom paths, not observed repairs. Sources:
[2026 ASE A8 tasks, pp. 44–47](https://www.ase.com/uploads/ASE_Automobile_Study_Guide_2026.pdf),
[AutoTechnician: Fuel trim analysis (April 2025)](https://autotechnician.co.uk/fuel-trim-analysis/),
[PicoScope automotive guided tests](https://www.picoauto.com/library/automotive-guided-tests/).
ASE covers ignition, fuel/air, emissions, engine mechanics and controls as
distinct but interacting areas. The fuel-trim article is professional secondary
discussion, not an exact engine calibration.

## Capture conditions before comparing trims

Collect whether fuel control is open or closed loop, coolant temperature,
RPM/load, STFT/LTFT by bank, commanded lambda/equivalence where accessible,
misfire counters, DTC freeze frame, fuel type and recent work. A cold
open-loop reading or a stale/unsupported generic parameter is not equivalent
to steady warm closed-loop trim.

**Positive fuel correction** means the controller is *requesting more fuel*
based on its control logic. It does not by itself identify an intake gasket,
oxygen sensor, injector or pump. Misfire leaves oxygen in the exhaust; this
can complicate interpreting a “lean” sensor report when the original defect
is spark, combustion or mechanical.

## Conditional pattern, not a lookup table of diagnoses

| Observed pattern | Candidate hypotheses | Most useful next separation |
| --- | --- | --- |
| Positive correction much greater at idle than raised, steady unloaded RPM | Unmetered air, vacuum/PCV path, intake leak; also sensor bias | Check intake/PCV plumbing and use an approved controlled smoke/leak test; recheck under matching states |
| Correction worsens with load or acceleration | Inadequate fuel delivery, metering error, exhaust restriction or measurement issue | Compare fuel command/delivery and intake reporting with exact service test |
| One bank differs strongly from the other | Bank-local air, injector, exhaust leak or sensor issue | Compare cylinder/bank observations before replacing common components |
| One cylinder's misfire counter leads | Spark, fuel, compression, valve sealing, local wiring | Qualified ignition/injector swap or compression/leak-down test; map any moved fault |
| Several sensors appear irrational simultaneously | Shared reference/ground/power or actual engine-state problem | Loaded reference and ground checks plus correlated data |

Even a typical idle-versus-RPM pattern is **not a proof**: controller strategy,
throttle, load, fuel cuts, exhaust leaks and sensor placement change meanings.
Capture both banks when the engine has two; do not manufacture a “bank 2.”

## Distinguishing path for rough idle with a lean code

1. Verify the complaint and freeze-frame condition; note if misfire is present
   *before* or concurrent with the lean indication.
2. Check air duct, PCV/vacuum and exhaust leak clues, plus electronic supply
   faults; do not spray flammable cleaner onto hot/ignition components.
3. Inspect trims in comparable closed-loop operating states and compare banks/
   cylinders; record raw readings rather than one composite “bad oxygen sensor.”
4. Choose a measured fuel-delivery test, controlled leak test, waveform, or
   cylinder-specific ignition/injector/compression check **according to the
   branch still plausible**. Manufacturer procedures control all limits.
5. Reproduce the original symptom and correction trend after actual repair;
   cleared DTCs alone are not verification.

No injector resistance, pressure, vacuum or misfire threshold is supplied.
Engine-fault conclusion `UNKNOWN`; physical verification `NOT_RUN`.
