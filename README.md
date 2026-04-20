# Open Design and Technology  
## Final Project README

> **Project Weight:** 70%  
> **Team Size:** 2 students  
> **Project Duration:** 4 weeks  
> **Class Time Available:** 6 hours per class  
> **Total Time Available:** 48 effort-hours per team  
> **Project Type:** Playful, interactive, technology-based experience

---

# Before you begin

## Fork and rename this repository
After forking this repository, rename it using the format:

`ODT-2026-TeamName`

### Example
`ODT-2026-PixelWizards`

Do not keep the default repository name.

---

# How to use this README

This file is your team’s **working project document**.

You must keep updating it throughout the 4-week build period.  
By the final review, this README should clearly show:
- your idea,
- your planning,
- your design decisions,
- your technical process,
- your build progress,
- your testing,
- your failures and changes,
- your final outcome.

## Rules
- Fill every section.
- Do not delete headings.
- If something does not apply, write `Not applicable` and explain why.
- Add images, screenshots, sketches, links, and videos wherever useful.
- Update task status and weekly logs regularly.
- Use this file as evidence of process, not only as a final report.

---

# 1. Team Identity

## 1.1 Studio / Group Name
`[Enter your group name]`

## 1.2 Team Members

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|---|---|---|---|
| `Abhinav Akhare` | `Ideation/ Electronics / Coding / App / Mechanics` | `Fabrication` | `Strong understanding of mechanisms, hands-on prototyping, and integrating electronics with physical systems through iterative testing.` |
| `Riddhi Piratwad` | `-` | `-` | `-` |

## 1.3 Project Title
`Chaos Catapult`

## 1.4 One-Line Pitch
`A sensor-triggered, motorized catapult that combines controlled mechanics with unpredictable outcomes, creating a repeatable yet chaotic play experience.`

## 1.5 Expanded Project Idea
In 1–2 paragraphs, explain:
- what your project is,
- what kind of playful experience it creates,
- what makes it fun, curious, engaging, strange, satisfying, competitive, or delightful,
- what technologies are involved.

**Response:**  
`The Chaos Catapult is a motorized, sensor-driven kinetic system designed to transform simple user input into dynamic launch actions. The project is built around a seesaw-like catapult mechanism, where a controlled sequence of motor movements—combined with a gated release system—creates a repeatable launching process. An IR sensor detects user interaction, triggering a programmed sequence that rewinds, locks, and releases the mechanism, resulting in the projection of an object.

The experience is designed to be playful and engaging through the contrast between control and unpredictability. While the system operates through precise electronic and mechanical coordination, the outcome of each launch varies based on factors like weight, placement, and timing, making every interaction slightly different. This creates a sense of anticipation and satisfaction, encouraging repeated use. The project integrates multiple technologies, including an ESP32 microcontroller, DC and stepper motors for motion control, sensor-based triggering, and LED feedback, all working together to produce a responsive and interactive physical system.`

---

# 2. Philosophy Fit

## 2.1 Experience, Not Social Problem
This module does **not** require your project to solve a large social problem.

You are allowed to build:
- toys,
- games,
- interactive objects,
- playful machines,
- kinetic artifacts,
- humorous devices,
- strange but delightful experiences,
- things that are entertaining to use or watch.

## 2.2 What kind of experience are you creating?
Answer the following:
- What is the experience?
- What do you want the player or participant to feel?
- Why would someone want to try it again?

**Response:**  
`The project creates a playful, interactive experience centered around cause-and-effect, where a simple user action triggers a chain of mechanical and electronic responses leading to a launch. It functions as a kinetic, game-like object that invites users to engage with it physically and observe the outcome. The experience is less about winning or scoring and more about interaction, anticipation, and observing how the system responds.
The intended feeling is a mix of curiosity, anticipation, and satisfaction. Users experience a build-up as the system prepares to launch, followed by a sudden release, which creates a sense of excitement. Since the outcome of each launch can vary based on small changes in input—such as object placement or timing—the interaction feels unpredictable and slightly chaotic.
Users are encouraged to try it repeatedly because each interaction can produce a different result. This variability, combined with the satisfying mechanical motion and responsive feedback, makes the system engaging and replayable, turning a simple action into an enjoyable and dynamic experience.`

## 2.3 Design Persona
Complete the sentence below:

> We are designing this project as if we are a small creative studio making a **[toy / game / playable object / interactive experience]** for **[children / teens / adults / classmates / exhibition visitors / mixed audience]**.

**Response:**  
`[Write here]`

---

# 3. Inspiration

## 3.1 References
List what inspired the project.

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| `[Toy` | `Traditional Catapult / Trebuchet` | `Influenced the idea of launching objects through stored and released energy, creating a playful and physics-based interaction.` |
| `Object / Board game / App / Video / Website / Object]` | `[Link or title]` | `[What did you learn or borrow?]` |
| `Game / Interaction` | `Arcade Trigger-Based Games` | `Inspired the simple input → action → response loop, where a user action immediately triggers a dynamic system reaction.` |

## 3.2 Original Twist
What makes your project original?

