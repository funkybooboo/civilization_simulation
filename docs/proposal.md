## Thoughts

Ours thoughts:
Banished
THE GAME
The game is a resource management simulation where players build and manage a growing town, facing various challenges and opportunities. Players control citizens with different roles (e.g., farmers, builders, doctors) and manage resources like food, firewood, tools, and medicine. Each year, players must ensure the well-being of their population by providing enough food and resources, while also considering citizens' health and happiness.
Random events such as droughts, plagues, bounties, and festivals can impact resources and citizen morale, adding an element of unpredictability. Players can construct various buildings (e.g., farms, hospitals, schools) to enhance productivity and improve citizens' quality of life. The game features a Monte Carlo simulation to analyze long-term survival rates and employs an epsilon-greedy algorithm for decision-making, allowing players to strategize based on potential outcomes. Overall, the game challenges players to balance resource management, citizen welfare, and adaptability to changing conditions, making it an engaging and thought-provoking experience.
THE SIMULATION
The simulation is a dynamic resource management model that replicates the complexities of building and sustaining a town. It incorporates several key components:
Key Components of the Simulation
Citizen Management:
Citizens are represented as objects with attributes like health, happiness, and roles (e.g., farmer, builder). Each citizen's skills and well-being directly affect the town's productivity and growth.
Resource Management:
The town has various resources, including food, firewood, tools, and medicine. Players must balance these resources to meet the needs of the population. For instance, food is consumed each year based on the population size.
Building Infrastructure:
Players can construct different types of buildings (e.g., farms, hospitals, schools) that enhance resource production or improve citizens' health and happiness. Each building has specific capacities and functions.
Yearly Simulation Cycle:
Each simulation year involves several steps:
Calculate resource consumption based on the population.
Handle random events that can impact resources and citizens.
Manage citizens' health and happiness based on available resources.
Record historical data for analysis.
Random Events:
The simulation introduces random events (e.g., droughts, plagues, bounties, festivals) that create variability in gameplay. These events can significantly affect resources and citizen morale.
Decision-Making:
The simulation employs an epsilon-greedy decision-making algorithm to determine actions like building construction. This allows for strategic planning based on potential benefits.
Monte Carlo Simulation:
The simulation can run multiple trials to analyze outcomes, providing insights into average survival years and variability in results. This helps in understanding long-term strategies.
Data Visualization:
The simulation tracks historical data over time, visualizing trends in resources, population, and happiness. This allows players to see the effects of their decisions and events on the town's sustainability.
Overall Purpose
The simulation serves as a testing ground for exploring different strategies in town management, emphasizing the balance between resource allocation, citizen welfare, and adaptability to unforeseen challenges. It provides a rich, interactive experience where players can experiment with decisions and witness the consequences, enhancing understanding of complex systems in resource management.
Check out a dummy implementation to get more of an idea about what I am thinking. We could make this super cool: https://github.com/funkybooboo/banished_simulation

### fine graded thoughts

Algorithms

Optimal stop for when the algo thinks this is the max happiness it can achieve
Monte Carlo simulation
Epsilon-Greedy (should I build more or put more farms down?) (should I keep planting this crop?)

### Bare bones of our project

Structures:
Houses (wood)
Churches (stone)
Cemeteries (stone)
Mine (on flat land) (to get stone)

Resources:
Lumber (resource)
Stone (resource)
Herbs (increase health) (in old forest)
A few kinds of crops
Cows (for clothes)

Landscape:
New forest
Old forest

Accessories:
Tools (wood, stone)
Clothes (make winter happier)

Actions:
Clear land (action)
Travel distance (drain on happiness)

Kinds of people:
Forester
Hunter?
Gatherer?
Farmer?

## started writing

Final Project Proposal
Echoes of Eden

Task description/Abstract:
Banished is a civilization simulator game in which the player constructs a city from scratch. The player assigns workers to various tasks, such as constructing homes, planting crops, and gathering resources. The goal of the game is to maximize the health and happiness of the game’s citizens. We propose to create a simulator

Methodology:

Outcomes and Deliverables:
The end goal is to optimize the levels of happiness and health globally across the village. Several different factors play into 
