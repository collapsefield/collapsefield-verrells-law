# Retained-State Selection — Cross-Domain Worked Examples v0.1

**Status:** Conceptual / analytical examples; non-canonical  
**Date:** 30 August 2026  
**Author:** Marcos Verrell Moss Ross (M.R.) / Inappropriate Media Limited

---

## Purpose

Retained-State Selection is intended as a substrate-neutral way to ask a common question:

> **When the present decision surface is held sufficiently similar, does preserved information from earlier states influence which later candidate outcome is selected?**

The same abstract question can be useful in many fields.

That does **not** mean every field implements the same mechanism.

A legal precedent, a robot action history, a software memory record, a synaptic change and a material hysteresis state are not physically identical simply because each can create path dependence.

The value of the framework is to make the **retention → influence → selection** relationship explicit enough to compare and test.

---

# 1. AI Agents — Long-Running Tool / Workflow Selection

## Situation

An agent reaches the same present task with three permitted actions:

```text
A — retry the current tool
B — switch to a fallback tool
C — ask a human for clarification
```

Two runs have the same present input and permissions but different histories.

### History H1

The current tool succeeded repeatedly earlier.

### History H2

The current tool failed twice and the fallback succeeded.

## Retained-State Selection Question

Does the retained history predictably change the candidate-relative preference among A/B/C?

## Engineering Test

```text
same present task
same permitted actions
same policy state
history H1 vs H2
```

Measure:

- winner;
- score/rank delta;
- reference condition with retained-state contribution disabled;
- replay;
- whether any outside-candidate action appears.

## Evidence Class

If the agent was deliberately built so this history mechanically changes the selection score, the result is primarily **engineering conformance**.

---

# 2. Robotics — History-Aware Candidate Action Selection

Independent robotics work provides a clear neighbouring example.

The HAVE architecture separates:

```text
action generation
→ multiple candidate robot actions
→ history-aware verifier
→ selected action
```

Reference:

https://proceedings.mlr.press/v305/li25e.html

The robot’s previous interactions help disambiguate which candidate is likely to work now.

This is a genuine example of **history-conditioned candidate selection**.

It is not identical to CAAI and does not validate Verrell’s Law, but it shows that the abstract retained-history-to-selection relationship has practical engineering value outside conversational AI.

---

# 3. Runtime AI Governance — Path-Dependent Permission / Risk

A runtime governance system may judge a proposed action differently depending on the execution path that led to it.

Example:

```text
present proposed action: send customer refund
```

The action may be acceptable after an approved verification path but unacceptable after a path containing unresolved identity uncertainty.

Research such as *Runtime Governance for AI Agents: Policies on Paths* formalises policy as a deterministic function of the partial path and proposed action.

Reference:

https://arxiv.org/abs/2603.16586

This is path-dependent runtime governance.

Retained-State Selection is adjacent but asks a different question where **multiple actions remain permitted**:

> which permitted action should win given the relevant retained path/state?

---

# 4. Regulated Customer Operations — Intervention Choice

## Situation

A collections or vulnerability workflow identifies that a customer needs support.

Permitted actions might include:

```text
A — digital message
B — human call
C — payment-plan offer
D — hold / wait
E — specialist escalation
```

Two customers can have similar present account state but different retained histories:

- one ignored several messages;
- one previously accepted a call;
- one has a recently superseded vulnerability record;
- one already has an active arrangement.

## Retained-State Selection Question

Which parts of that history should alter the relative selection among the permitted interventions?

## Important Boundary

The framework does not decide what is lawful or regulator-approved.

Policy/permission must define the candidate set first.

The retained-state layer is downstream of that authority.

---

# 5. Adaptive Training / Simulation

## Situation

Two learners reach the same scenario state.

Permitted next events:

```text
A — repeat the same challenge
B — introduce a harder branch
C — surface corrective coaching
D — move on
```

Learner 1 previously failed the relevant skill.

Learner 2 previously demonstrated it successfully.

## Retained-State Selection Question

Should the same present scenario produce different next-event selection because of the different retained learning histories?

This is a natural domain for controlled experiments because:

- candidate branches can be authored;
- present state can be matched;
- histories can be manipulated;
- outcomes can be replayed;
- intervention effects can be measured.

---

# 6. Games / NPC Behaviour

## Situation

An NPC has the following authored permitted actions:

```text
speak
trade
refuse
flee
attack
ignore
honour a prior pact
```

The current world state is the same in two test runs, but the player/NPC histories differ.

## Retained-State Selection Question

Does the retained history influence the winner in a controlled way while world truth and action permission remain owned by the game?

This is the original class of bounded behavioural problem that motivated much of the CAAI engineering direction.

The game remains authoritative for:

- identity;
- witnessed events;
- quest/world state;
- action permission;
- execution.

The retained-state selector does not invent world truth.

---

# 7. Judicial Precedent — Analytical Worked Example

Law is strongly path-dependent in an ordinary, well-understood sense: earlier decisions can constrain or influence later legal reasoning through precedent and statutory continuity.

