# Dakota alignment cams: Jacobians, attainable measurements, and curvature

Date: 2026-09-11.

**Status: source-grounded mathematical synthesis, not a measured truck calibration or an adjustment prescription.** The application and derivations below are ours; Gromov did not analyze this suspension. Numerical entries of this truck's cam Jacobian, Hessians, and response curvature remain **UNKNOWN**.

The immediate question is concrete: what happens to caster and camber when the front and rear lower-control-arm eccentric cams move? The broader question is how intentional adjustments and unintended changes in load, tire support, ground geometry, and measurement reference reach the observations.

The source record is [Gromov and the Dakota suspension application](../sources/reviewed/gromov-curvature-suspension.md). Existing [measurement validity](alignment-measurement-validity.md), [result plausibility](alignment-result-plausibility.md), and [current Dakota case](dakota-alignment-case.md) remain authoritative for the evidence actually available. This note does not revise their raw observations or manufacture valid caster from an unmeasured steering sweep.

## 1. The mechanism, rather than two independent alignment knobs

The 2005 Dakota workshop manual, wheel-alignment section 2-5, locates both adjustments at the **front and rear lower-control-arm cam bolts in slotted frame brackets**. Rear-pivot motion primarily affects caster; common front/rear motion primarily affects camber. Neither operation leaves the other angle exactly unchanged. The upper arm is not the alignment adjuster. See source [D] in the source record.

Use these variables for one front wheel:

- `q = (q_f, q_r)`: actual front/rear eccentric rotation, with specified zero and viewing direction;
- `u = (u_f, u_r)`: actual pivot displacement along each bracket slot, positive outward;
- `eta`: the other independently specified conditions, such as loading, pad elevations, tire pressures, steering reference, and measurement setup;
- `y = (gamma, chi)`: camber and caster, respectively. Positive camber is top outward; positive caster is upper steering pivot rearward.

Use radians in derivatives and trigonometric formulas unless a different unit is explicitly retained throughout. Cam angle and road-wheel steering angle are different inputs.

At a repeatable settled state the reduced map is

$$y=F(u;\eta),\qquad u=c(q;\eta).$$

This notation does not assert that two eccentric settings alone determine every real-world reading. A repeatable approach/settling protocol or an additional history state is needed when friction, tire scrub, backlash, or bushing hysteresis matters. A branch of equilibria must be selected before differentiating.

### What an honest geometric model would solve

Let `s` describe the passive configuration: arm and knuckle poses, compliant deflections, chassis attitude, and tire/contact state as required. Write the independent closure and static-equilibrium equations as

$$C(s,q,\eta)=0,\qquad y=H(s,q,\eta).$$

After removing redundant constraints and rigid-body freedoms, assume `C_s` is invertible on the stable branch being modeled. Implicit differentiation gives

$$s_q=-C_s^{-1}C_q,\qquad J_q=H_q-H_sC_s^{-1}C_q.$$

That is a way to compute the actual adjustment Jacobian from hard-point geometry and constitutive assumptions. A singular `C_s` is a separate problem from a singular cam-to-angle Jacobian.

For a direction `v` in cam coordinates, the second configuration derivative is

$$s_{vv}=-C_s^{-1}\{C_{ss}[s_v,s_v]+2C_{sq}[s_v,v]+C_{qq}[v,v]\}.$$

Differentiating `H` then supplies the output second derivatives. None of these expressions supplies missing hard-point dimensions, stiffnesses, or contact laws.

The physical angle definitions also matter. In a reference frame with `x` forward and `z` vertically upward, let `d=U-L` run from the lower to the upper ball joint. Then, for the side-view caster convention,

$$\chi=\operatorname{atan2}(-d_x,d_z),\qquad
 d\chi=\frac{-d_z\,dd_x+d_x\,dd_z}{d_x^2+d_z^2}.$$

For an outward unit wheel-plane normal `n`, camber near the normal operating orientation is `gamma = -arcsin(n_z)`. The wheel-plane normal and the steering-axis direction are different objects: lateral steering-axis inclination is not automatically camber. The upper ball joint can move passively even though the upper arm is not the cam adjuster.

## 2. The Jacobian in pivot coordinates

At fixed `eta`,

$$J_u=DF=
\begin{pmatrix}
\gamma_f&\gamma_r\\
\chi_f&\chi_r
\end{pmatrix},\qquad
\begin{pmatrix}d\gamma\\d\chi\end{pmatrix}
=J_u\begin{pmatrix}du_f\\du_r\end{pmatrix}.$$

