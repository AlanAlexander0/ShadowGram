# ShadowGram: Finalized Architecture, Design Tree & Comprehensive Audit Log
**Document Version:** 1.0 (Post-Grill Consensus)  
**Date:** October 3, 2026  
**Status:** Architecture Locked & Workshop Decisions Finalized  
**Target Event:** HackAthena 2.0 • Track 04 (Synthetic Identity & KYC) / Track 05 (Open Fraud)

---

## 1. Executive Summary & Design Consensus
Through an adversarial architectural audit and design-tree workshop, the ShadowGram system architecture has been fully resolved. The project pivots away from fragile black-box assumptions into a **deterministic, zero-cost, multi-device cyber-range demonstration** that operates 100% locally on CPU hardware without external cloud bills.

### Master Architecture Overview:
```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          LOCAL NETWORK TOPOLOGY (LAN)                       │
├──────────────────────────────────────┬──────────────────────────────────────┤
│ LAPTOP 1: RED TEAM SWARM RUNNER      │ LAPTOP 3: ATHENAPAY MICRO-LENDING APP│
│ • Python Playwright Swarm Engine     │ • Next.js / HTML Instant Loan Portal │
│ • NVIDIA NIM API (Llama-3.3-70B)     │ • 3-Step KYC & Loan Application      │
│ • Dispatches 20 AI Synthetic Personas│ • Used live by JUDGE or real human   │
│ • Simulates Residential Proxy Egress │ • Embedded 50ms JS Telemetry Hooks   │
├──────────────────────────────────────┴──────────────────────────────────────┤
│                                     │                                       │
│          Sends Bot Telemetry        │        Sends Human Telemetry          │
│          ───────────────────────►   │   ◄─────────────────────────          │
│                                     ▼                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│ LAPTOP 2: SHADOWGRAM CORE COMMAND COCKPIT (The Blue Team Defense)           │
│ • Ingestion Engine: FastAPI (Python 3.11) + WebSockets                      │
│ • Database: SQLite + SQLAlchemy (`shadowgram.db`)                           │
│ • Kinetic Classifier: 2D-CNN Spectrogram Model (<10ms ONNX Runtime CPU)     │
│ • NLP Embeddings: `all-MiniLM-L6-v2` (Local 384-dim CPU Inference)          │
│ • Graph Engine: NetworkX + Louvain Modularity Community Detection           │
│ • Visualization: 3D WebGL Glowing Force Graph with 2D Toggle                │
│ • 1-Click Simulation Fallback: Ingests mock swarm if Wi-Fi / time fails     │
├─────────────────────────────────────────────────────────────────────────────┤
│ LAPTOP 4: COMPLIANCE OFFICER TRIAGE & REPORTING                             │
│ • Live Forensic "Why Card" Dashboard: Explains Covariance & Metric Overlap   │
│ • 1-Click Blast-Radius Quarantine: Blocks 20 bots without human disruption  │
│ • CFPB-Compliant SAR Generator: NVIDIA NIM auto-compiles 2-page PDF Dossier │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Design Tree Decision Log (Consensus Outcomes)

| Decision Branch | Chosen Architecture | Rationale & Strategic Value |
| :--- | :--- | :--- |
| **1. Live Demo Interaction** | **Hybrid Dual Mode** | Real interactive loan portal on Laptop 3 for judges to test personally, backed by a 1-click automated simulation fallback button on Laptop 2 if venue Wi-Fi or time is restricted. |
| **2. Red-Team Swarm Runner** | **Python Playwright Engine + NVIDIA NIM** | Clean, 100% controllable script. Fetches dynamic persona text from free NVIDIA NIM APIs (Llama-3.3-70B) and drives real headless browser instances over LAN. Avoids heavy OpenClaw gateway dependencies. |
| **3. Kinetic Trajectory Layer** | **Lightweight 2D-CNN (ONNX) + Live Spectrogram Canvas** | Converts mouse coordinates $(x,y,t)$ into a 2D kinematic heatmap/spectrogram image. Runs sub-10ms CPU inference via ONNX Runtime and displays the live visual spectrogram on the dashboard. |
| **4. Relationship Graph UI** | **3D WebGL Force Graph + 2D Fallback Toggle** | Cinematic glowing 3D particle universe (Three.js / WebGL) with rotating camera, plus a 1-click toggle to switch to a 2D topological map if hardware graphics lag. |
| **5. The "Why Layer" Delivery** | **Interactive "Why Card" + 1-Click SAR PDF Exporter** | Frosted-glass on-screen evidence breakdown displaying exact covariance metrics, with a button that compiles and downloads an official 2-page CFPB-compliant PDF dossier formatted by NVIDIA NIM. |
| **6. Target FinTech Scenario** | **Instant Micro-Lending Portal ("AthenaPay")** | A 3-step loan application (KYC details, loan reason, bank payout) that mirrors the #1 real-world synthetic identity threat landscape and directly targets Track 4. |

---

## 3. Tool Separation of Concerns: OpenClaw vs. NVIDIA NIM

* **OpenClaw (Conceptual Blueprint / Attacker Hands):**  
  Represents the threat model: autonomous browser-driving agents. We extract its core headless browser automation pattern into our lightweight Python Playwright script. It acts as the **motor system** that executes clicks, fills fields, and triggers DOM events.
* **NVIDIA NIM Free API (The AI Brain & Legal Scribe):**  
  Uses free developer keys ($4 \times 40\text{ req/min}$):
  1. *Red-Team Side:* Generates 20 distinct persona backgrounds, varying names, and plausible loan reasons.
  2. *Blue-Team Side:* Takes the raw cluster telemetry and auto-drafts a formal, legal Suspicious Activity Report (SAR) PDF for compliance officers.

---

## 4. Adversarial Loophole Analysis & Built-In Defenses

```
┌─────────────────────────────────┬─────────────────────────────────┬─────────────────────────────────┐
│ Attack Loophole                 │ Why Legacy Systems Fail         │ ShadowGram Defense Mechanism    │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ 1. Flash Mob Spike              │ Single-account models panic on  │ Multi-signal convergence        │
│    (500 real humans rush in at  │ sudden traffic bursts; flag high│ (P < 10⁻⁵): Genuine humans have │
│    the same minute via an ad).  │ velocity as a bot attack.       │ chaotic micro-tremors and unique│
│                                 │                                 │ text; never form 3-layer edges. │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ 2. Manual Human Click-Farm      │ Biological mouse movements pass │ FSM sequence speed and token    │
│    (Sweatshop workers filling   │ kinetic checks.                 │ analysis: Workers exhibit zero  │
│    forms manually for low pay). │                                 │ exploration, extreme copy-paste │
│                                 │                                 │ frequency (30%), & fast submits.│
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ 3. Client Telemetry Tampering   │ Hackers block or spoof JS       │ Server-side ingress timing (Δt) │
│    (Disabling `telemetry.js`).  │ payloads.                       │ cannot be spoofed; fail-closed  │
│                                 │                                 │ HMAC token gate on loan submit. │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ 4. O(N²) Graph Scalability      │ Pairwise comparison freezes     │ Locality-Sensitive Hashing (LSH)│
│    (10,000 active sessions =    │ CPU hardware.                   │ and MinHash bucket pruning drops│
│    50,000,000 edge checks).     │                                 │ computation to O(N log N).      │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ 5. Low-and-Slow Swarms          │ In-memory 1-hour sliding graph  │ Two-tier architecture: In-memory│
│    (1 bot per day over weeks).  │ misses accounts across days.    │ sliding graph (bursts) + 30-day │
│                                 │                                 │ persistent HNSW vector store.   │
└─────────────────────────────────┴─────────────────────────────────┴─────────────────────────────────┘
```

---

## 5. Team Roles & Mentorship Execution Plan

1. **Role 1 (You): Principal Systems Architect & Graph Engine Lead**
   * *Tasks:* FastAPI master orchestration, NetworkX graph logic, Louvain modularity algorithm, composite edge formula ($S_{\text{comp}}$), and leading technical defense during judge Q&A.
2. **Role 2 (Aiswarya): Visual Command Center & 3D WebGL Lead**
   * *Tasks:* Next.js 14 dashboard implementation, 3D WebGL force-directed graph (`react-force-graph-3d`), dark liquid-glass UI styling, and the "Why Card" modal.
3. **Role 3 (Teammate 3): Red-Team Swarm & Telemetry Lead**
   * *Tasks:* Laptop 1 Playwright swarm runner script, dynamic persona injection, and client-side JavaScript telemetry hooks on Laptop 3 (`keydown`, `pointerdown`, route changes).
4. **Role 4 (Teammate 4): Data Engineering, NVIDIA API & Compliance PDF Lead**
   * *Tasks:* SQLite database schema, setting up the 4 NVIDIA NIM API keys (Llama-3.3-70B), and Python `ReportLab` script to compile the 2-page Suspicious Activity Report (SAR) PDF.

---

## 6. The 3-Minute Live Hackathon Presentation Script

* **Minute 1: The Macro Problem & The Judge Invitation (Laptops 2 & 3)**  
  *"Judges, in 2026, botnets don't look like bots. Attackers deploy autonomous AI agent swarms where each account has a unique name, a clean home IP, and an LLM-written bio. To prove how traditional security fails, we invite you to step up to Laptop 3 and apply for a ₹10,000 micro-loan as an authentic human."*
* **Minute 2: The Attack & The 3D Graph Snap (Laptops 1 & 2)**  
  *Teammate 3 launches 20 Playwright agents from Laptop 1.*  
  *"While our judge applies, a 20-agent syndicate attacks the exact same portal. Notice Laptop 2: The judge’s account appears as an isolated, stable blue node. But seconds later, the 20 bot accounts light up, their trajectory spectrograms flag synthetic Bézier curves, and bright red laser edges snap between them in 3D space. Louvain clustering isolates the syndicate with 98.4% confidence."*
* **Minute 3: The "Why Layer" & Legal Containment (Laptops 4 & 2)**  
  *Teammate 4 clicks the cluster on Laptop 4.*  
  *"Under CFPB Circular 2023-03, banks cannot ban accounts on an opaque '82% risk score'. ShadowGram opens the 'Why Card' showing exact factual proof: 96% state-machine path overlap, 38ms ingress arrival synchronization, and 0.89 semantic intent overlap. We click [QUARANTINE]: The 20 bots are locked instantly, the judge on Laptop 3 continues browsing completely unaffected, and ShadowGram prints a formal 2-page Suspicious Activity Report PDF ready for regulators."*
