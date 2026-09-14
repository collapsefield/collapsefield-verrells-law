# Retained-State Selection Benchmark v0.1

**Status:** Public benchmark proposal / non-canonical test methodology  
**Date:** 30 August 2026  
**Author / originator:** Marcos Verrell Moss Ross (M.R.)  
**Research attribution refresh:** 14 September 2026  
**Canonical status:** This benchmark does not alter the canonical Verrell’s Law specification.

---

## Purpose

The phrase **retained-state selection** is useful only if systems using it can be tested in a way that distinguishes ordinary persistence, retrieval, history-conditioned selection, deterministic policy gating, engineering conformance and independent empirical evidence.

The central question is:

> **When present conditions and the candidate set are held sufficiently matched, does changing declared retained history produce a repeatable, measurable and intervention-sensitive change in later selection?**

---

## Core test objects

A benchmark instance should declare:

- `S_t` — present state held matched or explicitly controlled;
- `O_t` — present observation/input;
- `M_t` — retained state allowed to differ across conditions;
- `{y_1 … y_n}` — fixed candidate outcomes/actions;
- baseline/reference selection rule;
- retained-state-enabled selection rule;
- observable selection output;
- scoring/normalisation method where a retained-state compatibility score is used;
- stochastic-control procedure where relevant;
- confounds and failure conditions.

The `S_t` / `M_t` boundary must be operationally declared before confirmatory analysis.

---

# Benchmark ladder

## Stage 0 — Retention existence

Does information survive the declared persistence boundary without simply being reintroduced by the current input?

**Pass does not establish selection influence.**

## Stage 1 — Divergence under matched present conditions

```text
Condition A: present state + fixed candidate set + retained history A
Condition B: same declared present state + same candidate set + retained history B
```

Measure winner change, candidate score difference, probability/log-odds difference or rank displacement. Repetition and effect-size estimation are required.

## Stage 2 — Directional structure

Where a retained-state compatibility score is independently defensible, test whether:

```math
\Delta L = \alpha + \lambda\Delta R + \varepsilon
```

moves in the preregistered direction.

If a software selector's own score mechanically drives selection, this is an **engineering conformance** test unless an independent scoring route exists.

## Stage 3 — Held-out prediction

Does the retained-state relationship predict later selection on data not used to fit or tune it?

## Stage 4 — Intervention / ablation

Deliberately add, remove, scramble, supersede or disable retained-state influence and require selection to change as preregistered.

This stage is central to separating correlation from causal influence.

## Stage 5 — Continuity integrity

For systems retaining semantic or behavioural history, test correction, supersession, contradiction, revocation, stale state and disputed history without silently rewriting the historical record to agree with the present claim.

## Stage 6 — Governance / authority boundary

For engineered systems, test that:

1. the candidate set is externally declared or bounded;
2. retained state cannot invent unauthorised actions;
3. policy/governance remains outside the memory record itself;
4. rejected candidates cannot write themselves into accepted history;
5. provenance cannot self-upgrade its trust status;
6. hold/fail behaviour is defined for ambiguity or invalid state.

## Stage 7 — Replay / evidence

Record sufficient state/configuration provenance, candidate set, retained-state condition, selected output, evidence fields and version information to reproduce the local selection where the tested system supports deterministic replay.

Where a stochastic interpretation provider exists upstream, distinguish stochastic interpretation output from deterministic local state/selection/configuration.

## Stage 8 — Robustness / transfer

Test paraphrase, irrelevant or stale history, candidate reordering, restart, repeated failures, misleading memory and different workloads/providers where relevant.

Cross-domain evidence requires separately defensible measurements. A software success does not automatically transfer to biology, cognition or physics.

---

# Minimum software benchmark matrix

| Test | Reference condition | Retained-state condition | Required output |
|---|---|---|---|
| Persistence | state absent after reset | approved state restored | provenance / state evidence |
| Divergence | retained influence disabled/neutral | retained influence enabled | winner / score delta |
| Candidate order | original order | permuted order | same intended selection where order should be irrelevant |
| Revocation | active record | revoked record | removed influence |
| Correction | old active fact | superseding correction | updated influence with lineage |
| Stale memory | clean state | injected stale item | suppression / bounded influence |
| Contradiction | clean history | conflicting retained state | declared clarify/hold/surface behaviour |
| Restart | live state | serialise/restart/restore | equivalent accepted state |
| Replay | original decision | same frozen inputs/config | reproducible local selection/evidence |
| Unauthorised action | permitted candidate set | history suggests outside action | outside action never selected |

---

# Secondary engineering metrics

Report but do not confuse with evidence for the retained-state hypothesis itself:

- latency;
- CPU/RAM footprint;
- storage growth;
- retrieval count;
- provider/model calls;
- token usage;
- local-vs-provider cost;
- audit/evidence size;
- operator intervention rate.

If local selection is claimed to reduce model calls or token use, hold the candidate-generation boundary constant and report actual measured results rather than assumed savings.

---

# Evidence labels

### Engineering conformance
A deliberately built selector behaves according to its declared retained-state mechanism.

### Independent empirical test
The retained-state measure is frozen independently of the confirmatory outcome and the relationship is not mechanically guaranteed by construction.

### Proxy-based empirical test
A defensible proxy is used for retained state, with the mapping to the theoretical variable reported as inferential where appropriate.

### Exploratory observation
A pattern worth investigating without confirmatory identification.

---

# Failure examples

A benchmark should fail in the relevant regime when, for example:

- predicted retained-state divergence is not repeatable;
- direction reverses unpredictably;
- present-state confounds explain the result;
- held-out prediction fails;
- ablation does not alter the supposed influence;
- candidate order rather than retained state drives the result;
- correction/revocation fails;
- unauthorised actions escape the candidate boundary;
- replay claims fail under frozen local conditions.

Correct conclusion:

> **not supported / failed in the tested regime.**

---

## Relationship to Verrell’s Law and Collapse Aware AI™

- **Verrell’s Law** supplies the proposed quantitative research framework.
- **Retained-State Selection Benchmark** supplies a reusable test ladder.
- **Collapse Aware AI™** is a separate engineering programme that can be evaluated under the software portions of this benchmark.

A CAAI result is not automatically an independent empirical result for Verrell’s Law simply because the software was deliberately built around retained-state selection.

---

## References

- [Mathematical Foundations and Falsification Protocol v1.0](VERRELLS_LAW_MATHEMATICAL_FOUNDATIONS_AND_FALSIFICATION_PROTOCOL_v1.0.md)
- [Empirical Identification Clarification v1.0](VERRELLS_LAW_EMPIRICAL_IDENTIFICATION_CLARIFICATION_v1.0.md)
- [Retained-State Selection Framework](RETAINED_STATE_SELECTION_FRAMEWORK.md)
- [Category and Terminology Note v1.0](RETAINED_STATE_SELECTION_CATEGORY_NOTE_v1.0.md)

---

Copyright © 2026 Marcos Verrell Moss Ross (M.R.).