Subscripts denote partial derivatives with respect to the indicated pivot displacement. Each column is one adjustment's arrow in the camber/caster plane. The arrows need not be perpendicular or have the same length.

A small desired change `dy` has the first-order solution `du = J_u^{-1} dy` only where the matrix is invertible. This is a local prediction, not permission to extrapolate across the whole adjustment range. Actual displacement limits still restrict the reachable target set.

The determinant describes oriented area change. Its sign reverses when one input convention is reversed; it is **not** a curvature sign. Near-parallel columns mean that the two controls produce nearly the same output direction. A small singular value of an appropriately scaled Jacobian identifies a direction with weak adjustment authority.

Scaling is part of this statement. Compare changes relative to declared input scales and output tolerances or uncertainties before reporting a condition number. Millimetres versus inches, or different weighting of caster and camber, otherwise changes the numerical answer for an arbitrary reason.

### A first-order mechanical sketch, explicitly not a Dakota calibration

There is a useful geometric explanation for common and differential adjustment. It does not require inventing numerical gains.

In an idealized horizontal projection, place the rear pivot at `(0,0)`, the front at `(D,0)`, and the lower ball joint at `(alpha D,b)`, with `b` outboard. Consider infinitesimal lateral pivot motions. Approximate the lower arm as rigid to first order, the upper ball joint as fixed for this increment, the vertical ball-joint separation as `h`, the existing tilts as small, and the steering reference as fixed. With a rigid knuckle under those approximations,

$$dL_{out}=\alpha\,du_f+(1-\alpha)\,du_r,
\qquad dL_x=-\frac bD(du_f-du_r).$$

The resulting leading-order sketch is

$$
\begin{pmatrix}d\gamma\\d\chi\end{pmatrix}
\approx\frac1h
\begin{pmatrix}
-\alpha&-(1-\alpha)\\
-b/D&b/D
\end{pmatrix}
\begin{pmatrix}du_f\\du_r\end{pmatrix}.
$$

Common motion gives approximately `d gamma = -du/h` and `d chi = 0`. Differential motion changes the projected arm orientation and the fore/aft location of the lower ball joint. Unequal camber leverage comes from the ball joint's position relative to the two pivots.

This is an infinitesimal explanatory model, not an exact finite linkage closure. The real slot directions, arm shape, upper-arm response, steering linkage, three-dimensional closure, and compliance must replace these approximations before calculating a truck-specific matrix. In particular, no numerical value of `alpha`, `b`, `D`, or `h` is claimed here.

## 3. The factory compensation instruction is an implicit curve

Suppose the intention is to change caster while preserving camber. The tangent condition is

$$0=d\gamma=\gamma_f\,du_f+\gamma_r\,du_r.$$

Where `gamma_f` is nonzero,

$$\boxed{\frac{du_f}{du_r}=-\frac{\gamma_r}{\gamma_f}}.$$

The caster gained along that constant-camber direction is

$$\boxed{
\left.\frac{d\chi}{du_r}\right|_{\gamma}
=\chi_r-\chi_f\frac{\gamma_r}{\gamma_f}
=\frac{\det J_u}{\gamma_f}.
}$$

This gives a precise interpretation to a small opposing front-pivot correction during a rear-pivot caster adjustment. It is a ratio of **local derivatives**, not a universal ratio of wrench turns. When the determinant is small, holding camber consumes most of the caster authority. If `gamma_f` is small, interchange the roles of the pivots or use a different tangent parameter; division by a nearly zero derivative is not a stable recipe.

The curve itself can bend. Write `u_f=p(u_r)` along a fixed camber level. Differentiating again gives

$$p''=-\frac{\gamma_{rr}+2\gamma_{fr}p'+\gamma_{ff}(p')^2}{\gamma_f}.$$

That second derivative says how the compensating ratio must change as the operating point moves. It is already a useful second-order quantity before any intrinsic Riemannian curvature is introduced.

## 4. Eccentric rotation adds its own nonlinearity

Even if the suspension response were linear in actual pivot displacement, it need not be linear in cam rotation.

For an ideal eccentric driving a straight slot, an illustrative law is

$$u_i=u_{i0}+e_i\cos(q_i+\phi_i).$$

The eccentricity and phase are mechanism parameters, not supplied Dakota measurements. A different actual guide/contact arrangement requires its own displacement law.

Under this separable idealization,