**Response:**  
`The project reinterprets a traditional catapult by shifting it from a purely manual mechanism to a partially automated, sensor-driven system. Instead of relying on direct human force, the interaction is mediated through a sequence of electronic and mechanical actions, including motorised actuation and controlled release through a gated mechanism. This introduces a layer of system logic between input and output, transforming a simple physical action into a multi-stage interactive process. What makes the project distinct is the combination of precise control and unpredictable outcomes. While the system is designed to operate through programmed sequences and controlled motion, the final result of each launch varies due to physical factors such as weight distribution, timing, and alignment. This tension between control and variability creates a unique play experience that blends engineered precision with emergent behaviour.`

---

# 4. Project Intent

## 4.1 Core Interaction Loop
Describe the main loop of interaction.

Examples:
- press → launch → score → reset
- connect → control → observe → repeat
- turn → trigger → react → repeat
- move object → sensor detects → sound/light response → player reacts

**Response:**  
`system ready → platform opens → weight drops → motor rewinds mechanism → IR sensor detects position → motor stops → gate closes to hold weight → motor releases (launch action) → system resets to initial state → repeat`

## 4.2 Intended Player / Audience

| Question | Response |
|---|---|
| Who is this for? | `Students & Peers` |
| Age range | `12+` |
| Solo or multiplayer | `Primarily solo, but can be observed and enjoyed by multiple people` |
| Expected duration of one round | `10-15 seconds per cycle` |
| What should the player feel? | `Curiosity, anticipation, and satisfaction from the launch action` |
| Is explanation required before use? | `Minimal explanation required; interaction is mostly intuitive with basic guidance` |

## 4.3 Player Journey
Describe exactly how a player will use the project.

1. **Approach:** `The player approaches the setup, noticing the catapult mechanism and multiple target cups placed at increasing distances.`
2. **Start:** `The player connects to the system through the app and prepares the catapult for use.`
3. **First Action:** `The player places a ball on the platform and uses the app to trigger the system.`
4. **Main Interaction:** `The system runs its sequence—opening the platform, rewinding the mechanism, and preparing for launch—while the player observes and anticipates the outcome.`
5. **System Response:** `The mechanism releases, launching the ball toward the target. The result varies based on placement, timing, and system dynamics.`
6. **Win / Lose / End Condition:** `If the ball lands in the target cup, the player successfully completes that level. If the player misses, they must move the catapult forward (using the wheeled base) to attempt the next target at a different distance.`
7. **Reset:** `The system resets to its initial state, allowing the player to reposition, place another ball, and attempt the next level.`

## 4.4 Rules of Play
If your project is a game, list the rules clearly.

- `The player must place a ball on the catapult platform before triggering the system.`
- `The system can only be activated through the app once the setup is ready.`
- `The objective is to land the ball inside the target cup.`
- `If the player misses, they must reposition the catapult using the wheeled base and attempt the next level.`
 - `Each successful shot allows progression to a farther or more challenging target.`
 - `The system must complete its full cycle (launch and reset) before the next attempt begins.`
---

# 5. Definition of Success

## 5.1 Definition of “Playable”
Your project will be considered complete only if these conditions are met.

- [x] `[The system responds to user input (app or sensor) and initiates the sequence]`
- [x] `[he mechanical system is able to perform the launch action]`
- [ ] `[The motor-driven rewind and release mechanism functions with partial or full consistency]`
- [x] `[The gate mechanism successfully controls the holding and release of the object]`
- [ ] `[The system is able to reset to an initial or near-initial state for repeated interaction]`

## 5.2 Minimum Viable Version
What is the smallest version of this project that still delivers the core experience?

**Response:**  
`The minimum viable version of the project focuses on achieving a partially automated interaction where the system responds to input and executes key stages of the sequence, even if the final actuation is inconsistent.

In this version, components such as sensor detection, sequencing logic, and control of intermediate stages like gate movement function as intended, demonstrating the designed interaction flow. However, the main motor-driven launch may not perform reliably due to hardware limitations.

This still allows the core idea of a staged, system-driven interaction to be understood, where user input triggers a chain of mechanical and electronic responses, even if the final output is not fully realized.`

## 5.3 Stretch Features
What features are nice to have but not essential?

- `Automated scoring system to track successful shots into the target`
- `Adjustable launch power or angle control through the app`
- `Multiple difficulty levels with dynamic target positions or distances`
---

# 6. System Overview

## 6.1 Project Type
Check all that apply.

- [x] Electronics-based
- [x] Mechanical
- [x] Sensor-based
- [x] App-connected
- [x] Motorized
- [ ] Sound-based
- [ ] Light-based
- [ ] Screen/UI-based
- [x] Fabricated structure
- [x] Game logic based
- [x] Installation / tabletop experience
- [ ] Other: `[Write here]`

## 6.2 High-Level System Description
Explain how the system works in simple terms.

Include:
- input,
- processing,
- output,
- physical structure,
- app interaction if any.

