# Station 2: Principal Systems Architect & Graph Engine Lead
**Assignee:** ParadoxPete (Role 1 - Lead Developer / Orchestrator)  
**Target:** Laptop 2 (Gaming Laptop - Dedicated GPU / Central Server)  
**Repository:** `shadowgram-station2-pete-backend`

---

## 🎯 What This Station Does
This station is the central hub of the ShadowGram cyber-range:
1. **FastAPI Forensics Dispatcher (`main.py`):**
   - Binds to `0.0.0.0:8000` over the mobile hotspot LAN.
   - Cryptographic HMAC-SHA256 telemetry verification.
   - Live WebSocket streams (`/ws/telemetry` & `/ws/graph_live`).
   - Reversible Step-Up Verification (`POST /api/step-up/verify`).
   - Denial-of-Wallet Economics API (`GET /api/dow-stats`).
   - 2-Page Official SAR PDF Compiler (`GET /api/sar/pdf/{cluster_id}`).
2. **Relational Physics Graph Engine (`graph_engine.py`):**
   - **Key 1 Fast Automation Filter:** Intercepts click-dwell & pre-hover invariants in $<5\text{ms}$.
   - **Key 2 Relational Physics Graph:** Multi-layer similarity convergence across 5 physical layers.
   - **Iannucci Time-Decay Kernel:** Exponential micro-arrival clustering.
   - **B-GUARD Boundary Graph Repair:** Disconnects synthetic bridge accounts.
   - **Leiden Community Detection:** Partitions graph with Newman-Girvan modularity $Q > 0.60$.
   - **Empirical Permutation Null Model:** Degree-preserving rewiring ($N=1,000$ null models, $p < 0.001$).
   - **Denial-of-Wallet Defense:** Calculates ₹61.00/bot capital savings before fee-bearing KYC APIs.
3. **Command Cockpit (`cockpit.html`):**
   - Standalone 3D/2D particle visualizer for the judge presentation with live bloom effects, Why Card modal, and one-click quarantine.

---

## 🚀 Quickstart Commands

### 1. Launch FastAPI Core Engine
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt  # fastapi uvicorn networkx sqlalchemy reportlab requests
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

### 2. Verify Station Connectivity
```bash
curl http://localhost:8000/health
curl http://localhost:8000/api/dow-stats
```

### 3. Open Live Cockpit
Open `cockpit.html` directly in Google Chrome / Brave:
```bash
xdg-open cockpit.html  # Or open via browser
```

---

## 📦 Git Repository Setup
To publish this station to your dedicated GitHub repository:
```bash
cd stations/station2_pete_backend
git init
git add .
git commit -m "feat(station2): Principal Backend Forensics & Leiden Graph Engine v2.0"
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/shadowgram-station2-backend.git
git push -u origin main
```
