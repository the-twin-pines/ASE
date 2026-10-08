# The Ram Man — proportioning, metering, and brake-valve distinctions

Status: **partial source review + companion-document corroboration**. The supplied playlists contain multiple Ram Man proportioning-valve videos, but this pass is based on the exact video metadata plus The Ram Man's own brake-hydraulic companion document rather than a full transcript.

## Supplied videos in this family

- `qzUk8W1-2pw` — **PROPORTIONING VALVES EXPLAINED by TheRamManINC.com** — 12:35
- `UR8FUjFOrmA` — **PROPORTIONING VALVES - HOW TO TEST FOR LEAKS (PART 1 OF 2), BY THERAMMANINC.COM**
- `is0AHkchX9U` — **PROPORTIONING VALVES - HOW TO TEST FOR LEAKS (PART 2 OF 2), BY THERAMMANINC.COM**
- `BBTOp-Xzgug` — **PROPORTIONING VALVES EXPLAINED- BY THERAMMANINC.COM** — 12:52

## What the companion hydraulic document actually distinguishes

The Ram Man's `Brake_Hydraulics.pdf` keeps three functions separate:

- **proportioning valve** — regulates pressure build-up to the **rear brakes** to reduce rear-wheel lockup during hard braking;
- **metering valve** — on the historical disc/drum systems discussed in the document, delays/holds off **front disc** pressure at low pressure so front application does not get ahead of the rear drums;
- **hydraulic safety/differential switch** — a separate warning/safety function, although later assemblies may combine functions in one housing.

That functional distinction is much more useful for ASE work than memorizing the shape of a combination valve.

## Application-specific numbers: keep them labeled

The document gives an old Mopar-style proportioning-valve test using roughly **500 psi** at the master-cylinder side and expecting about **350–400 psi** at the valve output. It also describes a metering-valve holdoff range of roughly **10–135 psi** on the floating-caliper systems under discussion.

These are useful examples of how the valves behave and how pressure gauges can test them. They are **not universal specifications** for modern vehicles and should never be memorized as generic ASE numbers.

## Bleeding interaction

The same source warns that a pressure bleeder operating at low pressure can interact with the metering valve. In the particular system described, about 30 psi from a pressure bleeder can keep the metering valve from allowing normal front-circuit flow, so the valve's push rod is held open during that bleeding procedure. This is another application-specific procedure: always follow the service information for the actual hydraulic layout.

## Diagnostic takeaways

1. Name the valve by its **job**, not by the block it happens to live in.
2. A rear-lockup complaint can involve rear pressure proportioning, but do not condemn the valve before checking friction, tire, load, hydraulic, and mechanical causes.
3. A pressure-regulation valve is testable with pressure measurements; title-level guesses are not enough.
4. A combination block may contain several logically different functions. Diagnose the function that matches the symptom.
5. Bleeding procedure can depend on valve state and system layout; a generic sequence is not automatically correct for every vehicle.

## Companion source inspected

- The Ram Man, `Brake_Hydraulics.pdf`: https://therammaninc.com/files/categories/Brake_Hydraulics.pdf