**Response:**  
`The project is a multi-stage interactive system that combines electronics, mechanical movement, and programmed logic to create a controlled launching mechanism. At its core, the system is designed so that a simple user input triggers a sequence of coordinated actions rather than a single direct response.
The interaction begins when the system receives input, either through an IR sensor detecting the presence or position of an object, or through a mobile app used to initiate the sequence. This input is processed by the ESP32 microcontroller, which acts as the central control unit. Based on the programmed logic, the ESP32 executes a step-by-step sequence that coordinates multiple components instead of activating them all at once. The system output is achieved through a combination of motors and visual feedback. A stepper motor controls the opening and closing of a gate mechanism, which determines when the object is held or released. A DC motor drives the rewind and release motion of the catapult, creating the force required for launching. LEDs are used to communicate system states, such as readiness, active motion, and completion, helping the user understand what stage the system is in. Physically, the project is built as a wheeled catapult structure with a pivot-based mechanism. The platform holds the object initially, and through the sequence of actions, the object is repositioned and eventually launched. The inclusion of wheels allows the entire system to be repositioned in space, enabling different levels or target distances as part of the gameplay.
The mobile app acts as an interface layer between the user and the system, allowing control over when the sequence begins and potentially adjusting how the system behaves. Overall, the project integrates input, processing, and output into a coordinated system where mechanical movement and electronic control work together to produce a dynamic and repeatable interaction.`

## 6.3 Input / Output Map

| System Part | Type | What It Does |
|---|---|---|
| IR Sensor          | Input                | Detects the presence or position of the weight/ball and signals the system to proceed with the sequence |
| Mobile App         | Input                | Allows the user to trigger and control the system remotely                                              |
| ESP32              | Processing           | Acts as the central controller, executing the programmed sequence and coordinating all components       |
| Step-Up Converter  | Processing / Power   | Regulates and boosts voltage to provide sufficient power for motors, ensuring stable operation          |
| Motor Driver       | Processing / Control | Interfaces between ESP32 and motors, controlling direction and power delivery                           |
| DC Motor           | Output               | Drives the rewind and release mechanism responsible for the launching action                            |
| Stepper Motor      | Output               | Controls precise opening and closing of the gate mechanism                                              |
| LEDs               | Output               | Provide visual feedback for system states (ready, active, rewinding, reset)                             |
| Catapult Mechanism | Physical Action      | Converts rotational motion into a launching force through a pivot-based system                          |
| Gate Mechanism     | Physical Action      | Holds and releases the object at the correct stage of the sequence                                      |
| Wheeled Base       | Physical Action      | Allows repositioning of the system for level-based gameplay   | NEMA 17 Stepper Motor | Output | Provides precise control for rewind and release |


---

# 7. Sketches and Visual Planning

## 7.1 Concept Sketch
Add an early sketch of the full idea.

**Insert image below:**  
`[Upload image and link here]`

Example:
```md

```

## 7.2 Labeled Build Sketch
Add a sketch with labels showing:
- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  
`[Upload image and link here]`

## 7.3 Approximate Dimensions

| Dimension | Value |
|---|---|
| Length | `40cm` |
| Width | `[25cm]` |
| Height | `[50cm]` |
| Estimated weight | `[400-500gms]` |

---

# 8. Mechanical Planning

## 8.1 Mechanical Features
Check all that apply.

- [ ] Gears
- [x] Pulleys
- [ ] Belt drives
- [ ] Linkages
- [x] Hinges
- [x] Shafts
- [ ] Springs
- [ ] Bearings
- [x] Wheels
- [ ] Sliders
- [x] Levers
- [ ] Not applicable

## 8.2 Mechanical Description
Describe the mechanism and what it is meant to do.

**Response:**  
`[The mechanical system is based on a lever-driven catapult mechanism, where a pivot point allows rotational motion to be converted into a launching action. A platform holds the object initially, and through controlled movement, the system transfers force to propel the object forward.
A pulley system is integrated with the motor to lift and rewind the weight. As the motor rotates, the pulley winds a string or linkage, pulling the mechanism into a loaded position. This allows energy to be stored and later released during the launch phase.
A gate mechanism is used to control when the object is released. This gate is actuated using a stepper motor, allowing precise opening and closing at specific stages of the sequence.
During development, the initial DC motor showed inconsistent performance during the rewind stage, including irregular motion and unreliable operation under load. To address this, a NEMA 17 stepper motor was introduced as an alternative, as it provides better control and more consistent torque for lifting and positioning the mechanism.
The entire system is mounted on a wheeled base, allowing it to be repositioned for different target distances and levels. The combination of lever mechanics, pulley-based lifting, and motor-driven control creates a staged and interactive mechanical system.]`

## 8.3 Motion Planning
If something moves, explain:
- what moves,
- what causes the movement,
- how far it moves,
- how fast it moves,
- what could go wrong.

**Response:**  
`[]`

## 8.4 Simulation / CAD / Animation Before Making
If your project includes mechanical motion, document the digital planning before fabrication.

| Tool Used | File / Link | What Was Tested |
|---|---|---|
| `Not Applicable]` | `-` | `[No simulation or animation was performed; the mechanism was developed through physical prototyping and testing` |

## 8.5 Changes After Digital Testing
What changed after the CAD, animation, or simulation stage?

**Response:**  
`Not applicable, as no digital simulation was used. Changes were made directly through physical testing and iteration during the build process.`

---

# 9. Electronics Planning

## 9.1 Electronics Used

| Component | Quantity | Purpose |
| Component              | Quantity | Purpose                                                 |
| ESP32                  |        1 | Main controller to process input and control the system |
| IR Sensor              |        1 | Detects the presence/position of the object             |
| DC Motor               |        1 | Drives the rewind and release mechanism                 |
| NEMA 17 Stepper Motor  |        1 | Used as an alternative for improved torque and control  |
| Stepper Motor (Gate)   |        1 | Controls opening and closing of the gate                |
| Motor Driver           |        1 | Controls motor direction and power delivery             |
| Step-Up Converter      |        1 | Boosts voltage to provide sufficient power to motors    |
| LEDs                   |        2 | Provide visual feedback for system states               |
| Power Bank             |        1 | Supplies power to the system                            |

