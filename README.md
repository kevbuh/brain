# brain

reverse engineering the human brain and recreating the neocortex, hippocampus, basal ganglia, amygdala, and thalamus into computer version.

Inspired the theory in ["A Brief History of Intelligence"](https://www.amazon.com/Brief-History-Intelligence-Humans-Breakthroughs/dp/0063286343) by Max Bennet and [geohot's](https://geohot.github.io/blog/jekyll/update/2024/03/27/where-the-bitter-lesson-ends.html) brief analysis.

in order to avoid complexity, entire repo must be under 10,000 lines of codes.

## Brain regions

### Neocortex
- simulation (frontal)
- model-based
- COMP: transformer
- allows for few-shot learning
- general purpose
### aPFC
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
### gPFC
- granular prefrontal cortex
- found in primates
- used to model intent from ones own inner simulation
  - explains intent by simulating what another person's inner simulation is like
- allows for theory of mind
### Hippocampus
- consolidation of information from short-term memory to long-term memory, and in spatial memory that enables navigation
- largest job is to hold short-term memories and transfer them to long-term storage in our brains
- COMP: really good RAG  
### Basal Ganglia
- TD-learning
- automatic
- model-free
### Amygdala
- has a primary role in the processing of memory, decision-making, and emotional responses (including fear, anxiety, and aggression)
- prevents the agent from destroying itself
- plays a key role in emotional responses and the formation of emotional memories
- activation of the fight-or-flight
### Thalamus
- coordinate the system and search
- acts as a relay station for sensory and motor signals, as well as regulating consciousness and alertness
- All information from your body's senses (except smell) must be processed through your thalamus before being sent to your brain's cerebral cortex for interpretation
- encoder and propogates information? attention mechanism to know where to send/focus information?

## Goal Hierarchy

aPFC (high-level goals)

$\downarrow$

premotor cortex (subgoals)

$\downarrow$

motor cortex (sub-subgoals)

$\downarrow$

Basal Ganglia

# Roadmap

- Evidence suggests that the humans brain is literally a scaled up primate brain: a bigger neocrtex, a bigger basal ganglia, but still containing all the same areas wired in all the same ways. 

Evolution to human brain:
1. Cynobacteria
2. Ancient Fish
3. Amphibian
4. Ancient mammal
5. Primate
6. Human

So we can first start by creating a working version of a Cynobacteria brain, and then slowly progress to a humanlike brain.