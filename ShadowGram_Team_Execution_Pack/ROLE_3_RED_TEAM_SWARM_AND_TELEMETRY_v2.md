# Role 3: Red-Team Swarm Runner & Client Telemetry Lead (v2.0)
**Assignee:** Alan E Alexander  
**Station:** Laptop 1 (Adversarial Swarm Runner) & Laptop 3 (Client Telemetry Instrumentation)  
**Dedicated Repository:** `shadowgram-station1-alan-swarm` (`stations/station1_alan_swarm/`)  
**Status:** 100% Fully Built, Verified & Ready for Demo

---

## 1. Where You Were Before Sleeping
Before you went to sleep, Station 1 had:
* A basic Playwright automation script executing identical sequential form submissions.
* Fixed synthetic persona generation that depended on live cloud APIs.
* Initial `telemetry.js` tracking standard keydown/keyup flight and dwell times.
* No way to demonstrate stealth vs. naive bot behavior to judges.

---

## 2. What Changed From the Stress-Test Research Audit
The deep-search audit of modern bot frameworks (Playwright Stealth, Ghost-Cursor, Puppeteer-Extra) and biometric detection papers revealed key findings:

1. **The Limitations of Pure Bézier Curves:**
   * Modern bots can generate curved cubic Bézier paths that trick naive curve checkers.
   * However, browser automation frameworks leave **event-stream distribution invariants**:
     - *Zero Pre-Click Pointer Movement:* Automated scripts often trigger `.click()` without antecedent micro-movements across coordinates.
     - *Dwell Time Distribution Invariance:* Synthetic scripts press and release keys with unnatural precision ($\sigma < 15\text{ms}$).
2. **Dual-Mode Attack Demonstration (`--mode naive` vs. `--mode stealth`):**
   * Judges will ask: *"What if the fraudster introduces human-like random delays?"*
   * Your swarm runner now supports two distinct operational modes:
     - `--mode naive`: Lockstep bot swarm firing in tight 38ms bursts (catches classical botnets).
     - `--mode stealth`: Injects Gaussian jitter into keystrokes, randomizes Bézier cursor velocities, and staggers ingress timing. The Two-Key Defense (Key 1 Event Invariants + Key 2 Semantic & Graph Correlation) catches them both!
3. **Zero-PII Telemetry Architecture:**
   * Regulators strictly penalize storing personal data in telemetry streams. `telemetry.js` captures purely kinematic, temporal, and navigational features—zero Aadhaar, PAN, or name strings are ever recorded.
4. **Offline Persona Cache Failsafe:**
   * If the mobile hotspot lags, the swarm instantly reads from `personas_cache.json` without failing the demo.

---

## 3. What Pete Built for You Overnight
While you were resting, Pete upgraded and validated your entire attack pipeline:

1. **`simulation/swarm_runner.py`:**
   * Added CLI argument parser: `--mode {stealth, naive}`, `--concurrency 20`, `--target http://localhost:3000/athenapay_portal.html`.
   * Implemented `--mode stealth` with Gaussian-distributed dwell times (`random.gauss(110, 25)`), randomized Bézier paths, and diversified semantic loan reasons.
   * Built-in offline fallback: seamlessly loads 20 pre-cached synthetic personas if NVIDIA NIM is unreachable.
2. **`public/telemetry.js`:**
   * Upgraded client-side telemetry hook capturing `click_dwell_duration_ms`, `mousemove_pre_click_count`, touch surface dynamics, and navigation state transitions.
   * Lightweight 50ms event buffering with zero main-thread UI jank.
3. **`simulation/tests/test_two_key_defense.py`:**
   * Wrote an automated 5-test test suite verifying:
     - Test 1: Key 1 Fast Filter flags zero-variance bot sessions.
     - Test 2: Authentic human sessions pass Key 1 with clean scores.
     - Test 3: Key 2 Relational Engine clusters stealth bots via semantic and temporal correlation.
     - Test 4: Empirical permutation test confirms significance ($p < 0.001$).
     - Test 5: Reversible step-up challenge clears quarantined accounts.
4. **Packaged Everything into Station 1:**
   * Copied all assets into `stations/station1_alan_swarm/` with dedicated `README.md` and Git instructions.

---

## 4. Code Location & Dedicated Git Repository
Your files are located in:
📁 `stations/station1_alan_swarm/`

### File Layout:
* `swarm_runner.py` — Multi-context Playwright attack engine (`--mode {stealth, naive}`)
* `trajectory.py` — Kinematic mouse path and cubic Bézier generator
* `generate_personas.py` — NVIDIA NIM Llama-3.3-70B persona generator
* `personas_cache.json` — 20 pre-generated synthetic personas for 100% offline reliability
* `test_two_key_defense.py` — Automated verification test suite
* `telemetry.js` — Client-side behavioral telemetry engine
* `README.md` — Station overview & quickstart guide

### Dedicated GitHub Setup:
Push your station directly to your personal GitHub repository:
```bash
cd stations/station1_alan_swarm
git init
git add .
git commit -m "feat(swarm): Dual-Mode Playwright Swarm & Zero-PII Telemetry Engine v2.0"
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB>/shadowgram-station1-swarm.git
git push -u origin main
```

---

## 5. Morning Quickstart & Pitch Checklist

### 1. Test Swarm Execution Locally:
```bash
cd stations/station1_alan_swarm
python3 -m venv venv
source venv/bin/activate
pip install playwright requests
playwright install chromium

# Launch the live attack:
python swarm_runner.py --mode stealth --target http://localhost:3000/athenapay_portal.html
```

### 2. Run the Verification Tests:
```bash
python test_two_key_defense.py
```
*(Confirms all 5 tests pass: Key 1 Fast Filter, Key 2 Graph, and Step-Up challenge).*

### 3. Pitch Choreography (Minute 0:45 - 1:30):
* When Pete cues you: *"Now Alan will deploy the syndicate attack."*
* Hit `Enter` on `python swarm_runner.py --mode stealth`.
* Tell the judges: *"We are now launching 20 autonomous agent bots using `--mode stealth`. Notice that each has a distinct name, phone number, and loan story. Each bot uses randomized mouse curves and typing jitter to bypass legacy bot filters. Watch how ShadowGram catches their coordination in real time on Laptop 2."*
