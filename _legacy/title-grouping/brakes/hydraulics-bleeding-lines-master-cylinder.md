# Hydraulics: fluid, bleeding, lines, hoses, master cylinder

This file deepens the hydraulics slice of the supplied brake playlist. The technical notes below are checked against vehicle service information or manufacturer material. The 28 video entries remain a metadata index unless an entry is later marked **video-reviewed**; a title alone is not evidence that the video proves a claim.

The 2006 Dakota 4WD V8 and 2009 CR-V 4WD procedures are concrete study examples, not universal specifications for every Dakota, CR-V, or brake system. For actual work, select service information by VIN, brake package, drivetrain, and ABS configuration.

No suspension or steering material is active in this note.

## Hydraulic model

The useful idealization is:

- line pressure: `P ≈ F_master / A_master`;
- force at a caliper or wheel-cylinder piston: `F_output ≈ P × A_output`;
- displaced volume: `A_master × master travel` must supply piston motion, clearance take-up, hose expansion, fluid compression, and any gas compression.

Pedal ratio and the booster change the force delivered to the master-cylinder piston. They do not remove the volume requirement. This explains three distinctions:

- **hard/high pedal** points first toward inadequate assist or a mechanical obstruction;
- **low pedal that becomes higher after one or two pumps** points toward excess clearance, knockback, or compressibility;
- **pedal that continues to sink during a steady hold** points toward pressure loss by external leakage, internal bypass, or another hydraulic path.

Liquid brake fluid and hoses are not perfectly rigid, but entrained air or vapor changes volume far more under normal brake pressure. Air can therefore consume master-cylinder travel without creating proportional wheel force.

## Diagnostic table

| Observation | Physical possibilities | Discriminating test | What the result means |
| --- | --- | --- | --- |
| First stroke is low; immediate second stroke is higher | air/vapor, rear-shoe clearance, pad knockback, excessive component travel | repeat the stroke without waiting; inspect clearances and hub/rotor motion before assuming a master cylinder | rapid pump-up favors travel/compressibility over a pure assist fault |
| Pedal slowly falls under steady light force | external leak, master-cylinder internal bypass, architecture-specific valve/modulator leak | with the engine off and booster reserve exhausted, inspect for leaks and hold steady pressure | the 2006 Dakota procedure calls a falling pedal an internal master-cylinder leak after the preliminary checks; do not skip the external-leak inspection ([Dakota master-cylinder test][d-mc-test]) |
| Pedal is high but takes excessive effort | booster/vacuum/check-valve fault, seized linkage, hydraulic restriction | exhaust booster reserve, hold the pedal, then start the engine | a small pedal drop as assist arrives supports normal booster action; it does not validate the rest of the hydraulic system ([Dakota master-cylinder/booster test][d-mc-test]) |
| One wheel remains hot or hard to rotate after release | caliper/pad/mechanical bind, parking-brake bind, trapped hydraulic pressure | after safe support and confirmation of drag, cautiously open that corner's bleeder | immediate release or a pressure spurt proves retained pressure upstream of the bleeder; it does **not** by itself identify the hose as the failed part ([NHTSA drag investigation][nhtsa-drag]) |
| Drag remains after the bleeder is opened | piston, slides, pad fit, drum/parking hardware, bearing or another wheel-end mechanical fault | inspect the wheel end and compare with the opposite side | the holding force is not being maintained solely by line pressure |
| Fluid level drops with no obvious wet wheel | line/joint leak, master-cylinder rear seal leaking into booster, other concealed leak | inspect the master-cylinder mounting end and booster as the applicable service procedure directs | fluid can be hidden in the booster; a clean floor does not rule out an external master-cylinder leak ([Acura master-cylinder recall procedure][acura-mc-leak]) |
| Pedal is soft after a line, hose, master cylinder, or HCU was opened | air remains in base circuit or ABS hydraulic unit | run the exact base/ABS bleed procedure; then perform the completion checks | repeated ordinary wheel bleeding may not move air trapped inside a modulator or at a high point ([Dakota ABS bleed][d-abs], [GM high-point-air bulletin][gm-bleed]) |

### What the bleeder-release test does and does not prove

The bleeder is downstream of the hose, hard line, ABS hydraulic unit, master cylinder, and any compensation path feeding that corner. If opening it releases a dragging brake, one of those upstream elements retained pressure. A collapsed hose is a strong **local** candidate, especially when only one corner is affected, but the result is not a hose verdict. Use the circuit diagram and the manufacturer's isolation procedure to move the boundary upstream.

