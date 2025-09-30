---
title: Prototyping for Evaluation
author: Dr Charles Martin
---

<!-- ![tutorial image goes here, a nice indicative image in wide format, e.g. 1200x650](img/image-name.jpg) -->
![Prototyping Illustration](https://media.licdn.com/dms/image/v2/D5622AQGIRq6YCYOECg/feedshare-shrink_800/feedshare-shrink_800/0/1691768560737?e=2147483647&v=beta&t=fNvrgpqVuEacFbzrVw_lEeZCmDBPfERqRnxzwVCDVik)

This tutorial will guide you in building prototypes that move beyond expressing a design concept and are prepared for evaluation, particularly in relation to the concept of testable interfaces. The work is directly connected to the final project.

<!-- link this to previous one. -->
<!-- half making, half testing on each other. -->

<!-- <https://hci.stanford.edu/courses/cs247/2012/readings/WhatDoPrototypesPrototype.pdf>-->

## Pre-Class Tasks
1. Choose a user interface described in a [UIST](https://dl.acm.org/conference/uist) or [CHI](https://dl.acm.org/conference/chi) paper
2. Post a forum post (100–200 words) answering:  
   - **What is the system and what does it do?**     
   - **Which parts of the interface are interactive?** How does the user engage with the system?  
   - **What steps/tasks did participants do in the user study?**  
   - **If you made a prototype, what would you need to include to test it?**  
   - Include **one image or sketch** to illustrate the interface (figure from paper, screenshot, or your annotated sketch highlighting key interactive components).

## Plan for the Class

1. Task 1: Understand the Concept of Testable Interactions (10m)
2. Task 2: Build a Testable Prototype (50 min)  
3. Task 3: Prototype Showcase & Peer Feedback (30 min)  

## In-Class Tasks

### Task 1: Understand the Concept of Testable Interactions (10 minutes)

**What makes a prototype testable?**  
A prototype is testable if it lets you **observe and learn from real user interactions**. Ask yourself:

1. **Interactive:** Can users actually perform the steps or tasks you’re trying to test? (even if simulated)
   - Users must be able to take action and see a response, even if it’s simulated.
   - Examples: pressing a paper button triggers a screen change, dragging a card moves it to a new location, or speaking a command triggers a response.
   - Ask: “Can someone unfamiliar with this prototype actually perform the task I want to test?”
   - Tip: A static sketch is not enough — the user must act on the prototype. 
2. **Clear:** Can users understand what the system is, what to do, and how it works?
   - Make the system’s state and feedback obvious.
   Examples: highlighting selections, showing confirmation messages, or providing visual cues for next steps.
   Ask: “Will a new user generally know what to do next without explanation?” 
3. **Evaluative:** Can you observe users, gather feedback, or identify what works and what doesn’t
   - Decide what success looks like and what errors or hesitation mean.
   - Examples: did the user complete the action correctly? Did they get confused or hesitate?
   - Ask: “What can I measure or observe that tells me if this interaction is effective?”  
4. **Focused:** Are you including only what’s needed to test the intended interaction or task?
   - Include the elements needed to test the key task; less focus on aesthetics or extra features.
   - Ask: “Does every part of this prototype help answer my testing question, or can something be removed?”

**Activity:**  
1. In your group, look at the pre-class forum posts.  
2. Choose **the most interesting system or interface** posted by a group member.  
3. Discuss:  
   1. Which part of the system could you prototype?  
   2. What is the key interaction?  
   3. What feedback would make it **clear** to users?  
   4. How could you **observe success**?  

### Task 2: Build a Testable Prototype (50 mins)

In groups, your tutor will give you a **random user problem**. Focus on **one key interaction**.

| #  | Scenario | Task (Key Interaction to Prototype) |
|----|---------|-------------------------------------|
| 1  | **Cat Cafeteria**: Patrons interact with digital feeders to dispense snacks to cats. | Prototype **one interaction** for choosing a cat and triggering a response from the feeder. |
| 2  | **Alien Plant Gardener**: Manage a garden of alien plants. | Prototype **one interaction** for taking an action that affects the plant’s state. |
| 3  | **Ghostly Museum Guide**: Friendly ghosts guide visitors via AR projections. | Prototype **one interaction** for a visitor to communicate or elicit a response from the ghost. |
| 4  | **Intergalactic Grocery Store**: Shopping in zero gravity with floating items. | Prototype **one interaction** for selecting or moving a floating item. |
| 5  | **Robo-Barista**: Robot makes drinks based on user input. | Prototype **one interaction** for specifying or changing a drink order. |
| 6  | **Secret Spy Office**: Hide/reveal documents using a smart desk. | Prototype **one interaction** for revealing or moving a confidential file. |
| 7  | **Pet Translator**: Device translates pet sounds into messages. | Prototype **one interaction** for capturing a pet signal and generating a readable output. |
| 10 | **Mini-Magic Keyboard**: Typing triggers tiny illusions. | Prototype **one interaction** for creating an effect based on user input. |

1. In your group,**Identify the key interaction** you want to focus on testing.  
2. **Sketch and build a testable prototype** based on that key interaction.
3. Then get building!

#### Mapping Table

| Scenario | Key Interaction | Interactive (User Action) | Clear (Feedback) | Evaluative (Observable Success) | Focused (Essential Elements) |
|----------|----------------|---------------------------|-----------------|--------------------------------|-----------------------------|
| …        | …              | …                         | …               | …                              | …                           |


**Guidelines:**  
- Focus only on the **essential elements needed to test the interaction** — do not worry about polish or aesthetics.  
- Materials can include **paper, printed screens, simple click-through slides, or other low-fidelity tools**.  
- Use a **Wizard of Oz** approach if you need to simulate system responses.  


### Task 3: Prototype Showcase & Peer Feedback (30 mins)

Groups will **present and demonstrate their testable prototypes** to the class, allowing peers to interact and provide feedback. The focus is on **observing real user interactions**, not just explaining how the prototype works.  

**Steps:**  

1. **Group Demo (1–2 min per group)**  
   - Introduce the **scenario and user problem**.  
   - Highlight the **key interaction**.  

2. **Peer Interaction (2–3 min per group)**  
   - Each **other group** tries the interaction.  
   - Observers record **one positive observation** and **one question or point of confusion** about the interaction.  
   - Use a **feedback sheet** or notebook to capture responses.

3. **Group Reflection (1–2 min per group)**  
   - Each presenting group reads aloud **the one positive and one question** received from peers.  
   - Discuss briefly how they might **improve the prototype** based on this feedback.



## Resources (optional)

You can include a section with links to external resources that may be necessary but these can also be placed in-line with the tasks.

## References

(reference list is added automatically but we need the heading to stay there)
