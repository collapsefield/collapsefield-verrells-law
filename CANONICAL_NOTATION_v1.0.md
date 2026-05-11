# Canonical Notation — Verrell’s Law
## Version 1.0

**Framework:** Verrell’s Law  
**Author:** M.R.  
**Maintainer:** Inappropriate Media Limited (t/a Collapse Aware AI)  
**Status:** Canonical Public Reference  
**Date:** 2026  
**Purpose:** Establish canonical notation, terminology, and operational definitions for the Verrell’s Law framework and Active Information Weight Principle.

> This document supersedes prior informal public statements regarding Verrell’s Law notation and Active Information Weight terminology. Version history and timestamped revisions are maintained through the official repository commit history.

---

# 1. Purpose

This document defines the canonical mathematical notation used throughout Verrell’s Law and associated Collapse Aware AI materials.

The goal is to:

- standardize terminology,
- reduce ambiguity,
- establish historical provenance,
- maintain mathematical consistency across documents,
- and prevent reinterpretation or silent variable substitution by derivative works.

This file acts as the primary notation reference for all public Verrell’s Law materials unless explicitly superseded by a newer version.

---

# 2. Core Principle

Verrell’s Law describes **memory-weighted selection**:

> Retained information from prior states can bias future outcome probabilities.

The operational mechanism for this process is termed:

# Active Information Weight (AIW)

AIW describes the measurable influence of retained prior information on future selection probability.

---

# 3. Canonical Selection Equation

The canonical memory-weighted selection equation is:

\[
P(y_i \mid S_t, O_t, M_t)
=
\frac{
\exp\left(
U(y_i; S_t, O_t)
+
\lambda B(y_i; M_t)
\right)
}{
\sum_j
\exp\left(
U(y_j; S_t, O_t)
+
\lambda B(y_j; M_t)
\right)
}
\]

---

# 4. Canonical Symbol Definitions

## \(P(y_i \mid S_t, O_t, M_t)\)

Probability of selecting candidate state or output \(y_i\) given:

- current state \(S_t\),
- observation/input \(O_t\),
- and retained memory/history \(M_t\).

---

## \(y_i\)

A candidate output, action, behavioural state, or selection possibility.

Examples:

- an AI response,
- a behavioural branch,
- a simulated action,
- a future probabilistic state.

---

## \(S_t\)

Current system state at time \(t\).

Examples:

- active runtime state,
- environmental conditions,
- current internal state variables,
- present system configuration.

---

## \(O_t\)

Current observation, prompt, measurement, or external input at time \(t\).

Examples:

- user prompt,
- sensory input,
- observed environment,
- interaction signal.

---

## \(M_t\)

Retained informational history or memory state accumulated prior to time \(t\).

This may include:

- weighted memories,
- anchors,
- recurrence traces,
- salience-weighted information,
- prior interactions,
- behavioural reinforcement history.

---

## \(U(y_i; S_t, O_t)\)

Present-state utility function.

Represents the immediate utility, relevance, or suitability of candidate \(y_i\) under the current state and observation.

This is the memory-independent component of selection.

---

## \(B(y_i; M_t)\)

Memory-derived bias term.

Represents the influence of retained informational history on candidate \(y_i\).

This term encodes Active Information Weight.

Examples of contributors include:

- prior reinforcement,
- salience,
- continuity pressure,
- recurrence,
- weighted memory traces,
- behavioural anchors,
- governor-approved persistence.

---

## \(\lambda\)

Memory-bias coupling coefficient.

Controls the influence strength of retained informational history on future selection probability.

Interpretation:

- \(\lambda = 0\): memoryless selection  
- \(\lambda > 0\): memory-weighted selection  
- larger \(\lambda\): stronger historical influence

This parameter is canonical within Verrell’s Law notation.

---

# 5. Canonical Divergence Expression

Path-dependent divergence is represented as:

\[
\Delta P(s_i)
\propto
\lambda
\cdot
\left[
B(s_i; M_t^A)
-
B(s_i; M_t^B)
\right]
\]

This formalizes the prediction that two systems with identical present-state inputs may diverge if their retained histories differ.

---

# 6. Weighted Emergence Layering (WEL)

Weighted Emergence Layering (WEL) describes the recursive accumulation of informational weighting across sequential selections.

Under WEL:

- prior selections influence future selections,
- retained traces accumulate probabilistically,
- behavioural continuity emerges through weighted informational layering,
- and future collapse tendencies become path-dependent.

WEL is a canonical subsystem concept within Verrell’s Law and Collapse Aware AI.

---

# 7. Canonical Terminology

