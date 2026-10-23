# A6 — voltage present is not a loaded electrical test

**Status:** general electrical diagnostic method, not a wiring diagram.
Sources: [Fluke, Electrical Automotive Troubleshooting](https://www.fluke.com/en/learn/blog/automotive/electrical-automotive-troubleshooting);
[2026 ASE A6 body-electrical/charging tasks, pp. 32–35](https://www.ase.com/uploads/ASE_Automobile_Study_Guide_2026.pdf).

For a conventional low-voltage motor/relay/load circuit, describe:

`source → protection → commanded switch/driver → load → return path`

Depending on the installed controller, switching may occur on the feed, on the
return, or electronically in both paths. A window motor can reverse its drive
polarity; do not assume one wire is permanently “ground.”

## Three instruments answer different questions

- **Test light:** lights when a particular path can supply enough current for
  that tester under that hookup. Its lamp/current demand is not the motor's.
  Tester polarity and electronic-module sensitivity matter.
- **High-impedance DMM voltage reading:** shows *potential difference* between
  two explicitly named points, often even through a circuit that cannot carry
  working load current. A reported 12.6 V is not a motor-current test.
- **Voltage drop under the actual commanded load:** probes the loss across
  a cable, fuse contact, switch or ground segment while current flows.
  A large drop localizes unwanted resistance in the measured segment.
  Fluke stresses that an idle/unloaded reading cannot substitute for this.

Never attach an incandescent test lamp to an unknown sensor/reference,
airbag, CAN, LIN or module signal terminal. Do not ohm-test a powered circuit
or short unknown terminals to see “what happens.” Use protected, connector-
appropriate methods and the exact circuit diagram.

## Four diagnostic partitions

| Observation | Candidate boundary | Next safe comparison |
| --- | --- | --- |
| No feed at switch under required key/command state | Fuse/relay/ignition/feed/harness | Verify BOTH fuse test points and upstream conditions using exact fuse legend |
| Feed exists, but collapses when load commands | High-resistance connection, weak feed, short/heavy load | Compare loaded feed at upstream and downstream points; record actual reference |
| Feed healthy, load command output absent | Switch/controller input, enable, or driver | Establish controller's required inputs and output mapping before replacement |
| Loaded supply and correct return at load, no movement | Motor, load binding, internal wiring | Compare motor behavior and mechanism using approved isolated test |

For return-side problems, compare the *load-side return node* to a verified
battery-negative/body reference **under command**. A convenient bolt head is
not automatically a good ground: verify it electrically, including paint,
looseness and corrosion. The meter reference is itself part of the test.

The physical fuse element, terminal tension and downstream short remain
separate questions. A fuse that blows again is a diagnostic clue; never
upspecify it or bypass fuse protection.

## Record each measurement

`point A / point B / key state / command / connector plugged? /
load moving or stalled? / instrument / result / expected per source`

Then state what the reading establishes and what it leaves UNKNOWN.
Sample numbers in a meter handbook do not become a vehicle-specific
acceptance threshold. Use the [exact-specification gate](../../specifications/README.md).
