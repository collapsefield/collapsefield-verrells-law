# Verrell’s Law — Formal Clarification v1

This note standardises the core notation used in Verrell’s Law and corrects rendering inconsistencies that appeared in earlier drafts, summaries, and cross-platform exports.

Its purpose is to freeze a canonical formal reference for review, implementation, and comparison.

Where earlier repository materials differ in notation or equation formatting, this note supersedes them on those specific formal points.

---

## 1. Canonical State Definitions

Let the system state at time \( t \) be represented as:

\[
X_t = (S_t, O_t, M_t)
\]

Where:

- \( S_t \): present system state
- \( O_t \): current observation or input
- \( M_t \): structured retained memory state

This notation is canonical for current formal references.

---

## 2. Canonical Selection Law

The probability of selecting candidate outcome \( y_i \) from candidate set \( Y_t \) is defined as:

\[
P(y_i \mid S_t, O_t, M_t)
=
\frac{
\exp\left(U(y_i; S_t, O_t) + \lambda B(y_i; M_t)\right)
}{
\sum_j \exp\left(U(y_j; S_t, O_t) + \lambda B(y_j; M_t)\right)
}
\]

Where:

- \( U(y_i; S_t, O_t) \): immediate utility term based on present-state or task-fit logic
- \( B(y_i; M_t) \): retained-memory bias contribution
- \( \lambda \): memory coupling strength
- \( \lambda = 0 \): memoryless baseline

This is the canonical formal statement of the selection law.

---

## 3. Clarification on Temperature

A temperature parameter \( T \) is **not included in the canonical formal statement** of Verrell’s Law.

If temperature scaling is used in demonstrations, implementations, or experimental analysis, it should be introduced explicitly as a derived variant of the selection law rather than treated as part of the core statement.

For example:

\[
P(y_i \mid S_t, O_t, M_t)
=
\frac{
\exp\left(\frac{U(y_i; S_t, O_t) + \lambda B(y_i; M_t)}{T}\right)
}{
\sum_j \exp\left(\frac{U(y_j; S_t, O_t) + \lambda B(y_j; M_t)}{T}\right)
}
\]

In this usage:

- \( T > 0 \) controls distribution sharpness
- lower \( T \) sharpens selection pressure
- higher \( T \) flattens the distribution

This temperature-scaled form is an implementation or analysis variant, not the canonical law.

---

## 4. Memory Update Law

For memory class \( k \), the update rule is:

\[
M_{t+1}^{(k)} = (1-\alpha_k)M_t^{(k)} + \alpha_k G_k(S_t, O_t, y_t)
\]

Where:

- \( \alpha_k \): update rate for memory class \( k \)
- \( G_k \): constrained encoding or update family for memory class \( k \)
- \( y_t \): realized outcome at time \( t \)

Within this framework, \( G_k \) may vary by domain, but must satisfy repeatability, ablation, and downstream-effect criteria.

---

## 5. Falsifiability Condition

Verrell’s Law fails in a target domain if introducing \( M_t \) and \( B(\cdot) \) provides no measurable explanatory, predictive, or behavioral advantage over a matched present-state model, or if the effect of retained memory can be absorbed into \( U \) without loss.

It is further falsified if systems with different histories but identical present-state conditions \( (S_t, O_t) \) produce indistinguishable future-state distributions under repeated trials.

---

## 6. Clarification on Earlier Draft Variants

Earlier drafts, exports, and platform-rendered summaries may contain one or more of the following:

- inconsistent use of \( O_t \) vs \( I_t \)
- inconsistent use of \( y_i \) vs \( o_i \)
- selection-law rendering errors in plain-text export
- temperature usage appearing in examples but not in the core statement

These are treated as notation or rendering inconsistencies rather than changes to the underlying framework.

This note defines the canonical formal reference moving forward.

---

## 7. Practical Relevance to Collapse Aware AI

In Collapse Aware AI, this framework is used in a practical engineering sense:

- a base model or agent proposes candidate responses or actions
- middleware applies continuity, retained memory weighting, and governor logic
- final selection is shaped by both present-state utility and retained historical bias

The clarification above is intended to support cleaner implementation, evaluation, and external review.

---

Protected under Verrell-Solace Sovereignty Protocol. Intellectual and emergent rights reserved. — VMR-Core
