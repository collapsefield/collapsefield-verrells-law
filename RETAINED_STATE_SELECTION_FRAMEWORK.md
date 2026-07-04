# Retained-State Selection Framework

## Status

Verrell's Law is currently presented as a **retained-state selection framework**, not as an established law of physics.

The core claim is:

> Prior interactions can leave persistent state changes. Those retained changes can bias future selection, producing path-dependent divergence even when present inputs appear similar or unchanged.

Shortest form:

> Memory shapes weighting.  
> Weighting shapes selection.  
> Selection shapes what follows.

This document defines the current public mathematical spine of Verrell's Law and the claim boundary around it.

---

## Claim Boundary

Verrell's Law does not currently claim that:

- memory is stored in a universal electromagnetic field;
- consciousness is proven to be field-indexed;
- quantum collapse is being redefined;
- general relativity is being modified;
- Collapse Aware AI proves new physics.

The present claim is narrower and stronger:

> Prior retained state can measurably bias later selection.

The framework allows field, biological, computational, environmental, or social substrates to participate where they are measurable, but it does not depend on any one substrate.

**Fields may participate; retained state is primary.**

---

## What Is New Here

The mathematics used here is deliberately standard.

The framework uses known selection and state-update formalisms because they are estimable, falsifiable, and compatible with existing engineering and scientific methods.

The contribution of Verrell's Law is not the invention of softmax, logit selection, leaky memory, hysteresis, state-dependent dynamics, Bayesian updating, reinforcement learning, or Markov processes.

The contribution is the explicit framing of retained-state influence as a measurable, governable selection-bias term across system classes, with a pre-committed route for estimating whether retained history contributes measurable divergence beyond present input.

In other words:

> The claim is the measurability and governability of retained-state influence, not the novelty of the selection equation.

---

## Core Process

```text
Observation / Interaction
↓
State change
↓
Retained information
↓
Weighting / bias
↓
Altered future selection
↓
Path-dependent outcome
```

A system does not need to store a perfect transcript of its past. It only needs a retained change that is strong enough to influence future weighting or selection.

---

## Collapse Means Selection Resolution

In this framework, **collapse** does not need to mean quantum wave-function collapse.

In the engineering and systems sense used here, collapse means:

> the resolution of competing candidate outcomes into a selected outcome under present input, retained state, and governing constraints.

That selected outcome may be an action, interpretation, behavioural response, prediction, classification, biological response, social consequence, or other resolved system state.

---

## Retained-State Update

The retained state of a system may be represented abstractly as:

```math
M_{t+1} = \rho M_t + \eta\Phi(O_t, y_t, E_t)
```

where:

| Symbol | Meaning |
|---|---|
| `M_t` | retained memory, history, or state at time `t` |
| `M_{t+1}` | updated retained state |
| `ρ` | retention/decay coefficient |
| `η` | imprint or encoding strength |
| `Φ(O_t, y_t, E_t)` | encoding function of observation, selected outcome, and environment |
| `O_t` | observation, input, or interaction |
| `y_t` | selected outcome at time `t` |
| `E_t` | environmental or contextual signal |

This is intentionally substrate-neutral. Depending on the system being studied, `M_t` may refer to neural state, software memory, physical configuration, environmental trace, institutional record, social memory, or another persistent state variable.

---

## Candidate Selection

For candidate outcome `y_i`, define a candidate score/logit:

```math
z_i = U(y_i; S_t, O_t) + \lambda B(y_i; M_t)
```

where:

| Symbol | Meaning |
|---|---|
| `z_i` | final candidate score/logit |
| `y_i` | candidate outcome, action, interpretation, or behaviour |
| `S_t` | current system state |
| `O_t` | current observation/input/interaction |
| `M_t` | retained memory/history/state |
| `U(y_i; S_t, O_t)` | baseline utility or selection pressure from present state and input |
| `B(y_i; M_t)` | retained-state bias term for candidate `y_i` |
| `λ` | retained-state influence coefficient |

### Operational Boundary Between `S_t` and `M_t`

The boundary between `S_t` and `M_t` is operational, not metaphysical.

`S_t` denotes the state variables held matched across conditions by the pre-registered test protocol. `M_t` denotes the retained-state variables allowed to differ across conditions because the systems have different histories.