If opening the bleeder does not release the wheel, stop chasing hydraulic pressure and inspect mechanical movement at that wheel end.

Do not road-test a vehicle with an unreliable pedal or a known severely overheated brake. Opening a pressurized bleeder can discharge hot fluid; support the vehicle correctly and protect eyes, skin, and paint.

## Bleeding

### Why bleeding is required

Bleeding removes gas from a circuit after it has been opened or has ingested air. A fluid exchange or flush also replaces old fluid, but moving clean fluid through a system is not proof that every air pocket has been purged. The job may involve three different volumes:

1. the master cylinder;
2. the base lines, hoses, calipers, and wheel cylinders;
3. the ABS hydraulic control unit (HCU/modulator).

Each can require a different procedure.

### Before opening a bleeder

- Identify the specified fluid from the exact service information. Do not select fluid by cap color, bottle advertising, or a different model-year procedure.
- Use fresh fluid from a sealed container. The Dakota manual specifies DOT 3 meeting SAE J1703; the CR-V manual specifies clean Honda DOT 3 from an unopened container ([Dakota base bleed][d-base], [CR-V bleed][h-bleed]).
- Clean around the reservoir cap and bleeders. Keep petroleum products, dirt, water, and incompatible fluid out.
- Protect paint and wash spilled brake fluid off with water as directed by the vehicle procedure.
- Start at the specified reservoir level and check it throughout. Letting the reservoir run empty can introduce air into both base and ABS sections.
- Do not reuse expelled fluid. The CR-V procedure states this explicitly ([CR-V bleed][h-bleed]).

### Manual bleed as a state sequence

For a conventional two-person procedure, preserve this order:

1. Connect a clear hose and position the collection container.
2. Have the helper apply the pedal slowly and hold it.
3. Open the bleeder enough to discharge fluid and gas.
4. Close the bleeder while the pedal remains down.
5. Allow the pedal to return only after the bleeder is closed.
6. Refill the reservoir as required and repeat until the service criterion is met.

The 2006 Dakota procedure says to open the bleeder, depress the pedal, close the bleeder with the pedal down, and repeat until the stream is clear and bubble-free. The 2009 CR-V procedure similarly calls for slow pumping, steady pressure, venting through a clear tube, and reservoir checks ([Dakota base bleed][d-base], [CR-V bleed][h-bleed]).

### Bleed order is not universal

Two service procedures in the user's own vehicle set give opposite-looking orders:

| Vehicle example | Specified sequence |
| --- | --- |
| 2006 Dodge Dakota 4WD V8-4.7L VIN N | right rear → left rear → right front → left front |
| 2009 Honda CR-V 4WD L4-2.4L | left front → right front → right rear → left rear |

The CR-V starts at the driver's front, not the geometrically farthest wheel. Therefore “always start farthest from the master cylinder” is a memory aid for some systems, not a rule. Circuit split, internal HCU routing, and the manufacturer's procedure decide the order ([Dakota base bleed][d-base], [CR-V bleed][h-bleed]).

### ABS/HCU air

The 2006 Dakota ABS procedure is explicit:

1. perform the complete base-brake bleed;
2. use the scan tool's ABS routine to cycle the HCU pump and solenoids;
3. perform the complete base-brake bleed again;
4. set fluid level and verify operation before moving the vehicle.

That is not the same as saying every pad change or ordinary fluid exchange needs a scan tool. It means that this vehicle's **ABS bleeding procedure** does when the HCU must be purged ([Dakota ABS bleed][d-abs]).

Air location matters. A GM bulletin for specific Impala/Monte Carlo systems explains that lines rising above the reservoir can retain air at a high point; its prescribed repair combines line positioning, repeated automated HCU operation, gravity bleeding, and a final firmness check. Repeating a generic wheel sequence would miss the architecture-specific trap ([GM high-point-air bulletin][gm-bleed]).

### Manual, pressure, gravity, vacuum, and one-person methods

