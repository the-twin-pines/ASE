# A6 field trace — 2002 Honda CR-V EX driver's power window

**Status: REPORTED / UNRESOLVED.** Field conversation from October 2026.
No vehicle VIN, current recall-completion report, approved service-wire diagram,
instrument receipt, repaired fault, or post-repair verification supplied.

## Observations kept separate from conclusions

- A driver's power-window fault reportedly appeared abruptly.
- The ignition was ON during testing. A test light/voltage-indicating tester
  appeared to show supply at multiple master-switch connector receptacles;
  “12.6 V” was mentioned. Do **not** reclassify this as a calibrated DMM
  measurement or assume it was measured while the motor carried current.
- The available visual inspection did not show obvious corrosion or damage.
  That does not establish the inside of the switch/controller is healthy.
- Fuse testing was not yet confirmed. Neither commanded motor feed/return
  nor motor current and mechanical freedom had been independently established.
- The complaint concerns the driver's switch/door, not proof that a window
  motor has failed. Exact reported scope of other windows must still be recorded.

## Exact model-year distinction

The [2002 CR-V power-window master input-test excerpt](https://workshop-manuals.com/honda/cr-v_lx_4wd/l4-2.4l/sensors_and_switches/sensors_and_switches_windows_and_glass/power_window_switch/component_information/testing_and_inspection/master_switch_test/replacement/page_1241/)
describes a **20-pin (20P)** master-switch connector and a driver's window
control unit *built into the master switch*. This is a period Honda service
procedure mirror for a 2002 LX 4WD, not yet an exact EX source approval.

Separately, the [2002 EX 4WD control-unit reset excerpt](https://workshop-manuals.com/honda/cr-v_ex_4wd/l4-2.4l/relays_and_modules/relays_and_modules_windows_and_glass/power_window_control_module/component_information/testing_and_inspection/component_tests_and_general_diagnostics/)
also identifies the 20P master connector and discusses the effect of
losing power/disconnecting it. **Resetting AUTO operation is not evidence that
a completely dead motor circuit has been repaired.** Do not substitute a
1997–2000 CR-V 14P connector view or a later 22P view for this 2002 EX.

No wire color, connector cavity number, motor terminal or fuse amperage
is asserted here without an exact EX connector-side diagram and an
explicit matching test procedure.

## Recall is an independent safety boundary

[American Honda, December 15, 2020](https://hondanews.com/en-US/releases/release-e1a157df687ff71da1f64a190f016099-statement-by-american-honda-regarding-power-window-master-switch-recall-2002-2006-honda-cr-v-2020),
announced a **replacement** recall for certain 2002–2006 CR-V master
power-window switches, superseding the 2012 repair campaign. Moisture
can damage the PCB, increase electrical resistance, overheat/melt the
switch and damage the harness; fire is possible. Check the specific VIN's
recall completion at [Honda's recall lookup](https://owners.honda.com/service-maintenance/recalls).
The earlier [Honda bulletin 12-067](https://static.nhtsa.gov/odi/rcl/2012/RCRIT-12V486-1675.pdf)
documents older inspection/repair variants, but **does not replace** the
later recall and is not authority to perform only the obsolete repair.
No visible corrosion and an illuminated tester **do not** exclude
internal damage or establish recall completion. Do not continue energized
probing if there is heat, smoke, melting or odor.

## Next discrimination, without a guessed pinout

1. Record which of the four windows works from its local switch and from
   the master. Confirm lockout position and whether manual up/down and AUTO
   differ. Do not confuse controller relearn with all-window power loss.
2. Identify the exact fuse(s), relay, supply and grounds from the **2002 EX**
   service diagram; inspect fuse element and both sides under correct key/
   command conditions, using fuse-protected tests. If a fuse is open,
   investigate the cause instead of simply fitting a larger one.
3. With the correct *20P connector view and orientation*, check the
   manufacturer's input tests and connector terminal fit. Record each
   cavity's measured voltage relative to a VERIFIED ground, load,
   polarity and switch position. A handy door bolt requires verification.
4. Only then establish whether the controller sends the correct
   directional motor drive under command, and whether the motor/door
   mechanism can respond. Use the vehicle's approved safe motor-isolation
   method; avoid shorting power pins, bypassing the controller or forcing
   a stalled window against its stop.
5. Check VIN-specific recall completion and any relevant updated Honda
   service action before treating the master assembly as ordinary repair.
6. Record exact confirmed cause, repair and repeatable movement under both
   directions, then check AUTO if applicable. All outcomes remain NOT_RUN.

## Unresolved

Power-window diagram for exact EX, actual tester and loaded results,
fuse findings, motor terminal behavior, physical drag, VIN recall completion,
diagnosis, remedy and successful retest: **UNKNOWN**.
