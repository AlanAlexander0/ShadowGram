# ShadowGram: Phase 2 Team Execution Guide & Git Workflow

**Document Code:** `SG-PHASE2-TEAM-GUIDE-01`  
**Classification:** Operational Station Briefing & Distributed Git Synchronization  
**Date:** October 6, 2026  
**Hotspot Server (Pete):** `http://10.215.30.162:8000`  
**Phase 2 Active Branch:** `feature/phase-2-innovations`  

---

## 🧭 Overview & Strategy for the Final Judging Round

While our parallel ChatGPT Deep Research audits our threat models and discovers cutting-edge algorithmic counters, each team member has clear, high-impact deliverables to build in Phase 2.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                               PHASE 2 STATION MATRIX                                   │
├─────────────────────┬─────────────────────┬─────────────────────┬──────────────────────┤
│ STATION 1 (ALAN)    │ STATION 2 (PETE)    │ STATION 3 (AISWARYA)│ STATION 4 (NIHAD)    │
│ Swarm & Telemetry   │ Backend & Graph Eng │ Frontend & Cockpit  │ Compliance & SAR     │
├─────────────────────┼─────────────────────┼─────────────────────┼──────────────────────┤
│ 1. Dynamic Jitter   │ 1. /api/repartition │ 1. Sensitivity Slid │ 1. RBI 2025 DL Clause│
│    Attack Mode      │    Dynamic Threshold│ 2. Web Audio Alerts │ 2. Permutation Null  │
│ 2. Digraph Keystroke│ 2. In-Memory 2D GNN │ 3. Account Aggregat.│    Model SAR Section │
│    Telemetry SDK    │    Graph Projections│    Modal in AthenaPay│ 3. 1-Click SAR Export│
└─────────────────────┴─────────────────────┴─────────────────────┴──────────────────────┘
```

---

## 🛠️ Station-by-Station Assignments

---

### 🔴 STATION 1: Alan E Alexander (Swarm Red Team & Telemetry)
* **Working Directory:** `stations/station1_alan_swarm/` or root clone on Laptop 1.
* **Remote Git:** `https://github.com/AlanAlexander0/ShadowGram.git`

#### Phase 2 Deliverables:
1. **Dynamic Poisson Jitter Attack Mode:**
   * In `swarm_runner.py`, add a new attack flag: `--mode dynamic-jitter`.
   * Simulates an advanced swarm attempting to evade Key 2 timing correlation by sampling inter-arrival intervals from an exponential Poisson distribution ($\Delta t \sim \text{Exp}(\lambda)$).
   * **Demo Value:** Pete can show judges: *"Alan tried Poisson-delay jitter, but our 3-Layer Orthogonal Sparsification still caught them across navigation route depth and kinetic jerk!"*
2. **Biometric Digraph Flight Time Telemetry (`telemetry.js`):**
   * Enhance `telemetry.js` to measure inter-key flight times between common digraphs (e.g. `th`, `er`, `in`, `an`).
   * **DPDP Act 2023 / GDPR Privacy Guarantee:** DO NOT transmit typed characters or PII. Only transmit the elapsed millisecond duration between consecutive KeyDown events.

#### 💻 Alan's Git Commands:
```bash
# 1. Fetch latest updates from Pete's central upstream
git fetch origin
# Or if Pete's repo is added as an upstream remote:
# git remote add upstream https://github.com/wolf-eye0/ShadowGram.git
# git fetch upstream

# 2. Switch to the Phase 2 feature branch
git checkout -b feature/phase-2-innovations origin/feature/phase-2-innovations

# 3. Make your changes in stations/station1_alan_swarm/
# ... edit swarm_runner.py and telemetry.js ...

# 4. Commit and push to your GitHub
git add stations/station1_alan_swarm/
git commit -m "feat(station1): add dynamic Poisson jitter attack mode & digraph telemetry"
git push -u origin feature/phase-2-innovations
```

---

### 🟣 STATION 2: ParadoxPete (Principal Architect & Graph Engine)
* **Working Directory:** `backend/` & root repository on Laptop 2 (Fedora Linux).
* **Remote Git:** `https://github.com/wolf-eye0/ShadowGram.git`

#### Phase 2 Deliverables:
1. **Dynamic Sensitivity Repartitioning API (`/api/repartition`):**
   * In `backend/main.py` & `backend/graph_engine.py`:
   * Implement endpoint: `POST /api/repartition?threshold=float` (e.g. $0.50 \le \theta \le 0.90$).
   * Dynamically re-runs Leiden community clustering on the cached pairwise similarity tensor $\mathbf{S}(u,v)$ without needing new client traffic.
   * Broadcasts updated cluster labels and Modularity $Q$ over WebSockets to all connected Cockpits.
2. **Node2Vec / 2D Graph Manifold Projection:**
   * Compute normalized Laplacian spectral coordinates or 2D spring coordinates for all active nodes in `graph_engine.py`.
   * Return 2D coordinates `(x, y)` in `/api/graph` to power the Why Card anomaly island scatter plot.
3. **Keep Live Server Running:**
   * Maintain Uvicorn daemon running on `0.0.0.0:8000` with `--reload`.

