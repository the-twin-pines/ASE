# A6 field trace — 2002 Honda CR-V EX driver's power window

**Status: REPORTED / UNRESOLVED.** Field conversation, October 20–22,
2026. This case also records bad assistant advice as regression evidence.
No VIN, confirmed blown fuse, exact EX pinout receipt, diagnosed root cause,
completed repair, or post-repair verification was supplied.

## Observations — not conclusions

- The **driver's window** reportedly stopped working abruptly.
- The **other windows work**. This is a reported discriminator: a common
  window supply/relay failure becomes less likely, but the driver's
  individually protected branch **is not cleared**. Whether the other
  windows were tried from their own switches or the master is unrecorded.
- Ignition **ON** during the test was explicitly established. The user was
  using a **test light**, with bolt heads as the chosen ground attachment.
  Tester details were not confirmed. The user described readings of
  **12.6 V at at least four receptacles** at the green master connector.
  Do not silently relabel these as independent calibrated DMM readings,
  a motor-load measurement, or proof that the driver's circuit is healthy.
- No visible corrosion, melting, or physical damage was seen. This does
  not verify unseen contacts, electronics, wiring, or current capacity.
- The driver-specific fuse had **not yet been tested** when the
  conversation ended. Neither motor drive nor mechanical movement had
  been verified.

## 2002 fuse topology — check this before probing the door

