# Deck 3: Team Execution, Hardware Allocation & Live Cyber-Range Demo

> **NotebookLM Instruction / Slide Deck Directive:**  
> Generate a highly visual, 11-slide presentation explaining team role assignments, the 4-laptop cyber-range architecture, hardware tier matching, local phone hotspot networking, and the step-by-step live pitch choreography. Emphasize team coordination, precision engineering, and seamless live demonstration execution.

---

## Slide 1: Title Slide — Operation ShadowGram: Team Execution & Live Cyber-Range
* **Subtitle:** 4 Engineers, 4 Laptops, 1 Unified Autonomous Cyber-Range
* **Slide Type:** Team War-Room Title Slide
* **Visual Concept:** A command center briefing room with 4 battle-station screens illuminated under low blue lighting, each labeled with its operational code and designated team member.
* **Key Takeaway:** How the Crafty Crew coordinates across 4 specialized roles to deliver an airtight, live-fire cybersecurity demonstration for the HackAthena judges.
* **Speaker Notes:** "Welcome team. In this presentation, we outline the exact battle plan: who does what, which laptop runs what workload, how our local hotspot network connects us, and how we will blow the judges away during our live demo."

---

## Slide 2: The 4-Laptop Live Attack Cyber-Range
* **Slide Type:** System Architecture & Cyber-Range Diagram
* **Visual Concept:** Panoramic 4-node network diagram showing laptops connected over a local Wi-Fi hotspot with directional data packet arrows.
* **The 4-Station Layout:**
  * **Laptop 1 (The Attacker):** Red Team Swarm Runner — launches 20 automated Playwright bot instances.
  * **Laptop 2 (The Command Cockpit):** ShadowGram Server & 3D Dashboard — runs FastAPI, SQLite, and Three.js WebGL visualization.
  * **Laptop 3 (The Target Portal):** AthenaPay Loan App — clean micro-lending portal where a **live judge** applies as a real human.
  * **Laptop 4 (The Compliance Station):** Officer's Terminal — opens the live "Why Card", triggers the 1-click quarantine, and downloads the SAR PDF.
* **Speaker Notes:** "We aren't doing a boring slide-only pitch or showing a pre-recorded video. We are running a full live-fire cyber-range right in front of the judges across four connected laptops."

---

## Slide 3: Hardware Allocation Strategy — 2 Gaming + 2 Normal Laptops
* **Slide Type:** Resource Optimization & Hardware Matrix
* **Visual Concept:** Hardware tier comparison table with icons for gaming laptops (GPU/CPU glow) and standard student laptops (battery/sleek icons).
* **The Allocation Matrix:**
  * **Station 1 (Laptop 1 - Red Team Attacker):** 🎮 **Gaming Laptop #1** (High Multi-Core CPU).  
    * *Workload:* Runs 20 parallel Playwright browser contexts. Optimized to 1 Chromium instance with 20 lightweight contexts (~600MB RAM).
  * **Station 2 (Laptop 2 - ShadowGram Cockpit):** 🎮 **Gaming Laptop #2** (Dedicated GPU).  
    * *Workload:* Hosts FastAPI backend, ONNX 2D-CNN, Sentence-Transformers, and renders the 3D WebGL particle universe at 60 FPS.
  * **Station 3 (Laptop 3 - AthenaPay Portal):** 💻 **Normal Laptop #1** (Basic Office Specs).  
    * *Workload:* Runs standard Next.js 3-step loan web application (<200MB RAM).
  * **Station 4 (Laptop 4 - Compliance Station):** 💻 **Normal Laptop #2** (Basic Office Specs).  
    * *Workload:* Displays compliance table and downloads SAR PDF via ReportLab (<300MB RAM, heavy LLM work offloaded to NVIDIA cloud).
* **Speaker Notes:** "We strategically mapped our hardware. Only two roles need gaming machines—the 3D graphics server and the multi-bot attacker. The other two run effortlessly on basic, everyday student laptops."

---

## Slide 4: Local LAN & Hotspot Networking — Zero Cloud Dependency
* **Slide Type:** Technical Networking & Resilience Guide
* **Visual Concept:** A mobile phone emitting a local Wi-Fi hotspot bubble connecting the 4 laptops with zero internet cables and zero external router dependencies.
* **The 3 Golden Networking Rules:**
  1. **FastAPI Host Binding (`0.0.0.0`):** Laptop 2 starts Uvicorn with `--host 0.0.0.0 --port 8000` so all hotspot peers can connect. (`localhost` is strictly forbidden).
  2. **Dynamic IP Targeting:** Linux server identifies local IP (`192.168.43.2`) via `hostname -I`. All client requests and telemetry hooks target `http://192.168.43.2:8000`.
  3. **Android Hotspot over iPhone:** Android hotspots allow open peer-to-peer pinging without AP client isolation. (Portable wall-powered offline Wi-Fi router used as secondary backup).
