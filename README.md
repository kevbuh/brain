# brain

Reverse engineering the human brain. Recreating the neocortex, hippocampus, basal ganglia, amygdala, and thalamus into their respective digital version.

Inspired the theory in ["A Brief History of Intelligence"](https://www.amazon.com/Brief-History-Intelligence-Humans-Breakthroughs/dp/0063286343) by Max Bennet, [geohot's](https://geohot.github.io/blog/jekyll/update/2024/03/27/where-the-bitter-lesson-ends.html) brief analysis, and ["How to Build a Brain"](https://www.amazon.com/How-Build-Brain-Architecture-Architectures/dp/0190262125).

In order to avoid complexity, entire repo must be under 10,000 lines of codes.

# Roadmap

Evidence suggests that the humans brain is simply a scaled up primate brain: a bigger neocrtex, a bigger basal ganglia, but still containing all the same areas wired in all the same ways. 

Evolution to human brain:
1. Cynobacteria
2. Ancient Fish
3. Amphibian
4. Ancient mammal
5. Primate
6. Human

So we can first start by creating a working version of a Cynobacteria brain, and then slowly progress to a humanlike brain.

# Documentation

### Brain regions overview:

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
- A highly interconnected cluster of brian areas found underneath the neocortex and near the thalamus
- Centrally implicated in the ability to choose between alternative courses of action
- Used for "action selection" in both motor and cognitive actions 
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

## Biological Neurons

Biological Neuron Communication
1. Signals flow down the dendrites of a neuron into its cell body
2. If the overall input to the cell body from the dendrites crosses that neuron's threshold, the neuron generates an action potential "spike" that travels down the axon
3. When the spike gets to the end of the axon, it causes chemicals to be released that open channels, producing a postsynaptic current in the receiving dendrite
4. This current then flows to the cell body of the next neuron, and the process repeats

An average cortical cell has 10,000 inputs and outputs connections.

The number of inputs to a cell can range from about 500 (retina) to 200,000 (purkinje cells in the cerebellum).

## NOCH

Neural optimal control hierarchy

PM and SMA
- Generate high-level control signal in low dimensional space

Basal Ganglia
- Define novel control signal using available synergies, scale movements, and train hierachy

Cerebellum
- Maintain internal models, control balance and rythmic movements, perform online error correction

M1
- Transform high level command to low-level, obtain control signal, and issue command to be implemented

Brainstem and spinal cord
- Amalgamate recieved control signals and implement; filter out and relay task releveant system feedback

S1/S2
- Provide relevant low-level and high-level feedback

## Fluid/Crystalized Intelligence

Fluid
- Sophisticated cognitive behavior that depends on currently available information
- Used for solving difficult planning problems

Crystalized
- Exemplified by recalling important facts about the world to solve a given problem

## Acronyms

- V1: Primary visual cortex
- V2: Secondary visual cortex
- V4: Extrastriate visual cortex
- IT: Inferotemporal cortex
- AIT: Anterior IT
- OFC: Orbitofrontal cortex
- vlPFC: Ventrolateral prefrontal cortex
- dlPFC: Dorsolateral prefrontal cortex
- PM: Premotor cortex
- SMA: Supplementary motor areas
- M1: Primary motor cortex
- PPC: Posterior parietal cortex
- PSC: Postsynaptic current
- PSP: Postsynaptic potential
- NPH: Nuclei prepositus hypoglossi
- LIF: Leaky integrate and fire neuron
- VOR: Vestibulo-ocular reflex
- S1: Primary somatosensory area
- S2: Secondary somatosensory area
- NEF: Neural Engineering Framework
- VSA: Vector symbolic architecture
- CM: Centromedian nucleus of the thalamus
- Pf: Parafascicular nucleus
- VA: Ventral lateral nucleus
- MD: Medio-dorsal nucleus
- SNc: Substantia niagra pars compacta
- GPe: External globus pallidus
- GPi: Internal globus pallidus
- SNr: Substantia niagra pars reticulata
- STN: Subthalamic nucleus