# ASE A7 field cases — compressor command, clutch, and mechanical failure

These notes preserve the order in which working mechanics divided the problem. They are not generic A/C component summaries. Source depth and unresolved claims are stated for each case.

## Case 1 — Watch Wes Work: a new compressor mistaken for a wiring fault

Video: [Another Shop Fixed It, Now It's More Broken](https://www.youtube.com/watch?v=wEJ3LiJdy5k)  
Vehicle: 2006 Dodge Ram 2500 with the Cummins diesel  
Source status: **11:07 auto-generated transcript reviewed end to end**

### Complaint and repair history

- The A/C did not work.
- Another shop installed a new compressor.
- The A/C still did not work, and the remaining problem was described as a wiring fault.
- Stored faults had included A/C clutch-control circuit open, circuit low, and overcurrent.

That history makes the new compressor tempting to accept as known-good. Wes does not accept it.

### What the scan data established

- Static refrigerant pressure reported about 58 psi on a cold day. That was plausible as an ambient-dependent static pressure, but it did not prove correct charge or compressor operation.
- The HVAC data showed the customer A/C selection as true.
- The clutch request was true.

This moved the diagnostic boundary forward: the button and request path were operating. It did **not** yet establish that the TIPM delivered usable power, that the clutch moved, or that the compressor pumped.

### Control architecture he had to account for

The truck divided the decision among three modules:

1. the HVAC control head accepted the driver's request;
2. the PCM/ECM considered engine speed, engine temperature, refrigerant pressure, evaporator temperature, and other permission conditions;
3. the TIPM performed the high-current switching to the clutch.

The TIPM also monitored current and could shut the output down. That made the overcurrent fault potentially meaningful rather than merely another code to clear.

### The tests, in order

1. Disconnect the clutch load at its connector.
2. Apply power directly to the clutch to see whether it physically engages.
3. Put a test light on the vehicle-side clutch feed to see whether the TIPM supplies the output.
4. If the output is absent, work backward through the circuit. If it is present, stop blaming the upstream circuit and test the load and compressor.

Direct power produced arcing but no clutch click. With the engine running, the vehicle-side feed illuminated the test light, so the command/output circuit was present at the clutch connector.

Physical inspection then showed no clutch air gap. The clutch plate was locked to the pulley, so the compressor was being driven continuously. Even while being driven, the pressure-transducer value did not rise. The new compressor was turning externally but was not compressing internally.

### Diagnosis and remaining uncertainty

- The wiring fault was not reproduced; power reached the clutch connector.
- The new clutch was mechanically stuck engaged.
- The compressor produced no observed pressure change and appeared to be mechanically failed.
- Oil around the compressor suggested leakage.
- Wes suspected that an internal failure may have distributed debris through the system. He discussed condenser, accumulator, and orifice replacement plus line flushing, but the video did not include teardown, debris inspection, the completed repair, or post-repair verification.

Do not convert the contamination suspicion into a confirmed finding. The confirmed findings were a powered circuit, a clutch with no air gap, continuous mechanical drive, and no pressure response.

### Lessons worth retaining

- A new part is untested until its behavior is measured.
- A request bit proves a request, not output delivery.
- Voltage at the connector proves neither clutch movement nor compressor pumping.
- Static pressure can show that the system is not empty, but it does not establish correct charge or dynamic operation.
- A jammed or abnormal load can explain current-related electrical faults even when the wiring is intact.
- Finish the chain: **request → power output → clutch motion → compressor pumping → system pressure/temperature response**.

---

## Case 2 — Car Wizard: divide the fault at the compressor relay

YouTube source: [AC not working!!! The CAR WIZARD shows how to easily isolate the problem](https://www.youtube.com/watch?v=bVYUzp8QQ0M)  
Captioned source reviewed: [AC Not Working? How to Easily Isolate the Problem!](https://www.facebook.com/CarWizardFB/videos/ac-not-working-how-to-easily-isolate-the-problem/1385625935727615/)  
Demonstration vehicle: Honda with a conventional compressor clutch  
Source status: **7:58 Facebook cut reviewed end to end using its on-screen captions; the 18:56 YouTube cut was not transcript-reviewed**

### His opening split

For this conventional clutch system, he begins by separating:

- failure to deliver or use electrical power at the clutch; and
- a compressor that is mechanically locked or internally failed.

This is a useful first division, but it is not a complete list for every vehicle. Variable-displacement and clutchless systems require a different test plan.

### Relay-boundary test

1. Find the A/C compressor relay using the owner information or relay-box diagram. The Honda diagram used a snowflake symbol.
2. Remove the relay.
3. Identify fused power and the terminal feeding the compressor load.
4. Use a grounded test light to inspect the relevant socket terminal.
5. Turn on the vehicle and request A/C.
6. Substitute a controlled relay switch so the clutch load can be commanded independently.
7. Listen and watch for clutch engagement.

The relay socket is valuable because it separates the command side from the downstream wiring, ground, clutch coil, and mechanical compressor.

In the demonstration, the A/C button illuminated and the control system requested A/C. The substitute relay switch made the clutch click. From that response he inferred that the downstream wiring and ground were intact and that the clutch coil could operate.

The button lamp alone does not prove the entire cabin control system. The stronger evidence is the command observed at the relay boundary together with successful downstream clutch operation.

### Separate clutch-coil failure from compressor seizure

He demonstrated two compressors away from the vehicle:

- On the good unit, direct battery voltage energized the magnetic coil. The center hub locked to the free-spinning pulley so both rotated together.
- On the failed electrical unit, direct power produced no movement. The compressor might still turn mechanically, but the coil circuit could not engage it.

He also distinguished the pulley from the compressor shaft. The pulley normally freewheels with the clutch released; the center hub is the part to turn when checking whether the compressor mechanism is seized. A locked center hub suggests mechanical failure.

Any direct-power test must use the correct circuit information and current protection. It is a brief diagnostic test, not a permanent bypass.

### Refrigerant presence versus correct charge

The video presses the service-port Schrader valve briefly to see whether any pressure is present. This establishes only **some refrigerant pressure versus apparently empty**. It cannot measure charge mass, diagnose system performance, or distinguish a slightly low charge from a correct one.

Do not promote that shortcut as the standard charge test. It deliberately releases refrigerant. The technically useful part follows: Car Wizard connects a recovery machine, removes the refrigerant, and weighs it. Comparing recovered mass with the vehicle specification is how he determines how low the system was.

Keep these questions separate:

- Is the circuit completely empty or does it retain some pressure?
- What are the static and operating pressures?
- What mass was recovered?
- What mass does the manufacturer specify?
- Where did any missing refrigerant escape?

### Mechanical failure and contamination

For a seized compressor, he warns against replacing only the compressor. His repair package includes the compressor, condenser, and receiver-drier, followed by appropriate line flushing. His reason is that metal from the failed compressor can remain in the circuit and destroy the replacement.

The exact parts that must be replaced rather than flushed depend on the vehicle, condenser construction, expansion device, service information, and warranty terms. Preserve the general lesson without turning one shop's package into a universal parts list:

> When a compressor fails internally, diagnose the whole refrigerant circuit as a contamination problem.

### Lessons worth retaining

- Use the relay socket as a deliberate dividing point.
- Test command and load sides separately.
- A clutch that clicks proves coil movement; it does not prove that the compressor pumps correctly.
- A compressor that turns mechanically can still have a failed clutch coil.
- A clutch coil that works can still be attached to a seized or non-pumping compressor.
- The correct charge is a specified mass, not the existence of pressure at a service port.
- After internal compressor failure, protect the replacement from debris left elsewhere in the circuit.

---

## Comparison — why these are better than a generic checklist

| Diagnostic boundary | Watch Wes Work case | Car Wizard demonstration |
|---|---|---|
| Driver request | Verified in scan data | A/C request made at the controls |
| Module/output decision | PCM/TIPM architecture and current faults considered | Relay socket used as the dividing point |
| Power delivery | Test light showed power at clutch connector | Substitute relay commanded the downstream load |
| Clutch response | Direct power gave no click; clutch was physically locked engaged | Good clutch clicked; failed coil did nothing |
| Compressor response | Externally driven but no pressure rise | Mechanical hub rotation used to screen for seizure |
| Refrigerant conclusion | 58 psi static was plausible but not proof of operation | Recovery-machine mass used to quantify charge |
| Repair closure | Diagnosis only; repair and debris were not verified | Demonstration and repair rationale, not a single completed customer case |

The common method is not “check the relay” or “replace the compressor.” It is to cross one boundary at a time and demand an observable response from the next part of the system.

---

## OldSchoolNoe A7 source — current honest boundary

Video: [3 ASE A7 Topics That Seem Difficult At First](https://www.youtube.com/watch?v=hhN-y0wfeds)  
Source status: **official video page, description, and creator's pinned post-test comment checked; no transcript was available and playback did not load**

The page identifies the three intended subjects as:

1. determining how much refrigerant is in the system;
2. leak testing;
3. Section 609 certification material.

In a pinned comment dated October 15, 2023, OldSchoolNoe said his first topic's metering-device material mattered on his test form, he received two leak-detection questions, and his form concentrated on R-134a rather than R-12, R-1234yf, SAE standards, or Section 609 material.

That is a presenter's report about one test experience, not an official or permanent statement of A7 coverage. No technical explanation from the spoken video is summarized here. A later source pass needs working audio, captions, or a transcript before adding his pressure, metering-device, or leak-test reasoning.

