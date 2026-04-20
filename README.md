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
| `[Button / Sensor / Switch / App Input]` | Input | `[Describe]` |
| `[ESP32 / Controller]` | Processing | `[Describe]` |
| `[LED / Motor / Servo / Buzzer / Display]` | Output | `[Describe]` |
| `[Mechanical Assembly]` | Physical Action | `[Describe]` |

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
| Length | `[Write here]` |
| Width | `[Write here]` |
| Height | `[Write here]` |
| Estimated weight | `[Write here]` |

---

# 8. Mechanical Planning

## 8.1 Mechanical Features
Check all that apply.

- [ ] Gears
- [ ] Pulleys
- [ ] Belt drives
- [ ] Linkages
- [ ] Hinges
- [ ] Shafts
- [ ] Springs
- [ ] Bearings
- [ ] Wheels
- [ ] Sliders
- [ ] Levers
- [ ] Not applicable

## 8.2 Mechanical Description
Describe the mechanism and what it is meant to do.

**Response:**  
`[Write here]`

## 8.3 Motion Planning
If something moves, explain:
- what moves,
- what causes the movement,
- how far it moves,
- how fast it moves,
- what could go wrong.

**Response:**  
`[Write here]`

## 8.4 Simulation / CAD / Animation Before Making
If your project includes mechanical motion, document the digital planning before fabrication.

| Tool Used | File / Link | What Was Tested |
|---|---|---|
| `[Fusion 360 / Tinkercad / other]` | `[Link or screenshot]` | `[What did you validate?]` |
| `[Tool]` | `[Link or screenshot]` | `[What did you validate?]` |

## 8.5 Changes After Digital Testing
What changed after the CAD, animation, or simulation stage?

**Response:**  
`[Write here]`

---

# 9. Electronics Planning

## 9.1 Electronics Used

| Component | Quantity | Purpose |
|---|---:|---|
| `[ESP32]` | `1` | `[Main controller]` |
| `[Component]` | `[Qty]` | `[Purpose]` |
| `[Component]` | `[Qty]` | `[Purpose]` |

## 9.2 Wiring Plan
Describe the main electrical connections.