- **Manual bleeding** uses controlled pedal displacement and a helper or a check-valve bottle. The open/close state still matters.
- **Pressure bleeding** pushes fluid from the reservoir. The Dakota procedure requires the correct master-cylinder adapter, purged tank lines, and adherence to the equipment maker's limit; it says 15–20 psi is generally sufficient for that procedure, not a universal pressure specification ([Dakota base bleed][d-base]).
- **Gravity bleeding** is slow flow caused by reservoir head. It is not categorically useless: the GM procedure above expressly requires a gravity-bleed phase. It also is not guaranteed to clear every high point or HCU.
- **Vacuum bleeding** pulls at the bleeder. Apparent bubbles can come from the hydraulic circuit or from air drawn around loose bleeder threads, so bottle bubbles alone do not establish where the air originated.
- **One-person bottles/check valves** are tools, not a different hydraulic objective. The reservoir must stay full, the return stroke must not draw air back, and the final pedal/leak/drag checks still apply.

Playlist items 011, 049, 051, 072, 094, and 170 are the supplied demonstrations to compare against this state sequence. Item 035's title claims gravity bleeding “doesn't work”; the service evidence above prevents turning that title into a universal rule.

### Completion gates

Before moving the vehicle:

- specified sequence completed;
- no air at the applicable outlets under the specified method;
- reservoir at the correct level and cap installed;
- every opened joint and bleeder dry during a firm pedal hold;
- pedal high/firm under the service procedure's test conditions;
- warning lamps and scan-tool routine in the expected state, when applicable;
- wheels checked for free rotation/drag after master-cylinder or hose work;
- hose routing checked for twist and interference.

The Dakota base and ABS procedures require a firm-pedal/operation check before moving. The CR-V master-cylinder replacement procedure adds a wheel-spin drag check after bleeding ([Dakota base bleed][d-base], [Dakota ABS bleed][d-abs], [CR-V master-cylinder replacement][h-mc]).

## Bench bleeding a master cylinder

Bench bleeding removes air from the master cylinder's short internal passages before the installed brake lines make that air harder to move. It does not bleed the base system or ABS hydraulic unit.

The 2006 Dakota procedure is concrete:

1. secure the new master cylinder in a vise without damaging it;
2. attach bleed tubes to both outlet ports and return their ends into the reservoir;
3. fill with fresh brake fluid;
4. stroke the pistons with a wood dowel, release them to return under spring force, and continue until bubbles stop;
5. install the cylinder, then bleed the base system.

The applicable service procedure or the replacement-cylinder instructions decide permitted stroke, plugs versus return tubes, and whether a separate bench procedure is specified. The 2009 CR-V replacement page directs a system bleed after installation but does not itself prescribe the Dakota bench method. Do not transfer the Dakota's details blindly to the Honda ([Dakota master-cylinder bleed][d-mc-bleed], [Dakota master-cylinder replacement][d-mc-replace], [CR-V master-cylinder replacement][h-mc]).

Playlist items 050, 053, and 054 are the supplied bench-bleed demonstrations. Items 046–048 explain operation, while 052 and 055 are diagnostic demonstrations. Their titles identify the study topic; the service sources above carry the checked procedure and diagnostic claims.

## Master cylinder

### Tandem circuits

A tandem master cylinder contains primary and secondary pistons so one body can pressurize two circuits. Do not infer the wheel split from the words “primary” and “secondary.” On the cited 2006 Dakota configuration, the manual says the primary piston feeds the front brakes and the secondary feeds the rear. Other vehicles can use a diagonal split or a more complex electrohydraulic arrangement.

The Dakota reservoir compartments equalize level in normal service while preserving enough fluid for the remaining circuit after a front- or rear-circuit malfunction. That redundancy is degraded braking, not permission to continue driving ([Dakota master-cylinder operation][d-mc-desc]).

### Compensation and release

On a compensating-port design, the released piston must uncover the reservoir path so pressure can return and thermal expansion can be accommodated. Insufficient pedal/pushrod free play can keep the port covered. Pressure may then remain after the pedal is released and rise as fluid heats.

A Honda safety-recall document gives the mechanism directly: insufficient free play can let a pressure cup block a compensating port, causing brake drag after release and enough heat to create a fire risk. That document concerns a motorcycle system; use it as a clear hydraulic mechanism, not as the service specification for a Dakota or CR-V ([Honda compensating-port recall][port-drag]).

Topology changes the symptom. A master-cylinder compensation fault may affect an entire circuit; a single hot corner makes a local hose or wheel-end fault more likely, though not certain.

### Internal bypass versus external leak

