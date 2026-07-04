# Verrell's Law Mathematical Reference v1.3

## Version Note

This version aligns the mathematical reference with the retained-state selection framing.

The current mathematical status is:

> Verrell's Law is a falsifiable retained-state selection framework. Its mathematics deliberately uses standard state-update and selection formalisms. The framework's claim is the measurability and governability of retained-state influence, not the novelty of the selection equation.

This reference should be read alongside:

- `RETAINED_STATE_SELECTION_FRAMEWORK.md`
- `FALSIFIABLE_MEMORY_BIAS_ESTIMATOR.md`
- `FALSIFICATION_CONDITIONS.md`
- `SPECULATIVE_EXTENSIONS.md`

---

## 1. Core Variables

| Symbol | Meaning |
|---|---|
| `S_t` | current system state |
| `O_t` | current observation, input, or interaction |
| `E_t` | environmental/contextual signal |
| `M_t` | retained memory, history, or state |
| `M_{t+1}` | updated retained state |
| `y_i` | candidate outcome, action, interpretation, or behaviour |
| `y^*` | selected outcome |
| `U(y_i;S_t,O_t)` | baseline utility or present-state selection pressure |
| `B(y_i;M_t)` | retained-state bias function |
| `λ` | retained-state influence coefficient |
| `z_i` | final candidate score/logit |
| `ρ` | retention/decay coefficient |
| `η` | imprint/encoding strength |
| `Φ(O_t,y_t,E_t)` | state encoding/update function |

---

## 2. Retained-State Update

```math
M_{t+1} = \rho M_t + \eta\Phi(O_t, y_t, E_t)
```

This states that future retained state depends on prior retained state plus encoded influence from the current observation, selected outcome, and environmental/contextual signal.

This is not claimed as a novel memory equation. It is a standard state-update structure used here because it is operational, measurable, and falsifiable.

---

## 3. Candidate Score / Logit

```math
z_i = U(y_i; S_t, O_t) + \lambda B(y_i; M_t)
```

The baseline term `U` represents selection pressure from the present state and input.

The retained-state term `B` represents the directional influence of retained state on the candidate outcome.

The coefficient `λ` controls retained-state influence strength.

---

## 4. Selection Probability

```math
P(y_i \mid S_t,O_t,M_t)
=
\frac{e^{z_i}}{\sum_j e^{z_j}}
```

The selected outcome may be sampled probabilistically:

```math
y^* \sim P(y_i \mid S_t,O_t,M_t)
```

or selected deterministically:

```math
y^* = \arg\max_i z_i
```

This single softmax/logit formalism covers both probabilistic and deterministic selection. No separate threshold equation is required in the main framework.

---

## 5. Equivalent Baseline Probability Form

```math
P(y_i \mid S_t,O_t,M_t)
=
\frac{
P_0(y_i \mid S_t,O_t)e^{\lambda W(M_t,y_i)}
}{
\sum_j P_0(y_j \mid S_t,O_t)e^{\lambda W(M_t,y_j)}
}
```

where `P_0` is the baseline probability when retained-state weighting is disabled, neutralised, randomised, or otherwise defined as absent for the tested regime.

These forms are equivalent with `U(y_i;S_t,O_t) = log P_0(y_i | S_t,O_t)` up to an additive constant, and `B = W`.

---

## 6. Operational `S_t` / `M_t` Boundary

The boundary between `S_t` and `M_t` is defined by the pre-registered test design.

`S_t` denotes state variables held matched across conditions. `M_t` denotes retained-state variables that differ because of different histories and are deliberately varied, ablated, randomised, or compared.

This prevents the framework from relying on a vague distinction between present state and memory. The distinction is experimental: what is controlled as baseline belongs to `S_t`; what is tested as history-dependent retained state belongs to `M_t`.

---

## 7. Baseline Condition

The baseline must be operationally defined before testing.

A valid baseline may be:

- the same system with retained-state weighting disabled;
- the same system with retained state randomised;
- the same system with retained state ablated;
- a matched control system with no relevant retained history;
- a pre-defined statistical null model using present input only.

In an engineering setting, a bias-off or memory-neutral condition can serve as the baseline where properly controlled.

---

## 8. Identifiability

Only the product enters the candidate score:

```math
\lambda B(y_i;M_t)
```

Therefore `λ` and `B` are not independently identifiable unless the bias function and baseline are pre-defined.

This is why Verrell's Law requires pre-committed tests rather than post-hoc curve fitting.

The estimation procedure should be handled through:

> `FALSIFIABLE_MEMORY_BIAS_ESTIMATOR.md`

---

## 9. Collapse as Selection Resolution

In this framework, collapse means resolution of competing candidates into a selected outcome.

It does not require quantum wave-function collapse.

The mathematical act of selection is represented by either:

```math
y^* \sim P(y_i \mid S_t,O_t,M_t)
```

or:

```math
y^* = \arg\max_i z_i
```

This keeps the framework compatible with engineering, cognitive modelling, behavioural systems, and probabilistic selection without overclaiming physics.

---

## 10. Minimal Falsifiable Prediction

If retained-state weighting is active, otherwise similar systems with different retained histories should show measurable divergence under matched present input.

If the retained-state term does not improve prediction beyond the baseline condition, the claim is not supported in that tested regime.

---

## 11. Physical Boundary

This mathematical reference does not assert a physical tensor extension.

Field activity, quantum interpretations, or deeper physical substrates belong in `SPECULATIVE_EXTENSIONS.md` and are not required for the retained-state selection framework.

---

**Version:** v1.3 retained-state hardening pass  
**Date:** 2026-07-04  
**Author:** Marcos Verrell Moss Ross (M.R.) / Inappropriate Media Limited  
**Repository target:** `collapsefield/collapsefield-verrells-law`
