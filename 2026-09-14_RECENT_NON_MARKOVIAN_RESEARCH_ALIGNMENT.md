# Recent Non-Markovian Research Alignment — 14 September 2026

**Status:** Research alignment note; not evidence for a new physical law  
**Scope:** 2024–2026 external literature relevant to the September 2026 non-Markovian information-path formulation

> **Interpretation boundary:** The papers below strengthen the *scientific setting* in which the framework is posed: multitime memory, history-sensitive open-system dynamics, information backflow, system–environment correlations, process tensors, causal interventions, thermodynamic consequences, and geometric witnesses are active and experimentally accessible research areas. They do **not** independently establish the additional history-weighted term proposed in the framework.

---

## 1. Why the recent literature matters

The strongest recent development is not a paper that “proves” the framework. It is the rapid maturation of **process-tensor and multitime methods** for describing, reconstructing, forecasting and exploiting non-Markovian dynamics.

This matters because the September 2026 formulation asks a deliberately narrower question than “does memory exist?”:

> After the best conventional multitime memory model has been fitted, does a **predeclared physical weighting variable** identify a reproducible, intervention-sensitive residual contribution to later dynamics?

The modern process-tensor literature makes that question more testable, but also raises the baseline the framework must beat.

---

## 2. Strongest recent alignments

### 2.1 Process tensors are becoming a practical general language for physical memory

**Keeling, Stoudenmire, Bañuls & Reichman — “Process Tensor Approaches to Non-Markovian Quantum Dynamics,” Physical Review X 16, 020502 (2026).**  
DOI: https://doi.org/10.1103/1ncg-11hz

The 2026 PRX Perspective argues that process-tensor methods, together with efficient tensor-network techniques, now make a broad class of observable non-Markovian problems computationally tractable. It emphasizes that Markov approximations fail when environments are structured, coupling is strong, low-frequency modes matter, or information propagates through the environment.

**Relevance:** This strongly supports the choice to formulate the physics-facing programme as a **multitime / history-sensitive** problem rather than as a mysterious new field. It does not support an extra kernel term by itself.

**Practical consequence:** Future versions of the framework should treat a reconstructed process tensor or equivalent influence-functional representation as a serious candidate for the conventional baseline `K0`, not merely a time-local master equation.

---

### 2.2 Non-Markovian memory can be a measurable thermodynamic resource

**Zambon & Adesso — “Quantum Processes as Thermodynamic Resources: The Role of Non-Markovianity,” Physical Review Letters 134, 200401 (2025).**  
DOI: https://doi.org/10.1103/PhysRevLett.134.200401

This work studies general multitime quantum processes with process tensors and identifies mechanisms through which non-Markovianity can increase extractable work: work investment, multitime correlations, and system–environment correlations. The advantage is related to a quantifier of process non-Markovianity.

**Relevance:** This is a useful external precedent for the narrower proposition that temporally retained correlations can have measurable physical consequences rather than being only descriptive bookkeeping.

**Boundary:** It is evidence for established non-Markovian thermodynamic effects, not for a distinct history-weighted law or `KV` term.

---

### 2.3 Long-range memory can be distributed across timescales

**Dowling, Modi, Muñoz, Singh & White — “Capturing Long-Range Memory Structures with Tree-Geometry Process Tensors,” Physical Review X 14, 041018 (2024).**  
DOI: https://doi.org/10.1103/PhysRevX.14.041018

The authors construct process-tree descriptions with polynomially decaying temporal correlations and memory distributed over multiple timescales, and show that they can approximate strong-memory spin-boson dynamics.

**Relevance:** This supports taking temporal structure seriously. A physically retained history need not reduce to a single exponential memory time.

**Practical consequence:** Any proposed weighting law should be tested against baselines with **multi-timescale and long-range memory**, not only simple one-timescale kernels.

---

### 2.4 Correlated quantum dynamics can be learned and forecast experimentally

**“Learning and forecasting open quantum dynamics with correlated noise,” Communications Physics (2025).**  
DOI: https://doi.org/10.1038/s42005-025-01944-2

The work reconstructs temporally correlated open-system dynamics on a superconducting quantum processor, tunes the system from near-Markovian to highly non-Markovian behaviour, and uses learned models to predict both observed and unobserved future dynamics. Larger memory models improve reconstruction in the strongly non-Markovian regime.

**Relevance:** This is important experimentally: multitime physical memory can be inferred from data and tested on held-out future behaviour.

**Practical consequence:** The framework’s strongest future criterion should remain **held-out predictive improvement**, not merely a better in-sample kernel fit.

---

### 2.5 Process-tensor tomography is already an experimental tool

