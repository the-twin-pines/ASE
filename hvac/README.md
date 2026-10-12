# HVAC diagnosis

Start with the complaint, operating conditions and installed compressor/control
architecture. A driver saying “A/C does not work” has not yet distinguished weak
airflow, warm delivered air, absent compressor output or intermittent permission.

| Question | Evidence to seek | What it does not establish |
| --- | --- | --- |
| Is A/C requested? | Relevant request and permission data | Usable electrical output |
| Is power delivered? | Application-specific loaded circuit test | Clutch motion or pumping |
| Is a clutch fitted and engaging? | Actual mechanical response | Compressor pressure/temperature response |
| Is displacement controlled electronically? | Command, temperatures and live data together | A failed compressor from pressure alone |
| Is cooling lost only at idle? | Condenser airflow and operating response under the same conditions | Low charge from warm vent air alone |
| Was the charge measured? | Specified refrigerant and service history; recovered/charged mass under the applicable procedure | Correct mass from static pressure |

Use the individually admitted passages:

- [New compressor, powered circuit, no pumping](../sources/passages/hvac-new-compressor.md)
- [Relay, clutch and compressor are separate boundaries](../sources/passages/hvac-clutch-boundary.md)
- [Charge quantity versus the existence of pressure](../sources/passages/hvac-charge-evidence.md)
- [Variable-displacement diagnosis](../sources/passages/hvac-variable-displacement.md)
- [Weak cooling in traffic](../sources/passages/hvac-idle-cooling.md)

[Historical field cases](history/a7-field-cases.md) and
[diagnosis notes](history/a7-air-conditioning-diagnosis.md) are preserved byte for
byte from `a7-heating-air-conditioning@b5e9fd31257cafc27e262751bb72f7703a8e0a26`.
[The five-video inventory](history/a7-playlist.md) retains the original review
states. This pass reads those notes; it does not replay videos or review the longer
Car Wizard cut. Only scoped new passages enter retrieval. Historical pressure
observations are case observations, not service limits.

Exact charge, oil, refrigerant, current, pressure, flushing and electrical test
procedures require [specification approval](../specifications/README.md). A relay
substitution cannot be generalized to module-switched or high-voltage compressors.
No refrigerant venting or permanent bypass is prescribed.