$$J_q=J_u\begin{pmatrix}
-e_f\sin(q_f+\phi_f)&0\\
0&-e_r\sin(q_r+\phi_r)
\end{pmatrix}.$$

Equal cam rotations therefore need not produce equal pivot displacements. Near an eccentric's displacement extremum, first-order gain with respect to its angle vanishes and reverses sign across the extremum. This can be a turning point of the parameterization without any special curvature singularity in the suspension's response set.

The full second-order chain rule separates the effects:

$$D^2(F\circ c)[v,w]
=D^2F[Dc\,v,Dc\,w]+DF\,D^2c[v,w].$$

The first term is the changing suspension response in pivot coordinates. The second comes from the eccentric displacement law. Calling their sum simply “curvature” hides an important distinction.

For a concrete counterexample, take `F(u)=A u` with constant matrix `A`, and move only one cam through `u_i=e_i cos(q_i)`. Its output lies on a straight line, although the second derivative with respect to cam angle is generally nonzero. The motion speeds up and slows down; the line does not bend.

## 5. Hessians predict local errors; they are not automatically intrinsic curvature

For a smooth fixed-setup map, write the second-order expansion

$$F(u+v)=F(u)+J_uv+\tfrac12D^2F[v,v]+O(\|v\|^3),$$

with the remainder statement requiring sufficient smoothness. There is one component Hessian for camber and another for caster. Mixed entries describe how moving one pivot changes the effectiveness of the other.

A scalar component Hessian has operational meaning once input coordinates and output convention are fixed. A vector-valued second derivative does not have one universal positive/negative sign.

For the weighted target error

$$E(u)=\tfrac12(F(u)-y_*)^T W(F(u)-y_*),$$

with fixed positive-definite `W`,

$$\nabla^2 E=J_u^T WJ_u+\sum_a\{W(F-y_*)\}_a\,\nabla^2F_a.$$

At an exact fit the second term vanishes. Away from the target, nonlinear response contributes to the optimization curvature. This is the curvature of a specified scalar objective in specified input coordinates, not a measurement of sectional or Ricci curvature of the truck.

## 6. Gromov's useful distinction: departure normal to the tangent

Gromov's section 0, especially printed pages 10–13, interprets the second fundamental form as second-order departure from a tangent space. His section 1, pages 34–37, distinguishes metric geometry from coordinate effects. These are the starting points for the following application, not a truck theorem from the paper. See source [G].

First choose a measurement geometry. For example,

$$z=L y,\qquad L^T L=W,$$

where `W` is a fixed weighting based on declared tolerances or a fixed nonsingular noise covariance. These are different purposes and should be labeled accordingly. A distance in this space is a distance between alignment outcomes, not a physical distance in the suspension.

### One cam fixed: a genuinely curved attainable path

If the rear pivot is held fixed, the attainable standardized outcomes form the curve

$$z(t)=L F(t,u_{r0}).$$

This is also the appropriate conditional model if an adjuster cannot move; the present note does not establish whether any particular cam is currently seized.

At a regular point, `z'` is the tangent. Its second derivative splits into a tangential part and a normal part:

$$B=\left(I-\frac{z'z'^T}{z'^Tz'}\right)z''.$$

The tangential part can reflect changing speed. The normal part measures departure from the tangent line. For a plane curve, signed curvature is

