# Field Memory Bias Test Design

This document outlines the Phase 2 test protocol for measuring informational field bias during simulated collapse events.

## Objective

Detect whether observed reality outcomes are statistically biased by prior memory resonance.

## Methodology

1. Run a control test with random data generation
2. Introduce a subject with memory-priming exposure
3. Run parallel test with identical generator configuration
4. Compare JSON logs using `avg_diff` field

## Log Structure

```json
{
  "timestamp": "...",
  "control_avg": 0.493,
  "test_avg": 0.538,
  "avg_diff": 0.045
}
```

## Expected Result

A positive `avg_diff` consistently above statistical noise margin over multiple tests indicates possible memory-based collapse bias.