**White et al. — “Non-Markovian Quantum Process Tomography,” PRX Quantum 3, 020344 (2022), plus subsequent process-tensor experimental work.**  
DOI: https://doi.org/10.1103/PRXQuantum.3.020344

Process-tensor tomography can characterize multitime correlations and has been demonstrated on superconducting quantum devices.

**Relevance:** The framework does not need to invent a new measurement language for multitime memory. It can build discriminating tests on top of established process-tensor tomography and causal interventions.

---

### 2.6 Causal breaks are directly useful for the intervention requirement

The process-tensor literature uses **causal breaks** — measurement/repreparation or reset operations that interrupt information flow through the system — to distinguish memory transmitted through the system from memory retained in the environment or system–environment correlations.

A useful reference is:

**“Non-Markovian memory strength bounds quantum process recoverability,” npj Quantum Information (2021).**  
DOI: https://doi.org/10.1038/s41534-021-00481-4

**Relevance:** This is closely aligned with the framework’s intervention/ablation level. A future physical test should not merely compare two histories with matched reduced states. It should ask which memory channel survives a causal break and whether the candidate weighting variable predicts that surviving component.

---

### 2.7 Local tests can distinguish quantum from classically modelled memory

**Bäcker, Beyer & Strunz — “Local Disclosure of Quantum Memory in Non-Markovian Dynamics,” Physical Review Letters 132, 060402 (2024).**  
DOI: https://doi.org/10.1103/PhysRevLett.132.060402

The paper proposes a local criterion for testing whether observed non-Markovian memory requires a genuinely quantum description or can be reproduced by classical memory.

**Relevance:** This is a valuable control lesson. Before assigning significance to a residual memory effect, classify whether ordinary classical latent memory already explains it.

---

### 2.8 Geometric observables can witness non-Markovian memory

**“Geometric signature of non-Markovian dynamics,” Annals of Physics 483, 170243 (2025).**  
DOI: https://doi.org/10.1016/j.aop.2025.170243

The paper studies geometric decoherence as a witness of non-Markovian dynamics and identifies time points associated with information backflow.

Earlier work also established memory-induced geometric phases in non-Markovian open systems.

**Relevance:** Geometry is promising as an **independent readout channel** in the evidence ladder.

**Boundary:** History-dependent geometric phase is already established. “Informational holonomy” should therefore not be presented as a new foundation unless a genuinely new invariant and discriminating prediction are derived. Geometry is better treated as a witness or metrological channel.

---

### 2.9 History dependence is not confined to quantum systems

**“History Dependence in Thermodynamic Properties of Solids,” International Journal of Thermophysics 47, 97 (2026).**  
DOI: https://doi.org/10.1007/s10765-026-03763-1

This work discusses history dependence in solids and the importance of finding sufficient state variables rather than automatically treating path dependence as evidence of exotic physics.

**Relevance:** It reinforces a crucial discipline of the framework: apparent history dependence may mean that the present state description is incomplete. A proposed retained-state effect only becomes interesting after hidden or omitted present-state variables have been aggressively controlled.

---

## 3. Assessment of the proposed mathematical “upgrades”

### 3.1 “Bake history into the projection operators” — useful idea, wrong novelty claim

Correlated projection superoperators have been used for strongly non-Markovian dynamics for roughly two decades, including work by Breuer and collaborators.

**Conclusion:** Do not claim that modifying `P` and `Q` to retain correlations is a new move. It may still be mathematically useful as a **baseline construction**, but not as the distinctive contribution.

The distinctive question must remain the predeclared **weight-conditioned residual** beyond the best conventional correlated projection / process-tensor model.

---

### 3.2 “Derive the weights from first principles” — high-value direction, but do not fake it

The present candidate weight vector contains physically meaningful quantities such as dissipated work, entropy production, generated system–environment correlation and correlation time. The weakness is not that these variables are unphysical; it is that an arbitrary linear combination can become flexible enough to fit almost anything.

**Best next move:** do not immediately invent a variational “law.” Instead compare three progressively stricter models:

1. **separate preregistered descriptors** — no composite weight;
2. **externally constrained composite** — coefficients fixed from an independent calibration set;
3. **theoretically constrained composite** — only if a derivation supplies coefficient relations before confirmatory data.

This makes model flexibility itself measurable.

---

### 3.3 “Historical speed limit” — do not launch this as a new law

Quantum speed limits and perturbation bounds for open systems already exist, including modern bounds on how quickly perturbed open-system trajectories may diverge.

A better move is to seek a **bound on the additional history-conditioned divergence** that can be generated by an available memory resource, for example temporal mutual information, process-tensor non-Markovianity or a related independently measurable quantity.