#### 💻 Pete's Git Commands:
```bash
# Active on Laptop 2:
git checkout feature/phase-2-innovations
git add backend/
git commit -m "feat(backend): implement dynamic /api/repartition threshold engine & graph coordinate projections"
git push -u origin feature/phase-2-innovations
```

---

### 🔵 STATION 3: Aiswarya Kallayil (Frontend, Cockpit & Borrower Portal)
* **Working Directory:** `stations/station3_aiswarya_frontend/` or root clone on Laptop 3.
* **Remote Git:** `https://github.com/kallayilaiswarya-code/ShadowGram.git`

#### Phase 2 Deliverables:
1. **Interactive Sensitivity Slider (Track 4):**
   * In `public/cockpit.html`: Add an interactive slider in the header:
     `[ 🎯 Detection Sensitivity θ: 0.50 ────●── 0.90 (Current: 0.70) ]`
   * On slider move, send an async fetch request to `http://10.215.30.162:8000/api/repartition?threshold=VAL`.
   * Watch the 3D graph re-color and re-cluster dynamically in front of the judge!
2. **Tactical Audio-Visual Cyber Alerts (Track 6):**
   * Using Web Audio API (zero external mp3 downloads required):
     * Ambient radar ping on standby.
     * Tactical red klaxon siren when swarm attack triggers ($Q \ge 0.60$).
     * Harmonic chime when the Step-Up 1-Rupee UPI verification passes.
     * Include an audio toggle button `[ 🔊 Audio Alerts: ON ]`.
3. **Account Aggregator (AA) Sandbox Option (Track 5):**
   * In `athenapay_portal.html`, add a second Step-Up challenge button:
     `[ 🏦 Verify via Account Aggregator (Setu / OneMoney) ]` demonstrating instant RBI-compliant bank statement retrieval.

#### 💻 Aiswarya's Git Commands:
```bash
# 1. Fetch latest updates from Pete's central upstream
git fetch origin
git checkout -b feature/phase-2-innovations origin/feature/phase-2-innovations

# 2. Make changes in public/cockpit.html, public/athenapay_portal.html
# ... edit files ...

# 3. Commit and push to Aiswarya's GitHub
git add public/cockpit.html public/athenapay_portal.html stations/station3_aiswarya_frontend/
git commit -m "feat(frontend): add interactive sensitivity slider, Web Audio cyber alerts, and AA modal"
git push -u origin feature/phase-2-innovations
```

---

### 🟢 STATION 4: Nihad & Ashlin (Compliance, SAR Generator & Legal)
* **Working Directory:** `stations/station4_nihad_compliance/` on Laptop 4.
* **Key Files:** `sar_generator.py`, `fallback_sar.py`, `page.tsx`

#### Phase 2 Deliverables:
1. **Permutation Null Model & Modularity SAR Section:**
   * In `sar_generator.py`: Add an explicit forensic audit section to the 2-page PDF:
     * Table detailing the **Maslov-Sneppen Permutation Null Model**: 1,000 degree-preserving graph rewirings showing empirical $p$-value ($p < 0.001$).
     * Leiden Newman-Girvan Modularity ($Q = 0.7241$).
     * Minimum-Jerk kinematic variance ($J = d^3x/dt^3$).
2. **RBI Digital Lending Guidelines (2025 Directions) Legal Clause:**
   * Cite Section 6.2 of the RBI Master Directions on algorithmic transparency and Equal Credit Opportunity Act (ECOA) Regulation B (12 CFR § 1002.9).
   * Officer HMAC digital seal for tamper-evident regulatory audits.

#### 💻 Nihad & Ashlin's Git Commands:
```bash
# 1. Pull Phase 2 branch
git fetch origin
git checkout -b feature/phase-2-innovations origin/feature/phase-2-innovations

# 2. Update sar_generator.py in stations/station4_nihad_compliance/
# ... edit sar_generator.py ...

# 3. Test PDF generation locally
python -c "from sar_generator import generate_sar_pdf; generate_sar_pdf('cluster-test', {'nodes':['u1','u2']}, 'test_sar.pdf')"

# 4. Commit and push
git add stations/station4_nihad_compliance/
git commit -m "feat(compliance): embed Maslov-Sneppen p-value null model & RBI 2025 regulatory clauses in SAR PDF"
git push -u origin feature/phase-2-innovations
```

---

## 🔄 Cross-Station Hotspot Integration Verification

When all stations are running:
1. **Pete's Fedora Linux:** Running `uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload`.
2. **Alan's Laptop (10.215.30.174):** Fires `python swarm_runner.py --telemetry-url http://10.215.30.162:8000/telemetry --bots 20 --mode stealth`.
3. **Aiswarya's Laptop (10.215.30.204):** Displays `http://10.215.30.162:8000/cockpit.html`. Audio alerts chime, red cluster forms, and judges adjust the sensitivity slider.
4. **Judge or Aiswarya types on AthenaPay:** Instant green single node appears with zero false edges.
5. **Nihad's Station:** Clicks `[ Export SAR PDF ]`, instantly producing the 2-page legal defense document.
