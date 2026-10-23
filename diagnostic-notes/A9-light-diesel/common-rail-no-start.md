# A9 — diesel cranks but will not start: split supply, rail and enable

**Status:** synthetic common-rail diagnostic trace; no vehicle-specific
pressure target, equipment authorization or repair. A9 covers multiple
injection architectures; do **not** apply this common-rail branch to HEUI,
pump-line-nozzle or electronic unit-injector systems without identifying the
engine. See [2026 ASE A9 tasks, pp. 49–53](https://www.ase.com/uploads/ASE_Automobile_Study_Guide_2026.pdf).

Mechanism reference: [Delphi Technologies, Hard or non-start problems due to
fuel injection system](https://www.delphiautoparts.com/resource-center/article/hard-or-non-start-problems-due-to-fuel-injection-system).
Delphi's example concerns a **specific 2.0 HDi application**; its published
low-feed and rail-pressure numbers are **not universal specifications**.
Injector diagnosis reference:
[Delphi, Common Rail injector diagnosis](https://www.delphiautoparts.com/en-gb/mom/need-to-know/article/how-to-diagnose-typical-cri-faults-on-a-ford-mondeo-2.0-tdci).

## Separate the stages

`battery/cranking speed → synchronization and start authorization →
 low-pressure fuel supply → high-pressure generation/retention →
 injector command → combustion/air/exhaust`

Rail pressure can be inadequate because the high-pressure pump is starved,
the pump/control valve cannot build pressure, fuel returns/leaks excessively,
or a sensor falsely reports the pressure. Conversely, apparently adequate rail
pressure does not prove injectors are commanded or that combustion is possible.

## Capture real observations

- Does the crankshaft rotate normally? Battery behavior *under cranking*,
  starter current if available, engine speed data and mechanical sound.
- Crank/cam synchronization, immobilizer/start enable and relevant fault codes.
- Rail **requested** versus **reported actual** during the same cranking window;
  record sampling cadence and whether the pressure sensor itself is plausible.
- Identified lift/transfer pump configuration; filtration, water/
  contamination/air entry, low-side electrical power and supply state.
- Any recent filter, injector, timing, tank or high-pressure work.
- Smoke/smell/exhaust observations recorded only when safe and not treated as
  proof of successful injection.

## Hypotheses by discriminator

| Observation | Candidate | Still unknown |
| --- | --- | --- |
| No/weak low-side delivery *by approved method* | Filter, feed, low-pressure pump, electrical supply or air leak | High-pressure pump condition |
| Low side meets exact procedure, but requested rail differs from reported actual | High-pressure generation/control, leakback, sensor issue | Which individual part failed |
| Reported rail acceptable, but no injector enable | Security/sync/ECM or other inhibit | Injector mechanical health |
| Injector command and rail appear adequate | Compression, timing, glow/temperature where applicable, air/exhaust, fuel quality | Original physical cause |

Only qualified equipment and exact engine procedures may isolate the
high-pressure circuit or measure injector return. Delphi describes specialist
sealed-rail and injector back-leak tools; **do not loosen, crack open, spray
or feel for leaks at high-pressure diesel lines, including during cranking**
and after shutdown when pressure may be retained. Skin injection injury can
occur. No starting-fluid shortcut or improvised high-pressure gauge connection.

## Proposed verification

Identify the actual architecture, obtain approved low/high-side procedures,
capture paired commanded/actual data, then choose the least invasive
discriminator. After repair, verify normal starts under the original cold/
hot conditions and absence of repeated codes/leaks.

Vehicle and fault `UNKNOWN`; pressure/service approval `UNKNOWN`;
instrumented and physical verification `NOT_RUN`.
