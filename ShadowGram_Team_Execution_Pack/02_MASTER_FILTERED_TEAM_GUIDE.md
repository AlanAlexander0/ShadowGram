# ShadowGram: Clean Team Implementation Guide, Bank Case Studies & Competitor Analysis
**Document Code:** `SG-GUIDE-02`  
**Audience:** All Crafty Crew Team Members (Aiswarya, Alan, Mohammed Nihad, Ashlin)  
**Purpose:** Actionable, clean briefing on the problem, real-world banking attacks, competitor failures, tech stack, and execution roadmap.

---

## 1. What is ShadowGram? (The 60-Second Team Mental Model)

ShadowGram is a cyber-forensics platform that catches **coordinated AI bot swarms** attacking digital banking and fintech platforms.

### The Core Problem in Plain English:
* Traditional fraud tools check accounts **one by one**: *"Does Account A look like a bot?"*
* In 2026, scammers don't use dumb bots. They use autonomous AI agents. Each bot has a unique name, a unique ChatGPT-written bio, and a clean home Wi-Fi IP address.
* Because each bot looks 100% human in isolation, traditional security lets all 50 of them walk in. Together, they take out micro-loans and vanish.
* **The fraud is not inside any single account—it is in the relationship between accounts.**

### What ShadowGram Does Differently:
Instead of asking if one account is fake, ShadowGram connects the dots:
1. It watches **subtle interaction habits** (typing rhythm, navigation routes, request timing, text meaning).
2. It draws digital lines (edges) between accounts moving in sync, creating a **relational behavioral graph**.
3. It uses graph community detection (**Louvain**) to catch the entire syndicate as a glowing cluster.
4. It auto-generates a **plain-English legal evidence card (The "Why Layer")** explaining why they were linked, allowing banks to freeze the entire network with one click.

---

## 2. Documented Industry Facts & Adversarial Threat Models (Memorize These for Judges!)

When judges ask: *"Where does this actually happen?"*, deliver this exact, 10/10 fact-checked response:

### 1. Documented Industry Fact: Digital Micro-Lending Regulatory Exposure
* **The Legal Evidence:** In *M/s Krazybee Services Private Limited vs. Directorate of Enforcement* (High Court of Telangana, March 2025), investigative proceedings pursuant to 43 FIRs led to provisional attachment orders of **~₹65.87 Crore** under the Prevention of Money Laundering Act (PMLA).
* **The Core Lesson:** Automated micro-credit pipelines face catastrophic operational and legal clawback risks when automated underwriting lacks multi-dimensional behavioral governance.

### 2. Documented Network Trend: BNPL Payment Fraud Surge (+211%)
* **The Verified Metric:** Sift’s Digital Trust & Safety Index confirmed that **attempted payment fraud targeting Buy Now, Pay Later (BNPL) surged by +211% year-over-year** in their global network (compared to +13% in broad fintech).
* **The Vulnerability:** Fraudsters exploit the latency gap between instant credit checkout and asynchronous bureau reporting.

### 3. Our Evaluated Threat Models (Adversarial Simulation Scenarios)
* **Simulation Scenario A (Flash Loan Stacking):** We simulate 200 automated agent accounts attacking simultaneously at 3:00 AM for ₹10,000 each (₹20,00,000 theoretical exposure) before human risk teams intervene.
* **Simulation Scenario B (Denial-of-Wallet API Bleed):** Under UIDAI’s official ₹3.00 e-KYC regulation and commercial API aggregators (PAN ₹1.50–₹3.50, Face Liveness ₹4–₹10, Bureau ₹25–₹100), full onboarding costs **₹33.50 to ₹118.50 per applicant**. A flood of 100,000 synthetic applications can exhaust **₹33.5 Lakh to ₹1.18 Crore** in downstream verification fees even when rejected.
* **ShadowGram Solution:** Quarantines the syndicate at Step 2 of the form *before* paid third-party verification APIs are invoked!


---

## 3. Competitor Analysis: Why Existing Billion-Dollar Tools Fail

If a judge asks: *"Why can't Sift, BioCatch, or Arkose Labs stop this?"*, here is your exact answer:

