# ShadowGram Phase 2 Deep Research Audit — Research Context

**Project:** ShadowGram  
**Document:** Deep Research findings captured from the completed Deep Research run  
**Date:** 2026-10-06  
**Status:** Completed research snapshot for Phase 2 implementation

> **Important:** This file captures the Deep Research result returned in this conversation. It is a research snapshot, not a claim that every recommendation is production-validated or legally sufficient. Several claims in the original dossier should be empirically calibrated before being presented as facts.

---

# Executive Summary

The Deep Research audit identified several important upgrades for ShadowGram:

1. **Keystroke Track 3 should not be only a digraph heatmap.** Adaptive attackers can reproduce marginal timing distributions. The detector should examine higher-order temporal structure, key-dependent distributions, covariance, entropy, distribution shape, and consistency with other motor signals.

2. **Node2Vec should not be the sole mathematical centerpiece.** It is useful for relational visualization but is stochastic and comparatively expensive. Deterministic spectral signatures can provide a more mathematically transparent complement.

3. **Topology should be used as a filtration/signature, not as a simplistic fraud proof.** β₀ and β₁ are cheap, but neither alone establishes fraud.

4. **Biomechanical laws are useful features, not proof of biological origin.** Fitts' law, the two-thirds power law, and log-normal velocity models can strengthen the signal when treated as probabilistic evidence.

5. **Privacy claims must be tightened.** Timing-only telemetry does not automatically become anonymous merely because it is hashed.

6. **Regulatory language must be qualified.** A fraud/security Step-Up is not automatically equivalent to an ECOA adverse action.

7. **The strongest presentation is an adaptive-resilience demonstration:** show an attack bypassing a primitive detector, then demonstrate that independent relational/motor/topological evidence still identifies the coordinated swarm.

8. The proposed wildcard is an **active deception layer** using carefully controlled honeypot/dynamic UI signals, subject to accessibility and fairness safeguards.

---

# 1. RUTHLESS RED-TEAM STRESS TEST

## 1.1 Keystroke Digraph / Trigraph Defense

### Threat

An advanced autonomous typing model could sample timing values that resemble human distributions.

Therefore, a detector based only on:

- mean
- variance
- Gaussian jitter
- individual digraph latency

is vulnerable to distribution matching.

A sophisticated attacker could potentially reproduce the *marginal* statistics of human typing without reproducing the complete underlying behavioral process.

### Defensive upgrade

Instead of only storing:

- mean flight time
- variance
- digraph frequency

ShadowGram should derive a compact feature vector containing:

- digraph/trigraph timing statistics
- key/context-conditioned timing
- heavy-tail statistics
- entropy
- covariance between neighboring intervals
- transition-conditioned statistics
- session-to-session stability
- correlation with pointer behavior
- correlation with navigation behavior

For example, a candidate distribution can be tested as:

\[
H_0:D_{uv}\sim\operatorname{LogNorm}(\mu_{uv},\sigma^2_{uv})
\]

versus:

\[
H_A:D_{uv}\not\sim\operatorname{LogNorm}(\mu_{uv},\sigma^2_{uv})
\]

However, ShadowGram should **not assume that every human digraph is log-normal**.

The appropriate approach is empirical calibration against ShadowGram's legitimate-user population.

### Core defensive principle

An attacker may reproduce:

\[
P(\Delta t)
\]

but reproducing the entire joint structure is harder:

\[
P(
\Delta t,
\text{context},
\text{trajectory},
\text{navigation},
\text{session}
)
\]

Therefore ShadowGram should detect:

> **cross-signal behavioral consistency**

rather than simply asking:

> "Does this timing histogram look human?"

---

# 2. GRAPH ADVERSARIAL STRESS TEST

## 2.1 Potential Attack Classes

A sophisticated adversary could attempt:

- synthetic bridge nodes
- plausible edges toward legitimate users
- noisy connections intended to dilute communities
- topology manipulation
- temporal staggering
- heterogeneous browser/device fingerprints
- edge-weight perturbation
- coordinated low-amplitude behavioral changes

Recent research on adversarial graph attacks demonstrates that graph-based bot detectors can be targeted through constrained structural manipulation.