This matters because any real system's current state may already contain traces of history. Verrell's Law therefore defines the `S_t` / `M_t` split by test design: what is controlled as present-state baseline belongs to `S_t`; what is deliberately varied, ablated, randomised, or compared as retained history belongs to `M_t`.

Selection probability is then:

```math
P(y_i \mid S_t, O_t, M_t) = \frac{e^{z_i}}{\sum_j e^{z_j}}
```

A selected outcome may be sampled probabilistically:

```math
y^* \sim P(y_i \mid S_t, O_t, M_t)
```

or selected deterministically:

```math
y^* = \arg\max_i z_i
```

---

## Equivalent Baseline Probability Form

The same retained-state selection structure can also be written as:

```math
P(y_i \mid S_t, O_t, M_t)
=
\frac{
P_0(y_i \mid S_t,O_t)e^{\lambda W(M_t,y_i)}
}{
\sum_j P_0(y_j \mid S_t,O_t)e^{\lambda W(M_t,y_j)}
}
```

where:

| Symbol | Meaning |
|---|---|
| `P_0(y_i \mid S_t,O_t)` | baseline probability without retained-state weighting |
| `W(M_t,y_i)` | compatibility between retained state and candidate outcome |
| `λ` | retained-state influence coefficient |

These forms are equivalent with `U(y_i;S_t,O_t) = log P_0(y_i | S_t,O_t)` up to an additive constant, and `B = W`.

Operationally, the baseline condition should be defined before testing. In an engineering test, it may be the same system with retained-state weighting disabled, ablated, randomized, or held neutral.

---

## Identifiability Constraint

Only the product of retained-state strength and retained-state bias enters the candidate score.

```math
\lambda B(y_i;M_t)
```

Therefore, `λ` and `B` are not separately identifiable unless the bias function, baseline condition, and estimation protocol are defined before testing.

For this reason, public claims should not rely on post-hoc fitting of `B` after observing the result.

A valid test should pre-commit:

1. the baseline condition;
2. the retained-state condition;
3. the candidate set;
4. the retained-state feature or scoring rule;
5. the decision rule for whether retained-state influence is supported;
6. known confounds to be checked before verdict.

The estimation machinery for this claim should be handled through the dedicated estimator document:

> `FALSIFIABLE_MEMORY_BIAS_ESTIMATOR.md`

---

## Relationship to Collapse Aware AI

Verrell's Law and Collapse Aware AI are connected but separate.

- **Verrell's Law** is the retained-state selection framework.
- **Collapse Aware AI** is the engineering track.

Collapse Aware AI does not prove Verrell's Law as physics.

It tests the engineering analogue:

> Can retained weighted state influence future behavioural selection in a governed, measurable, inspectable runtime without retraining the underlying model?

Public engineering claims should remain limited to demonstrated behaviour, such as candidate selection, retained-state influence, governor constraints, persistence evidence, restart-safe recall, bias-on/bias-off divergence, and diagnostic traceability.

Do not disclose internal Crown control structure or map public coefficients directly onto private implementation parameters.

Publish measurement, not control.

---

## Triviality Objection

A likely objection is:

> "This is just hysteresis, state-dependent selection, a Markov process with state, an RNN, Bayesian updating, or reinforcement learning."

The response is:

> Verrell's Law does not deny those precedents. It deliberately uses standard state-dependent selection mathematics. The framework's claim is not that retained-state influence is unknown. The claim is that retained-state influence can be explicitly parameterised, governed, measured, compared across regimes, and tested through pre-committed divergence protocols.

That makes the framework falsifiable rather than merely metaphorical.

---

## Minimal Falsifiable Claim

Otherwise similar systems with different retained histories should show measurable divergence under matched present input if retained-state weighting is active.

If no repeatable divergence appears under controlled conditions, or if the fitted retained-state influence is indistinguishable from the pre-registered null condition, the claim is not supported in that tested regime.

The correct null wording is:

> refuted in the tested regime.

Not:

> disproven everywhere.

---

**Version:** v1.0 retained-state hardening pass  
**Date:** 2026-07-04  
**Author:** Marcos Verrell Moss Ross (M.R.) / Inappropriate Media Limited  
**Repository target:** `collapsefield/collapsefield-verrells-law`
