# ShadowGram: Phase 2 Deep Research, Architectural Audit & Innovation Dossier

**Document Code:** `SG-PHASE2-DEEP-RESEARCH-01`  
**Classification:** Master Context, Architecture Audit, Threat Model & Phase 2 Innovation Blueprint  
**Target:** OpenAI ChatGPT Deep Research / Academic Peer Review / Elite Red-Team Panel  
**Date:** October 6, 2026  
**Project:** ShadowGram (Antigravity Athena Cyber Defense Gateway)  
**Authors:** Crafty Crew (Pete - Principal Architect & Backend, Alan - Swarm Red Team, Aiswarya - Frontend & Borrower Portal, Nihad & Ashlin - Compliance & SAR)

---

## 1. Executive Context & Mission

**ShadowGram** is the first in-flight, behavioral graph-forensic gateway designed to defend digital micro-lending platforms and fintechs against autonomous, coordinated AI agent swarms executing synthetic identity fraud and Denial-of-Wallet (DoW) attacks.

We are competing in a high-stakes hackathon/fintech cybersecurity competition. We have successfully passed the initial judging round, where our live 4-laptop cyber range and mathematical foundations were demonstrated.

We are now preparing for the **Final Judging Round**. We need to:
1. **Stress-test and audit our existing Phase 1 architecture and mathematical proofs.**
2. **Ruthlessly challenge our proposed Phase 2 roadmap.**
3. **Discover novel, bleeding-edge graph algorithmic, biometric, and fintech innovations** that will amaze senior bank CISOs, graph theory professors, and regulatory judges.

---

## 2. Phase 1 Ground Truth: What We Have Built, Tested & Verified

Our system runs live on a distributed **4-laptop mobile hotspot LAN (`0.0.0.0:8000`)**:
- **Laptop 1 (Alan - Red Team):** Playwright automated swarm (`swarm_runner.py`) running headless Chromium browsers executing human-mimicking Bézier mouse trajectories and Gaussian keystroke jitter using 20 pre-cached Indian identities.
- **Laptop 2 (Pete - Backend & Graph Engine):** Central Fedora Linux server running FastAPI, SQLite SQLAlchemy, Leiden community detection, B-GUARD graph repair, and the Two-Key defense engine.
- **Laptop 3 (Aiswarya - Borrower Portal & Cockpit):** Honest borrower application (`AthenaPay`) and live 3D command dashboard with 1-Rupee UPI Step-Up challenge.
- **Laptop 4 (Nihad & Ashlin - Compliance):** Bank-grade 2-page Suspicious Activity Report (SAR) PDF generator compliant with 12 CFR § 1002.9 and RBI guidelines.

### 2.1 The Two-Key Defense Architecture

#### Key 1: Single-Session Invariant Fast Filter (<5ms latency)
Evaluated at Form Step 2 (before any fee-bearing verification APIs are called):
- **Click-Dwell Variance:**
  $$\mu_{\text{dwell}} = \frac{1}{N}\sum_{i=1}^N d_i, \quad \sigma^2_{\text{dwell}} = \frac{1}{N}\sum_{i=1}^N (d_i - \mu_{\text{dwell}})^2$$
  *Biological Invariant:* Human muscle contraction cannot release a switch with sub-millisecond precision. If $\sigma^2_{\text{dwell}} < 15.0\text{ ms}^2$ or instantaneous $d_i \le 2.0\text{ ms}$ (programmatic `.click()`), the session trips `flagged_automation`.
- **Pre-Click Pointer Density:**
  $$k_{\text{hover}} = \sum_{t = t_{\text{click}}-500\text{ms}}^{t_{\text{click}}} \mathbf{1}(\text{event} == \text{pointermove})$$
  Bots issuing headless click dispatches have $k_{\text{hover}} = 0$.

#### Key 2: The 5-Layer Relational Multiplex Physics Tensor
When advanced bots randomize delays and generate smooth Bézier curves to bypass Key 1, Key 2 calculates pairwise edge similarities across all incoming applicants:
$$\mathbf{S}(u,v) = \sum_{m=1}^5 w_m \cdot S_m(u,v), \quad \vec{w} = [0.25, 0.25, 0.25, 0.15, 0.10]$$

1. **Layer 1: Arrival Timing ($S_{\text{time}}$) — Iannucci Continuous Exponential Decay Kernel:**
   $$S_{\text{time}}(u,v) = \begin{cases} 
   0.99 & \Delta t < 0.15\text{s} \\
   0.92 - (0.06 \cdot \Delta t) & 0.15\text{s} \le \Delta t < 1.50\text{s} \\
   0.82 - (0.05 \cdot \Delta t) & 1.50\text{s} \le \Delta t < 4.00\text{s} \\
   \exp\left(-\frac{\Delta t}{\tau}\right) & \Delta t \ge 4.00\text{s} \quad (\tau = 10.0\text{s})
   \end{cases}$$