| Term | Canonical Meaning | Common Misrepresentation to Watch For |
|---|---|---|
| Active Information Weight (AIW) | Influence of retained information on future selection probability | Incorrectly reduced to simple context-window retention or token persistence |
| Memory-Weighted Selection | Selection influenced by retained informational history | Misrepresented as ordinary prompt conditioning alone |
| Weighted Emergence Layering (WEL) | Recursive layering of retained informational influence | Mischaracterized as static reinforcement learning memory |
| Strong Memory Anchor | High-weight persistent informational trace | Incorrectly framed as a fixed hard-coded rule |
| Continuity Pressure | Bias toward maintaining behavioural consistency | Confused with deterministic scripting |
| Governed Selection | Selection constrained/modulated by governor systems | Reduced to moderation-only filtering |
| Path-Dependent Divergence | Divergence caused by differing retained histories | Incorrectly reframed as random drift or noise |
| Collapse Selection | Final probabilistic selection from competing candidate states | Misrepresented as ordinary single-pass generation |
| Memoryless Baseline | Selection without retained informational influence | Incorrectly conflated with stateless prompting alone |
| Informational Bias Term \(B(y_i; M_t)\) | Quantified historical weighting contribution to selection | Incorrectly reframed as attention weights alone |

---

# 8. Worked Comparative Numerical Example

This example demonstrates path-dependent divergence using identical present-state utility values but different retained histories.

Assume two agents:

- Agent A possesses reinforced prior history related to candidate \(y_i\)
- Agent B possesses weaker or absent prior reinforcement

Both agents receive the same current input.

---

## Shared Present-State Utility

For both agents:

\[
U(y_i)=0.7
\]

Memory coupling coefficient:

\[
\lambda=0.8
\]

---

## Agent A — Reinforced Prior History

Agent A possesses stronger retained informational weighting:

\[
B_A(y_i; M_t)=0.5
\]

Selection score:

\[
0.7 + (0.8 \times 0.5)
=
1.1
\]

Exponentiated weighting:

\[
e^{1.1}\approx3.004
\]

---

## Agent B — Weak Prior History

Agent B possesses weaker retained informational weighting:

\[
B_B(y_i; M_t)=0.1
\]

Selection score:

\[
0.7 + (0.8 \times 0.1)
=
0.78
\]

Exponentiated weighting:

\[
e^{0.78}\approx2.182
\]

---

## Comparative Selection Probability

Assume only two candidates exist:

\[
y_i,\quad y_j
\]

and candidate \(y_j\) has baseline exponentiated weighting:

\[
e^{0.5}\approx1.649
\]

---

### Agent A Probability

\[
P_A(y_i)
=
\frac{3.004}{3.004+1.649}
\approx0.646
\]

---

### Agent B Probability

\[
P_B(y_i)
=
\frac{2.182}{2.182+1.649}
\approx0.570
\]

---

## Result

Although both agents possessed identical present-state utility:

\[
U(y_i)=0.7
\]

their differing retained histories produced measurably different future selection probabilities:

\[
0.646 \neq 0.570
\]

Explicit divergence:

\[
\Delta P(y_i)\approx0.076
\]

This divergence is attributable entirely to retained informational weighting difference:

\[
\Delta B = 0.4
\]

under:

\[
\lambda = 0.8
\]

This is the operational prediction of Active Information Weight.

The divergence was not caused by randomness alone, but by differing retained informational weighting histories.

---

# 9. Prior Art Boundary Statement

Verrell’s Law and the Active Information Weight Principle do not claim to invent probabilistic selection, utility scoring, Bayesian updating, reinforcement learning, Markov processes, or softmax functions.

These mathematical and computational structures existed prior to the framework.

The claim of Verrell’s Law is narrower and more specific:

> Retained informational history can function as an active probabilistic weighting mechanism influencing future selection behaviour across time.

The framework differs from ordinary stateless selection systems by explicitly formalizing:

- retained historical weighting,
- continuity-driven bias,
- salience-weighted persistence,
- path-dependent divergence,
- and recursive informational layering across sequential selections.

For example:

- standard softmax selection does not inherently define persistent cross-temporal memory weighting;
- ordinary Markov models typically assume future state dependence primarily on current state;
- attention mechanisms prioritize contextual relevance during processing but do not inherently formalize persistent probabilistic continuity weighting across long-term retained histories as defined under Active Information Weight.

The Active Information Weight Principle therefore operates as a structured memory-bias formalism layered onto probabilistic selection systems rather than a replacement for existing probability theory.

---

# 10. Provenance and Authorship

This notation system forms part of the Verrell’s Law framework and associated Collapse Aware AI architecture.

Canonical terminology, symbol structure, operational definitions, and worked examples originate from the Verrell’s Law project archive and associated timestamped public materials.

This document establishes the canonical notation reference for Active Information Weight and associated memory-weighted selection terminology.

---

# 11. Canonical One-Line Definition

> Active Information Weight is the measurable influence of retained prior information on future selection probability.

---

# 12. Attribution

**Author:** M.R.  
**Maintainer:** Inappropriate Media Limited (t/a Collapse Aware AI)
