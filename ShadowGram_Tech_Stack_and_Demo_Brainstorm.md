# ShadowGram: Tech Stack, Multi-Device Demo & Team Strategy Brainstorm
**Document Status:** Working Draft & Brainstorming Blueprint (Iterative & Modular)

---

## 1. Executive Vision: The "Showstopper" Hackathon Strategy
The goal is to deliver an end-to-end cyber-forensics platform that is:
1. **Zero Cost / Free Tier:** Exploiting local CPU compute and free developer tiers (e.g., NVIDIA NIM free API keys) with zero cloud hosting bills.
2. **Visually Jaw-Dropping:** Moving away from static slides to a **live 4-laptop multi-device cyber-range demonstration** on a local Wi-Fi hotspot.
3. **Technically Above-Grade:** Utilizing real 3D WebGL graphs, kinematic trajectory classifiers, local sentence embeddings, and live agentic attack runners (OpenClaw/Playwright).
4. **Pedagogically Empowering:** Structuring tasks so the technical lead can architect the system while teaching and leveling up the three teammates with high-impact, achievable modules.

---

## 2. Tech Stack Evaluation & Compatibility Matrix

Here is an objective analysis of the candidate technologies, filtering what provides high leverage versus what should be discarded:

| Technology / Keyword | Status | Where It Fits in ShadowGram | Verdict / Rationale |
| :--- | :--- | :--- | :--- |
| **FastAPI (Python)** | **CORE (Adopt)** | Central ingestion engine, WebSocket live telemetry streaming, REST endpoints. | **Essential:** Sub-10ms response time, async event handling, zero cost. |
| **SQLite + SQLAlchemy** | **CORE (Adopt)** | Single-file database (`shadowgram.db`) storing sessions, vectors, and cluster logs. | **Essential:** Zero configuration, zero server management, portable across laptops. |
| **Sentence-Transformers (`all-MiniLM-L6-v2`)** | **CORE (Adopt)** | Converts user loan text / profile bios into 384-dimensional dense vectors on CPU. | **Essential:** 100% offline, runs on local CPU in <80ms, no API rate limits. |
| **NetworkX + Louvain** | **CORE (Adopt)** | Constructs the dynamic account graph and isolates clusters via modularity optimization. | **Essential:** Mathematical backbone of the relational paradigm. |
| **Next.js 14 + Tailwind CSS + Framer Motion** | **CORE (Adopt)** | The cyber-forensics command cockpit with dark liquid-glass styling. | **Essential:** Matches Aiswarya's UI blueprint with fast rendering. |
| **3D WebGL Graph (`react-force-graph-3d`)** | **SHOWSTOPPER (Adopt)** | Renders the account universe in 3D space with glowing red syndicate clusters. | **High Leverage:** Massive visual upgrade over flat 2D network graphs. |
| **NVIDIA NIM Free APIs (Llama-3.3-70B / Nemotron)** | **UPGRADE (Adopt)** | 4 free keys $\times$ 40 req/min. Used to: (1) auto-generate diverse bot bios, and (2) compile the final SAR PDF legal report. | **High Leverage:** Free, unlimited LLM horsepower without paying OpenAI. |
| **2D-CNN / Trajectory Classifier** | **FEATURE (Adopt)** | Converts mouse $(x, y, t)$ coordinates into a 128x128 trajectory image/spectrogram to detect Bézier math. | **High Leverage:** Visual proof on screen of why synthetic cursor paths fail. |
| **OpenClaw / Playwright** | **RED TEAM (Adopt)** | Headless browser agent swarm runner executing live attacks from Laptop 1. | **High Leverage:** Shows real-world agentic automation live. |
| **Traditional Heavy CNNs (ResNet-50 for Images)** | **DISCARD** | Not needed unless testing fake passport/KYC document deepfakes. | **Discard:** Heavy training overhead; mouse trajectory 2D-CNN only needs a tiny MobileNet/custom CNN. |
| **Cloud Postgres / Docker / Kubernetes** | **DISCARD** | Overcomplicates a local hackathon demo; risk of networking failures on venue Wi-Fi. | **Discard:** Keep everything local via SQLite and localhost/LAN IPs. |

---

## 3. The 4-Laptop Live Cyber-Range Architecture

Instead of running a simulation on a single screen, the team deploys a **live Red-Team vs. Blue-Team cyber-range** connected over a local mobile hotspot / Wi-Fi network:

