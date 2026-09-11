# Gromov curvature concepts applied to Dakota alignment

Review date: 2026-09-11.

Application: [Dakota cam Jacobian and curvature note](../../notes/dakota-cam-jacobian-curvature.md).

## [G] Mikhail Gromov — Sign and Geometric Meaning of Curvature

M. Gromov, *Rendiconti del Seminario Matematico e Fisico di Milano* 61 (1991), 9–123; expanded from a lecture delivered in 1990.

- [Official IHES record](https://www.ihes.fr/~gromov/expository/34/)
- [Official PDF](https://www.ihes.fr/~gromov/wp-content/uploads/2018/08/177.pdf)
- [Walnut/Burgundy reading guide](https://github.com/walnut-burgundy/fulton/blob/c5033874227918a621f9ffba2bc2905df6e29e07/references/mikhail-gromov/sign-and-geometric-meaning-of-curvature.md)
- [Coxeter cross-post](https://github.com/isomorphismes/coxeter/blob/97dd4547b098d35d912a452536414b97fc38fc5d/references/gromov/sign-and-geometric-meaning-of-curvature.md)
- [Hopf-fibration cross-post](https://github.com/isomorphismes/hopf_fibration/blob/f2fdb7e6d626d66df8af820d3acd0cba641fcc41/docs/references/gromov-sign-and-geometric-meaning-of-curvature.md)

Status: relevant primary-paper passages inspected. The discussion uses printed journal pagination, not a viewer's page count. The PDF begins on printed page 9.

Passages used: section 0, pages 10–13, for normal second-order departure and coorientation; pages 13–17 for equidistant offsets; section 1, pages 34–37, for Jacobians, metrics, coordinate effects, and local flatness; section 2, page 42, for the special role of the Gauss normal map. Page 11's tangent/normal figure and page 15's deformation formulas were inspected as page images. This is a targeted review, not a new full-paper verification of every older guide entry.

The response-space constructions, compensation equations, tolerance-band fitting calculation, and synthetic examples in the companion note are independently written applications. They are not attributed to Gromov as truck results. No scanned figures or paper text/PDF are added here; the official source remains linked.

## [D] 2005 Dodge Dakota workshop manual — wheel alignment

[Inspectable reproduction of the factory workshop manual](https://manualmachine.com/dodge/dakota2005/3868971-workshop-manual/).

Status: primary service-manual text inspected through a public mirror, particularly printed section 2-5, “Camber, Caster and Toe Adjustment.” This is not a newly verified exact-VIN specification or torque source.

The mechanism used in the mathematical note is the two lower-control-arm cam/slot adjustment, not an upper-control-arm arrangement. The source's qualitative rear-pivot and common-pivot instructions motivate the local Jacobian questions; they do not provide numerical derivative entries or a universal ratio of cam rotations.

Existing [alignment measurement sources](alignment-measurement-sources.md) and [plausibility sources](alignment-plausibility-sources.md) retain the vehicle/instrument qualifications and unresolved torque/specification boundaries. Nothing in this cross-post resolves those boundaries by assumption.

## Repository evidence

Read against suspension branch commit `63c81b29712d8a9a333d38a77ab86233adbf177a`:

- [Current Dakota case](../../notes/dakota-alignment-case.md): current observations and unsupported quantities remain as classified there.
- [Measurement validity](../../notes/alignment-measurement-validity.md): distinguish physical setup changes from reference corrections and retain the actual-wheel-angle requirement for caster sweeps.
- [Result plausibility](../../notes/alignment-result-plausibility.md): mathematical computability is not permission to prescribe an adjustment.

No valid cam-perturbation dataset was identified in that case record. This note introduces no numerical calibration, updated alignment reading, or diagnosis of a failed component.