- **External leak:** fluid leaves the intended hydraulic volume. Inspect lines, junctions, calipers/wheel cylinders, the master-cylinder body, and the booster-facing end.
- **Internal bypass:** fluid crosses a piston seal inside the master cylinder. Fluid level may not drop, but pressure decays and the pedal can continue to sink during a steady hold.
- **Air/clearance:** the pedal may start low yet pump higher. That is different evidence from a pedal that keeps falling while held.

The Dakota test exhausts booster reserve with the engine off, applies light steady pressure, and treats a pedal that falls away as internal master-cylinder leakage. The same page then starts the engine and expects a slight pedal movement as booster assist appears. These are two separate tests ([Dakota master-cylinder/booster test][d-mc-test]).

A master cylinder can leak rearward into the booster. Manufacturer recall procedures for Acura and Ford direct technicians to inspect the back of the master cylinder/booster mounting surface and replace the booster when contaminated or leaking. This is why “no puddle” is not the same as “no external leak” ([Acura master-cylinder recall procedure][acura-mc-leak], [Ford master-cylinder recall procedure][ford-mc-leak]).

### Diagnostic order

1. Describe travel, effort, force, and release separately.
2. Verify fluid type/level and inspect the complete system for external leakage.
3. Determine whether one quick repeat stroke raises the pedal.
4. With the engine off and reserve assist depleted, perform the service-information pedal-hold test.
5. Test booster action separately by holding force while starting the engine.
6. If a wheel drags, use the bleeder-release discriminator before naming the caliper, hose, HCU, or master cylinder.
7. Use manufacturer-approved isolation fittings/procedures when circuit isolation is required; do not crush a brake hose with locking pliers.
8. After replacement, perform the specified master/base/ABS bleeding and the leak, pedal, and drag completion checks.

“Soft pedal” alone does not condemn a master cylinder. Air, vapor, excess clearance, knockback, external leakage, and ABS/HCU air remain live until separated by tests.

## Rigid lines, flexible hoses, flares, and banjo joints

### Inspection

The 2009 CR-V inspection procedure supplies a useful complete list:

- hoses: damage, deterioration, leakage, interference, and twisting;
- hard lines: damage, rust, leakage, and bending;
- all hose/line joints and connections: leakage;
- master cylinder and VSA modulator-control unit: damage and leakage.

Run the inspection with the hose in all positions it will actually occupy. A hose that looks relaxed with the wheels straight may twist, stretch, or rub at another wheel position ([CR-V hose/line inspection][h-line-inspect]).

### Rigid-line repair

Before cutting tube, identify all four of these from service information or the original part:

1. tube material and wall construction;
2. outside diameter;
3. flare geometry;
4. tube nut/thread and mating seat.

Do not reduce “brake flare” to one shape. The cited 2006 Dakota manual specifies an **ISO flare**, recommends a preformed factory tube, and permits double-wall steel tube for an emergency repair when the preformed part is unavailable. It calls for a tubing cutter, removal of internal burrs, installing the tube nut before flaring, the correct ISO adapter, and a squarely seated tool ([Dakota ISO flare][d-iso]).

An SAE 45-degree double/inverted flare and an ISO bubble flare are not interchangeable just because the tube nut starts in the hole. The flare seat is the hydraulic seal; the threads supply clamping force. Do not add pipe-thread tape or sealant to a flare joint.

After forming a line:

- reject a split, lopsided, thinned, or off-center flare;
- start the fitting by hand to prevent cross-threading;
- torque to the exact service specification;
- reproduce routing, bends, clips, shields, and clearance from heat/moving parts;
- bleed and inspect every disturbed joint under pedal pressure.

Playlist items 025, 058, 101, and 103 are the supplied fabrication/joint demonstrations. Items 102 and 127 raise the compression-fitting question. The checked rule here is narrower and stronger than a video-title slogan: use the vehicle maker's specified preformed tube or approved tube, flare, nut, and union repair. A generic plumbing compression union is not the repair described by the Dakota service information. Do not make an unsupported claim that every fitting sold under the word “compression” has the same construction or legal status everywhere.

### Flexible hoses and trapped pressure

A hose must transmit pressure in both directions: application flow toward the wheel and release flow back toward the reservoir. Damage or internal restriction can therefore appear as either weak application or delayed release.

Use symptom localization:

- a dragging wheel that releases when its bleeder is opened has retained pressure upstream;
- a wheel that stays bound with the bleeder open has a mechanical wheel-end fault;
- if only one corner is affected, the local hose is a high-priority upstream component, but valves, lines, HCU routing, and the master-cylinder circuit still exist upstream.

Replace a hose that is damaged, deteriorated, leaking, twisted, or incorrectly routed. Never let a caliper hang by the hose. The CR-V procedure requires no twist or interference, a bleed after replacement, and a leak check. The Dakota front-hose procedure likewise ends with bleeding ([CR-V hose replacement][h-line-service], [Dakota front hose][d-hose]).

Playlist item 090 is the supplied caliper-versus-hose isolation demonstration. Item 125 concerns hose clamps. Treat any clamping method as tool- and manufacturer-specific; ordinary locking pliers can damage hose structure and are not an acceptable generic isolation tool.

### Banjo joints

A banjo joint uses a sealing washer on each side of the hose eye. The fastener supplies clamping force; the washers make the fluid seal.

For the cited vehicles:

- the CR-V procedure specifies a banjo bolt with **new sealing washers**, then bleeding, joint-leak inspection, and a twist/interference check;
- the Dakota procedure says to discard the old copper washers, install new ones, and torque its front banjo bolt to 28 N·m (250 in·lbf). That torque belongs only to the cited configuration.

Do not reuse flattened washers, stack extras, guess bolt length, or transfer torque between vehicles. Playlist items 059 and 132 are the supplied banjo-joint prompts ([CR-V hose replacement][h-line-service], [Dakota front hose][d-hose]).

### Compressing a caliper piston

Playlist item 019 asks whether to open the bleeder while retracting a piston. There is no universal answer in the title. The vehicle procedure may route displaced fluid back to the reservoir or may prescribe opening/isolating part of the circuit. Relevant variables include ABS architecture, fluid condition, reservoir capacity, an electric parking-brake mechanism, and whether the hydraulic system is being opened.

If a bleeder is opened, expelled fluid must be controlled, the reservoir must be managed, the bleeder must be closed correctly, and the system must pass the applicable bleed/leak/pedal checks. Do not turn a shop preference into a universal ASE rule.

## ASE reasoning traps

- **“Always bleed farthest first.”** False as a universal rule; the cited CR-V starts left front.
- **“Gravity bleeding never works.”** False as a universal rule; a GM service bulletin expressly specifies it as one phase of a particular repair.
- **“A low pedal means the master cylinder is bad.”** Too broad; test pump-up, leaks, clearance, air/vapor, and steady-hold behavior.
- **“A hard pedal means air.”** Usually the wrong direction; air classically adds travel/compliance, while inadequate assist raises effort.
- **“Opening the bleeder proves the hose is bad.”** It proves trapped upstream pressure if the wheel releases; further isolation identifies the component.
- **“Bench bleeding finishes the job.”** It removes master-cylinder air, not air in lines, wheel units, or the HCU.
- **“All brake-line flares are double flares.”** False; the cited Dakota repair is ISO.
- **“No visible puddle means no master-cylinder leak.”** False; fluid can leak into the booster.
- **“A video title is a checked procedure.”** False; use the title to route study, then check the content and the exact service information.

## Supplied-video study map

| Slice | Playlist entries | Questions to carry into review |
| --- | --- | --- |
| fluid exchange and base bleeding | 011, 049, 051, 072, 094, 170 | Is the reservoir continuously protected? What is the open/close/pedal state sequence? Is the shown wheel order vehicle-specific? |
| bleeder service and gravity claims | 018, 035 | Is the bleeder salvage method safe for the caliper? Is a gravity claim limited to the demonstrated architecture? |
| master-cylinder operation/test | 046, 047, 048, 052, 055, 134 | Does the explanation separate internal bypass, external rear-seal leakage, air, and booster action? What circuit split is actually shown? |
| bench bleeding | 050, 053, 054 | Are both outlets purged, returns submerged, strokes controlled, and the later base/ABS bleed acknowledged? |
| hard lines, flares, unions | 025, 058, 101, 102, 103, 127 | Are material, diameter, flare, nut, seat, routing, and local approval all identified rather than assumed? |
| hoses, banjo joints, isolation | 019, 059, 090, 125, 132 | Are new washers and torque specified? Does an isolation result localize only a boundary, or is it overclaimed as a component verdict? |

## Videos

The entries below preserve the supplied playlist metadata. None is marked video-reviewed in this pass.