```
┌─────────────────────────────────┬─────────────────────────────────┬─────────────────────────────────┐
│ Competitor System               │ How They Defend Today           │ Why They Fail Against AI Swarms │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ 1. BioCatch                     │ Behavioral biometrics on single │ Requires a user's past history. │
│    (Behavioral Biometrics)      │ users (learns your unique habits│ Fails completely on brand-new   │
│                                 │ over months of usage).          │ synthetic accounts with no past!│
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ 2. Arkose Labs                  │ Interactive puzzles, CAPTCHAs,  │ USENIX 2025 research (Halligan) │
│    (Bot Challenge Management)   │ and proof-of-work challenges.   │ proved Vision-LLMs solve puzzles│
│                                 │                                 │ with over 70% accuracy!         │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ 3. Sift & ThreatMetrix          │ Global identity graphs linking  │ Bots use residential rotating   │
│    (Digital Trust Consortium)   │ shared IPs, credit cards, or    │ proxies and anti-detect browsers│
│                                 │ device GUIDs.                   │ — they share ZERO static IDs!   │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ 4. Cloudflare / DataDome        │ Perimeter WAF checking IP       │ Bots inject real Chrome browser │
│    (Edge Bot Detection)         │ reputation and TLS headers.     │ profiles via anti-detect tools. │
└─────────────────────────────────┴─────────────────────────────────┴─────────────────────────────────┘
```

**ShadowGram's Competitive Advantage:**  
We require **zero prior user history**, rely on **zero shared IPs or device IDs**, and require **zero user CAPTCHA friction**. We evaluate *relational interaction physics* in real time across active sessions.

---

## 4. Our Agreed Zero-Cost Tech Stack

Everything we use is **100% free, fast, and runs locally on standard laptops**:

1. **Frontend:** **Next.js 14 + Tailwind CSS + Framer Motion** (Dark liquid-glass cyber-forensics aesthetic).
2. **3D Graph Canvas:** **`react-force-graph-3d` (Three.js / WebGL)** (Cinematic glowing galaxy with 2D fallback toggle).
3. **Backend API:** **FastAPI (Python 3.11)** with async WebSockets for sub-10ms real-time event streaming.
4. **Database:** **SQLite + SQLAlchemy** (Single-file `shadowgram.db`, zero setup, zero cloud bills).
5. **Kinetic Classifier:** **Lightweight 2D-CNN in ONNX Runtime** (<10ms CPU inference) evaluating cursor spectrogram heatmaps.
6. **NLP Embeddings:** **`all-MiniLM-L6-v2` via Sentence-Transformers** (384-dimensional dense vectors on local CPU in <80ms).
7. **Graph Community Detection:** **NetworkX + Louvain Modularity** (Isolates clusters without specifying cluster count $k$).
8. **NVIDIA NIM Free API (Llama-3.3-70B):** 4 developer keys $\times$ 40 req/min for synthetic persona generation and legal SAR PDF report compiling.
9. **Red-Team Swarm Runner:** **Python Playwright** headless automation script.

---

## 5. The 4-Laptop Live Cyber-Range Setup & Desk Geometry

On presentation day, we connect all 4 laptops to a single local phone hotspot (no venue Wi-Fi dependency):

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                LIVE DEMO TABLE ARRANGEMENT                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [ LAPTOP 1: ALAN ]              [ LAPTOP 2: AISWARYA & LEAD ]     [ LAPTOP 3 & 4 ]   │
│  Red-Team Swarm Runner           3D Command Cockpit (Main Display)  Judge Portal & SAR │
│  • Gaming Laptop #1              • Gaming Laptop #2 (Dedicated GPU) • Normal Laptops   │
│  • Spawns 20 AI bots             • 3D WebGL Particle Graph 60 FPS   • L3: Judge inputs │
│  • Submits loan swarm            • Live cluster detection & audio   • L4: SAR Legal    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

* **Laptop 1 (Red Team Attacker - Alan):** Runs `swarm_runner.py` (Playwright) to launch 20 parallel AI bot accounts attacking the portal. Uses 1 Chromium instance with 20 browser contexts + route-aborting media to keep RAM < 600MB.
* **Laptop 2 (ShadowGram Server & 3D Dashboard - Aiswarya & Lead):** The main display facing judges. Runs FastAPI + SQLite and displays the glowing 3D relationship graph with procedural Web Audio effects.
* **Laptop 3 (AthenaPay Target App - Judge Station):** An instant ₹10,000 loan portal where **we invite a live judge to apply as a genuine human**.  
  * **The 6-Second Judge Interaction Rule:** Pre-fill 95% of the loan form (Name, PAN, Address). Leave ONLY 1 field blank: *"Loan Reason: [ Type 3 words ]"* followed by a big glowing button `[ >> APPLY NOW << ]`. This guarantees the judge tests the system in <6 seconds without typos or hesitation!