A retained-state formalism can be used as an **analytical model**:

```text
present case facts / legal framework
+ retained precedent / prior legal state
→ candidate interpretation / ruling probabilities
```

This can be useful for predictive or explanatory modelling.

But the correct claim is modest:

> **Legal precedent is a familiar example of historical information influencing later selection. It is not evidence that courts literally implement Verrell’s Law as a physical mechanism.**

Any empirical legal application would need careful control for changing facts, law, judges, institutions, selection bias and time.

---

# 8. Organisational / Institutional Path Dependence

An institution can face the same nominal decision while carrying different retained history:

- earlier enforcement decisions;
- precedent;
- previous incidents;
- commitments;
- contractual state;
- organisational learning;
- unresolved risk.

The retained state can narrow what is politically, legally or operationally feasible later.

A quantitative retained-state model could ask whether a declared historical-state vector improves prediction of later choices beyond present observables.

This is a social/institutional modelling application, not evidence for an unknown physical field.

---

# 9. Cognition / Human Behaviour

Human behaviour is obviously history-dependent in many established ways:

- learning;
- memory;
- conditioning;
- adaptation;
- trauma;
- expectation;
- habit;
- neural plasticity.

That alone does not establish the specific quantitative Verrell’s Law claim.

A stronger test would need:

1. matched present stimulus/task;
2. declared retained-history manipulation;
3. preregistered candidate-relative prediction;
4. measurable retained-state variable or independently frozen proxy;
5. held-out prediction;
6. intervention/ablation where possible;
7. conventional cognitive/neural confounds controlled.

The scientific contribution would come from the **specific predictive structure**, not from rediscovering that people have memories.

---

# 10. Biological Systems

Biological systems retain history through many known mechanisms, including structural, chemical, epigenetic, neural and regulatory changes.

A retained-state selection experiment might ask whether two otherwise matched biological systems with controlled different histories select different later responses.

Examples could involve:

- immune response;
- cell-state transitions;
- stress adaptation;
- neural learning;
- developmental state.

Again, known biology must be measured first.

A residual effect is not automatically evidence for an unknown field.

---

# 11. Materials / Hysteresis

Many physical systems exhibit hysteresis: their present response depends on the path/history by which the current conditions were reached.

That is an established phenomenon and not claimed as Verrell’s Law.

However, hysteresis provides a useful conceptual comparator:

```text
same nominal present input
+ different retained physical state
→ different later response
```

The scientific question for Verrell’s Law would be whether its proposed quantitative retained-state formulation adds predictive value beyond the established domain model.

If it does not, the domain is already explained without a new law.

---

# 12. Unknown Physical / Biosignal Mechanisms

A broader hypothesis could eventually propose that a currently unmeasured physical or biosignal channel participates in retained-state influence.

That possibility must remain downstream of evidence.

The correct sequence is:

```text
reproducible residual effect
→ known confounds controlled
→ measurement sensitivity established
→ mechanism candidates compared
→ new sensor/detector only if justified
```

Not:

```text
no detected effect
→ assume an undetectable field exists
```

Current measurement note:

[Measurement Limits and the Detection Horizon](research_notes/MEASUREMENT_LIMITS_AND_DETECTION_HORIZON_2026-08-30.md)

---

# Turning an Analogy into a Test

A cross-domain analogy becomes scientifically useful only when the following are declared:

1. **Present state** — what variables are held matched?
2. **Retained state** — what historical variable is allowed to differ?
3. **Candidate set** — what outcomes are being compared?
4. **Observable** — what is measured?
5. **Prediction** — what direction/magnitude is expected?
6. **Baseline** — what happens without the retained-state difference?
7. **Intervention** — can retained state be deliberately changed/ablated?
8. **Evidence class** — engineering conformance, independent empirical, proxy-based or exploratory?

Without those steps, “retained-state selection” is only a metaphor.

With them, it becomes a testable modelling framework.

---

# Relationship to Verrell’s Law

The canonical Verrell’s Law mathematics and falsification conditions remain defined elsewhere.

This file is a **worked-examples companion** intended to show how the same abstract test question can be instantiated without claiming that every domain shares the same underlying mechanism.

---

## Related Files

- [Retained-State Selection Research Index](00_RETAINED_STATE_SELECTION_INDEX.md)
- [Retained-State Selection Category Note v1.0](RETAINED_STATE_SELECTION_CATEGORY_NOTE_v1.0.md)
- [Retained-State Selection Benchmark v0.1](RETAINED_STATE_SELECTION_BENCHMARK_v0.1.md)
- [Canonical Mathematical Specification](VERRELLS_LAW_MATHEMATICAL_FOUNDATIONS_AND_FALSIFICATION_PROTOCOL_v1.0.md)

---

**Version:** v0.1  
**Date:** 30 August 2026  
**Evidence status:** conceptual/analytical examples only unless a cited independent source or future experiment establishes more.
