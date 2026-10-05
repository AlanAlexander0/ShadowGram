# ShadowGram: Master Project Briefing for Deep Research Audit

**Project:** ShadowGram (HackAthena 2.0 • Track 04: Synthetic Identity & KYC / Track 05: Open Fraud)  
**Team:** Crafty Crew (Lead Architect: Pete, Frontend: Aiswarya, Red Team: Alan, Data/Compliance: Nihad/Ashlin)  
**Purpose:** Comprehensive context document to accompany the Deep Research Audit Prompt.

---

## 1. Executive Summary & Core Paradigm
* **The Problem:** In 2026, financial fraudsters deploy coordinated, autonomous multi-agent AI swarms (using Playwright, OpenClaw, and local LLMs). Each bot possesses a unique synthetic identity, an authentic-looking LLM bio, and a clean residential mobile 4G/5G proxy IP.
* **The Legacy Blindspot:** Traditional fraud systems (BioCatch, Sift, Arkose) inspect single accounts in isolation (*"Does Account A look fake?"*). Each synthetic bot passes individual heuristics easily.
* **The ShadowGram Innovation:** ShadowGram evaluates the **relational interaction topology** across concurrent sessions (*"Are multiple accounts moving in statistical lockstep?"*).
* **The Visual Core:** Rather than showing boring tables or static risk scores, ShadowGram renders a cinematic **3D WebGL Particle Graph (Three.js)**. Genuine users float as calm, isolated cyan/green stars; coordinated bot swarms light up as a glowing red cluster bound by laser-like relational edges.

---

## 2. The 4-Laptop Live Cyber-Range Setup

| Station | Assigned Role & Hardware | Operating System | Software Stack & Operational Role |
| :--- | :--- | :--- | :--- |
| **Station 1 (The Attacker)** | **Alan Alexander**<br>🎮 Gaming Laptop #1 (Multi-Core CPU) | Windows | Runs `swarm_runner.py` (Python Playwright). Dispatches **20 parallel Chromium browser contexts** simultaneously attacking Station 3 across the local hotspot. |
| **Station 2 (The Command Cockpit)** | **YOU (Pete)**<br>🎮 Gaming Laptop #2 (RTX 2050 4GB GPU, i5-13420H, 16GB RAM) | Linux (CachyOS) | **The Main Showpiece:**<br>• Hosts FastAPI (`uvicorn main:app --host 0.0.0.0 --port 8000`), SQLite, NetworkX, and ONNX 2D-CNN.<br>• Renders the **3D WebGL Three.js Particle Universe at 60 FPS** on the main presentation display/projector. |
| **Station 3 (The Target Portal)** | **Aiswarya**<br>💻 Normal Laptop #1 (Basic Office Specs, &lt;200MB RAM) | Windows | Runs **AthenaPay**, a lightweight Next.js instant micro-lending portal. **Handed to a live judge** to apply for an instant ₹10,000 loan as a real human. |
| **Station 4 (The Compliance Station)** | **Mohammed Nihad / Ashlin**<br>💻 Normal Laptop #2 (Basic Office Specs, &lt;300MB RAM) | Windows | Displays officer review queue. Triggers `[ 1-Click Blast-Radius Quarantine ]` and `[ Export SAR ]`. Generates a 2-page legal PDF via NVIDIA NIM API and ReportLab. |

---

## 3. Local Networking Architecture (Zero Cloud Dependency)
* **Access Point:** Google Pixel running stock Android mobile hotspot with Jio 5G/4G SIM (`192.168.43.0/24`).
* **Why Google Pixel:** Stock Android does not enforce AP client isolation, allowing all 4 laptops to ping and exchange local HTTP/WebSocket packets freely.
* **FastAPI Binding:** Laptop 2 binds Uvicorn to `--host 0.0.0.0 --port 8000` (exposing the API across the LAN at `http://192.168.43.2:8000`).
* **Zero Docker & Zero CI/CD:** Avoids Windows WSL2 virtualization bugs, NAT bridge network isolation, and RAM exhaustion. All software runs natively in Python `venv` and Node.js.
* **Cross-Platform Rules:** Mandatory use of `pathlib.Path` or `os.path.join`; mandatory acceptance of Windows Defender Firewall "Private Network" prompt.

---

## 4. The 5-Layer Interaction Physics Model
An edge $(u, v)$ is established between sessions if composite similarity $S_{\text{comp}}(u, v) \ge 0.78$ across at least three layers:

$$S_{\text{comp}}(u, v) = w_{\text{time}} S_{\text{time}} + w_{\text{nav}} S_{\text{nav}} + w_{\text{sem}} S_{\text{sem}} + w_{\text{kin}} S_{\text{kin}} + w_{\text{env}} S_{\text{env}}$$

1. **Temporal Rhythm ($S_{\text{time}}$):** Inter-arrival delta $\Delta t < 50\text{ms}$ between sequential form submissions across sessions.
2. **Navigation FSM ($S_{\text{nav}}$):** Longest Common Subsequence (LCS) sequence alignment score $\ge 0.85$ across DOM route transitions (`/auth` $\to$ `/kyc` $\to$ `/submit`).
3. **Kinetic Micro-Biometrics ($S_{\text{kin}}$):** Converts cursor coordinate streams $[x, y, t]$ into 128x128 frequency spectrograms. A lightweight **2D-CNN in ONNX Runtime** (<10ms CPU inference) detects absence of biological 8–12 Hz physiological tremor and flags piecewise mathematical Bézier jerk ($\frac{d^3x}{dt^3} \approx 0$).
4. **Semantic Embedding NLP ($S_{\text{sem}}$):** Local CPU model (`sentence-transformers/all-MiniLM-L6-v2`, 384-dim dense vectors, <15ms) evaluates cosine similarity between loan justifications ($\text{Cosine} \ge 0.88$).
5. **Environmental Entropy ($S_{\text{env}}$):** AudioContext oscillator decay curves, WebGL canvas render hashes, and clock drift entropy.

---

## 5. Graph Engine & Explainable Intelligence
* **Community Detection:** In-memory `networkx.Graph()` partitioned via **Newman-Girvan Louvain Modularity**:
  $$Q = \frac{1}{2m} \sum_{i,j} \left[ A_{ij} - \frac{k_i k_j}{2m} \right] \delta(c_i, c_j)$$
  Clusters with $Q > 0.60$ and node count $\ge 3$ are mathematically classified as coordinated syndicates ($P < 10^{-5}$).
* **The "Why Card" Modal:** Clicking any clustered node opens a dark liquid-glass modal displaying hard factual evidence:
  * Arrival synchronization: $\Delta t = 38\text{ms}$ ($Z\text{-score} = 4.82, P < 0.0001$).
  * Route sequence identity: $96\%$ LCS alignment.
  * Semantic vector similarity: $0.89$ cosine overlap.
* **1-Click Blast-Radius Quarantine:** Freezes the entire Louvain community with one click, neutralizing all 20 bot accounts simultaneously without touching genuine green nodes.
* **Automated Legal SAR PDF:** NVIDIA NIM API (Llama-3.3-70B) formats the raw graph metrics into formal Adverse Action Reason Codes complying with **ECOA Regulation B (12 CFR § 1002.9)**, compiled into a 2-page PDF via ReportLab in $<2$ seconds.

---

## 6. The 180-Second Live Pitch Choreography
* **0:00 – 0:45 (The Threat Hook):** Pete introduces the digital lending risk landscape. Aiswarya turns Laptop 3 to a **live judge** and invites them to apply for an instant ₹10,000 loan as a real human.
* **0:45 – 1:30 (The Live Swarm Attack):** Alan hits Enter on Laptop 1, launching 20 parallel Playwright bots. On Laptop 2's big screen, red laser-like connection lines snap across the bot swarm in real time in 3D WebGL space.
* **1:30 – 2:15 (The Differentiation):** Aiswarya highlights the judge's node on Laptop 2: glowing green, isolated, calm, and completely unaffected. Aiswarya clicks the red cluster $\to$ the "Why Card" modal pops open with mathematical proofs.
* **2:15 – 3:00 (The Legal Kill-Switch):** Nihad clicks `[ 1-Click Quarantine ]` on Laptop 4 $\to$ grey containment shields drop over the bots. Click `[ Export SAR ]` $\to$ downloads the official 2-page PDF dossier. Pete concludes with zero-cost architecture and opens Q&A.

---

## 7. Failsafe Architecture (Zero-Crash Guarantee)
* **Tier 1 (Normal Live):** Queries NVIDIA NIM API over local hotspot.
* **Tier 2 (Offline Cache):** Local `personas_cache.json` and pre-baked Python ReportLab template generate the SAR PDF instantly without internet.
* **Tier 3 (Emergency):** Prominent **`[ 🔥 Deploy Swarm Simulation ]`** button on Laptop 2 runs the entire 20-bot attack and 3D graph clustering completely in-memory in 3 seconds if local Wi-Fi drops.