* **Laptop 4 (Compliance Station - Mohammed Nihad / Ashlin):** The officer's screen. Shows the live "Why Card", executes the 1-click quarantine, and downloads the legal SAR PDF.
* *Backup Guarantee:* Laptop 2 has a 1-click **`[ 🔥 Deploy Swarm Simulation ]`** button to run the entire demo in-memory if time is short.

---

## 6. How Your Team Operates: Checkpoint Logging Rules

Every team member has a dedicated atomic role file. When you or your AI coding assistant write code:
1. **Never change API endpoints or variable names:** Check `00_CHECKPOINT_AND_INTEGRATION_PROTOCOL.md`.
2. **Test locally before handing over:** Make sure your script or UI component runs without errors.
3. **Generate a `PROGRESS_CHECKPOINT_<NAME>.md` report:** Include the files modified, local test output, and code snippets.
4. **Hand over to Lead Architect (ParadoxPete):** The Lead Architect will audit the code against the master protocol before merging.

---

## 7. Hardware Allocation Matrix (2 Gaming + 2 Normal Laptops)

Only two roles require heavy hardware; the other two run smoothly on everyday office/student laptops:

| Station | Assigned Role | Required Hardware Tier | Workload / Why |
| :--- | :--- | :--- | :--- |
| **Laptop 1** | **Red Team Attacker** | 🎮 **Gaming Laptop #1** (Multi-Core CPU) | Spawns 20 parallel Playwright Chromium browser contexts. Needs 8GB–16GB RAM and multi-core CPU. *(Optimization: 1 Chromium instance with 20 browser contexts + route-abort media = strictly < 600MB RAM).* |
| **Laptop 2** | **ShadowGram Cockpit** | 🎮 **Gaming Laptop #2** (Dedicated GPU) | Hosts FastAPI + SQLite + ONNX 2D-CNN + **3D WebGL Three.js Particle Universe**. Uses `THREE.InstancedMesh` and half-res selective bloom for 60 FPS camera rotation. |
| **Laptop 3** | **AthenaPay Portal** | 💻 **Normal Laptop #1** (Basic Office Specs) | Just renders a standard 3-step HTML/Next.js loan web form for the live judge. (< 200MB RAM). |
| **Laptop 4** | **Compliance Station** | 💻 **Normal Laptop #2** (Basic Office Specs) | Displays compliance list and downloads SAR PDF via ReportLab. Heavy LLM runs on NVIDIA's cloud with a 1500ms circuit breaker (< 300MB RAM). |

---

## 8. Cross-Platform Rules: Linux vs. Windows (Zero Docker, Zero CI/CD)

* **No Docker Needed:** Docker Desktop on Windows requires WSL2, BIOS virtualization, and high RAM. We are running everything natively in Node.js and Python venv (100% cross-platform).
  * Linux Lead: `python3 -m venv venv && source venv/bin/activate` | `npm run dev`
  * Windows Teammates: `py -m venv venv && .\venv\Scripts\activate` | `npm run dev`
* **Rule 1 (Python Paths):** Never use hardcoded slashes like `"data/test.json"`. Always use `pathlib.Path("data") / "test.json"` or `os.path.join("data", "test.json")`.
* **Rule 2 (Windows Firewall):** On Windows laptops, run this in an Administrative PowerShell so incoming requests are never blocked:
  ```powershell
  netsh advfirewall firewall add rule name="ShadowGram Port 8000" dir=in action=allow protocol=TCP localport=8000
  ```
* **No CI/CD:** We do not need GitHub Actions or complex pipelines for a 48h hackathon. Work on your feature branches and merge locally on the Lead's machine.

---

## 9. Hotspot & Local LAN Networking Guide (Aiswarya's Phone / Jio SIM Dedicated AP)

