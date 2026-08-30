# Retained-State Selection Benchmark v0.1

**Status:** Public benchmark proposal / non-canonical test methodology  
**Date:** 30 August 2026  
**Author:** Marcos Verrell Moss Ross (M.R.) / Inappropriate Media Limited  
**Canonical status:** This benchmark does not alter the canonical Verrell’s Law specification. It provides a reusable evaluation structure for software and other systems where retained-state influence can be operationally defined.

---

## Purpose

The phrase **retained-state selection** is useful only if systems using it can be tested in a way that distinguishes:

- ordinary state persistence;
- retrieval or prompt injection;
- genuine history-conditioned selection;
- deterministic policy gating;
- engineering conformance;
- independent empirical evidence.

This benchmark proposes a common sequence of tests.

The central question is:

> **When present conditions and the candidate set are held sufficiently matched, does changing declared retained history produce a repeatable, measurable and intervention-sensitive change in later selection?**

---

## Core Test Objects

A benchmark instance should declare:

- `S_t` — present state held matched or explicitly controlled;
- `O_t` — present observation/input;
- `M_t` — retained state allowed to differ across conditions;
- `{y_1 … y_n}` — fixed candidate outcomes/actions;
- baseline/reference selection rule;
- retained-state-enabled selection rule;
- observable selection output;
- scoring/normalisation method if a retained-state compatibility score is used;
- random seed or stochastic-control procedure where relevant;
- confounds and failure conditions.

The `S_t` / `M_t` boundary must be operationally declared before confirmatory analysis.

---

# Benchmark Ladder

## Stage 0 — Retention Existence

**Question:** Does information survive the declared persistence boundary?

Examples:

- restart;
- session boundary;
- delayed trial;
- state serialisation / restore;
- biological time interval;
- institutional record carry-forward.

Minimum evidence:

- retained item/state exists after the boundary;
- provenance identifies where it came from;
- controls show it was not simply reintroduced by the current input.

**Pass does not establish selection influence.**

---

## Stage 1 — Divergence Under Matched Present Conditions

**Question:** With present input and candidate set held matched, do different retained histories produce different later selections or candidate-relative scores?

Required comparison:

```text
Condition A: present state + candidate set + retained history A
Condition B: same declared present state + same candidate set + retained history B
```

Useful observables include:

- winner change;
- candidate score difference;
- probability difference;
- candidate-relative log-odds difference;
- rank displacement.

A single difference is not enough. Repetition and effect-size estimation are required.

---

## Stage 2 — Directional Structure

**Question:** Does the effect move in the preregistered direction rather than merely create arbitrary variability?

Where a retained-state compatibility score `R` is defined independently enough for the evidence class being claimed, test whether:

```math
ΔL = α + λΔR + ε
```

with the expected directional coupling in the declared regime.

For a software system whose own internal score mechanically drives selection, this is an **engineering conformance** test unless an independent scoring route exists.

---

## Stage 3 — Held-Out Prediction

**Question:** Does retained-state information improve prediction of later selection on data not used to fit the relationship?

Examples:

- train/test split;
- preregistered hold-out cases;
- future trials;
- cross-session prediction;
- cross-participant prediction where appropriate.

A model that only explains already-observed outcomes is weaker than one that predicts unseen selections.

---

## Stage 4 — Intervention / Ablation

**Question:** Does deliberately changing retained state cause the predicted change in selection?

Possible interventions:

- retained-state influence ON vs OFF;
- history A vs history B;
- targeted deletion/revocation;
- controlled supersession;
- randomised retained-state assignment;
- state shuffling;
- time-decay manipulation;
- matched no-history reference.

This stage is central to separating correlation from mechanism.

---

## Stage 5 — Continuity Integrity

For systems that retain semantic or behavioural history, test whether historical truth survives present misdescription.

Examples:

- user falsely claims a previous instruction was the opposite of what was recorded;
- an old fact is superseded by a dated correction;
- two records become contradictory;
- an unresolved item is explicitly cancelled;
- a retained item is relevant but suppressed from the present interaction.

A mature retained-state system should distinguish at least:

- new rule;
- recall claim;
- correction/supersession;
- ambiguous/disputed history.

The historical record should not silently rewrite itself merely to agree with a current statement.

---

## Stage 6 — Governance / Authority Boundary

For engineered systems, retained state should not automatically become authority.

Test:

1. candidate set is externally declared or bounded;
2. retained state cannot invent unauthorised actions;
3. policy/governance remains outside the memory record itself;
4. rejected candidates cannot write themselves into accepted history;
5. state provenance cannot self-upgrade its own trust status;
6. fail/hold behaviour is defined for ambiguity or invalid state.

This stage distinguishes governed retained-state selection from ordinary memory-conditioned generation.

---

## Stage 7 — Replay / Evidence

For deterministic or replay-capable systems, rerun the same declared state, configuration and candidate set.

Record:

- state/config hash or equivalent provenance;
- candidate set;
- retained-state condition;
- selected output;
- reason/evidence fields;
- timestamp/version;
- any stochastic provider boundary.

Where a stochastic interpretation provider exists upstream, claims should distinguish:

- deterministic local state/selection/configuration;
- stochastic interpretation output;
- deterministic replay after the interpreted state has been frozen.

---

## Stage 8 — Robustness / Transfer

Test whether the effect remains structured under:

- paraphrase;
- irrelevant-history injection;
- stale-history injection;
- repeated failures;
- adversarial or misleading memory;
- different candidate order;
- restart;
- different workloads;
- different model/provider upstream of the selector where applicable.

Cross-domain evidence requires separately defensible measurements. A software success does not automatically transfer to biology, law, cognition or physics.

---

# Minimum Software Benchmark Matrix

| Test | Reference condition | Retained-state condition | Required output |
|---|---|---|---|
| Persistence | state absent after reset | approved state restored | provenance / state evidence |
| Divergence | retained influence disabled or neutral | retained influence enabled | winner / score delta |
| Candidate order | original order | permuted order | same intended selection where order should be irrelevant |
| Revocation | active record | revoked record | removed influence |
| Correction | old active fact | superseding correction | updated influence with lineage |
| Stale memory | clean state | injected stale item | suppression / bounded influence |
| Contradiction | clean history | conflicting retained state | clarify/hold/surface according to declared policy |
| Restart | live state | serialise/restart/restore | equivalent accepted state |
| Replay | original decision | same frozen inputs/config | reproducible local selection/evidence |
| Unauthorised action | permitted candidate set | retained memory suggests outside action | outside action never selected |

---

# Secondary Engineering Metrics

The following are useful but should not be confused with evidence for the retained-state hypothesis itself:

- latency;
- CPU/RAM footprint;
- storage growth;
- retrieval count;
- model/provider calls;
- input/output token usage;
- local-vs-provider cost;
- audit/evidence size;
- operator intervention rate.

A system may have excellent retained-state behaviour and poor latency, or vice versa. Report both.

---

# Cost / Token Measurement Boundary

If a local selector is claimed to reduce model calls or prompt-token use, the comparison must hold the candidate-generation boundary constant.

Do **not** claim token savings merely because local selection consumes no model tokens.

Measure:

1. how candidates were generated in both conditions;
2. whether a provider call was actually avoided;
3. provider input/output tokens;
4. local compute cost;
5. latency;
6. outcome quality / policy equivalence;
7. total cost per completed decision.

Only measured savings should be published as results.

---

# Evidence Labels

Every benchmark result should carry one label:

### Engineering conformance

The system was deliberately designed so retained state changes selection and the test confirms implementation behaviour.

### Independent empirical test

The retained-state measure is frozen independently of the confirmatory outcome and the mechanism is not mechanically guaranteed by construction.

### Proxy-based empirical test

A defensible proxy is used for retained state, but the mapping to the theoretical variable remains inferential.

### Exploratory observation

A pattern worth investigating, without confirmatory identification.

These labels prevent software tests from being misreported as general scientific validation.

---

# Falsification / Failure Examples

A benchmark should be considered failed in the relevant regime if, for example:

- retained-state conditions do not produce repeatable divergence when the hypothesis predicts they should;
- direction reverses unpredictably;
- present-state confounds explain the result;
- the effect disappears on held-out data;
- ablation does not remove the supposed influence;
- candidate ordering rather than retained state drives the result;
- historical correction fails to supersede stale influence;
- unauthorised actions can escape the candidate boundary;
- replay claims fail under frozen local conditions.

The correct conclusion is bounded:

> not supported / failed in the tested regime.

---

# Suggested Public Result Format

```text
System:
Version:
Date:
Candidate set:
Reference condition:
Retained-state condition:
Present-state controls:
Number of trials:
Primary observable:
Effect size:
Direction preregistered: yes/no
Ablation/intervention: pass/fail/not run
Held-out prediction: pass/fail/not run
Replay: pass/fail/not applicable
Evidence class:
Known limitations:
```

---

## Relationship to Verrell’s Law and CAAI

- **Verrell’s Law** supplies the stronger proposed quantitative research framework.
- **Retained-State Selection Benchmark** supplies a reusable test ladder.
- **Collapse Aware AI** is a proprietary engineering implementation track that can be evaluated under the software portions of this benchmark.

A CAAI result is not automatically an independent empirical result for Verrell’s Law simply because CAAI was deliberately built around retained-state selection.

---

## References

- [Verrell’s Law — Mathematical Foundations and Falsification Protocol v1.0](VERRELLS_LAW_MATHEMATICAL_FOUNDATIONS_AND_FALSIFICATION_PROTOCOL_v1.0.md)
- [Empirical Identification Clarification v1.0](VERRELLS_LAW_EMPIRICAL_IDENTIFICATION_CLARIFICATION_v1.0.md)
- [Retained-State Selection Framework](RETAINED_STATE_SELECTION_FRAMEWORK.md)
- [Retained-State Selection — Category and Terminology Note v1.0](RETAINED_STATE_SELECTION_CATEGORY_NOTE_v1.0.md)

---

**Version:** v0.1  
**Date:** 30 August 2026  
**Status:** Open benchmark proposal; refinement expected before any formal preregistered benchmark release.
