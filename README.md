# ShadowGram — Role 3: Red-Team Swarm Runner & Client Telemetry Engine

**Author / Assignee:** Alan E Alexander (Teammate 3)  
**Event:** HackAthena 2026 | **Track:** Track 04 (Synthetic Identity & KYC) & Track 05 (Open Fraud)  
**Station Allocation:** Laptop 1 (Red Team Attacker) & Laptop 3 (Target Portal Instrumentation)  
**Protocol Compliance:** `SG-PROTO-00` / `CP-REDTEAM-01`

---

## 📌 Executive Summary

This repository contains the standalone, complete deliverables for **Role 3 (Alan E Alexander)** within the ShadowGram Autonomous AI Swarm Fraud Defense Cyber-Range. 

Role 3 is responsible for:
1. **The Adversary (Laptop 1):** Deploying a 20-agent autonomous bot swarm that uses neuromotor trajectory mathematics, LLM-generated personas, and micro-temporal synchronization to attack digital micro-lending portals.
2. **The Sensor (Laptop 3):** Providing the client-side JavaScript telemetry SDK that silently captures human-computer interaction dynamics (keystroke flight/dwell times, cursor jerk, navigation routes) without touching any sensitive PII.

---

## 🗂️ Deliverables File Tree

```
ShadowGram (Role 3 - Alan E Alexander)
├── simulation/
│   ├── trajectory.py           # Flash & Hogan biological minimum-jerk trajectory generator
│   ├── generate_personas.py    # Live NVIDIA NIM API (Llama-3.2-11B) persona generator
│   ├── personas_cache.json     # 20 cached Indian borrower KYC identities & narratives
│   └── swarm_runner.py         # Async Playwright swarm runner (<600MB RAM, 1.4s burst)
├── public/
│   ├── telemetry.js            # Zero-PII client telemetry SDK with HMAC-SHA256 signing
│   └── athenapay_portal.html   # Standalone 6-second judge testing portal
├── app/
│   └── loan/
│       └── page.tsx            # Next.js 14 React loan portal with embedded telemetry
├── tests/
│   └── test_role3_pipeline.py  # 4/4 automated unit tests & mock ingress pipeline
├── PROGRESS_CHECKPOINT_MEMBER3.md # Standardized handover report for Lead Architect (Pete)
└── .gitignore                  # Strict exclusion of .env and local cache files
```

---

## ⚡ Core Technical Features

### 1. Flash & Hogan Neuromotor Kinematics (`simulation/trajectory.py`)
* Implements biological 5th-degree minimum-jerk polynomial curves:
  $$s(\tau) = 10\tau^3 - 15\tau^4 + 6\tau^5$$
* Features dynamic overshoot correction when target distance exceeds 220px.
* Emulates realistic 8–12 Hz physiological micro-tremor.
* Pure Python with **zero external dependencies**.

### 2. High-Performance Swarm Runner (`simulation/swarm_runner.py`)
* **Strict Memory Limit:** Operates **1 single Chromium process** with 20 lightweight isolated `BrowserContext` instances.
* **Media Route Abort:** Intercepts and blocks images, fonts, and styles, keeping total RAM consumption **strictly < 600MB**.
* **Micro-Temporal Arrival Burst:** Synchronizes all 20 bot loan applications within a tight **1.4-second arrival window** to test ShadowGram's $\Delta t$ correlation layer.
* **Dual Operation Modes:** Supports full Playwright browser automation or high-speed direct synthetic telemetry dispatch.

### 3. Live NVIDIA NIM Persona Generator (`simulation/generate_personas.py`)
* Connects live to NVIDIA NIM (`meta/llama-3.2-11b-vision-instruct`) via OpenAI-compatible endpoints.
* Generates 20 authentic Indian identities with varied occupations, cities, PANs, and convincing emergency loan reasons.
* Includes a local deterministic generator so the system works 100% offline if venue Wi-Fi drops.

### 4. Client Telemetry SDK (`public/telemetry.js`)
* **Zero-PII Mandate:** Captures no key characters, names, or values. Only records millisecond time deltas ($\Delta t$): Key Flight Time and Key Dwell Time.
* **50ms Cursor Throttle:** Samples cursor coordinates at most once per 50ms to guarantee zero UI lag when a visiting judge types.
* **Cryptographic HMAC Signing:** Signs every telemetry batch using `HMAC_SHA256(session_id + timestamp, session_salt)` to reject forged cURL requests.
* **Honey-DOM Tripwire:** Detects clicks on invisible DOM elements to flag crude automated scrapers instantly.

### 5. AthenaPay Target Portal (<6-Second Judge Testing Rule)
* Built in both React/Next.js ([`app/loan/page.tsx`](app/loan/page.tsx)) and standalone HTML ([`public/athenapay_portal.html`](public/athenapay_portal.html)).
* 95% pre-filled by default (Name: Rohan Verma, PAN: ABCDE1234F, Income: ₹45,000, Amount: ₹10,000).
* Exactly **1 editable field**: *"Loan Reason: [ Type 3 words ]"*.
* Allows a visiting hackathon judge to walk up, type 3 words, click apply, and complete an authentic human test in under 6 seconds.

---

## 🧪 Verification & Testing

Run the automated test suite:
```powershell
python tests/test_role3_pipeline.py
```
Output:
```
test_01_minimum_jerk_trajectory_generation ... ok
test_02_personas_cache_integrity ............. ok
test_03_telemetry_schema_and_hmac_signing .... ok
test_04_end_to_end_mock_telemetry_ingress .... ok

Ran 4 tests in 1.085s
OK (100% Pass Rate)
```

---

## 🚀 Live Demonstration Execution

### 1. Launch the Target Portal (Laptop 3)
```powershell
python -m http.server 3000 --directory public
```
Open `http://localhost:3000/athenapay_portal.html` in any browser.

### 2. Launch the Swarm Attack (Laptop 1)
```powershell
# Live Playwright browser attack:
python simulation/swarm_runner.py --target-url http://192.168.43.3:3000 --bots 20

# Direct high-speed synthetic mode (fallback):
python simulation/swarm_runner.py --direct --telemetry-url http://192.168.43.2:8000/telemetry --bots 20
```

---

## 📄 Protocol Audit Report
For the complete technical audit, API contract compliance checklist, and architecture excerpts for the Lead Systems Architect (Pete), refer to:  
👉 **[`PROGRESS_CHECKPOINT_MEMBER3.md`](PROGRESS_CHECKPOINT_MEMBER3.md)**