To connect our 4 laptops smoothly during the live demo without venue Wi-Fi:

1. **FastAPI Host Binding (`0.0.0.0`):**  
   On Laptop 2 (Linux Server), FastAPI must be started with:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
   *(Binding to `127.0.0.1` or `localhost` blocks external laptops. `0.0.0.0` allows all hotspot laptops to connect).*
2. **Dedicated Aiswarya Phone Hotspot Setup (Google Pixel / Jio):**  
   * Connect Aiswarya's phone to continuous USB-C power bank.
   * In Developer Options: Turn ON "Stay Awake While Charging" and "Tethering Hardware Acceleration". Turn OFF "Wi-Fi Power Saving".
   * Fixed IP `192.168.43.2` assigned to Laptop 2. All other laptops point to: `http://192.168.43.2:8000`.
3. **Hotspot AP Isolation Warning:**  
   * **Android Hotspot (Google Pixel):** Recommended. Android does not isolate clients; laptops communicate with <2ms ping.
   * **iPhone Hotspot:** Avoid if possible due to client isolation; use an offline travel router if iPhone is the only option.

---

## 10. Live Hackathon Demonstration Choreography (The 3-Minute Pitch Script)

* **Minute 0:00 - 0:45 (The Hook & Judge Interaction on Laptop 3):**  
  Turn to the judge: *"Sir/Ma'am, please type a 3-word reason for a loan on Laptop 3 and hit Apply."* As they submit, show them their green node appear on Laptop 2: *"You are an authentic human. You type with biological neuromotor tremor and unique pacing. You are approved."*
* **Minute 0:45 - 1:30 (The Attack from Laptop 1):**  
  Alan hits `Enter` on Laptop 1. Twenty headless Playwright bots flood the portal simultaneously: *"Right now, an autonomous AI bot syndicate is submitting 20 fraudulent loan applications. Notice that each has a completely different name, phone, and story generated by LLMs. Legacy tools let them in."*
* **Minute 1:30 - 2:15 (The Detection & 3D Visual Pop on Laptop 2):**  
  The sub-bass audio drops. Red laser edges snap across the 20 bot nodes on Laptop 2, clustering them into an isolated crimson sphere while the judge's node stays safe and green: *"ShadowGram detects the invisible threads: identical route state transitions, synchronized 38ms arrival bursts, and zero jerk variation."*
* **Minute 2:15 - 3:00 (The 1-Click Quarantine & Legal SAR on Laptop 4):**  
  Mohammed Nihad / Ashlin clicks `[ 🛑 Quarantine Entire Cluster ]`. The 3D nodes turn grey inside a containment shield. They click `[ Export SAR ]` and hand the judge a freshly generated, 2-page CFPB-compliant PDF: *"One click halts the entire syndicate before a single rupee leaves the bank. And compliance gets a regulator-ready audit dossier."*

---

## 11. Team Battlecards: How Anyone on Our Team Answers Tough Judge Questions

| Judge Question | Plain-English Answer to Deliver |
| :--- | :--- |
| **"What if the bots change their names and emails?"** | *"That only tricks old KYC. ShadowGram doesn't look at names. We look at behavior: how they move the mouse, how fast they click, and how their requests arrive together. Changing a name doesn't change their bot code."* |
| **"Why not use a heavy AI Graph Neural Network (GNN)?"** | *"A GNN takes 200–400 milliseconds and needs huge GPUs. Our Louvain graph algorithm runs in under 5 milliseconds on a basic CPU, so we can stop the fraud before the loan money leaves the account."* |
| **"Can't scammers record real mouse movements and play them back?"** | *"No, because when websites resize on different screens, recorded mouse paths click empty air. Also, if 20 bots replay the same recorded mouse path, their movements match 100%, which makes them even easier for ShadowGram to catch!"* |
| **"What if students in a college hostel use the same Wi-Fi?"** | *"IP address is only 1 out of 5 layers, and it has the smallest weight. To get flagged, you must match on at least 3 layers simultaneously (typing rhythm, navigation path, micro-timing). Honest students will never match all three."* |
| **"How do you stop people from sending fake bot data via cURL?"** | *"Every telemetry packet is cryptographically signed with a session-salted HMAC token. Raw cURL requests without the proper session handshake are rejected immediately."* |