2. **Layer 2: Route FSM Sequence Matching ($S_{\text{nav}}$):**
   $$S_{\text{nav}}(u,v) = \left( 0.5 \cdot \frac{|\mathcal{R}_u \cap \mathcal{R}_v|}{|\mathcal{R}_u \cup \mathcal{R}_v|} + 0.5 \cdot \text{Match}_{\text{order}}(\mathcal{R}_u, \mathcal{R}_v) \right) \cdot \delta_{\text{depth}}$$
3. **Layer 3: Neuromotor Interaction Kinetics ($S_{\text{kin}}$):**
   Flash & Hogan Minimum-Jerk derivative:
   $$J = \frac{d^3\mathbf{x}}{dt^3} = \frac{d\mathbf{a}}{dt}$$
   Discriminates piecewise-linear Bézier curves ($\bar{J} > 0.70$ or macros with $\bar{J} < 0.05$) from human physiological micro-tremor ($8-12\text{ Hz}$).
4. **Layer 4: Dense Local Semantic Intent Cosine ($S_{\text{sem}}$):**
   Cosine similarity of local TF-IDF / sentence embeddings on loan purpose statements:
   $$S_{\text{sem}}(u,v) = \cos(\vec{e}_u, \vec{e}_v) = \frac{\vec{e}_u \cdot \vec{e}_v}{\|\vec{e}_u\|_2 \|\vec{e}_v\|_2}$$
5. **Layer 5: Client Hardware Environment Entropy ($S_{\text{env}}$):**
   WebGL GPU hash, screen resolution, and Canvas fingerprint hash match.

#### The 3-Layer Orthogonal Sparsification Filter (Zero False Positives on Shared Wi-Fi)
An edge is formed between applicant $u$ and applicant $v$ **if and only if**:
$$\mathbf{S}(u,v) \ge 0.70 \quad \mathbf{AND} \quad \sum_{m=1}^5 \mathbf{1}(S_m(u,v) \ge 0.70) \ge 3$$
*Mathematical Proof:* For two unrelated students on the same college Wi-Fi:
$$P(\ge 3 \text{ layers converge by chance}) < 0.00032$$
This mathematically prevents viral traffic or shared residential IP proxies from generating false positive edges.

#### B-GUARD Adversarial Boundary Graph Repair
Defeats synthetic bridge node injection attacks (BOCLOAK, ICML 2026) where fraud syndicates introduce dummy accounts to dilute Newman-Girvan Modularity $Q$:
$$C_B(v) = \sum_{s \ne v \ne t} \frac{\sigma_{st}(v)}{\sigma_{st}}$$
If $C_B(v) > 0.35$ and the node has $<3$ converged layers with neighbors, its incident edges are down-weighted by 50% prior to clustering.

#### Community Detection & Legal Audit Null Model
- **Leiden Algorithm (Traag et al., 2019):** Partitions graph into communities, guaranteeing well-connected, non-empty clusters ($Q = 0.7241$).
- **Maslov-Sneppen Permutation Null Model ($p < 0.001$):** Shuffles 1,000 degree-preserving random graphs to prove non-random coordination for Equal Credit Opportunity Act (ECOA) Reg B (12 CFR § 1002.9) statutory compliance.

#### Denial-of-Wallet (DoW) Economic Quantification
Pre-KYC interception at Form Step 2 aborts the workflow before fee-bearing vendor verification APIs are triggered:
$$\text{Cost}_{\text{KYC}} = ₹3.00\text{ (Aadhaar)} + ₹2.00\text{ (PAN)} + ₹6.00\text{ (Liveness)} + ₹50.00\text{ (CIBIL Pull)} = \mathbf{₹61.00\text{ INR / Bot}}$$
Stopping Alan's 20-bot attack saved **₹1,220.00 INR** instantly (saving ₹61 Lakh INR on a 100,000-bot syndicate).

---

## 3. Initial Judge Feedback & Challenges

In Round 1, the judges raised critical questions that we addressed and need to strengthen further:
1. **"You used the Leiden algorithm; that is existing literature. What did YOU innovate?"**
   * *Our Answer:* In digital lending, applicants have NO EDGES (each bot has a clean IP, unique name, separate browser). Leiden cannot run on disconnected nodes. We innovated the 5-layer multiplex physics tensor that *generates* the edges, the 3-layer orthogonal sparsification gate, B-GUARD boundary repair, the Maslov-Sneppen null model test, and Pre-KYC DoW economics.
2. **"How do you handle shared IP addresses (CGNAT / University Wi-Fi / Starbucks)?"**
   * *Our Answer:* We do not rely on IP addresses. IP is not even one of our 5 primary tensor layers. Edges require kinetic, semantic, route, and timing convergence across $\ge 3$ orthogonal dimensions.
3. **"Is your system legal under US and Indian adverse action regulations?"**
   * *Our Answer:* Yes, ECOA Regulation B (12 CFR § 1002.9) requires specific, verifiable reasons for credit denial. Our "Why Card" and automated SAR PDF cite empirical mathematical invariants ($Q \ge 0.60$, $p < 0.001$, jerk variance), avoiding illegal black-box neural scoring. Furthermore, we provide a 1-Rupee reversible UPI Step-Up challenge compliant with EU AI Act Art. 13 & 14 human oversight.

