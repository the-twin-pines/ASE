# Steering diagnostic coverage

| Architecture | Assist path | Relevant split |
| --- | --- | --- |
| Engine-driven hydraulic | Engine drive → pump → fluid/hoses → gear | Drive, reservoir/aeration, flow/relief, restriction, gear leakage, mechanical load |
| EHPS/EPHS | Electrical supply/control → motor-pump → hydraulic gear | Electrical supply plus hydraulic circuit; engine-speed inference is not direct pump-speed evidence |
| EPS, rack or column | Torque/angle input/control → motor/gear → steering | Supply/ground/communication, input plausibility, motor/control, mechanical load; no hydraulic steering pump/reservoir |

Rack EPS may use a belt internally. That does not make it an engine-driven
hydraulic pump. Mechanical joints/linkages, wheel-end load, tires/alignment and
brake drag remain separate competing causes in all architectures. A brake
hydraulic-assist unit is not interchangeable with steering assist.

Start by identifying exact vehicle, year, variant and installed architecture.
[Approved passages](../sources/passages.tsv) contain seven steering traces, each
with an observation order, competing hypotheses, a discriminator, conditional
outcomes, limits and planned verification. They are not actual repair reports.

High-pressure/flow testing requires a trained technician, correct equipment and
exact service documentation including temperature/load/relief limits. Never open
a pressurized hose or feel for a high-pressure leak by hand. Column separation,
airbags, clock springs, steering locks and centering likewise require exact
procedures. Pressure, flow, fluid, torque and clearance remain UNKNOWN without
the specification gate. Qualitative diagnosis remains useful without inventing
those numbers. See [source review](../sources/reviewed/power-steering-review.md).