### 011. How to do a Complete Brake Flush and Bleed

- Channel: ChrisFix
- Duration: 12:53
- Video ID: `n1NvtUwfRJc`
- https://www.youtube.com/watch?v=n1NvtUwfRJc

### 018. How To Remove A Seized or Rusted Brake Bleeder Screw

- Channel: TutorialGenius.com
- Duration: 9:19
- Video ID: `_Da93hkQiXw`
- https://www.youtube.com/watch?v=_Da93hkQiXw

### 019. should you open bleeder valve when cmpressing caliper

- Channel: RB The Mechanic
- Duration: 2:37
- Video ID: `IlUUX2bXmp4`
- https://www.youtube.com/watch?v=IlUUX2bXmp4

### 025. DIY Brake Lines The Easy (And Correct) Way

- Channel: SuperfastMatt
- Duration: 15:11
- Video ID: `_Tm6N5l69_c`
- https://www.youtube.com/watch?v=_Tm6N5l69_c

### 035. What, how, & why gravity bleeding doesn't work! #shorts

- Channel: Rob The Mechanic
- Duration: 1:00
- Video ID: `OhRd9v13w7k`
- https://www.youtube.com/watch?v=OhRd9v13w7k

### 046. A master cylinder explained in under a minute

- Channel: WrenchCoach CAD Publishing for Training
- Duration: 0:46
- Video ID: `jjo4hq61f3I`
- https://www.youtube.com/watch?v=jjo4hq61f3I

### 047. The Master Cylinder: How It Works

- Channel: Motorcar Parts of America - MPA
- Duration: 2:02
- Video ID: `DNcDtIQAC9s`
- https://www.youtube.com/watch?v=DNcDtIQAC9s

### 048. Vehicle Brakes: Master Cylinder(How it works)

- Channel: electronicsNmore
- Duration: 8:31
- Video ID: `WYB4vOv7Iag`
- https://www.youtube.com/watch?v=WYB4vOv7Iag

### 049. How to Make a One Person Brake Bleeder for Under $5

- Channel: ChrisFix
- Duration: 4:13
- Video ID: `1wwq1Vlk4Wg`
- https://www.youtube.com/watch?v=1wwq1Vlk4Wg

### 050. How to Bench Bleed Master Cylinder

- Channel: Garage Gurus
- Duration: 6:58
- Video ID: `7rImn6nJ4Dw`
- https://www.youtube.com/watch?v=7rImn6nJ4Dw

### 051. AutoZone Car Care: How to Bleed the Master Cylinder and Brake System

- Channel: AutoZone
- Duration: 7:29
- Video ID: `zoewhwUu3UQ`
- https://www.youtube.com/watch?v=zoewhwUu3UQ

### 052. Brake Master Cylinder Testing

- Channel: DoItYourway Corner
- Duration: 9:25
- Video ID: `ZaB7wfuQ6Mk`
- https://www.youtube.com/watch?v=ZaB7wfuQ6Mk

### 053. Master Cylinder - How to Bench Bleed!

- Channel: Trick Shift Garage
- Duration: 13:25
- Video ID: `-kbDLUHZFqU`
- https://www.youtube.com/watch?v=-kbDLUHZFqU

### 054. Make a Bench Bleeding Tool! DIY Bleed Car / Truck Master Cylinder

- Channel: 1A Auto: Repair Tips & Secrets Only Mechanics Know
- Duration: 11:17
- Video ID: `xW8L-6u6nko`
- https://www.youtube.com/watch?v=xW8L-6u6nko

### 055. Soft, Squishy Brakes? Hard to Stop? How to Diagnose Brake Master Cylinder Leak!

- Channel: 1A Auto: Repair Tips & Secrets Only Mechanics Know
- Duration: 13:17
- Video ID: `RZJkFcvP65c`
- https://www.youtube.com/watch?v=RZJkFcvP65c

### 058. Mechanic Tip: Tightening Brake Line Bolts

- Channel: Technician Red
- Duration: 1:00
- Video ID: `zoSQsVZfIcc`
- https://www.youtube.com/watch?v=zoSQsVZfIcc

### 059. repairing a LEAKING “banjo bolt” (fuel line, brake line)

- Channel: Live Free
- Duration: 2:03
- Video ID: `uvgwU0raLRY`
- https://www.youtube.com/watch?v=uvgwU0raLRY

### 072. How to flush and bleed your brakes

