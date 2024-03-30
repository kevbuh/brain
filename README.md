# brain

reverse engineering the human brain and recreating the neocortex, hippocampus, basal ganglia, amygdala, and thalamus into computer version.

Based off of the theory in ["A Brief History of Intelligence"](https://www.amazon.com/Brief-History-Intelligence-Humans-Breakthroughs/dp/0063286343) by Max Bennet and [geohot's](https://geohot.github.io/blog/jekyll/update/2024/03/27/where-the-bitter-lesson-ends.html) brief analysis.

## Brain Areas

Neocortex
- transformer
- simulation (frontal)
- model based
- allows for few shot learning
Hippocampus
- really good RAG
  
Basal Ganglia
- TD-learning
- automatic
- model-free
  
Amygdala

Thalamus

# aPFC

- Agranular Prefrontal Cortex
- creates a simulation of an animals own movements and internal states (self model)
- constructs intnet to explain one's own behavior
- the aPFC and sensory neocortex worked together to enable early ammals to pause and simulate aspects of the world that were not currently being experienced. aka model-based reinforcement learning. 
- somehow solves the search problem by intelligently selecting paths to simulate and determining when to simulate them.
- Enabled vicarious trial and error
- Enabled counterfactual learning
  - offers a more advanced solution to the credit assignment problem
- These simulations enabled early mammals to engage in episodic memory 
- Allows for the "imaginarium"

## Motor Hierarchy

aPFC (high-level goals)

$\downarrow$

premotor cortex (subgoals)

$\downarrow$

motor cortex (sub-subgoals)

$\downarrow$

Basal Ganglia