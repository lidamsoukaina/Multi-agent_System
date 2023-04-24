# **Argumentation-based negotiation interaction**


## ❓ Context
Imagine that a car manufacturer wants to launch a new car on the market. A crucial choice is the engine, which must meet certain technical requirements but at the same time be attractive to customers (economical, robust, ecological, etc.). Several types of engines exist and thus allow a wide range of car models to be offered: internal combustion engine (ICE) with gasoline or diesel, compressed natural gas (CNG), electric battery (EB), fuel cell (FC), to name but a few. 

The company decides to take into account different criteria to evaluate them: Consumption, environmental impact (CO2, clean fuel, NOX,...), cost, durability, weight, target maximum speed, etc. To establish the best offer/choice among a considerable set of options, it decides to simulate a negotiation process where agents, with different opinions and preferences (and even different knowledge and skills), discuss the issue to arrive to the best offer.  The simulation will offer the company the possibility to simulate different behaviors, different typologies of agents (expertise, role, preferences, ...) at a lower cost in a reasonable time.

## 🎯 Objective
The objective is to schedule this negotiation protocol.  The agents will have to negotiate with each other in order to make a joint decision about which engine is best. Negotiation occurs when agents have different preferences on criteria and argumentation will be used to help them decide which item to choose. In addition, the arguments supporting the best choice will help to build the justification of this choice, an important element for the company to build its marketing campaign.

## :memo: Modeling specifications
For our problem, we generated N agents randomly. A class named **Preferences** models the list of preferred criteria with their scores. To simplify our model, we assume that all the agents consider the same set of criteria. The difference lies in the **order** in which these criteria are initialized in the Preference object. During the test phase, we randomly shuffle the list of criteria while creating the agents. Regarding the **generate_preferences** function, it takes the list of considered criteria as input and assigns a random score between 0 and 4 to each criterion (0 for very bad and 4 for very good).

During the negotiation, agents propose their **most preferred** item to each other. The receiver's response could be a direct acceptance if the proposed item is among the **top 10%** of items on the receiver's list. In this case, the agents commit to the proposed item and stop sending or receiving proposals. 

Otherwise, the **argumentation process** begins. To model an argument, we use an object with four predicates. The first attribute (decision) specifies whether the argument is for or against the second attribute, which represents an item. The third and fourth attributes encapsulate the essence of the argument in a form of lists of CoupleValue or Comparison.

So when the receiver asks for **supporting** arguments for the sender's proposal. The sender checks first if the item has a **high score** (3 or 4) for any criterion (starting from the most preferred one). If it does, an argument message is sent with the item, criterion name and its value. The receiver in his turn checks if it also has a good score for that criterion. If true, the receiver accepts, and the negotiation process ends between the pair. 

If not true or if the item itself showcase a **low score** (0 or 1) for an important criterion of the receiver, the receiver sends a **counter-argument** which justify their decision. The process continues until a commit is achieved or the number maximum of steps is achieved.

**Remark**: The different classes are tested during the development phase.

## :pencil2: Authors
- LETAIEF Maramq
- LIDAM Soukaina