## 9.2 Wiring Plan
Describe the main electrical connections.

**Response:**  
`The system is powered using a power bank, which was modified to supply power through a step-up converter. The output from the step-up converter is connected to the power rails, which distribute power to the motors and other components.
The ESP32 is also powered through the power rails. A resistor-based connection is used along with a GPIO pin (keep_alive) to keep the power bank active continuously and prevent it from shutting off due to low current draw.
The IR sensor is connected to the ESP32, with power from the 3.3V pin and its output connected to a GPIO pin for input detection.
Motor control is handled using L298N motor drivers. The ESP32 is connected to the input pins (IN1, IN2, etc.) of the motor drivers to control motor direction. The enable pins are kept active or controlled via PWM depending on the requirement. One driver is used for the DC motor (and later testing with the NEMA 17), and another is used for additional motor control.
The motors are connected to the output terminals of the motor drivers, which receive power from the step-up converter to ensure sufficient voltage for operation under load.
LEDs are connected to GPIO pins on the ESP32 with resistors to provide visual feedback for different system states.
All components share a common ground through the power rails, ensuring stable communication and proper functioning of the system.`

## 9.3 Circuit Diagram
Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[Upload image and link here]`

## 9.4 Power Plan

| Question | Response |
|---|---|
| Power source | `[USB / battery / adapter / other]` |
| Voltage required | `[Write here]` |
| Current concerns | `[Write here]` |
| Safety concerns | `[Write here]` |

---

# 10. Software Planning

## 10.1 Software Tools

| Tool / Platform | Purpose |
| Tool / Platform                    | Purpose                                                                 |
| ---------------------------------- | ----------------------------------------------------------------------- |
| MicroPython                        | Used to program the ESP32 and control sensors, motors, and system logic |
| MIT App Inventor                   | Used to create a mobile app for triggering and controlling the system   |
|Thonny | Used to write, upload, and test code on the ESP32                       |


## 10.2 Software Logic
Describe what the code must do.

Include:
- startup behavior,
- input handling,
- sensor reading,
- decision logic,
- output behavior,
- communication logic,
- reset behavior.

**Response:**  
`The system is programmed using MicroPython on the ESP32 and follows a stage-based logic controlled through a mobile app.
At startup, all pins are initialized for motors, LEDs, and sensors, and the ESP32 connects to the app. The user sends commands like calibration, drop, close, rewind, and unwind through the app.
The system first runs in a manual calibration mode, where the gate position is adjusted using left/right controls. Once set, a “done” command locks the position.
After calibration, the system follows a sequence. A drop command opens the gate using the stepper motor. Then the rewind stage starts, where the mechanism is pulled back. In the DC motor version, this is done using continuous motor rotation, while in the NEMA stepper version, controlled stepping is used.
In the NEMA version, the rewind continues until the IR sensor detects the correct position, at which point the motor stops. This adds more control compared to the DC motor version.
A close command then shuts the gate to hold the weight. Finally, the unwind stage releases the stored energy, creating the launch action.
LEDs are used throughout to show system states like active movement, rewinding, and completion.
The system runs in a loop, constantly checking for app inputs and updating its state, allowing repeated cycles of interaction.`

## 10.3 Code Flowchart
Insert a flowchart showing your code logic.

Suggested sequence:
- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

**Insert image below:**  
`[Upload image and link here]`

## 10.4 Pseudocode

```text
START

Initialize system (ESP32, pins, app)

WHILE true:
    Check for app input

    IF not calibrated:
        Allow manual gate control (left/right)
        IF user presses done:
            lock system

    ELSE:
        IF drop command:
            open gate

        IF rewind active:
            run motor
            IF IR detects position:
                stop motor

        IF close command:
            close gate

        IF unwind active:
            release mechanism (launch)

    Update LEDs based on state

