# Alignment diagnostic patterns

This is the reusable alignment layer for the A4 branch. It is aimed at real diagnosis, not memorizing angle definitions or treating the alignment machine's red/green boxes as a diagnosis.

Primary source families used here:

- Hunter Learning Channel alignment-video catalog: https://phoenixtireequipment.com/all-videos/alignment-angles/
- Hunter Vehicle Alignment seminar training supplement: https://bccskillsusa.weebly.com/uploads/4/3/3/2/43327659/hec_alignment_manual_edu_2.pdf
- Hunter current alignment/collision material: https://www.hunter.com/alignment-machines/hawkeye-elite/ and https://www.hunter.com/collision
- QuickTrick current written caster/camber/toe procedure: https://quicktrickalignment.com/alignment-101/
- transcript-reviewed 1A Auto tire video: `sources/reviewed/1a-auto-tires-alignment.md`

The Hunter supplement is old training material, so its numerical examples and thresholds are not vehicle specifications. Use the geometry and diagnostic relationships, then use current vehicle service information for the actual limits and procedures.

## An alignment reading is a geometric observation

A measured angle tells where the wheel or steering axis is at the time and under the conditions of the measurement. It does not by itself tell why it is there.

An out-of-spec value can come from:

- an ordinary adjustment being wrong;
- a worn bushing or joint allowing the wheel to move;
- a spring or torsion-bar/ride-height problem;
- a bent arm, knuckle, strut, axle, frame, subframe, or mounting point;
- shifted cradle/subframe geometry;
- collision damage;
- load or vehicle attitude that changes the measurement reference;
- a measurement/setup problem.

The repair question is therefore not merely **which angle is red?** It is **what geometry produced that angle, and is that geometry stable when the vehicle is loaded?**

## Establish the measurement conditions before interpreting numbers

Before using alignment numbers as evidence:

1. verify tire size and inflation;
2. inspect the tires for unequal wear, obvious construction differences, damage, or circumference differences that can create a pull;
3. check the wheels for damage/runout when relevant;
4. inspect steering and suspension joints and bushings for play or binding;
5. verify ride height where the vehicle procedure calls for it or where sag/load is plausible;
6. make sure the suspension is settled and the wheels are free to move on the turn/slip plates during measurement;
7. know whether the vehicle or frame is level enough for the measurement being interpreted, and apply the vehicle's frame-angle procedure when required;
8. use the specified load state.

A good alignment machine cannot turn unstable suspension geometry into a valid static adjustment.

## Do not use an unlevel truck as an invisible zero reference

Caster is referenced to vertical through the steering axis, but truck frame pitch can matter to how the useful caster value is interpreted. Hunter's training material defines **frame angle** as the front-to-rear slope of the frame rail and provides a frame-corrected caster procedure for vehicles that require it.

The practical lesson is important:

- do not assume the truck is level merely because it is sitting still;
- do not treat a straight-ahead display or a raw inclinometer reading as a valid caster measurement if the measurement method requires a steering sweep or frame correction;
- measure the relevant reference rather than silently treating the floor/frame as zero;
- if left and right frame rails sit at different slopes because of setup, load, tire height, or chassis condition, investigate that before comparing small caster differences.

Hunter's supplement also says caster is calculated from steering the front wheels left and right, not from one straight-ahead snapshot. That is why a caster sweep contains information a straight-ahead camber-style reading does not.

## Adjustment order: rear geometry, then caster, camber, toe

For a total four-wheel alignment, Hunter's training sequence is:

1. rear camber, if adjustable;
2. rear individual/total toe and thrust angle;
3. front caster;
4. front camber;
5. front individual and total toe.

The durable rule for the front is **caster first, then camber, then toe** unless the vehicle-specific procedure requires another coupled sequence.

Why this order matters:

- caster and camber adjustments can interact on control-arm/eccentric/shim arrangements;
- moving control arms to change caster or camber can move toe;
- toe is therefore normally the last primary front angle to finalize;
- rear toe/thrust establishes the direction to which the front wheels should be referenced on a four-wheel alignment.

Some designs require iteration because one eccentric or arm position affects more than one angle. The sequence is not permission to ignore that coupling; it tells which target gets priority as the coupled geometry converges.

## Camber

Camber is wheel tilt viewed from the front. It is useful for both tire-wear and pull diagnosis, but it must be interpreted in context.

Important distinctions:

- a large individual camber error can produce edge loading/wear;
- a left-right camber difference can contribute to a pull or drift;
- camber that changes when the wheel is loaded can point to looseness rather than mere adjustment;
- severe camber difference with abnormal SAI/included-angle information is a bent/displaced-part problem until proved otherwise;
- ride-height changes can change camber on many independent suspensions.