* **Cross-Platform Rule:** **Zero Docker** (avoids Windows WSL2 and bridge NAT bugs). Python `venv` and Node.js run natively cross-platform across Linux and Windows.
* **Speaker Notes:** "Hackathon Wi-Fi is notorious for crashing. We don't rely on the venue Wi-Fi at all. We bring our own local hotspot. Even if the entire building loses internet, our cyber-range runs perfectly."

---

## Slide 5: Role 1 — Principal Systems Architect & Graph Engine Lead
* **Assignee:** ParadoxPete (Lead Developer / Orchestrator)
* **Station & Hardware:** 🎮 Gaming Laptop #2 • Station: Laptop 2
* **Slide Type:** Role Dossier & Technical Deliverables
* **Visual Concept:** Code editor showing FastAPI backend routing and NetworkX graph adjacency matrix calculations.
* **Core Responsibilities:**
  * Builds the core FastAPI backend and async WebSocket dispatcher (`backend/main.py`).
  * Implements `ShadowGraphEngine` with Louvain modularity clustering and dynamic edge weighting ($S_{\text{comp}} \ge 0.78$).
  * Integrates the pre-exported 2D-CNN ONNX model for kinetic cursor jerk classification ($<10\text{ms}$).
  * Deploys `sentence-transformers/all-MiniLM-L6-v2` for dense semantic vector embeddings.
  * Leads technical defense and mathematical Q&A against hackathon judges.
* **Speaker Notes:** "Pete is the central engine builder. He writes the backend server, implements the Louvain graph mathematics, and ensures sub-10 millisecond response times."

---

## Slide 6: Role 2 — Visual Command Center & 3D WebGL Lead
* **Assignee:** Aiswarya Kallayil Rajesh (Frontend Lead)
* **Station & Hardware:** 🎮 Gaming Laptop #2 • Station: Laptop 2 (Main Presentation Display)
* **Slide Type:** UI/UX Showcase & Frontend Architecture
* **Visual Concept:** Sleek dark liquid-glass Next.js dashboard screenshot with glowing 3D particle nodes, floating KPI counters, and the interactive "Why Card" modal.
* **Core Responsibilities:**
  * Develops the Next.js 14 frontend using Tailwind CSS and dark liquid-glass styling (`shadowgram-template by ais.md`).
  * Implements `react-force-graph-3d` (Three.js WebGL) with camera rotation, node bloom shaders, and 2D fallback toggle.
  * Builds the interactive **"Why Card" modal** displaying factual telemetry metrics (arrival $\Delta t$, LCS route overlap, cosine similarity).
  * Implements the 1-click **`[ 1-Click Blast-Radius Quarantine ]`** action button with instant visual feedback.
  * Integrates the in-memory **`[ 🔥 Deploy Swarm Simulation ]`** emergency demo button.
* **Speaker Notes:** "Aiswarya is the visual architect. She turns complex backend mathematics into a gorgeous, Hollywood-grade 3D cyber-cockpit that makes the judges immediately understand the value."

---

## Slide 7: Role 3 — Red-Team Swarm Runner & Client Telemetry Lead
* **Assignee:** Alan E Alexander (Teammate 3 - Adversarial Simulation Lead)
* **Station & Hardware:** 🎮 Gaming Laptop #1 • Station: Laptop 1 (Attacker) & Laptop 3 (Target Portal Instrumentation)
* **Slide Type:** Red-Team Tooling & Telemetry Pipeline
* **Visual Concept:** Headless Chromium browser automation terminal launching synchronized bot sessions alongside a live telemetry JSON packet waterfall.
* **Core Responsibilities:**
  * Writes `swarm_runner.py` using Python Playwright async API to spawn 20 simultaneous bot sessions.
  * Queries free NVIDIA NIM API (Llama-3.3-70B) to generate realistic, non-repeating applicant personas.
  * Injects parametric cubic Bézier curves for automated cursor movement.
  * Authors client-side `telemetry.js` running on Laptop 3: captures keystroke flight/dwell intervals and throttled 50ms pointer positions.
  * Enforces Zero-PII: streams strictly numerical time deltas $\Delta t$ and coordinates to Laptop 2.
* **Speaker Notes:** "Alan is our Red-Team attacker. He writes the automation script that launches 20 AI bots against our target bank app and instruments the web pages to capture micro-biometrics."

---

