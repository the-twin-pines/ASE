# Front-end diagnostic patterns

This file is the reusable layer distilled from reviewed A4 sources. It is meant to improve real troubleshooting answers, not memorize test facts.

## A wheel shake is an input, not a diagnosis

The common hand tests are useful because they load several joints, but the clock position alone does not identify the failed part.

When a wheel moves, watch the boundaries:

- **tie rod end:** does the stud/socket or tie rod move late relative to the knuckle when steering input reverses?
- **ball joint:** does the knuckle move relative to the control arm at the joint?
- **hub/bearing:** does the wheel/rotor/hub move relative to the knuckle or bearing housing?
- **control-arm bushing:** does the arm translate excessively relative to its chassis mount under load?

The question is always: **where is the lost motion?**

This prevents the lazy rule “3-and-9 means tie rod, 12-and-6 means bearing.” Those positions are useful starting inputs, not component oracles.

## Loading matters

Ball joints are especially easy to inspect incorrectly because suspension architectures carry spring load differently.

Do not assume every lower joint is the load-carrying joint or that every upper joint is merely a follower. Determine the design and use the vehicle procedure. A joint that is still loaded by spring force can appear tight even when it has wear; an incorrectly unloaded design can also produce misleading motion.

A generic video demonstration is therefore best treated as a way to recognize **relative looseness**, not as a universal lifting procedure or wear specification.

## Noise needs a reproducing condition

“Clunk,” “rattle,” and “groan” are not parts names.

Useful conditions to preserve:

- knock/rattle mainly over small bumps → inspect links, bushings, mounts, ball joints, tie rods, and anything that can reverse load rapidly;
- sway-bar-link diagnosis becomes much stronger when the link can be moved by hand, its joint separates, or it visibly strikes nearby structure;
- groan/hum that changes as the vehicle is gently loaded left/right → wheel bearing becomes plausible, but confirm at the hub rather than replacing from the road test alone;
- repeated bouncing, float, excessive brake dive, or poor body control → damping problem becomes plausible; inspect shocks/struts and mounts.

Try to reproduce the symptom in a way that loads the suspected component, then inspect while that load is applied.

## Shock/strut fluid: distinguish weepage from leakage

A little oil film is not the same thing as a failed damper.

Monroe's service guidance distinguishes acceptable light weepage from real leakage. A unit that is broadly wet, dripping, physically damaged, or accompanied by degraded damping is a much stronger failure case than a faint film around the seal.

This is a useful correction to simplistic videos that say any visible oil means replacement.

## Alignment is downstream of measurement validity

Do not use an alignment rack or inclinometer to hide looseness, sag, tire force, or a bad reference surface.

Before treating caster/camber/toe adjustment as the repair, pass the complete gate in `alignment-measurement-validity.md` and record the field data in `alignment-measurement-checklist.md`.

At minimum:

1. verify tire application, pressure, wear/damage, and wheel/runout concerns;
2. inspect steering/suspension for looseness or binding with the design-correct loading method;
3. measure OEM ride height at its specified datum;
4. survey all four wheel-contact/pad elevations, not one vague “level” reference;
5. settle the suspension and establish the instrument/runout/turn-plate references;
6. distinguish **RAW**, **REFERENCE-CORRECTED**, **DERIVED**, and **UNKNOWN** values;
7. derive caster only from a valid instrument-specific, actual-per-wheel steering sweep;
8. inspect the vehicle-specific adjustment geometry before prescribing movement;
9. remeasure every angle that the chosen adjustment couples into; set toe last only where the vehicle procedure says it is final.

Tie-rod replacement directly changes toe. Control-arm, strut, knuckle, cradle, or ride-height changes can also alter alignment depending on architecture. The direction and sequence of correction come from the actual suspension/service procedure, not a generic mnemonic.

## Separate free articulation from free play

Ball-and-socket joints must articulate. Movement through the designed angle is not itself a defect.

The defect is lost motion inside the joint: the input reverses but the connected part does not immediately follow, the stud shifts axially/radially beyond specification, or the socket rattles instead of moving with controlled resistance.

That distinction matters for tie rods, ball joints, and many sway-bar links.

## Better answer shape for suspension questions

When given a symptom, avoid dumping a parts list. A better response is:

1. name the most useful reproducing condition;
2. say which component boundary to watch or measure;
3. say what relative motion/noise would implicate that component;
4. say what the test does **not** rule out;
5. choose the next boundary if the first one is tight.

For alignment photographs, the equivalent answer shape is:

1. transcribe only what is actually legible as **RAW**;
2. state the setup/reference facts already known;
3. state which displayed/raw values survive those setup uncertainties;
4. mark unsupported corrections/derived quantities **UNKNOWN**;
5. ask for the smallest missing measurement that makes the next inference valid;
6. only then prescribe an adjustment.

That structure prevents a precise-looking number from outrunning its evidence.