END LOOP
```

---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?
- [x] Yes
- [ ] No

If yes, complete this section.

## 11.2 Why is the app needed?
Explain what the app adds to the experience.

Examples:
- remote control,
- score tracking,
- mode selection,
- personalization,
- triggering effects,
- displaying data.

**Response:**  
`The app is used to control and trigger the system wirelessly, allowing the user to interact with the catapult without directly touching the hardware. It enables actions such as calibration, opening and closing the gate, and controlling the rewind and release stages.
The app also allows movement control, enabling the system to move forward and backward for different levels or target distances. This adds flexibility to the interaction and supports the gameplay aspect.
Using the app makes the interaction more controlled and intuitive, as all actions are managed through a single interface instead of multiple physical inputs.`

## 11.3 App Features

| Feature | Purpose |
| -------------------------- | -------------------------------------------------- |
| Left / Right Control       | Used during calibration to adjust gate position    |
| Done Button                | Locks the system after calibration is complete     |
| Drop Button                | Triggers opening of the gate to release the object |
| Close Button               | Closes the gate to hold the object in place        |
| Rewind Button              | Activates motor to pull the mechanism back         |
| Unwind Button              | Releases the mechanism to perform the launch       |
| Stop Button                | Stops motor movement when required                 |
| Forward / Backward Control | Moves the system for level-based gameplay          |

## 11.4 UI Mockup
Insert a sketch or screenshot of the app interface.

**Insert image below:**  
`[Upload image and link here]`

## 11.5 App Screen Flow

1. Open the app and access the control interface
2. Use left/right controls to calibrate the gate position
3. Press “Done” to lock the system in place
4. Use buttons like drop, rewind, close, and unwind to run the sequence
5. Use forward/backward controls to reposition the system for different levels
6. Repeat the process for each attempt
---

# 12. Bill of Materials

## 12.1 Full BOM

| Item                  | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec     | Why This Choice?                          |
| --------------------- | -------: | ------- | ------------ | -------------: | ------------------- | ----------------------------------------- |
| ESP32                 |        1 | Yes     | No           |              0 | Microcontroller     | Main controller for system logic          |
| IR Sensor             |        1 | Yes     | No           |              0 | Digital sensor      | Detects object position                   |
| DC Motor              |        2 | No      | Yes          |           ₹150 | Standard DC motor   | Used for rewind and motion                |
| NEMA 17 Stepper Motor |        1 | Yes     | No           |              0 | Stepper motor       | Tested for better torque and control      |
| Stepper Motor (Gate)  |        1 | Yes     | No           |              0 | Stepper motor       | Controls gate opening/closing             |
| L298N Motor Driver    |        2 | Yes     | No           |              0 | Motor driver module | Controls motor direction and power        |
| Step-Up Converter     |        1 | No      | Yes          |           ₹100 | Voltage booster     | Provides sufficient voltage to motors     |
| Wheels                |      2–4 | No      | Yes          |           ₹150 | Plastic wheels      | Enables movement for level-based gameplay |
| LEDs                  |        2 | Yes     | No           |              0 | Red & Green LEDs    | Visual feedback                           |
| Resistors             |      Few | Yes     | No           |              0 | Standard            | Used for LEDs and keep-alive circuit      |
| Power Bank            |        1 | Yes     | No           |              0 | 5V output           | Main power source                         |
| Wires / Connectors    |     Many | Yes     | No           |              0 | Jumper wires        | Electrical connections                    |
| Structural Material   |        — | Yes     | No           |              0 | MDF / board         | Physical structure                        |
| NEMA 17 Stepper Motor | 1 | No | Yes | ₹500 | Stepper motor | Purchased as a replacement due to DC motor performance issues |

## 12.2 Material Justification
Explain why you selected your main materials and components.

Examples:
- Why acrylic instead of cardboard?
- Why MDF instead of 3D print?
- Why servo instead of DC motor?
- Why bearing instead of a plain shaft hole?

**Response:**  
`The main structure of the project is made using MDF and wood as they are strong, easily available, and suitable for building stable mechanical systems. These materials are easy to cut, assemble, and modify during testing, which was important for iterative prototyping.
MDF provides a flat and rigid surface for mounting components, while wood adds additional strength to areas requiring support. Compared to materials like cardboard, they offer better durability and can handle the load and movement of motors and the catapult mechanism.`

## 12.3 Items to Purchase Separately

| Item                  | Why Needed                                                       | Purchase Link | Latest Safe Date to Procure | Status   |
| --------------------- | ---------------------------------------------------------------- | ------------- | --------------------------- | -------- |
| DC Motors             | For rewind and movement mechanism                                | —             | Week 2                      | Received |
| Step-Up Converter     | To provide sufficient voltage for motors                         | —             | Week 2                      | Received |
| Wheels                | To enable movement for level-based gameplay                      | —             | Week 2                      | Received |
| NEMA 17 Stepper Motor | Emergency purchase to replace DC motor due to performance issues | —             | Week 4                      | Received |


## 12.4 Budget Summary

| Budget Item           | Estimated Cost |
| --------------------- | -------------: |
| Electronics           |           ₹650 |
| Mechanical parts      |           ₹150 |
| Fabrication materials |           ₹100 |
| Purchased extras      |             ₹0 |
| Contingency           |             ₹0 |
| **Total**             |       **₹900** |


## 12.5 Budget Reflection
If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  
`Most of the components were selected appropriately for the project, but the main challenge was with motor performance. The emergency purchase of the NEMA 17 stepper motor increased the overall cost but did not fully resolve the issue.
In hindsight, a better motor driver or power management setup for the DC motor could have been a more effective solution instead of replacing the motor entirely. This highlights the importance of selecting the right control and power components early in the design process.`

---

# 13. Planning the Work

## 13.1 Team Working Agreement
Write how your team will work together.

Include:
- how tasks are divided,
- how decisions are made,
- how progress will be checked,
- what happens if a task is delayed,
- how documentation will be maintained.

**Response:**  
`The project was initially planned with different parts like mechanics, electronics, and coding. However, since all these parts were closely connected, most of the work was handled together to keep the system consistent.
Work was done through continuous testing and iteration. Decisions were made based on what worked during testing, and changes were made accordingly.
Progress was tracked by testing different parts of the system and updating the documentation alongside the build. Any issues or delays were handled during the process by adjusting the approach and trying alternative solutions.`

## 13.2 Task Breakdown

| Task ID | Task                                | Owner          | Estimated Hours | Deadline | Dependency | Status      |
| ------- | ----------------------------------- | -------------- | --------------: | -------- | ---------- | ----------- |
| T1      | Finalize concept and interaction    | Abhinav Akhare |               3 | Week 1   | None       | Done        |
| T2      | Create sketches and design planning | Abhinav Akhare |               4 | Week 1   | T1         | Done        |
| T3      | Source components and finalize BOM  | Abhinav Akhare |               2 | Week 1   | T1         | Done        |
| T4      | Test electronics (motors, sensors)  | Abhinav Akhare |               6 | Week 2   | T3         | Done        |
| T5      | Build mechanical structure          | Abhinav Akhare |               8 | Week 2   | T2         | Done        |
| T6      | Develop and test control code       | Abhinav Akhare |              10 | Week 3   | T4         | Done        |
| T7      | Integrate system (hardware + code)  | Abhinav Akhare |               8 | Week 3   | T5, T6     | Done        |
| T8      | Debug and refine system             | Abhinav Akhare |               5 | Week 4   | T7         | Done        |
| T9      | Documentation and final updates     | Abhinav Akhare |               4 | Week 4   | T8         | In Progress |


## 13.3 Responsibility Split

| Area                 | Main Owner     | Support Owner |
| -------------------- | -------------- | ------------- |
| Concept and gameplay | Abhinav Akhare | —             |
| Electronics          | Abhinav Akhare | —             |
| Coding               | Abhinav Akhare | —             |
| App                  | Abhinav Akhare | —             |
| Mechanical build     | Abhinav Akhare | —             |
| Testing              | Abhinav Akhare | —             |
| Documentation        | Abhinav Akhare | —             |


---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk
Expected outcomes:
- [x] Idea finalized
- [ ] Core interaction decided
- [x] Sketches made
- [x] BOM completed
- [x] Purchase needs identified
- [x] Key uncertainty identified
- [ ] Basic feasibility tested

### Week 2 — Build Subsystems
Expected outcomes:
- [x] Electronics tests completed
- [x] CAD / structure planning completed
- [ ] App UI started if needed
- [x] Mechanical concept tested
- [x] Main subsystems partially working

### Week 3 — Integrate
Expected outcomes:
- [x] Physical body built
- [x] Electronics integrated
- [x] Code connected to hardware
- [ ] App connected if required
- [ ] First playable version exists

### Week 4 — Refine and Finish
Expected outcomes:
- [ ] Technical bugs reduced
- [ ] Playtesting completed
- [ ] Improvements made
- [x] Documentation completed
- [x] Final build ready

## 14.2 Weekly Update Log

| Week   | Planned Goal               | What Actually Happened                                                                              | What Changed                                                | Next Steps                                     |
| ------ | -------------------------- | --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ---------------------------------------------- |
| Week 1 | Finalize idea and planning | Idea and overall interaction were finalized; initial direction was clear                            | Focus was more on concept than detailed technical planning  | Begin building structure and gather components |
| Week 2 | Build and test subsystems  | Mechanical structure was developed and components were organized                                    | Electronics setup was planned but not fully implemented yet | Start electronics integration and coding       |
| Week 3 | Integration and coding     | Coding and wiring were developed, and initial system integration was attempted                      | Motor behavior required further tuning and testing          | Improve motor control and refine system        |
| Week 4 | Final build and testing    | Major system integration, coding updates, and component adjustments (including NEMA) were completed | Adjustments were made to improve performance and control    | Finalize documentation and system explanation  |

---

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk                                         | Likelihood | Impact | Mitigation / Response                                                       |
| -------------------------------------------- | ---------- | ------ | --------------------------------------------------------------------------- |
| DC motor not providing enough torque         | High       | High   | Issue identified during testing; replacement with NEMA motor attempted late |
| NEMA motor driver not handling load properly | High       | High   | Limited time for proper tuning; basic testing done                          |
| Stepper motor jamming during operation       | Medium     | High   | Observed during testing; likely due to alignment/load issues                |
| IR sensor giving inconsistent readings       | Medium     | Medium | Position adjusted but readings remained unreliable                          |
| Wheels unable to support system weight       | Medium     | Medium | Movement was reduced to avoid overload                                      |
| Power supply instability (power bank limits) | High       | High   | Step-up converter and keep-alive used, but limitations remained             |
| Timing mismatch between stages               | Medium     | Medium | Minor adjustments in code, but full synchronization not achieved            |
| Integration issues between components        | High       | High   | Integration attempted late; limited time for full debugging                 |
| Platform shape causing instability and misalignment | Medium | High | Iterated on shape during build, but consistent alignment was difficult to achieve |

## 15.2 Biggest Unknown Right Now
What is the single biggest uncertainty in your project at this stage?

**Response:**  
`One of the main failures in the system was the rewind mechanism. Both the DC motor and later the NEMA 17 stepper motor struggled to pull the weight effectively through the pulley system. The DC motor showed inconsistent behavior and lacked sufficient torque under load, which caused unreliable movement.
To address this, a NEMA 17 motor was introduced, but it also faced issues due to driver limitations and insufficient torque delivery in the given setup. As a result, the system was unable to consistently lift and position the weight for the launch sequence.
Additional issues included the stepper motor jamming at times, inconsistent readings from the IR sensor, and instability caused by the shape of the platform, which affected alignment. The wheels also faced difficulty supporting the overall load during movement.
These failures highlighted challenges in motor selection, load handling, and overall system integration.`

---

# 16. Testing and Playtesting

## 16.1 Technical Testing Plan

| What Needs Testing             | How You Will Test It                                        | Success Condition                                             |
| ------------------------------ | ----------------------------------------------------------- | ------------------------------------------------------------- |
| App connection (WiFi/App link) | Connect phone to ESP32 network and send commands from app   | Commands are received and printed/responded correctly         |
| Mechanism movement             | Run motors (DC/NEMA and stepper) through app commands       | Motors move in correct direction and complete intended motion |
| Sensor behavior (IR)           | Place/remove object in front of sensor and monitor response | Sensor reliably detects presence/absence and triggers logic   |
| App communication              | Send actions like drop, close, rewind, unwind from app      | System responds correctly to each command without delay       |

## 16.2 Playtesting Plan

| Question                             | How You Will Check                                                                                                         |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| Do players understand what to do?    | Observe if users can place the ball correctly and use the app controls (drop, rewind, close) without detailed instructions |
| Is the interaction satisfying?       | Observe reactions during the launch attempt, especially the rewind → release sequence                                      |
| Do players want another turn?        | Check if users try to adjust position (using wheels) and attempt again after missing the target                            |
| Is the challenge balanced?           | Test different distances of the cup and see if users can reasonably aim using repositioning                                |
| Is the response clear and immediate? | Observe if users understand system states through motor movement and LED feedback during each stage                        |


## 16.3 Testing and Debugging Log

| Date            | Problem Found                                         | Type        | What You Tried                                             | Result | Next Action                                  |
| --------------- | ----------------------------------------------------- | ----------- | ---------------------------------------------------------- | ------ | -------------------------------------------- |
| Week 4          | DC motor unable to pull weight consistently           | Technical   | Increased voltage using step-up converter and reduced load | Partly | Look into stronger motor option              |
| Week 3          | IR sensor giving inconsistent readings                | Technical   | Adjusted sensor placement and tested multiple times        | Partly | Improve positioning and stability            |
| Week 4          | Stepper motor jamming during movement                 | Mechanical  | Checked alignment and reduced friction in mechanism        | Partly | Refine alignment and reduce resistance       |
| Week 3          | Wheels unable to support system weight                | Mechanical  | Tested movement with reduced load                          | Partly | Improve wheel support or reduce weight       |
| Week 4          | NEMA motor introduced but driver struggled under load | Technical   | Tested NEMA with existing driver setup                     | Failed | Explore better driver or alternative setup   |
| Post-exhibition | Full system integration not stable                    | Integration | Tested components individually and reviewed sequence       | Partly | Improve power management and synchronization |

## 16.4 Playtesting Notes

| Tester  | What They Did                                             | What Confused Them                                                                | What They Enjoyed                            | What You Will Change                                             |
| ------- | --------------------------------------------------------- | --------------------------------------------------------------------------------- | -------------------------------------------- | ---------------------------------------------------------------- |
| Baratth | Tried to operate the system and place the ball for launch | Had difficulty understanding how to correctly set and calibrate the gate position | Liked the idea of launching towards a target | Simplify the gate calibration process and make it more intuitive |

---

# 17. Build Documentation

## 17.1 Fabrication Process
Describe how the project was physically made.

Include:
- cutting,
- 3D printing,
- assembly,
- fastening,
- wiring,
- finishing,
- revisions.

**Response:**  
The fabrication process started with a rough foam model to understand the proportions and basic working of the mechanism. This helped in figuring out the placement of components and overall structure before moving to final materials.
Based on this, measurements were taken alongside ideation and the main parts were laser cut using MDF. During assembly in the wood lab, several adjustments were made to improve alignment and fit, especially for the pivot and pulley system.
The structure was assembled using basic fastening methods like screws and joints. Some components, such as axle caps, were 3D printed to support the wheel mechanism and ensure proper fitting.
Electronics were integrated after the basic structure was ready. Wiring was done using power rails, with the power bank connected through a step-up converter. The power bank was modified and connected in a way that allowed continuous supply using a keep-alive setup.
Multiple revisions were made during the build process, especially to adjust alignment, improve movement, and integrate the motors properly. Final finishing involved securing components, organizing wiring, and making the system stable for testing.

## 17.2 Build Photos
Add photos throughout the project.

Suggested images:
- early sketch,
- prototype,
- electronics testing,
- mechanism test,
- app screenshot,
- final build.

Example:
```md



