# Station 1: Red-Team Swarm Runner & Client Telemetry
**Assignee:** Alan E Alexander (Role 3)  
**Target:** Laptop 1 (Red-Team Attacker)  
**Repository:** `shadowgram-station1-alan-swarm`

---

## 🎯 What This Station Does
This station runs the autonomous red-team swarm simulation that tests the ShadowGram defense engine:
1. **Playwright Swarm Engine (`swarm_runner.py`):** Launches 20 concurrent bot contexts with route aborting to keep RAM strictly `<600MB`.
2. **Three Attack Modes:**
   - `--mode naive`: Naive automation (zero pre-click hover moves, zero click dwell variance). Triggers Key 1 Fast Filter in `<5ms`.
   - `--mode stealth`: Advanced bots (Gaussian dwell $\mu=95\text{ms}, \sigma=14\text{ms}$, pre-click hover streams). Bypasses Key 1, but is caught by Key 2 (Relational Physics Graph & Leiden Community Detection)!
   - `--mode dynamic-jitter`: Advanced adversarial swarm sampling inter-arrival intervals from an exponential Poisson distribution ($\Delta t \sim \text{Exp}(\lambda)$). Evades simple time-window binning, but is intercepted across navigation route depth and kinetic jerk.
3. **Biological Trajectory Engine (`trajectory.py`):** Flash & Hogan (1985) minimum-jerk mathematics with physiological 8-12 Hz tremor.
4. **Client-Side Telemetry SDK (`telemetry.js`):** Zero-PII behavioral telemetry library with HMAC-SHA256 signing and **biometric digraph flight time tracking** (`th`, `er`, `in`, `an`).

---

## 🚀 Quickstart Commands

### 1. Setup Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt  # Or: pip install playwright
playwright install chromium
```

### 2. Run Direct High-Speed Swarm (Recommended for Demo)
Runs in direct synthetic telemetry mode without needing full browser render:
```bash
python swarm_runner.py --direct --telemetry-url http://10.215.30.162:8000/telemetry --bots 20 --mode stealth
```

### 3. Run Dynamic Poisson Jitter Swarm (Phase 2 Advanced Attack)
Tests resilience against Poisson-staggered arrival attacks:
```bash
python swarm_runner.py --direct --telemetry-url http://10.215.30.162:8000/telemetry --bots 20 --mode dynamic-jitter
```

### 4. Run Naive Mode to Demonstrate Key 1 (<5ms Interception)
```bash
python swarm_runner.py --direct --telemetry-url http://10.215.30.162:8000/telemetry --bots 20 --mode naive
```

### 5. Run Two-Key Verification Test Suite
```bash
python test_two_key_defense.py
```

---

## 📦 Git Repository Setup
To publish this station to your own dedicated GitHub repository:
```bash
cd stations/station1_alan_swarm
git init
git add .
git commit -m "feat(station1): Red-Team Swarm Runner & Two-Key Telemetry Engine v2.0"
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/shadowgram-station1-swarm.git
git push -u origin main
```