```
                    ┌────────────────────────────────────────┐
                    │      LOCAL WI-FI / HOTSPOT (LAN)       │
                    └───────────────────┬────────────────────┘
                                        │
        ┌───────────────────────────────┼───────────────────────────────┐
        │                               │                               │
        ▼                               ▼                               ▼
┌───────────────────┐       ┌───────────────────────┐       ┌───────────────────┐
│ LAPTOP 1: RED TEAM│       │   LAPTOP 2: DEFENSE   │       │ LAPTOP 3: THE APP │
│ (The Attacker)    │       │   (ShadowGram Server) │       │ (FinTech Portal)  │
├───────────────────┤       ├───────────────────────┤       ├───────────────────┤
│ • OpenClaw /      │       │ • FastAPI Backend     │       │ • Dummy Loan /    │
│   Playwright      │       │ • SQLite Database     │       │   KYC Web App     │
│ • Launches 20 AI  │       │ • 3D Force Graph UI   │       │ • Used by:        │
│   synthetic agents│       │ • Louvain Clustering  │       │   LIVE JUDGE or   │
│ • Simulates       │       │ • Kinetic CNN Engine  │       │   honest human    │
│   residential IPs │       │ • SAR PDF Generator   │       │ • Shows genuine   │
│ • Runs attack     │       │ • Displayed on big    │       │   user behavior   │
│   scripts         │       │   screen / projector  │       │   in real-time    │
└─────────┬─────────┘       └───────────▲───────────┘       └─────────┬─────────┘
          │                             │                             │
          │     Sends Bot Telemetry     │     Sends Human Telemetry   │
          └────────────────────────────►┴◄────────────────────────────┘
                                        ▲
                                        │
                                        │ Live Alerts & Evidence Review
                            ┌───────────┴───────────┐
                            │ LAPTOP 4: COMPLIANCE  │
                            │ (Analyst Triage / SAR)│
                            ├───────────────────────┤
                            │ • Officer Triage Queue│
                            │ • "Why Card" Review   │
                            │ • 1-Click Quarantine  │
                            │ • Mobile / Tablet or  │
                            │   Secondary Human User│
                            └───────────────────────┘
```

### The Live 3-Minute Demo Flow for Judges:
1. **The Invitation:** You invite a judge to step up to **Laptop 3** and apply for a quick micro-loan as a genuine human (moving the mouse, filling their own details).
2. **The Attack:** Simultaneously, on **Laptop 1**, your Red-Team teammate clicks `[Launch 20 OpenClaw Agents]`. Twenty headless browser sessions hit Laptop 3's portal in parallel with AI-generated personas.
3. **The Defense Cockpit (Laptop 2):**
   * The judge's account appears as an isolated, stable **green/blue node**.
   * The 20 bot accounts light up across the screen, their kinetic spectrograms show synthetic Bézier curves, and **red dynamic edges snap between them**.
   * Louvain clustering highlights the entire 20-node syndicate in bright crimson.
4. **The Proof & Containment (Laptop 4 or Laptop 2):**
   * You click the cluster to reveal the plain-English **"Why Card"** showing the 96% path overlap and synchronized arrivals.
   * You click **`[Quarantine Cluster]`**: The 20 bots are blocked instantly, while the judge on Laptop 3 continues browsing completely unaffected!
   * You click **`[Download SAR]`**: It prints an official legal dossier generated via NVIDIA API.

---

## 4. Team Role Distribution & Mentorship Strategy

To allow the technical lead to build at an advanced level while teaching and giving distinct, high-impact responsibilities to the other three team members:

### Role 1: Principal Systems Architect & Graph Engine Lead (You)
* **Core Responsibilities:**
  * System architecture and end-to-end pipeline integration.
  * Graph modeling in NetworkX: composite edge formulation ($S_{\text{comp}}$) and Louvain community detection.
  * Mathematical proofs and judge defense lead during Q&A.
  * Mentoring teammates on their respective modules.

### Role 2: Visual Command Center & Frontend Lead (Aiswarya)
* **Core Responsibilities:**
  * Building the Next.js 14 dashboard based on her `shadowgram-template by ais.md` specification.
  * Implementing the **3D WebGL Force-Directed Graph** (`react-force-graph-3d`) and dark liquid-glass styling.
  * Building the interactive modals: the **"Why Are These Accounts Linked?"** investigation card and the quarantine shockwave animation.
* **Skill Growth:** Next.js 14, Tailwind CSS, 3D WebGL rendering, component state management.

### Role 3: Red-Team Swarm Simulation & Telemetry Lead (Team Member 3)
* **Core Responsibilities:**
  * Operating **Laptop 1** (The Attacker Station).
  * Writing the browser automation scripts using Playwright / OpenClaw scripts to simulate 20 parallel agent accounts.
  * Integrating client-side JavaScript telemetry hooks (`keydown`, `pointerdown`, route changes) on Laptop 3.
* **Skill Growth:** Python automation, Playwright/Puppeteer, browser DOM events, client-server communication.

### Role 4: Data Engineering, NVIDIA LLM Integration & Compliance Lead (Team Member 4)
* **Core Responsibilities:**
  * Operating **Laptop 4** (The Compliance Station) or managing data feeds.
  * SQLite database schemas, API routes in FastAPI, and synthetic dataset loading.
  * Integrating the **NVIDIA NIM free API keys** (Llama-3.3-70B) to:
    1. Generate synthetic persona backstories and loan narratives.
    2. Format the automated 2-page Suspicious Activity Report (SAR) PDF for download.
* **Skill Growth:** FastAPI, SQLite/SQLAlchemy, prompt engineering, PDF generation (`ReportLab` / `pdfkit`).

---

## 5. Next Practical Milestones
1. **Repository Setup:** Initialize a clean monorepo (`/frontend` in Next.js, `/backend` in FastAPI, `/simulation` in Python/Playwright).
2. **Minimal Viable Pipeline (MVP):** Build the local telemetry receiver $\to$ NetworkX graph $\to$ 3D visualizer.
3. **Red-Team Scripting:** Verify that Playwright agents can send real telemetry to the FastAPI server over local LAN.
4. **NVIDIA NIM Integration:** Hook up free API keys for automated persona generation and report drafting.