Do not infer the failed component from camber alone. Watch where the knuckle, control arms, strut, subframe, or ball-joint pivots are actually displaced.

## Caster

Caster is the fore/aft tilt of the steering axis viewed from the side. Its important effects include directional stability and return-to-center.

For diagnosis:

- compare left and right caster under valid measurement conditions;
- distinguish a true cross-caster condition from vehicle/frame pitch or setup error;
- poor return-to-center can involve caster, but binding ball joints, strut bearings, steering gear/linkage, or improperly torqued/bound components can produce a similar complaint;
- do not increase or decrease caster to hide mechanical binding;
- after changing caster with control-arm/shim/eccentric adjustments, recheck camber and then toe.

A caster complaint is especially easy to misread on a truck sitting nose-high/nose-low or on a nonlevel measurement surface. Record the reference geometry rather than assuming it away.

## Toe

Toe is the directional relationship of the wheels viewed from above. It is highly sensitive and is directly changed by tie-rod length on common steering systems.

Useful distinctions:

- **total toe** says how the two wheels on an axle relate to each other;
- **individual toe** says how each wheel relates to the relevant vehicle/thrust reference;
- correct total front toe does not guarantee a centered steering wheel if individual toe is split incorrectly;
- a rear thrust angle can leave the front wheels and steering wheel apparently corrected relative to a crooked rear thrust direction while the vehicle dog-tracks;
- worn tie rods, control-arm bushings, or other moving pivots can make static toe change under road load.

Toe is usually finalized after caster and camber because the preceding adjustments can disturb it.

QuickTrick's current home-measurement instructions also use caster, camber, then toe and recommend stringing the vehicle when toe needs adjustment so the operator can determine which side needs correction. That is much better than changing both tie rods from a total-toe number with no vehicle reference.

## Rear toe, thrust line, and dog tracking

Do not stop at the front axle just because the complaint is felt at the steering wheel.

The rear wheels define a thrust direction. If the thrust line is not parallel to the geometric centerline, the vehicle can dog-track and the steering wheel/front individual toe can be misleading if the rear geometry is ignored.

Even when rear toe is not adjustable, measure it. A nonadjustable red rear reading is diagnostic evidence: it can point toward a bent axle, shifted/damaged suspension, cradle/subframe displacement, or body/frame damage.

**Nonadjustable does not mean irrelevant.**

## SAI and included angle are diagnostic measurements

Steering-axis inclination (SAI) is the inward tilt of the steering axis viewed from the front. Included angle is SAI combined with camber.

These are valuable because they help distinguish an ordinary camber-setting problem from displaced or bent steering/suspension structure.

Hunter's older training examples use large cross-SAI differences to direct inspection toward control arms, strut towers, frame/subframe, or axle geometry, and large cross-included-angle differences toward the spindle/knuckle/ball-joint-stud region.

Do not copy Hunter's example threshold as a universal specification. The useful pattern is:

1. establish that the camber difference is real;
2. measure SAI/IA with the specified procedure;
3. compare side-to-side and to vehicle specifications where supplied;
4. use the combination of camber, SAI, and included angle to decide which physical geometry to inspect;
5. do not try to 'adjust SAI' as though it were ordinary toe.

The measurement itself is also procedure-sensitive. Hunter's material warns that wheel rotation/brake slip during an SAI/IA steering measurement can falsify the result.

## Ride height is part of alignment geometry

Springs and torsion bars establish the suspension's operating position. A sagged corner or changed ride height alters control-arm and tie-rod angles and can therefore alter static and dynamic wheel geometry.

When a vehicle has:

- visibly unequal corner height;
- recent spring/torsion-bar/strut/control-arm work;
- added or removed permanent load;
- a truck with front/rear attitude noticeably different from specification;

measure ride height before deciding that the cure is an eccentric or shim adjustment.

If the suspension is sitting at the wrong operating point, an alignment adjustment can merely tune around the underlying ride-height problem.

## Bump steer is dynamic toe/steering geometry, not ordinary looseness

Bump steer is a direction/toe change caused by suspension travel. It occurs when the steering linkage does not follow the wheel's suspension arc appropriately.

To diagnose it, separate three questions:

1. Is there free play in the linkage? If yes, fix the lost motion first.
2. Does the wheel change toe/direction as suspension jounces and rebounds even with tight joints? That is a geometry problem.
3. Does the road merely deflect the tire/steering because of crown, ruts, or compliance? That is a different input.

Tie-rod angle and attachment geometry matter. A vehicle that changes direction over a dip/bump without steering-wheel command deserves inspection of linkage height/angles, rack or steering-gear mounting, bent parts, ride height, and any suspension modification that changed the relationship between the steering link and control arm.