---

## 4. Proposed Phase 2 Roadmap (The 6 Enhancement Tracks)

With time remaining before the final judging round, we outlined 6 potential upgrades:

### Track 1: Full 3D Force-Directed Gravitational Orbit Engine (Three.js)
- **Concept:** Upgrade Cockpit 2D Canvas to a true Three.js WebGL 3D Sphere with OrbitControls.
- **Physics:** Implement Barnes-Hut gravitational attraction so incoming bot swarm nodes physically pull toward each other and collapse into a dense, rotating 3D red cluster with glowing volumetric bloom.

### Track 2: Node2Vec / GNN Relational Embeddings & UMAP 2D Projection
- **Concept:** Run an in-memory random-walk graph embedding ($d=8$) over `self.graph` and project via UMAP.
- **Visualization:** Show a 2D scatter plot in the Why Card modal proving the fraud syndicate forms an isolated, hyper-dense anomaly island in relational embedding space, while genuine borrowers scatter widely.

### Track 3: Biometric Keystroke Digraph & Trigraph Transition Matrix
- **Concept:** Track inter-key flight times for frequent digraphs (`th`, `er`, `in`, `an`, `he`, `nd`) in `telemetry.js`.
- **The Biological Invariant:** Humans have muscle memory (e.g., `th` is 40% faster than `qz`).
- **The Bot Vulnerability:** Automated bots draw typing delays from a global Gaussian or uniform distribution, resulting in a flat digraph transition curve.
- **Visualization:** Live digraph latency matrix heatmap in the Cockpit sidebar.

### Track 4: Interactive Modularity & Sensitivity Slider
- **Concept:** Add a live slider `[ Detection Threshold θ: 0.50 ────●── 0.90 ]` on the Cockpit header.
- **Dynamic API:** Triggers `/api/repartition?threshold=X` over WebSockets so judges can drag the slider and watch the graph re-partition live, illustrating boundary repair and cluster isolation in real time.

### Track 5: Account Aggregator (AA) Sandbox Simulation Rail
- **Concept:** Integrate India's RBI-regulated Account Aggregator (Setu / OneMoney) framework into `athenapay_portal.html` alongside the 1-Rupee UPI challenge.
- **Value:** Demonstrates instant paperless financial consent recovery for flagged borrowers.

### Track 6: Tactical Audio-Visual Cyber Defense Alerts (Web Audio API)
- **Concept:** Zero-dependency browser synthesized audio:
  - Low ambient radar hum during idle monitoring.
  - Tactical alert siren when Alan's bot swarm triggers $Q \ge 0.60$.
  - Harmonic resolution chime when Step-Up challenge clears an honest applicant.

---

## 5. Critical Questions & Dilemmas for Deep Research

We want ChatGPT Deep Research to thoroughly investigate and answer:

1. **Adversarial Stress-Testing of Phase 2:**
   - How can a sophisticated red-team attacker evade our Phase 2 enhancements? Specifically:
     - How could a swarm evade the **Keystroke Digraph Matrix** (e.g. using n-gram delay sampling dictionaries)?
     - How could an attacker manipulate **Node2Vec random walks** or GNN embeddings to blend into the human cluster (e.g. node injection or topology obfuscation)?
     - What counter-countermeasures should ShadowGram implement to stay resilient against adaptive adversaries?
2. **Algorithmic Evaluation & Recommendations:**
   - Is **Node2Vec** the best choice for real-time graph embeddings in a sub-50ms cyber gateway, or is an inductive method (e.g., GraphSAGE, simple Spectral Graph Wavelets, or Laplacian Eigenmaps) faster and more defensible?
   - Can we extract higher-order topological features (e.g., Persistent Homology, Betti numbers $\beta_0, \beta_1$, or Simplicial Complexes) to prove multi-agent swarm coordination?
3. **Biomechanical & Kinetic Invariants:**
   - Beyond minimum-jerk ($d^3x/dt^3$), what other motor control invariants from neuroscience literature (e.g., Fitts' Law speed-accuracy tradeoff, Viviani's Two-Thirds Power Law for 2D trajectories, log-normal velocity profiles) can be captured in client JavaScript without introducing battery or CPU lag?
4. **Fintech Production Realism & Regulatory Defensibility:**
   - How does capturing keystroke timing interact with privacy laws (India's Digital Personal Data Protection Act 2023, GDPR, CCPA)? How can we prove to a compliance judge that timing intervals do NOT capture key content (preventing keylogging liability)?
   - Under RBI's Digital Lending Guidelines (2025 Master Directions), what are the exact mandatory disclosures required when an algorithmic gateway flags an applicant for Step-Up verification?
5. **Hackathon Winning Strategy & Prioritization:**
   - Given a limited development window before final judging, rank the 6 tracks by **Judge Impact vs. Implementation Feasibility**.
   - Which specific track will deliver the biggest "jaw-drop" moment for technical and banking judges?
   - What additional "wildcard" feature (not in our 6 tracks) could elevate this project to an undisputed 1st-place victory?

---
*End of Dossier.*
