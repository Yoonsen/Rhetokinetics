# Rhetokinetics: A Quantitative Model of Meaning, Power, and Cultural Drift

## Abstract

We propose a novel framework called *rhetokinetics*, which formalizes how utterances exert force and acquire meaning over time. By representing both speaker authority and interpretive response in the complex plane, we model not only what is said, but how it becomes socially consequential. Our approach extends Boole's logical calculus into a rhetorical domain using complex numbers to encode truth, value, and illocutionary efficacy. This enables the simulation of cultural drift, propaganda dynamics, and historical reinterpretation.

## Core Definitions

### Interpretive Value ($o$-calculus)

Each proposition $A$ receives a complex value: $$ o(A) \= p(A) \+ i \\cdot v(A) $$

- $p(A)$: perceived truth (logos)  
- $v(A)$: emotional or normative weight (pathos)

Modulus: $$ |o(A)| \= \\sqrt{p^2 \+ v^2} $$ Argument: $$ \\theta \= \\arctan\\left(\\frac{v}{p}\\right) $$

### Illocutionary Force ($F$-vector)

The utterance is delivered with a force vector: $$ F(A) \= \\alpha \+ i \\cdot \\phi $$

- $\\alpha$: speaker authority (ethos)  
- $\\phi$: illocutionary efficacy, i.e., the speaker's ability to make the utterance true

We model humans as truth-makers: an utterance becomes true not only based on external conditions, but through the listener's relation to the speaker. These relations can range from institutional authority to interpersonal trust, kinship, or alignment within a shared cultural context. A listener can accept, resist, or reinterpret an utterance's truth depending on their perceived proximity or alignment with the speaker.

## Rhetokinetic Impact

We define the combined rhetorical impact of an utterance as: $$ R(A) \= |F(A)| \\cdot |o(A)| $$ This measure allows us to compare, rank, and simulate how utterances influence social space over time.

## Cultural Drift and Feedback

We simulate entrenchment through a feedback loop:

- Initial utterance: $o\_0 \= p\_0 \+ iv$  
- Compute impact: $|o\_0|$  
- Update $p$: $$ p\_{t+1} \= p\_t \+ \\epsilon (|o\_t| \- p\_t) $$ where $\\epsilon$ is a small learning rate (e.g., 0.05)

This models how emotionally charged but initially false claims (e.g., propaganda) can become perceived as true through repeated exposure and rhetorical force.

## Applications

- Modeling historical reinterpretation (e.g., Lindgren, Céline, Hamsun)  
- Simulating sociological alignment and disalignment  
- Quantifying the effect of institutional speech acts  
- Visualizing propaganda and belief shifts

## Example: Missionary Rhetoric

The 19th-century statement:

"Thanks to him, missionaries can now preach the evangelium to poor unknowing negroes."

- High $F(A)$ (institutional authority and efficacy)  
- Original $o(A)$: high $p$, mild $v$  
- Modern $o(A)$: lower $p$, strong negative $v$  
- Simulated as a rotation in the complex plane

## Future Work

- Introduce population-scale alignment models  
- Encode contradiction and contestation  
- Extend to multi-agent rhetorical games  
- Compare rhetokinetic simulations with historical data

## Conclusion

Rhetokinetics offers a powerful formalism to explore how language acts in culture. It bridges logic, rhetoric, and social theory, creating a space where meaning is not just measured, but moved.

### Rhetorical Triad in Rhetokinetics: Functional Roles of Utterances

In our rhetokinetic model, the classical rhetorical triad—ethos, logos, and pathos—is reinterpreted not as stylistic domains, but as distinct functional components of how utterances operate in cultural space.

Each component reflects a different aspect of how an utterance is received, enacted, or responded to:

- **Logos** governs the **descriptive content** of the utterance. It reflects coherence, propositional form, and epistemic plausibility. Logos answers the question: *What is being said, and how does it fit into our knowledge system?*  
    
- **Ethos** captures the **capacity to make the statement true**. It is not limited to the trustworthiness of the speaker, but more broadly indicates whether the speaker has the authority, position, or social force to enact the truth of the utterance. Ethos thus answers: *Who says it, and can they make it true?*  
    
- **Pathos** encodes the **affective and normative weight** of the utterance. It governs the degree to which a statement evokes response, value, urgency, or resonance. Pathos answers: *Why does this matter? What should we feel or do in response?*

This mapping allows us to analyze performatives (e.g., "You are now married") in a structured way:

- A **priest** saying it during a ceremony: high **ethos**, moderate **logos**, high **pathos**.  
- A **friend** saying it as a joke: low **ethos**, low **logos**, mid **pathos** (social nudge).  
- A **historian** reporting it retrospectively: no illocutionary force—only **logos** remains.

### Rhetokinetic Message Arc

This also yields a directional arc:

**Speaker (ethos)** → **Statement (logos)** → **Receiver/Culture (pathos)**

Although we assign numeric values and abstract away from specific agents, both speaker and listener are implicitly modeled:

- The **speaker** is indexed through ethos: the power to make true.  
- The **listener** is reflected in pathos: the cultural or personal response value.

In this way, our rhetokinetic calculus provides a structured model of rhetorical movement—one in which truth is not a static property, but something enacted, valued, and propagated through cultural systems.