- Channel: Way of the Wrench
- Duration: 31:52
- Video ID: `_EJ5s2ZnDwQ`
- https://www.youtube.com/watch?v=_EJ5s2ZnDwQ

### 090. How To Isolate a Seized Caliper or Failed Brake Hose

- Channel: Colin Chilibeck
- Duration: 2:13
- Video ID: `7kTmosL_x1c`
- https://www.youtube.com/watch?v=7kTmosL_x1c

### 094. Common Mistakes Bleeding Brakes! How to Do a Full Brake Bleed the Right Way, and Why!

- Channel: 1A Auto: Repair Tips & Secrets Only Mechanics Know
- Duration: 23:29
- Video ID: `gAKBZG9kQPw`
- https://www.youtube.com/watch?v=gAKBZG9kQPw

### 101. How to Flare Brake Lines for Your Truck, Car, or SUV

- Channel: 1A Auto: Repair Tips & Secrets Only Mechanics Know
- Duration: 10:07
- Video ID: `fQnt08Yjti0`
- https://www.youtube.com/watch?v=fQnt08Yjti0

### 102. Dangerous Brake Line Fix: Why You Shouldn't Use Compression Fittings

- Channel: Gulf Coast Flips
- Duration: 0:42
- Video ID: `uiGq9vjwrF0`
- https://www.youtube.com/watch?v=uiGq9vjwrF0

### 103. How to mate brake or fuel lines with a double flare union

- Channel: Projectgattago
- Duration: 6:36
- Video ID: `0I0cqn6uQCQ`
- https://www.youtube.com/watch?v=0I0cqn6uQCQ

### 125. Brake Job Tools: Hose Clamps

- Channel: Raybestos Brakes
- Duration: 1:22
- Video ID: `YAgJpKyAR1Y`
- https://www.youtube.com/watch?v=YAgJpKyAR1Y

### 127. Compression fittings on brake lines?

- Channel: Jimmy, Making it work
- Duration: 0:16
- Video ID: `cLJFwYYSgio`
- https://www.youtube.com/watch?v=cLJFwYYSgio

### 132. TR Banjo Bolt

- Channel: TR Fastenings
- Duration: 0:53
- Video ID: `xP8yl5HItY0`
- https://www.youtube.com/watch?v=xP8yl5HItY0

### 134. MOPAR MASTER CYLINDER DOCTORATE (PART 1 OF 2)- BY THERAMMANINC.COM

- Channel: The Ram Man Inc.
- Duration: 8:32
- Video ID: `_HioFTF2JPE`
- https://www.youtube.com/watch?v=_HioFTF2JPE

### 170. This simple trick keeps air out of your brake system!!

- Channel: Wrenching With Kenny
- Duration: 4:21
- Video ID: `P0OhnhD_opc`
- https://www.youtube.com/watch?v=P0OhnhD_opc

## Checked service sources

- [2006 Dakota — base brake bleeding][d-base]
- [2006 Dakota — ABS brake bleeding][d-abs]
- [2006 Dakota — master-cylinder bench bleeding][d-mc-bleed]
- [2006 Dakota — master-cylinder description and operation][d-mc-desc]
- [2006 Dakota — master-cylinder/booster testing][d-mc-test]
- [2006 Dakota — master-cylinder replacement][d-mc-replace]
- [2006 Dakota — ISO flaring][d-iso]
- [2006 Dakota — front caliper hose][d-hose]
- [2009 CR-V — brake-system bleeding][h-bleed]
- [2009 CR-V — brake hose/line inspection][h-line-inspect]
- [2009 CR-V — brake-hose replacement][h-line-service]
- [2009 CR-V — master-cylinder replacement][h-mc]
- [GM bulletin PIC5468C — high-point air and automated/gravity bleed][gm-bleed]
- [Acura recall 10-047 — master-cylinder leakage into booster][acura-mc-leak]
- [Ford recall 22S11 — inspect master cylinder/booster for leakage][ford-mc-leak]
- [Honda recall material — blocked compensating port and brake drag][port-drag]
- [NHTSA investigation — bleeder pressure-release discriminator][nhtsa-drag]

Operation CHARM pages are mirrors of manufacturer service information. The NHTSA links host manufacturer bulletins, recall procedures, or investigation material. None of these vehicle-specific procedures should be transferred to another configuration without checking its own service information.