```

## 17.3 Version History

| Version | Date     | What Changed                                                   | Why                                                           |
| ------- | -------- | -------------------------------------------------------------- | ------------------------------------------------------------- |
| `v1`    | Week 1   | Initial concept with basic catapult and manual mechanism       | To establish core idea and interaction                        |
| `v2`    | Week 2–3 | Added motor control, gate mechanism, and app integration       | To automate the system and improve interaction                |
| `v3`    | Week 4   | Introduced NEMA motor and made structural + wiring adjustments | To address motor performance issues and improve load handling |

---

# 18. Final Outcome

## 18.1 Final Description
Describe the final version of your project.

**Response:**  
`The final version of the project is a motor-driven catapult system controlled through an app, combining a gate mechanism, pulley-based rewind system, and sensor-based logic. The system is designed to follow a sequence where the gate opens, the mechanism rewinds, and then releases to launch an object.
While individual parts like the app control, gate movement, and basic motor responses worked, the full system did not perform consistently due to issues with motor torque, load handling, and integration. However, the project demonstrates the intended interaction flow and system design.`

## 18.2 What Works Well
- `1. App control and command-based interaction works reliably
2. Gate mechanism using stepper motor functions as intended
3. Overall mechanical system (lever, pulley, structure) works well
4. Overall concept and interaction flow is clear and understandable`

## 18.3 What Still Needs Improvement
- `1. Motor system is not strong enough to handle the load consistently
2. Power and driver setup needs better optimization
3. Full system integration and synchronization between stages
4. Better alignment of pulley and platform to reduce resistance and jamming
5. More reliable sensor behavior (IR stability and accuracy)
6. Improved structural balance to support weight distribution (especially for wheels and movement)
7. Simplification of control flow to reduce dependency on multiple manual triggers`

## 18.4 What Changed From the Original Plan
How did the project change from the initial idea?

**Response:**  
`The initial idea was to create a fully automated catapult system where all stages—gate opening, rewind, detection, and release—would happen smoothly in a single sequence with minimal user input.
During development, the project evolved due to practical challenges with motor performance, load handling, and power supply. The system required more manual control through the app, and stages like rewind and release had to be triggered separately rather than running seamlessly.
There were also changes in components, such as replacing the DC motor with a NEMA stepper motor in an attempt to improve torque and control. Structural adjustments were made to the platform and pulley system to improve movement and alignment.
Overall, the project shifted from a fully automated system to a semi-controlled interactive system, focusing more on demonstrating the sequence and interaction rather than achieving perfect automation.`

---

# 19. Reflection

## 19.1 Team Reflection
What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
`The project was handled mostly individually, which helped maintain consistency across mechanics, electronics, and coding. A lot of progress was made through hands-on experimentation and trying things out directly.
What slowed things down was time management and late integration. Many components came together towards the end, which made debugging difficult. Better planning and earlier testing of critical parts like motors and power systems would have improved the overall outcome.`

## 19.2 Technical Reflection
What did you learn about:
- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
`This project helped in understanding how electronics, coding, and mechanical systems work together in a real setup. Working with motors, drivers, and power systems showed how important torque and proper voltage are, especially under load.
On the coding side, writing logic for stages, handling inputs from the app, and integrating sensors was a good learning experience. It also highlighted how small issues in hardware can affect the entire system.
Fabrication and mechanisms were interesting to work on, especially combining lever motion with pulley systems. Overall, the biggest learning was how difficult integration is when multiple systems depend on each other.`

## 19.3 Design Reflection
What did you learn about:
- designing for play,
- delight,
- clarity,
- physical interaction,
- player understanding,
- iteration?

**Response:**  
`The project showed that designing for play is not just about the idea but also about how clearly the interaction is understood by the user. Even a simple action like launching becomes more engaging when combined with stages and anticipation.
It also became clear that too many steps or controls can make the interaction confusing, so simplifying the flow is important. Physical interaction, like moving the system and aiming, added a fun aspect to the design.
Iteration played a big role, as many changes were made during the build to improve how the system worked and felt.`

## 19.4 If You Had One More Week
What would you improve next?

**Response:**  
`With more time, the main focus would be on improving the motor and power system to make the launch sequence reliable. I would also simplify the control flow so that the system runs more automatically instead of relying on multiple manual inputs.
Better testing earlier in the process would be a priority, especially for load handling and integration. Minor improvements in alignment, sensor stability, and overall finishing would also help make the system more consistent and user-friendly.`

---

# 20. Final Submission Checklist

Before submission, confirm that:
- [x] Team details are complete
- [x] Project description is complete
- [x] Inspiration sources are included
- [x] Player journey is written
- [ ] Sketches are added
- [x] BOM is complete
- [x] Purchase list is complete
- [x] Budget summary is complete
- [ ] Mechanical planning is documented if applicable
- [x] App planning is documented if applicable
- [ ] Code flowchart is added
- [x] Task breakdown is complete
- [x] Weekly logs are updated
- [x] Risk register is complete
- [x] Testing log is updated
- [x] Playtesting notes are included
- [ ] Build photos are included
- [x] Final reflection is written

---

# 21. Suggested Repository Structure

```text
project-repo/
├── README.md
├── images/
│   ├── concept-sketch.jpg
│   ├── labeled-sketch.jpg
│   ├── circuit-diagram.jpg
│   ├── ui-mockup.jpg
│   ├── prototype-1.jpg
│   └── final-build.jpg
├── code/
│   ├── main.py
│   ├── test_code.py
│   └── notes.md
├── cad/
│   ├── models/
│   └── screenshots/
└── docs/
    ├── references.md
    └── extra-notes.md
```

---

# 22. Instructor Review

## 22.1 Proposal Approval
- [ ] Approved to proceed
- [ ] Approved with changes
- [ ] Rework required before proceeding

**Instructor comments:**  
`[Instructor fills this section]`

## 22.2 Midpoint Review
`[Instructor fills this section]`

## 22.3 Final Review Notes
`[Instructor fills this section]`