If the candidate term predicts more divergence than the measured resource can physically support, the candidate should fail.

This would strengthen falsifiability without prematurely declaring another law.

---

### 3.4 Fluctuation-theorem route — useful as a baseline residual test

Non-Markovian fluctuation theorems already exist; Crooks/Jarzynski-style relations can survive or acquire memory-related corrections depending on the setting.

**Conclusion:** Do not present a history-sensitive fluctuation theorem as automatically novel.

A potentially useful discriminating test is narrower:

> Fit the best conventional non-Markovian forward/reverse path-probability relation first. Then ask whether a preregistered physical weighting variable predicts a held-out residual in the path-probability ratio, and whether that residual disappears under the specified history intervention.

That is a legitimate future route, but it is not the cheapest first experiment.

---

### 3.5 “Informational holonomy” — interesting metaphor, weak priority

Geometric phase and geometric signatures of non-Markovianity are already established research topics.

**Conclusion:** Treat geometry as a possible **Level-4 convergent measurement**, not as the conceptual foundation of the law. A new holonomy claim would require a mathematically defined invariant with a prediction that standard geometric open-system theory cannot reproduce.

---

## 4. Strongest mathematical move now: nested multitime model comparison

The cleanest next mathematical step is not to add more speculative structure. It is to formalize the proposal as a nested comparison:

```text
M0: best conventional multitime model
    (process tensor / influence functional / correlated projection baseline)

M1: M0 + preregistered weight-conditioned candidate contribution
```

Then require M1 to satisfy all of the following:

1. improve **held-out** predictive likelihood or a preregistered proper score;
2. preserve the predicted sign / ordering as the declared weight changes;
3. survive instrument and drift controls;
4. disappear or change as predicted under history scramble / erasure / causal break;
5. beat flexible conventional baselines with comparable model capacity;
6. replicate on a second independently generated dataset.

This reframes the problem from “can I write another memory kernel?” to the harder and more meaningful question:

> Does the declared weight explain out-of-sample multitime structure that the best ordinary memory model does not?

---

## 5. Strongest practical experiment now: simulation before expensive hardware

A simulation programme is high-value because it can test whether the proposed inference strategy can distinguish an added candidate contribution from ordinary non-Markovianity **before** any laboratory claim is made.

### Suggested toy-model ladder

1. **Baseline A — Markovian:** simple qubit amplitude damping / dephasing.
2. **Baseline B — ordinary non-Markovian:** Jaynes–Cummings or spin-boson model with structured bath.
3. **Baseline C — long-range memory:** process-tensor / influence-functional model with multiple memory timescales.
4. **Candidate-injected model:** same conventional dynamics plus a deliberately controlled synthetic weight-conditioned perturbation.

Use established simulation tooling such as **OQuPy** where appropriate.

### Required test

Blind the inference pipeline to which datasets contain the injected candidate term.

Ask whether it:

- returns null on A–C at the declared false-positive rate;
- detects the injected term on D;
- estimates sign and scaling on held-out histories;
- loses the effect under the declared ablation;
- remains calibrated when conventional memory strength is increased.

If the method cannot separate synthetic `KV` from ordinary strong non-Markovianity, there is no reason to proceed to expensive physical instrumentation.

---

## 6. Stronger experimental design for Protocol A

The existing “matched present state, varied history” idea is necessary but not sufficient.

Two runs can have the same reduced system state while carrying different **system–environment correlations**, and ordinary non-Markovian physics can then make their futures diverge.

That divergence would be real physics but would not establish the proposed extra term.

Protocol A should therefore be strengthened to include:

1. matched reduced system state at the comparison time;
2. reconstructed / bounded conventional multitime process;
3. explicit system–environment correlation controls where experimentally accessible;
4. causal-break or history-scramble intervention;
5. sham history with matched conventional energetic/thermal statistics;
6. held-out prediction of the direction and size band of the future divergence;
7. model-capacity-matched comparison against conventional non-Markovian alternatives.

This is the single most important methodological tightening suggested by the recent literature.

---

## 7. A useful cross-domain precedent — but not physical evidence

**Sevetlidis & Pavlidis — “Process-Tensor Tomography of SGD: Measuring Non-Markovian Memory via Back-Flow of Distinguishability,” AISTATS 2026.**  
https://proceedings.mlr.press/v300/sevetlidis26a.html

This work treats neural-network training as a classical multitime process, measures observable memory using distinguishability backflow, and reports collapse of the effect when optimizer state is reset by a causal break.

**Why it is interesting:** It is a clean modern example of the abstract pattern:

```text
same observable-level present
+ different retained internal history
→ different later behaviour
→ reset retained state
→ history effect collapses
```

**Boundary:** This is evidence about stateful optimization, not quantum physics and not evidence for the physical extension. It is nevertheless a useful independent precedent for intervention-sensitive retained-state analysis.

---

## 8. What the literature strengthens — and what it does not

### Strengthened

The external literature strongly supports these background statements:

- multitime history can matter physically;
- reduced present state need not be sufficient to predict future open-system dynamics;
- system–environment correlations can carry information across time;
- environmental information backflow can be operationally observed;
- non-Markovianity can have thermodynamic consequences;
- memory can be reconstructed, quantified and forecast from experiment;
- causal interventions can localize or destroy memory channels;
- geometric and thermodynamic observables can provide independent memory-sensitive readouts;
- long-range temporal memory may require richer baselines than a single decay constant.

### Not strengthened

The literature does **not** currently establish:

- a distinct universal `KV` term;
- the proposed physical weighting vector as a law of nature;
- a universal relationship between dissipated work / entropy production and future selection bias;
- an informational holonomy unique to this framework;
- a new historical speed limit;
- a universal physical carrier shared across software, cognition, biology and quantum systems.

Those remain hypotheses or possible mathematical directions.

---

## 9. Recommended research priority

### Highest-value move

Build a **simulation falsification harness** around a process-tensor / influence-functional baseline before adding more public theoretical machinery.

The harness should answer one question:

> Can a preregistered weight-conditioned model reliably distinguish an injected history-weighted contribution from ordinary non-Markovian memory, including strong and long-range memory, without producing false positives?

If yes, the result strengthens the experimental programme and gives a concrete target for a laboratory collaborator.

If no, revise the identification strategy before spending money or widening the claim.

---

## 10. Public wording recommendation

A safe summary for public use is:

> Recent work in open quantum systems increasingly treats memory as a multitime, experimentally reconstructable resource. Process tensors, causal interventions, information-backflow measures and thermodynamic analyses now provide stronger baselines for asking history-sensitive questions. This strengthens the experimental setting of the framework, but it also raises the burden of proof: any proposed history-weighted contribution must outperform those conventional models on preregistered held-out predictions and respond correctly to direct intervention on the retained history.

That is stronger than saying recent physics “confirms” the framework, because it is accurate and makes the proposed test harder rather than easier.

---

## References / starting points

- Keeling, J., Stoudenmire, E. M., Bañuls, M.-C., & Reichman, D. R. (2026). *Process Tensor Approaches to Non-Markovian Quantum Dynamics*. Physical Review X 16, 020502. https://doi.org/10.1103/1ncg-11hz
- Zambon, G., & Adesso, G. (2025). *Quantum Processes as Thermodynamic Resources: The Role of Non-Markovianity*. Physical Review Letters 134, 200401. https://doi.org/10.1103/PhysRevLett.134.200401
- Dowling, N. et al. (2024). *Capturing Long-Range Memory Structures with Tree-Geometry Process Tensors*. Physical Review X 14, 041018. https://doi.org/10.1103/PhysRevX.14.041018
- Bäcker, C., Beyer, K., & Strunz, W. T. (2024). *Local Disclosure of Quantum Memory in Non-Markovian Dynamics*. Physical Review Letters 132, 060402. https://doi.org/10.1103/PhysRevLett.132.060402
- *Learning and forecasting open quantum dynamics with correlated noise* (2025). Communications Physics. https://doi.org/10.1038/s42005-025-01944-2
- *Geometric signature of non-Markovian dynamics* (2025). Annals of Physics 483, 170243. https://doi.org/10.1016/j.aop.2025.170243
- *History Dependence in Thermodynamic Properties of Solids* (2026). International Journal of Thermophysics 47, 97. https://doi.org/10.1007/s10765-026-03763-1
- White et al. (2022). *Non-Markovian Quantum Process Tomography*. PRX Quantum 3, 020344. https://doi.org/10.1103/PRXQuantum.3.020344
- *Non-Markovian memory strength bounds quantum process recoverability* (2021). npj Quantum Information. https://doi.org/10.1038/s41534-021-00481-4
- Sevetlidis, V., & Pavlidis, G. (2026). *Process-Tensor Tomography of SGD: Measuring Non-Markovian Memory via Back-Flow of Distinguishability*. AISTATS 2026. https://proceedings.mlr.press/v300/sevetlidis26a.html

---

**Research interpretation:** This note updates the external-research context only. It does not supersede the current mathematical specification, the September 2026 technical edition, or the current research-position note.