One cited example is:

**Mukherjee et al., "Optimal Transport-Guided Adversarial Attacks on Graph Neural Network-Based Bot Detection," ICML 2026 / arXiv:2602.00318.**

The important lesson for ShadowGram is:

> A graph detector must assume that an attacker can manipulate observable topology.

---

# 3. GRAPH COUNTER-COUNTERMEASURES

## 3.1 Motif Statistics

For suspicious neighborhoods, calculate small graph motifs:

- triangles
- wedges
- short cycles
- rectangles
- local clustering

Then compare the observed motif distribution against calibrated null models.

This gives ShadowGram another structural axis beyond community modularity.

---

## 3.2 Degree-Preserving Null Models

The Maslov-Sneppen approach can be used to generate randomized graphs preserving degree structure.

The basic idea:

\[
G_0 \rightarrow
G_1,G_2,\ldots,G_N
\]

where each randomized graph preserves the relevant degree sequence.

Then calculate a statistic \(T(G)\).

An empirical p-value can be estimated as:

\[
p=
\frac{
1+\sum_{i=1}^{N}
\mathbf{1}[T(G_i)\geq T(G_0)]
}{
N+1
}
\]

This is much more defensible than claiming that an observed cluster is "obviously fraudulent."

---

# 4. ADVERSARIAL FRAGILITY SCORE

A useful research feature is to estimate how much graph modification would be required before an anomalous subgraph becomes statistically ordinary.

Conceptually:

\[
F(G)=
\min_{\Delta G}
\left\{
|\Delta G|:
\operatorname{Anomaly}(G+\Delta G)<\tau
\right\}
\]

Interpretation:

- low \(F(G)\): anomaly is structurally fragile
- high \(F(G)\): anomaly is structurally persistent

This should be presented as an **additional robustness metric**, not as proof of malicious intent.

---

# 5. NODE2VEC VS DETERMINISTIC METHODS

## 5.1 Node2Vec

### Advantages

- intuitive
- captures higher-order neighborhood similarity
- useful for visual clustering
- easy to demonstrate visually

### Disadvantages

- stochastic random walks
- embedding stability depends on parameters
- repeated computation can cost latency
- UMAP adds another nonlinear/stochastic layer
- difficult to present as a clean deterministic forensic proof

Therefore:

> **Node2Vec is excellent for visualization, but should not be the only forensic evidence.**

---

# 6. LAPLACIAN EIGENMAPS

Given adjacency matrix:

\[
A
\]

and degree matrix:

\[
D
\]

the graph Laplacian is:

\[
L=D-A
\]

Solve:

\[
Ly=\lambda Dy
\]

The embedding can use the first nontrivial eigenvectors:

\[
y(v)=
[
\phi_2(v),
\phi_3(v),
\ldots,
\phi_k(v)
]
\]

### Advantages

- deterministic under fixed preprocessing
- mathematically transparent
- directly related to graph connectivity
- effective for relatively small in-memory graphs
- easy to explain to graph-theory judges

---

# 7. RECOMMENDED GRAPH REPRESENTATION

Instead of choosing one algorithm:

### Primary forensic representation

Use:

- weighted degree
- local clustering coefficient
- k-core level
- motif counts
- Laplacian eigenfeatures
- β₀ / β₁ filtration features
- community structure
- null-model statistics

### Secondary visualization

Use:

- Node2Vec \(d=8\)
- UMAP

This gives ShadowGram both:

**mathematical defensibility**

and

**visual impact.**

---

# 8. RANDOM WALK WITH RESTART

Random Walk with Restart can be expressed as:

\[
r=(1-\alpha)Pr+\alpha e_v
\]

or:

\[
(I-(1-\alpha)P)r=\alpha e_v
\]

where:

- \(P\) = transition matrix
- \(e_v\) = seed vector
- \(\alpha\) = restart probability

RWR provides a localized influence signature.

However, solving RWR independently for every node may be unnecessary.

### Recommendation

Use RWR selectively:

> suspicious node → suspicious neighborhood → RWR analysis

rather than applying it globally to every incoming applicant.

---

# 9. TOPOLOGICAL INVARIANTS

