# Suspension response: geometry, identification, and linked notes

Date: 2026-09-11.

**Status: documentation and proposed analysis. No new truck measurements, fitted adjustment coefficients, repair prescription, or physical acceptance.**

This follows the owner's request to retain the eccentric-cam/Jacobian/curvature discussion in ASE, Econometrician in a Box, Fulton, and Coxeter. The [full Dakota derivation](dakota-cam-jacobian-curvature.md) remains the mechanical and mathematical starting point; this note does not replace it or alter its equations.

## What belongs where

- **ASE:** the actual mechanism, vehicle-specific measurement validity, repeatable settled states, and the evidence required before an adjustment prediction. See the [derivation](dakota-cam-jacobian-curvature.md), [measurement gate](alignment-measurement-validity.md), [plausibility gate](alignment-result-plausibility.md), and [field worksheet](alignment-measurement-checklist.md).
- **[Econometrician in a Box](https://github.com/bl4ckb4ll/econometrician/blob/main/notes/suspension-response-identification.md):** identifying local responses from interventions; correlated observations; input uncertainty; weak inverse directions; and the distinction between estimation and a mechanically valid adjustment.
- **[Fulton](https://github.com/walnut-burgundy/fulton/blob/main/references/mikhail-gromov/suspension-response-geometry.md):** the source-to-application argument for tangent/normal decomposition, pullback flatness, the Gauss equation, and normal tolerance bands. It distinguishes the paper's geometry from our suspension application.
- **[Coxeter](https://github.com/isomorphismes/coxeter/blob/main/notes/suspension-response-structure.md):** retaining spaces, maps, units, metrics, orientations, and exact hypotheses rather than treating every matrix or sign as the same object. No compiler feature or group-theoretic speedup is established by these notes.

These are complementary notes, not four independent calibrations. Keep a single provenance chain for any future measured response fit.

## The experiment the discussion actually calls for

The local question concerns the two front/rear **lower-control-arm** eccentric adjustments of the 2005 Dakota case, not a generic upper-arm arrangement. The mechanism source is recorded in [Gromov and the Dakota suspension application](../sources/reviewed/gromov-curvature-suspension.md). The existing vehicle and instrument checks still control any use of specifications or procedures.

Distinguish actual eccentric rotation from actual pivot displacement along the slot. Record the zero, viewing direction, units, approach direction, and uncertainty. A counted wrench movement is not automatically a measured pivot displacement. A road-wheel steering sweep varies a different input and does not identify the cam response.

A useful future record would preserve:

| Record | What must remain visible |
| --- | --- |
| Adjustment | Which wheel and pivot, before/after settings, measured movement, units, uncertainty, and approach direction |
| Physical conditions | Load and location, tire conditions/pressures, four contact-pad elevations, relevant ride-height observations, and settling history |
| Raw observations | Original instrument readings and individual road-wheel sweep positions, timestamps, runout/reference information, and repeats |
| Derived outputs | Caster/camber only after the existing arithmetic, geometry, vehicle-plausibility, and cross-check gates |
| Fit | Coordinate definitions, neighborhood, derivative estimates, uncertainty, correlations, rank/conditioning, and excluded observations with reasons |
| Validation | A separately observed small response not used to fit the local model, compared with its prediction and uncertainty |

This is a data specification, not an instruction to loosen, force, or experimentally load suspension components. Physical adjustments must follow the applicable service procedure and safe support requirements.

## Conditions are not interchangeable nuisance labels

Changing the gauge reference and physically changing the wheel supports are different interventions. Load can change the passive equilibrium and the local cam response, rather than merely adding a fixed offset. Observed ride height may be an outcome of loading; it must not be silently treated as an independently controlled cause in the same experiment.

If returning to a setting from opposite directions produces incompatible settled readings, first investigate state/history dependence. Do not average two mechanical branches and call the resulting curve the truck's response law. A smooth local derivative is conditional on a specified, repeatable branch.

Repeated outputs from one shared baseline or steering sweep have shared error. Generating many pairwise differences does not create new independent measurements or independent cam movements.

## What the geometry does and does not authorize

The Jacobian describes local adjustment directions. Hessians describe how those directions change in declared coordinates. Normal second-order departure describes bending of an attainable path or surface. Intrinsic curvature requires a specified metric. These distinctions are worked out in the linked notes.

A residual outside the cams' local tangent response is not automatically evidence of a bent part. An omitted physical condition, invalid observation, unmodeled freedom, or incorrect model remains a competing explanation. Two available controls also do not guarantee that a target lies inside the safe attainable range.

**Current numerical status remains UNKNOWN:** this truck's Jacobian entries, usable inverse neighborhood, response Hessians, curvature radii, and load-dependent gain changes have not been identified by this documentation work.

## Source and validation boundaries

The earlier derivation's source record separates Gromov's paper, its reading guides, the service-manual mechanism, and our own derivations. The companion posts retain that separation. They do not mirror the paper or assert new redistribution rights.

This cross-post adds navigation and an identification/evidence plan. It changes no raw record, existing mathematical check, numerical threshold, executable behavior, or service specification. Earlier synthetic checks are not new vehicle evidence and are not reported here as a fresh test run.