**Response:**  
`[Write here]`

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
|---|---|
| `[MicroPython / Arduino / MIT App Inventor / CAD tool / other]` | `[Purpose]` |
| `[Tool]` | `[Purpose]` |

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
`[Write here]`

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
[Write your pseudocode here]
```

---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?
- [ ] Yes
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
`[Write here]`

## 11.3 App Features

| Feature | Purpose |
|---|---|
| `[Bluetooth connect button]` | `[Purpose]` |
| `[Score display]` | `[Purpose]` |
| `[Control button / slider / label]` | `[Purpose]` |

## 11.4 UI Mockup
Insert a sketch or screenshot of the app interface.

**Insert image below:**  
`[Upload image and link here]`

## 11.5 App Screen Flow

1. `[Step 1]`
2. `[Step 2]`
3. `[Step 3]`
4. `[Step 4]`

---

# 12. Bill of Materials

## 12.1 Full BOM

| Item | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec | Why This Choice? |
|---|---:|---|---|---:|---|---|
| `[ESP32]` | `1` | `Yes` | `No` | `0` | `[Spec]` | `[Reason]` |
| `[Item]` | `[Qty]` | `[Yes/No]` | `[Yes/No]` | `[Cost]` | `[Spec]` | `[Reason]` |
| `[Item]` | `[Qty]` | `[Yes/No]` | `[Yes/No]` | `[Cost]` | `[Spec]` | `[Reason]` |

## 12.2 Material Justification
Explain why you selected your main materials and components.

Examples:
- Why acrylic instead of cardboard?
- Why MDF instead of 3D print?
- Why servo instead of DC motor?
- Why bearing instead of a plain shaft hole?

**Response:**  
`[Write here]`

## 12.3 Items to Purchase Separately

| Item | Why Needed | Purchase Link | Latest Safe Date to Procure | Status |
|---|---|---|---|---|
| `[Item]` | `[Reason]` | `[Link]` | `[Date]` | `[Pending / Ordered / Received]` |
| `[Item]` | `[Reason]` | `[Link]` | `[Date]` | `[Pending / Ordered / Received]` |

## 12.4 Budget Summary

| Budget Item | Estimated Cost |
|---|---:|
| Electronics | `[Cost]` |
| Mechanical parts | `[Cost]` |
| Fabrication materials | `[Cost]` |
| Purchased extras | `[Cost]` |
| Contingency | `[Cost]` |
| **Total** | `[Cost]` |

## 12.5 Budget Reflection
If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  
`[Write here]`

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
`[Write here]`

## 13.2 Task Breakdown

| Task ID | Task | Owner | Estimated Hours | Deadline | Dependency | Status |
|---|---|---|---:|---|---|---|
| T1 | `[Finalize concept]` | `[Name]` | `2` | `[Date]` | `None` | `To Do` |
| T2 | `[Complete BOM]` | `[Name]` | `1` | `[Date]` | `T1` | `To Do` |
| T3 | `[Test electronics]` | `[Name]` | `2` | `[Date]` | `T1` | `To Do` |
| T4 | `[Build structure]` | `[Name]` | `4` | `[Date]` | `T1` | `To Do` |
| T5 | `[Write control code]` | `[Name]` | `4` | `[Date]` | `T3` | `To Do` |
| T6 | `[Integrate system]` | `[Name]` | `4` | `[Date]` | `T4, T5` | `To Do` |
| T7 | `[Playtest]` | `[Name]` | `2` | `[Date]` | `T6` | `To Do` |
| T8 | `[Refine and document]` | `[Name]` | `3` | `[Date]` | `T7` | `To Do` |

## 13.3 Responsibility Split

| Area | Main Owner | Support Owner |
|---|---|---|
| Concept and gameplay | `[Name]` | `[Name]` |
| Electronics | `[Name]` | `[Name]` |
| Coding | `[Name]` | `[Name]` |
| App | `[Name]` | `[Name]` |
| Mechanical build | `[Name]` | `[Name]` |
| Testing | `[Name]` | `[Name]` |
| Documentation | `[Name]` | `[Name]` |

---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk
Expected outcomes:
- [ ] Idea finalized
- [ ] Core interaction decided
- [ ] Sketches made
- [ ] BOM completed
- [ ] Purchase needs identified
- [ ] Key uncertainty identified
- [ ] Basic feasibility tested

### Week 2 — Build Subsystems
Expected outcomes:
- [ ] Electronics tests completed
- [ ] CAD / structure planning completed
- [ ] App UI started if needed
- [ ] Mechanical concept tested
- [ ] Main subsystems partially working

### Week 3 — Integrate
Expected outcomes:
- [ ] Physical body built
- [ ] Electronics integrated
- [ ] Code connected to hardware
- [ ] App connected if required
- [ ] First playable version exists

### Week 4 — Refine and Finish
Expected outcomes:
- [ ] Technical bugs reduced
- [ ] Playtesting completed
- [ ] Improvements made
- [ ] Documentation completed
- [ ] Final build ready

## 14.2 Weekly Update Log

| Week | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Week 1 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 2 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 3 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 4 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |

---

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| `[Example: Bluetooth disconnects]` | `Technical` | `Medium` | `High` | `[Fallback interaction / simplify connection flow]` | `[Name]` |
| `[Example: Structure breaks during play]` | `Mechanical` | `Medium` | `High` | `[Reinforce joints / change material]` | `[Name]` |
| `[Risk]` | `[Technical / Material / Time / Gameplay]` | `[Low/Medium/High]` | `[Low/Medium/High]` | `[Plan]` | `[Name]` |
| `[Risk]` | `[Type]` | `[Low/Medium/High]` | `[Low/Medium/High]` | `[Plan]` | `[Name]` |

## 15.2 Biggest Unknown Right Now
What is the single biggest uncertainty in your project at this stage?

**Response:**  
`[Write here]`

---

# 16. Testing and Playtesting

## 16.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|---|---|---|
| `[Bluetooth connection]` | `[Method]` | `[What counts as success?]` |
| `[Mechanism movement]` | `[Method]` | `[What counts as success?]` |
| `[Sensor behavior]` | `[Method]` | `[What counts as success?]` |
| `[App communication]` | `[Method]` | `[What counts as success?]` |

## 16.2 Playtesting Plan

| Question | How You Will Check |
|---|---|
| Do players understand what to do? | `[Method]` |
| Is the interaction satisfying? | `[Method]` |
| Do players want another turn? | `[Method]` |
| Is the challenge balanced? | `[Method]` |
| Is the response clear and immediate? | `[Method]` |

## 16.3 Testing and Debugging Log

| Date | Problem Found | Type | What You Tried | Result | Next Action |
|---|---|---|---|---|---|
| `[Date]` | `[Describe issue]` | `[Technical / Mechanical / UI / Gameplay]` | `[What you did]` | `[Worked / Partly / Failed]` | `[Next step]` |
| `[Date]` | `[Describe issue]` | `[Type]` | `[What you did]` | `[Result]` | `[Next step]` |

## 16.4 Playtesting Notes

| Tester | What They Did | What Confused Them | What They Enjoyed | What You Will Change |
|---|---|---|---|---|
| `[Peer / friend / classmate]` | `[Observation]` | `[Observation]` | `[Observation]` | `[Action]` |
| `[Peer / friend / classmate]` | `[Observation]` | `[Observation]` | `[Observation]` | `[Action]` |

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
`[Write here]`

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

| Version | Date | What Changed | Why |
|---|---|---|---|
| `v1` | `[Date]` | `[Describe]` | `[Reason]` |
| `v2` | `[Date]` | `[Describe]` | `[Reason]` |
| `v3` | `[Date]` | `[Describe]` | `[Reason]` |

---

# 18. Final Outcome

## 18.1 Final Description
Describe the final version of your project.

**Response:**  
`[Write here]`

## 18.2 What Works Well
- `[Point 1]`
- `[Point 2]`
- `[Point 3]`

## 18.3 What Still Needs Improvement
- `[Point 1]`
- `[Point 2]`
- `[Point 3]`

## 18.4 What Changed From the Original Plan
How did the project change from the initial idea?

**Response:**  
`[Write here]`

---

# 19. Reflection

## 19.1 Team Reflection
What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
`[Write here]`

## 19.2 Technical Reflection
What did you learn about:
- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
`[Write here]`

## 19.3 Design Reflection
What did you learn about:
- designing for play,
- delight,
- clarity,
- physical interaction,
- player understanding,
- iteration?

**Response:**  
`[Write here]`

## 19.4 If You Had One More Week
What would you improve next?

**Response:**  
`[Write here]`

---

# 20. Final Submission Checklist

Before submission, confirm that:
- [ ] Team details are complete
- [ ] Project description is complete
- [ ] Inspiration sources are included
- [ ] Player journey is written
- [ ] Sketches are added
- [ ] BOM is complete
- [ ] Purchase list is complete
- [ ] Budget summary is complete
- [ ] Mechanical planning is documented if applicable
- [ ] App planning is documented if applicable
- [ ] Code flowchart is added
- [ ] Task breakdown is complete
- [ ] Weekly logs are updated
- [ ] Risk register is complete
- [ ] Testing log is updated
- [ ] Playtesting notes are included
- [ ] Build photos are included
- [ ] Final reflection is written

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