[d-base]: https://charm.li/Dodge%20and%20Ram/2006/Dakota%204WD%20V8-4.7L%20VIN%20N/Repair%20and%20Diagnosis/Brakes%20and%20Traction%20Control/Hydraulic%20System/Brake%20Bleeding/Service%20and%20Repair/Base%20Brake%20System/
[d-abs]: https://charm.li/Dodge%20and%20Ram/2006/Dakota%204WD%20V8-4.7L%20VIN%20N/Repair%20and%20Diagnosis/Brakes%20and%20Traction%20Control/Hydraulic%20System/Brake%20Bleeding/Service%20and%20Repair/ABS%20Brake%20Bleeding/
[d-mc-bleed]: https://charm.li/Dodge%20and%20Ram/2006/Dakota%204WD%20V8-4.7L%20VIN%20N/Repair%20and%20Diagnosis/Brakes%20and%20Traction%20Control/Hydraulic%20System/Brake%20Bleeding/Service%20and%20Repair/Master%20Cylinder%20Bleeding/
[d-mc-desc]: https://charm.li/Dodge%20and%20Ram/2006/Dakota%204WD%20V8-4.7L%20VIN%20N/Repair%20and%20Diagnosis/Brakes%20and%20Traction%20Control/Hydraulic%20System/Brake%20Master%20Cylinder/Description%20and%20Operation/
[d-mc-test]: https://charm.li/Dodge%20and%20Ram/2006/Dakota%204WD%20V8-4.7L%20VIN%20N/Repair%20and%20Diagnosis/Brakes%20and%20Traction%20Control/Hydraulic%20System/Brake%20Master%20Cylinder/Testing%20and%20Inspection/
[d-mc-replace]: https://charm.li/Dodge%20and%20Ram/2006/Dakota%204WD%20V8-4.7L%20VIN%20N/Repair%20and%20Diagnosis/Brakes%20and%20Traction%20Control/Hydraulic%20System/Brake%20Master%20Cylinder/Service%20and%20Repair/Master%20Cylinder/
[d-iso]: https://charm.li/Dodge%20and%20Ram/2006/Dakota%204WD%20V8-4.7L%20VIN%20N/Repair%20and%20Diagnosis/Brakes%20and%20Traction%20Control/Hydraulic%20System/Brake%20Hose%2FLine/Service%20and%20Repair/ISO%20Flaring/
[d-hose]: https://charm.li/Dodge%20and%20Ram/2006/Dakota%204WD%20V8-4.7L%20VIN%20N/Repair%20and%20Diagnosis/Brakes%20and%20Traction%20Control/Hydraulic%20System/Brake%20Hose%2FLine/Service%20and%20Repair/Front%20Caliper%20Hose/
[h-bleed]: https://charm.li/Honda/2009/CR-V%204WD%20L4-2.4L/Repair%20and%20Diagnosis/Brakes%20and%20Traction%20Control/Hydraulic%20System/Brake%20Bleeding/Service%20and%20Repair/
[h-line-inspect]: https://charm.li/Honda/2009/CR-V%204WD%20L4-2.4L/Repair%20and%20Diagnosis/Brakes%20and%20Traction%20Control/Hydraulic%20System/Brake%20Hose%2FLine/Testing%20and%20Inspection/
[h-line-service]: https://charm.li/Honda/2009/CR-V%204WD%20L4-2.4L/Repair%20and%20Diagnosis/Brakes%20and%20Traction%20Control/Hydraulic%20System/Brake%20Hose%2FLine/Service%20and%20Repair/
[h-mc]: https://charm.li/Honda/2009/CR-V%204WD%20L4-2.4L/Repair%20and%20Diagnosis/Brakes%20and%20Traction%20Control/Hydraulic%20System/Brake%20Master%20Cylinder/Service%20and%20Repair/
[gm-bleed]: https://static.nhtsa.gov/odi/tsbs/2014/SB-10038752-1726.pdf
[acura-mc-leak]: https://static.nhtsa.gov/odi/rcl/2010/RCMN-10V504-0989.pdf
[ford-mc-leak]: https://static.nhtsa.gov/odi/rcl/2022/RCMN-22V150-4118.pdf
[port-drag]: https://static.nhtsa.gov/odi/rcl/2011/RCORRD-11V567-8637.pdf
[nhtsa-drag]: https://static.nhtsa.gov/odi/inv/2007/INME-EA07016-33584.pdf