For a simple graph:

\[
\beta_0=
\text{number of connected components}
\]

and:

\[
\beta_1=E-V+\beta_0
\]

where:

- \(E\) = number of edges
- \(V\) = number of vertices

These can be computed extremely cheaply.

---

# 10. CRITICAL WARNING ABOUT BETTI NUMBERS

Do **not** tell judges:

> "High β₁ proves a fraud clique."

That is mathematically incorrect.

β₁ measures independent cycles.

A legitimate social, transaction, or communication graph can also contain many cycles.

The stronger formulation is:

> "ShadowGram measures the evolution of β₀ and β₁ across an edge-weight filtration and compares the resulting topological signature against calibrated legitimate and adversarial null models."

---

# 11. EDGE-WEIGHT FILTRATION

Define:

\[
G_\tau=
(V,
\{
(u,v):S(u,v)\geq\tau
\})
\]

Then sweep:

\[
\tau_1>
\tau_2>
\cdots>
\tau_n
\]

and monitor:

\[
\beta_0(\tau)
\]

and:

\[
\beta_1(\tau)
\]

This gives ShadowGram a **topological persistence signature**.

The key information is not merely:

\[
\beta_1=17
\]

but:

> At what similarity threshold do components merge, cycles appear, and suspicious structures persist?

---

# 12. PERSISTENT HOMOLOGY

Persistent homology generalizes this filtration concept.

For the hackathon:

### Do NOT

run expensive persistent homology on the entire graph continuously.

### DO

run lightweight topological analysis on:

- suspicious components
- high-risk neighborhoods
- candidate anomaly islands

This gives a strong mathematical story without destroying the latency budget.

---

# 13. BIOMECHANICAL INVARIANTS

## 13.1 Two-Thirds Power Law

A common formulation is:

\[
\omega\propto\kappa^{2/3}
\]

where:

- \(\omega\) = angular velocity
- \(\kappa\) = curvature

Equivalently:

\[
v\propto\kappa^{-1/3}
\]

This can be approximated from pointer trajectories.

### Browser-observable data

Possible features:

- \(x(t),y(t)\)
- velocity
- acceleration
- curvature
- angular velocity

### Confounders

- mouse vs touchpad
- touchscreens
- pointer acceleration
- browser sampling rate
- accessibility software
- high-DPI devices

Therefore:

> Do not claim this proves biological origin.

---

# 14. FITTS' LAW

Fitts' law:

\[
T=
a+b\log_2
\left(
\frac{D}{W}+1
\right)
\]

where:

- \(T\) = movement time
- \(D\) = distance to target
- \(W\) = target width
- \(a,b\) = fitted constants

ShadowGram can estimate whether repeated pointer actions demonstrate a plausible relationship between target difficulty and movement time.

Again:

> One movement is not evidence.

Repeated interaction data should be used.

---

# 15. MINIMUM JERK

The original dossier currently writes:

\[
J=
\frac{d^3x}{dt^3}
\]

That is **jerk**.

The classical minimum-jerk optimization is better expressed as:

\[
J_{\text{cost}}
=
\int_0^T
\left\|
\frac{d^3x}{dt^3}
\right\|^2dt
\]

The distinction is important.

### Better wording for judges

> "We measure jerk and minimum-jerk deviation metrics."

Do not imply that a particular jerk value uniquely identifies a human.

---

# 16. SIGMA-LOGNORMAL MOVEMENT MODEL

A simplified log-normal velocity pulse can be represented as:

\[
v(t)=
D
\frac{1}{
\sqrt{2\pi}\sigma(t-t_0)
}
\exp
\left[
-
\frac{
(\ln(t-t_0)-\mu)^2
}{
2\sigma^2
}
\right]
\]

This model can characterize movement subcomponents.

### Potential ShadowGram features

- number of velocity pulses
- pulse width
- pulse overlap
- peak velocity
- timing variability
- goodness-of-fit

This provides richer information than simply computing total movement distance.

---

# 17. CROSS-MODAL MOTOR CONSISTENCY

This is potentially the strongest Track 3 concept.

Instead of:

```text
Typing looks human → PASS