[2002 Honda CR-V owner's manual, fuse charts pp. 339–340](https://www.manualslib.com/manual/706236/Honda-2002-Cr-V.html)
and the [2002 fuse-chart transcription](https://www.startmycar.com/us/honda/cr-v/info/fusebox/2002)
show **four separate 20 A under-dash window fuses**:

| Under-dash fuse | Protection |
| --- | --- |
| #22 — 20 A | Front **right** window |
| **#23 — 20 A** | Front **left / driver's** window (U.S. left-hand drive) |
| #24 — 20 A | Rear **left** window |
| #25 — 20 A | Rear **right** window |

The same model-year chart identifies under-dash **#6 — 7.5 A**
as the power-window relay fuse and under-hood **#13 — 40 A**
as the common power-window fuse. The
[2002 EX 4WD service excerpt](https://workshop-manuals.com/honda/cr-v_ex_4wd/l4-2.4l/relays_and_modules/relays_and_modules_windows_and_glass/power_window_control_module/component_information/testing_and_inspection/component_tests_and_general_diagnostics/)
independently names under-dash #6 and #23 for the driver's window
controller reset after loss of power.

**Crucial inference:** working passenger/rear windows strongly disfavor
a complete common-supply or relay outage. They say **nothing conclusive
about the separate #23 fuse**. Sudden failure does not prove the fuse
blew; it makes an inexpensive first check particularly appropriate.

## Lowest-effort diagnostic order for this observation set

1. **Inspect/test under-dash #23 before switch or motor work.** For a
   powered fuse circuit with ignition ON, compare the two exposed fuse
   test points using the user's correctly attached test light:
   one side lit and the other dark suggests an open fuse; both lit shows
   potential on both sides under the tester's load; neither lit calls
   for a feed/condition check. Check the exact fuse-box legend.
2. If #23 is open, replace **only with the specified 20 A rating** after
   considering a short or overload. A repeatedly opening fuse requires
   fault localization; do not bypass protection or up-rate the fuse.
   If both fuse points light, do **not** infer sufficient current at the
   driver's motor; proceed through the correct diagram and loaded checks.
3. Identify the exact installed 2002 EX driver's master switch,
   connector-side orientation, wire functions and authorized electrical
   test procedure. The [2002 period master input-test excerpt](https://workshop-manuals.com/honda/cr-v_lx_4wd/l4-2.4l/sensors_and_switches/sensors_and_switches_windows_and_glass/power_window_switch/component_information/testing_and_inspection/master_switch_test/replacement/page_1241/)
   establishes a **20P connector** and driver's window control electronics
   in the master switch, but that LX excerpt alone does not approve
   EX-specific cavity assertions.
4. If feed and return are demonstrated, compare inputs, directional
   command, output under load, door harness and motor/mechanism in that
   order. For reversal, a motor's terminal polarity may swap; never
   assume a permanent ground on a directional output. Use the motor
   isolation instructions applicable to the installed option.
5. Verify the VIN's recall completion and any updated repair action.
   After an identified repair, demonstrate manual up/down; check AUTO
   operation/relearn separately where fitted.

**No step above has been reported complete**, including testing #23.
“Likely fuse,” “bad motor,” and “bad master switch” remain hypotheses,
not a confirmed fault.

## Assistant failure record — what to prevent

1. **Wrong diagnostic order:** The assistant gave connector pinouts and
   motor tests before finding the per-window fuse. It should have
   established which other windows worked and checked dedicated
   protection first.
2. **Conflated common and branch protection:** Working other windows
   can eliminate or lower common-feed hypotheses; it cannot rule out
   a fuse feeding **only the driver's window**. The correction was given
   only after the user raised it.
3. **Ignored supplied facts:** Re-asked whether ignition was ON after
   the user had established it. Suggested the battery negative post
   for a ground lead even though the user was working at the door with
   an appropriate nearby bolt-head attachment.
4. **Changed instrument without evidence:** Treated the reported
   indication as a multimeter measurement, although the user used a
   test light. Record instrument and hookup as reported; do not
   transform the observation into another instrument's capability.
5. **Unverified precision:** Presented master-switch pin positions,
   colors, directional output assignments and a hand-drawn numbered
   layout too confidently without a checked, correct-side, exact-model
   connector diagram. **Do not reuse the assistant's pin/cavity
   assignments as service data.** The supplied URL or an image search
   is not proof of the correct installed connector view.
6. **Bad inference from negatives:** Clean-looking contacts do not
   establish conductivity under load; multiple hot test points do not
   prove the specific fuse, controller, output or motor is healthy.
7. **Poor listening:** Lengthy speculation displaced the user's
   immediate question: where to test the fuses and what the observed
   working windows imply. Ask only for a missing distinction that
   actually changes the next test.

### Correct short answer at the point of failure

> The other windows working makes the shared 40 A fuse and window
> relay less likely. But each window has its own fuse: on this 2002
> CR-V the driver's is **under-dash #23, 20 A**. Test its two exposed
> terminals with your test light before we investigate the motor.

This wording identifies the simplest discriminator without claiming
the fuse is blown, the motor is bad, or the vehicle has been repaired.

## Recall is a separate safety boundary

[American Honda, December 15, 2020](https://hondanews.com/en-US/releases/release-e1a157df687ff71da1f64a190f016099-statement-by-american-honda-regarding-power-window-master-switch-recall-2002-2006-honda-cr-v-2020)
announced a **replacement** recall for certain 2002–2006 CR-V
master power-window switches, superseding the 2012 repair campaign.
Moisture can damage the PCB, increase resistance, overheat/melt the
switch and damage the harness; fire is possible. Check the individual
VIN at [Honda's recall lookup](https://owners.honda.com/service-maintenance/recalls).
The earlier [Honda bulletin 12-067](https://static.nhtsa.gov/odi/rcl/2012/RCRIT-12V486-1675.pdf)
describes older inspection/repair variants, **not** the current
replacement decision. No visible corrosion and a lit tester do not
establish recall completion or eliminate internal damage. Do not
continue energized probing if there is heat, smoke, melting or odor.

## Evidence states

- **SOURCE:** 2002 owner manual fuse charts and period Honda service
  excerpts linked above; scoped documents, not a VIN-level approval.
- **REPORTED:** single abrupt driver's failure, other windows operating,
  ignition ON, tester and ground setup, apparent 12.6 V at four
  receptacles, no visible damage.
- **NOT_RUN / UNKNOWN:** #23 fuse result, loaded driver feed, pin
  orientation, commanded output, motor test, recall status, exact cause,
  repair and repeatable retest.
- **ADMISSION:** working fieldbook case only; not approved retrieval
  evidence, not an accepted repair, and not a reviewed video transcript.