## Memory steer: check binding before blaming caster

Memory steer is the tendency for the front wheels to seek or retain a position other than straight ahead after a turn.

A caster reading may look relevant because caster contributes to returnability, but a binding joint or mount can defeat the self-centering forces even when caster is acceptable.

Useful inspection targets include:

- upper strut bearing/mount;
- load-carrying or follower ball joints as appropriate to the design;
- tie-rod ends and inner joints;
- steering gear/rack and mounts;
- steering shaft/u-joints;
- bushings tightened in the wrong suspension position or otherwise bound.

Observe whether the steering releases smoothly through the full range before using alignment adjustment as the cure.

## Tire pull/conicity is a competing cause, not an alignment angle

A vehicle can pull with acceptable alignment because a tire generates lateral force. Pressure, construction, tread pattern, conicity/ply-steer, circumference, or damage can all matter.

Therefore a pull diagnosis should preserve at least these competing classes:

- tire/wheel force;
- brake drag;
- steering assist imbalance/binding;
- cross-camber/cross-caster;
- rear thrust geometry;
- suspension compliance or movement under acceleration/braking;
- road crown/load distribution.

Do not 'correct' caster or camber against a tire pull without isolating the tire contribution.

## Torque steer is another pull differential

Torque steer is a drive-force/driveline/suspension phenomenon that appears under acceleration or deceleration. It is not proof of a static alignment error.

If a pull depends strongly on throttle, compare the behavior to:

- engine/transaxle mount movement;
- left/right driveshaft/CV geometry;
- tire traction/circumference differences;
- suspension bushing movement under drive load;
- differential/driveline behavior;
- static alignment only after those load-dependent mechanisms are considered.

A good diagnostic question is **what input turns the pull on?** Constant cruise, braking, acceleration, a bump, or the last steering direction are different experiments.

## Pull diagnosis should be condition-based

Do not ask only 'does it pull left or right?' Record when it happens:

- steady cruise on a known road;
- low versus higher road speed;
- light versus hard braking;
- acceleration versus coast;
- immediately after a left/right turn;
- over a bump or dip;
- with a changed load;
- after a tire rotation or suspension repair.

Then reproduce the condition and watch the boundary likely to move. A static alignment printout cannot reproduce every one of those loads.

## Steering wheel center is not the same as total toe

A straight steering wheel requires the front individual toe to be distributed correctly relative to the vehicle's actual travel/thrust direction. Merely achieving the correct sum of left and right toe can leave the rack/steering wheel off center.

Likewise, centering the steering wheel by arbitrarily moving one tie rod can hide a rear thrust problem. Read front individual toe, total toe, rear individual/total toe, and thrust angle together.

After alignment on vehicles that require it, perform the specified steering-angle-sensor reset and ADAS calibration/relearn. Mechanical straight-ahead, electronic steering zero, and camera/radar calibration reference need to agree with the OEM procedure.

## Home measurement: useful, but know what is being measured

A home setup can measure caster/camber/toe well enough for diagnosis or iterative mechanical work if its references are controlled. QuickTrick's written procedure contains several sound setup habits:

- check pressure;
- use a hard surface;
- settle the suspension;
- establish the gauge's level reference;
- use a steering-angle sweep for caster;
- measure both sides;
- string the vehicle when deciding individual toe.

But a simple pair of toe plates or one inclinometer does not automatically provide:

- rear thrust line;
- reliable individual toe relative to the vehicle;
- SAI/included angle;
- setback/symmetry/body-dimension information;
- runout compensation;
- steering-angle-sensor reset;
- ADAS calibration.

State what the setup actually measures and do not infer the missing geometry.

## A compact real-world sequence

For a pull, wander, crooked steering wheel, or abnormal tire wear:

1. reproduce and classify the complaint;
2. verify tires, pressures, load, and ride height;
3. inspect joints/bushings/mounts for lost motion or binding;
4. establish the vehicle/floor/frame reference needed for valid measurements;
5. measure rear geometry and thrust first;
6. measure front caster with the proper steering sweep, not a straight-ahead guess;
7. measure camber and use SAI/IA when the pattern suggests bent/displaced structure;
8. adjust rear geometry where available;
9. adjust front caster;
10. adjust front camber;
11. adjust front toe last;
12. jounce/settle and remeasure after adjustments as the procedure requires;
13. center/verify steering and perform required electronic resets/calibration;
14. road-test the same condition used to establish the baseline.

The goal is not merely four green boxes. The goal is stable geometry, a vehicle that tracks as intended, and measurements that still make sense after the suspension is loaded and driven.