## Slide 8: Role 4 — Data Engineering, NVIDIA LLM & Legal SAR Lead
* **Assignee:** Mohammed Nihad PC / Ashlin Theres James (Teammate 4 - Compliance & Data Lead)
* **Station & Hardware:** 💻 Normal Laptop #2 • Station: Laptop 4 (Compliance Officer Station)
* **Slide Type:** Enterprise Data Architecture & Regulatory Compliance
* **Visual Concept:** An automated PDF document assembly pipeline converting raw database rows into an official government-ready Suspicious Activity Report (SAR).
* **Core Responsibilities:**
  * Defines SQLite database schema (`shadowgram.db`) using SQLAlchemy (`sessions`, `telemetry_events`, `clusters`).
  * Authors `sar_generator.py`: calls NVIDIA NIM API (Llama-3.3-70B) to convert raw cluster metrics into CFPB Circular 2023-03 compliant adverse action reasons.
  * Implements `generate_sar_pdf.py` using Python `ReportLab` to output a clean 2-page legal dossier.
  * Deploys lightweight KYC document artifact scanner (`kyc_scanner.py`) using PIL/OpenCV for synthetic ID detection.
* **Speaker Notes:** "Nihad and Ashlin handle the legal credibility and data storage. They ensure that every caught syndicate can be frozen with a legally compliant, two-page SAR PDF ready for regulators."

---

## Slide 9: The 3-Minute Live Pitch Choreography
* **Slide Type:** Demonstration Timeline & Stage Script
* **Visual Concept:** A high-tempo 180-second countdown timeline dividing the presentation into 4 distinct phases.
* **The Pitch Sequence:**
  * **0:00 – 0:45 (The Threat Hook):** Pete introduces the ₹20 Lakh micro-lending attack case study. Point to Laptop 3 (AthenaPay portal) and invite a judge to step up and apply for a ₹10,000 loan.
  * **0:45 – 1:30 (The Live Swarm Attack):** Alan hits enter on Laptop 1. 20 Playwright bots assault the portal simultaneously. On Laptop 2's big screen, the 3D WebGL galaxy instantly lights up as red laser lines bind the 20 bot nodes together.
  * **1:30 – 2:15 (The Differentiation):** Aiswarya points to the judge's node on Laptop 2: glowing green, isolated, calm, and completely unaffected. Aiswarya clicks the red cluster $\to$ the "Why Card" pops open showing exact mathematical proof.
  * **2:15 – 3:00 (The Legal Knockout):** Teammate 4 on Laptop 4 clicks **`[ 1-Click Quarantine ]`** $\to$ grey shields drop over the bots. Click **`[ Export SAR ]`** $\to$ download the formal 2-page PDF dossier. Pete concludes with zero-cost architecture and opens Q&A.
* **Speaker Notes:** "Every second of our three-minute pitch is choreographed. The judges see a live attack, test it with their own hands, and watch our system isolate the criminals while keeping the judge 100% safe."

---

## Slide 10: The Live Judge Interaction — The "Golden Touch"
* **Slide Type:** Interactive Demonstration Tactic
* **Visual Concept:** A hackathon judge typing their real name into Laptop 3 while watching their own avatar appear as a green glowing node on the big screen.
* **Why This Guarantees 1st Place:**
  * **Overcoming Skepticism:** Judges see dozens of pre-baked slides and fake mockups. Handing a judge the keyboard completely removes doubt.
  * **Real-Time Contrast:** While the 20 bot accounts are flagged and grouped by Louvain modularity, the judge's organic typing cadence and natural mouse tremor keep their node firmly in the green safe zone ($Q < 0.15$).
  * **Emotional Impact:** The judge experiences the security system not as a theoretical idea, but as an active, living digital defense.
* **Speaker Notes:** "When judges touch the system themselves and see their own node stay green while the attack is quarantined right next to them, the competition is won."

---

## Slide 11: Milestone Roadmap & Anti-Hallucination Checkpoints
* **Slide Type:** Quality Assurance & Project Roadmap
* **Visual Concept:** A milestone progression ladder leading up to the final demo, with green quality-gate verification badges.
* **The 4 Integration Milestones:**
  * **M1 (Ingestion & DB):** Endpoints `/telemetry` live on Laptop 2; SQLite logging verified via cURL.
  * **M2 (Graph & Louvain):** NetworkX calculates composite edge weights and partitions test clusters with $Q > 0.60$.
  * **M3 (3D Visuals & Why Card):** Next.js connects via WebSocket, renders Three.js galaxy, and displays the "Why Card".
  * **M4 (Full LAN Cyber-Range):** Laptop 1 attacks Laptop 3 over local hotspot; Laptop 2 detects and quarantines in $<3\text{s}$.
* **The Checkpoint Rule:** Every teammate logs progress using `PROGRESS_CHECKPOINT_<NAME>.md` to ensure zero API schema drift.
* **Speaker Notes:** "We don't build randomly. We build against frozen milestone quality gates. Each member verifies locally, files a checkpoint report, and merges cleanly."