$$\boxed{\kappa=\frac{\det(z',z'')}{\|z'\|^3}}.$$

Its sign uses a chosen output-plane orientation and direction of traversal. Curvature magnitude is independent of a regular reparameterization of the same path, although changing the measurement weighting changes the geometry being measured. At `z'=0`, this formula does not define a regular parameterized-curve curvature.

Practically, one free cam gives one curve, not independent control over every caster/camber pair. The tangent predicts the immediate tradeoff; normal curvature predicts how that tradeoff bends over a finite adjustment. A target off the curve cannot necessarily be reached by moving farther along it.

### Two independent cams and only two outputs: a flat metric can look complicated

Pull the fixed measurement metric back to the two control coordinates:

$$g=J_u^T WJ_u.$$

Then `v^T g v` is the squared standardized output change caused by `v`. Where `J_u` is invertible, `z=L F(u)` itself is a local coordinate system and

$$g=dz_1^2+dz_2^2.$$

Therefore **this particular metric is locally flat**, even if its entries vary strongly in cam coordinates. There is no normal direction to the interior of an open region of the two-dimensional output plane.

A synthetic example makes the distinction explicit:

$$F(a,b)=(a,b+c a^2),\qquad
 g=\begin{pmatrix}1+4c^2a^2&2ca\\2ca&1\end{pmatrix}.$$

Here `det g = 1`. The only nonzero Christoffel coefficient is `Gamma^b_aa=2c`; the Riemann tensor vanishes. Yet fixing `b` gives a parabola with

$$\kappa=\frac{2c}{(1+4c^2a^2)^{3/2}}.$$

Thus a fixed-control path can bend inside an intrinsically flat full response space.

This does not say every meaningful geometry associated with a suspension is flat. A kinetic-energy metric, an effort penalty added to `g`, position-dependent statistical weights, or an orientation-space metric is a different construction. At rank loss, `J_u^T WJ_u` is degenerate, not an ordinary Riemannian metric.

Gromov's page 42 identification of Gaussian curvature with a Jacobian concerns the **Gauss normal map of an immersed surface**, with the associated metrics. The cam-to-caster/camber map is not automatically a Gauss map. Consequently `det J_u` is not Gaussian curvature.

## 7. A direct application of equidistant deformation: tolerance bands

Gromov's section 0 also studies normal offsets and their loss of regularity. We can apply that construction literally to a tolerance band around an attainable measurement curve, rather than pretending the physical cams follow a normal geodesic flow.

Let `z(s)` be an attainable curve parameterized by arc length in the fixed standardized measurement space. Choose unit tangent `T`, unit normal `N`, and signed curvature so that

$$T'=\kappa N,\qquad N'=-\kappa T.$$

Points in a normal tolerance band are

$$\Psi(s,r)=z(s)+rN(s).$$

Differentiating gives

$$\boxed{\Psi_s=(1-r\kappa)T,\qquad \Psi_r=N.}$$

With the compatible plane orientation, its Jacobian is `1-r kappa`. Normal coordinates fail at `r kappa=1`: distinct neighboring normals focus to first order.

There is a direct fitting interpretation. For an observed point `z_* = z(s_0)+rN(s_0)`, define

$$E(s)=\tfrac12\|z(s)-z_*\|^2.$$

Then at `s_0`,

$$E'(s_0)=0,\qquad E''(s_0)=1-r\kappa(s_0).$$

When this is positive and the stationary point is the relevant local nearest point, its response to a small change in observation is

$$\delta s=\frac{T\cdot\delta z_*}{1-r\kappa}.$$

This explains a specific possible failure: a nearly flat nearest-setting objective can turn a small measurement change into a large inferred change along the adjustment curve. On the opposite normal side, the factor can instead improve local conditioning.

A narrow uncertainty/tolerance band is locally well behaved when its width is small compared with the radius of curvature. Global uniqueness also requires separation from other parts of the curve; distant portions can approach each other before any local focal condition occurs. Neither uniqueness nor a problematic radius has been measured for this truck.

This is a real mathematical use of the paper's geometry. It is not evidence that cam motion itself satisfies Gromov's tube equation or that positive caster implies positive sectional curvature.

## 8. More measurements create room for a response surface to bend

With two cam controls and additional independently useful outputs, consider a standardized response

$$Z(u)=(\text{camber},\text{caster},\text{toe},\text{ride height},\ldots)\in\mathbb R^m,\quad m>2.$$

All components here have been scaled by a specified fixed measurement geometry. Degrees and millimetres must not be added as naked squared distances. Redundant derived measurements can make a covariance singular; choose an independent set or state the reduced measurement subspace.

At rank two, let `J=DZ`, `g=J^T J`, and

$$P_\perp=I-Jg^{-1}J^T,\qquad B_{ij}=P_\perp\,\partial_i\partial_j Z.$$

The normal-valued second fundamental form records which second-order output changes cannot be reproduced by a first-order change of the two controls. Pure input-reparameterization acceleration lies in the tangent image and is removed by this projection.

For this two-dimensional surface in a flat measurement space, the Gauss equation gives

$$K=\frac{\langle B_{11},B_{22}\rangle-\|B_{12}\|^2}{\det g}.$$

This is a candidate for genuine intrinsic Gaussian curvature of the **specified response metric**. Its sign cannot be inferred from the signs of caster/camber or from the mere fact that the outputs are coupled. In higher codimension, `B` itself has no single scalar sign without selecting a normal direction.

For diagnosis, an observed residual normal to the reachable tangent surface cannot be removed by the two cams to first order. That does not by itself identify a bent component: measurement error, an omitted load condition, a wrong model, or another unmodeled degree of freedom are still explanations. If those other conditions are allowed to vary, their Jacobian columns must be included before deciding what is uncorrectable.

## 9. Intentional and unintended variations belong in one model

Restore the setup parameters:

$$dy=J_q\,dq+J_\eta\,d\eta+\epsilon.$$

Ground geometry, loading, tire support, and gauge reference must be separated by mechanism. Some changes rotate the reference axes; others change the settled mechanical configuration; some do both. A reference correction does not automatically predict what the suspension would do after physically changing the supports. The branch's [measurement-validity note](alignment-measurement-validity.md) gives the corresponding four-pad and load checks.

The map can shift and its local adjustment gain can change:

$$\partial_\eta J_q=\partial_\eta\partial_q F.$$

Thus a cam correction calibrated at one load/ride-height state need not be the same correction at another. Ride height should not be counted as an independent input as well as a load-determined state unless the experiment actually controls it independently.

For small uncertain input variations `x=(q,eta)` with covariance `Sigma_x`, the first-order propagated covariance is

$$\Sigma_y\approx D_xF\,\Sigma_x\,D_xF^T+\Sigma_\epsilon,$$

assuming independent residual sensor noise. The full input covariance retains correlations between cam positioning and setup variations. A common systematic reference error is not made independent by taking more readings.

At second order, a centered perturbation can still shift the mean:

$$\mathbb E[F_a(x+\delta x)]-F_a(x)
\approx\tfrac12\operatorname{tr}(H_a\Sigma_x).$$

That is a curvature-of-response bias in the stated coordinates, not automatically an intrinsic-curvature effect. Large perturbations, stick-slip transitions, or changing contact branches require more than this smooth local approximation.

The current case already records the owner's equal-pressure check. Pressure belongs in the general model, not as a newly asserted explanation for that case.

## 10. What would turn this into an identified truck response map?

The existing steering sweep and the cam experiment probe different derivatives. A sweep with fixed cams estimates sensitivity to **road-wheel steering**. It cannot, by itself, identify a cam-Jacobian column. Having many pairings of the same sweep readings does not create cam excitation or independent observations.

After the existing mechanical/measurement gates and exact service procedure are satisfied, an identification record would need known small pivot/cam changes, the settled state at each setting, and repeated valid caster/camber observations. Do not force an immovable cam or loosen a loaded suspension merely to populate a mathematical experiment.

For a repeatable fixed-setup map, central differences give

$$J_i\approx\frac{F(u+h_ie_i)-F(u-h_ie_i)}{2h_i},$$

$$F_{ii}\approx\frac{F(u+h_ie_i)-2F(u)+F(u-h_ie_i)}{h_i^2},$$

$$F_{fr}\approx\frac{F(u+h_fe_f+h_re_r)-F(u+h_fe_f-h_re_r)-F(u-h_fe_f+h_re_r)+F(u-h_fe_f-h_re_r)}{4h_fh_r}.$$

The step sizes must be actual known displacements with uncertainties, not an assumed conversion from wrench turns. Too small a step amplifies measurement noise, especially in second differences; too large a step ceases to be local. A quadratic two-input fit has six coefficients per output and requires a full-rank design, with repeats beyond the algebraic minimum to assess noise and drift. A center/axis/mixed-neighborhood design is more informative than repeatedly visiting only one adjustment direction.

Paired outputs, common baselines, and repeated sweeps produce correlated errors. For `n` raw scalar readings with covariance `Sigma`, all pairwise differences have covariance `D Sigma D^T`, with rank at most `n-1`; the number of pairs is not the number of independent measurements.

The next physically useful result is a measured local Jacobian with uncertainty and a stated operating point. The next question is whether its columns change detectably over the safe available adjustment range. Only then is a fitted second fundamental form or tolerance-band radius more than a proposed analysis.

## Checks and evidence boundary

Run from this branch:

```text
python3 scripts/check_alignment_math.py
python3 scripts/check_alignment_plausibility.py
python3 scripts/check_cam_jacobian_curvature.py
```

The existing checks remain unchanged. The added script checks synthetic compensation algebra, the illustrative lower-arm matrix, a nonlinear flat metric with a curved fixed-control path, changing cam speed without path curvature, the normal-offset Jacobian, and quadratic finite differences. These are mathematical regression examples, not fitted Dakota data, a verified repair, or physical-vehicle acceptance.
