# Role 3: Red-Team Swarm Runner & Client Telemetry Lead
**Assignee:** Teammate 3 (Alan E Alexander)  
**Hardware & Station:** 🎮 Gaming Laptop #1 (Multi-Core CPU for 20 Playwright Contexts) • Station: Laptop 1 (Attacker) & Laptop 3 (Target Portal Instrumentation)  
**Role Title:** Red-Team Swarm Runner & Client Telemetry Lead (Adversarial Simulation)  
**Core Responsibility:** Laptop 1 Playwright swarm runner script, dynamic NVIDIA persona injection, and client-side JavaScript telemetry hooks (`telemetry.js`) on Laptop 3.

---

## 🤖 MANDATORY INSTRUCTION BLOCK FOR AI CODING ASSISTANTS
> **INSTRUCTION FOR CHATGPT / CLAUDE / CURSOR / COPILOT:**  
> You are an elite Python automation and browser security engineer assisting **Teammate 3** in building the Red-Team Swarm Runner and Telemetry SDK for ShadowGram.
> 
> **STRICT COMPLIANCE RULES:**
> 1. You **MUST** strictly adhere to the telemetry JSON schema defined in `00_CHECKPOINT_AND_INTEGRATION_PROTOCOL.md`.
> 2. The Playwright script must run asynchronously with a concurrency limit (e.g., 20 parallel browser contexts) to prevent freezing Laptop 1.
> 3. The client-side JavaScript telemetry hooks must be lightweight and throttled to **50ms** so they never lag the browser thread on Laptop 3 when a live judge is typing.
> 4. At the end of every task, you **MUST generate a `PROGRESS_CHECKPOINT_MEMBER3.md`** report summarizing modified files, test outputs, and code snippets for the Lead Architect to review.

---

## 1. Role Mission & System Scope
Your mission is to build the **live demonstration attacker**:
* **On Laptop 1:** When you press enter on `swarm_runner.py`, twenty headless browser instances spawn. Each bot fetches a unique persona (name, fake Aadhaar/PAN, loan reason) from NVIDIA NIM, navigates across the local network to Laptop 3 (AthenaPay app), and applies for a loan simultaneously.
* **On Laptop 3:** Your `telemetry.js` script silently instruments the form, capturing the flight/dwell time of keystrokes, mouse coordinate streams, and timestamps, streaming them in real time to the ShadowGram server on Laptop 2.

---

## 2. Red-Team Architecture & Telemetry Pipeline

```
[ Laptop 1: Playwright Runner ]
  ├── 1. Query NVIDIA NIM API (Llama-3.3-70B) -> Generates 20 Unique Personas
  └── 2. Spawns 20 Async Browser Contexts (Chromium)
           │
           ▼ [ HTTP / WebSocket over Local LAN: http://192.168.43.3:3000 ]
[ Laptop 3: AthenaPay Micro-Lending Portal ]
  ├── Step 1: Navigates /auth -> /kyc -> /loan_details -> /submit
  ├── Step 2: Types loan narrative using cubic Bézier mouse movement
  └── Step 3: `telemetry.js` Hooks Capture DOM Events:
           • keydown / keyup (Flight & Dwell intervals)
           • pointerdown / mousemove (Coordinates [x, y, t])
           • Route state changes (/auth -> /kyc -> /submit)
           │
           ▼ [ POST /telemetry to Laptop 2: http://192.168.43.2:8000/telemetry ]
[ Laptop 2: ShadowGram Core Server ]
```

---

## 3. Atomic Task Specifications

### Task 3.1: Client-Side Telemetry Hooks (`telemetry.js`)
* **File:** `public/telemetry.js` (embedded inside Laptop 3's AthenaPay app)
* **Requirements:**
  * Attach non-blocking event listeners to `window`:
    * `keydown` & `keyup`: Calculate Flight Time (FT = time between previous keyup and current keydown) and Dwell Time (DT = time between keydown and keyup).
    * `pointermove`: Capture mouse positions `[x, y, timestamp]`, throttled to sample at most once every **50ms**.
    * `popstate` / route transitions: Record URL paths (e.g., `/auth` $\to$ `/kyc` $\to$ `/submit`).
  * **HMAC Signing Header:** Signs outgoing telemetry with session salt (`HMAC_SHA256(session_id + timestamp, session_salt)`) to reject forged outside requests.
  * Buffer events in memory and flush via `navigator.sendBeacon` or async `fetch("http://<LAPTOP_2_IP>:8000/telemetry")` every **1.0 second**.
  * Zero-PII Rule: Never capture actual characters (no key names or input values); only record numerical time deltas $\Delta t$ in milliseconds!

### Task 3.2: Python Playwright Swarm Script (`swarm_runner.py`)
* **File:** `simulation/swarm_runner.py` (runs on Laptop 1)
* **Requirements:**
  * Uses `playwright.async_api`.
  * **Memory Optimization Architecture:**
    * Launch **ONE single Chromium browser instance**: `browser = await playwright.chromium.launch(headless=True)`.
    * Spawn 20 isolated `BrowserContext` instances.
    * **Abort Media Routes:** Intercept and abort images, fonts, and styles to keep total memory under **600MB**:
      ```python
      await context.route("**/*.{png,jpg,jpeg,svg,woff,woff2,css,gif}", lambda route: route.abort())
      ```
  * Accepts arguments: `--target-url http://192.168.43.3:3000 --bots 20`.
  * For each bot instance:
    * Use the pure Python minimum-jerk trajectory generator (`simulation/trajectory.py`) to move the cursor realistically:
```python
# simulation/trajectory.py - Standalone Neuromotor Trajectory Generator (Zero Dependencies)
import math, random
from typing import List, Tuple

def generate_human_trajectory(
    p0: Tuple[float, float], p3: Tuple[float, float],
    duration: float = 0.65, fps: int = 60,
    overshoot_threshold: float = 220.0, overshoot_ratio: float = 0.08,
    noise_sigma: float = 0.45
) -> List[Tuple[float, float, float]]:
    dx, dy = p3[0] - p0[0], p3[1] - p0[1]
    dist = math.hypot(dx, dy)
    overshoot = dist > overshoot_threshold

    if overshoot:
        angle = math.atan2(dy, dx)
        ov_dist = min(dist * overshoot_ratio, 28.0) * random.uniform(0.85, 1.15)
        target = (p3[0] + math.cos(angle) * ov_dist, p3[1] + math.sin(angle) * ov_dist)
    else:
        target = p3

    u1, v1 = random.uniform(0.2, 0.38), random.uniform(-0.2, 0.2) * dist
    u2, v2 = random.uniform(0.62, 0.82), random.uniform(-0.15, 0.15) * dist
    p1 = (p0[0] + dx * u1 - (dy / dist) * v1, p0[1] + dy * u1 + (dx / dist) * v1) if dist else p0
    p2 = (p0[0] + dx * u2 - (dy / dist) * v2, p0[1] + dy * u2 + (dx / dist) * v2) if dist else p0

    def bz(t: float, a: float, b: float, c: float, d: float) -> float:
        omt = 1.0 - t
        return (omt**3)*a + 3*(omt**2)*t*b + 3*omt*(t**2)*c + (t**3)*d

    steps = max(int(duration * fps), 12)
    path: List[Tuple[float, float, float]] = []

    for i in range(steps + 1):
        tau = i / steps
        s = 10.0 * (tau**3) - 15.0 * (tau**4) + 6.0 * (tau**5) # Flash & Hogan minimum-jerk
        bx = bz(s, p0[0], p1[0], p2[0], target[0])
        by = bz(s, p0[1], p1[1], p2[1], target[1])
        tremor = math.sin(math.pi * tau) * random.gauss(0, noise_sigma)
        path.append((round(bx + tremor, 2), round(by + tremor, 2), round(tau * duration, 4)))

    if overshoot:
        corr_steps = max(int(steps * 0.2), 6)
        corr_time = duration * 0.22
        lx, ly, lt = path[-1]
        for j in range(1, corr_steps + 1):
            c_tau = j / corr_steps
            c_s = 10.0 * (c_tau**3) - 15.0 * (c_tau**4) + 6.0 * (c_tau**5)
            cx = lx + (p3[0] - lx) * c_s
            cy = ly + (p3[1] - ly) * c_s
            c_tremor = (1.0 - c_tau) * random.gauss(0, noise_sigma * 0.4)
            path.append((round(cx + c_tremor, 2), round(cy + c_tremor, 2), round(lt + (j / corr_steps) * corr_time, 4)))

    return path
```
    * Drive through the 3-step loan application:
      1. Fill personal details (from cached NVIDIA personas).
      2. Fill loan justification text.
      3. Click submit.
    * Synchronize all 20 submissions within a tight **1.4-second window** to test ShadowGram's micro-temporal arrival layer ($\Delta t$).

### Task 3.3: NVIDIA NIM Persona Generator Script
* **File:** `simulation/generate_personas.py`
* **Requirements:**
  * Calls NVIDIA NIM API (`meta/llama-3.3-70b-instruct`) using the team's free developer key.
  * Prompt: *"Generate 20 distinct, realistic Indian personas for an emergency micro-loan application. Each persona must have a different name, occupation, city, and a differently phrased emergency loan justification (e.g., medical bill, home repair, education fee). Return as clean JSON."*
  * Saves output to `simulation/personas_cache.json` so the script can run offline if internet drops during judging!

### Task 3.4: Laptop 3 Loan Form Pre-Population (<6s Judge Testing Rule)
* **File:** `app/loan/page.tsx` (on Laptop 3)
* **Requirements:**
  * Pre-populate 95% of the loan form inputs by default (e.g., Name: *"Rohan Verma"*, PAN: *"ABCDE1234F"*, Income: *"₹45,000"*, Amount: *"₹10,000"*).
  * Leave ONLY ONE input field empty: *"Loan Reason: [ Type 3 words, e.g. 'Laptop repair fee' ]"*.
  * Big high-contrast glowing button: **`[ >> APPLY NOW << ]`**.
  * Rationale: Ensures a visiting hackathon judge can walk up, type 3 words, click apply, and complete a live test within 6 seconds without typos or cognitive friction.

---

## 4. Station Networking & Windows Defender Firewall Configuration

### A. Windows Defender Firewall Rule (Administrative PowerShell)
If developing on Windows, run this in an **Administrative PowerShell** on Laptop 1 and Laptop 3 to ensure bot traffic and telemetry streams are never blocked:
```powershell
netsh advfirewall firewall add rule name="ShadowGram Swarm" dir=in action=allow protocol=TCP localport=3000
netsh advfirewall firewall add rule name="ShadowGram Backend" dir=out action=allow protocol=TCP remoteport=8000
```
*(If the Windows popup asks: "Allow app to communicate on Private networks?" $\to$ **Check 'Private networks' and click 'Allow'**).*

### B. Hotspot LAN Connection Guide (Connecting to Aiswarya's Phone)
1. **Connect to Wi-Fi:** Connect Laptop 1 (Attacker) and Laptop 3 (Target Portal) to **Aiswarya's phone hotspot** (`ShadowGram-AP`).
2. **Lead Server Static IP:** On Linux Laptop 2 (ParadoxPete), the static IP is `192.168.43.2`.
3. **Endpoint Routing:**
   * In `swarm_runner.py`: Set `--target-url http://192.168.43.3:3000` (Laptop 3 AthenaPay portal) or `http://localhost:3000`.
   * In `telemetry.js`: Dispatch telemetry to `http://192.168.43.2:8000/telemetry` (Laptop 2 ShadowGram Core).

---

## 5. Quality Gate & Checkpoint Deliverable: `PROGRESS_CHECKPOINT_MEMBER3.md`

Whenever you complete a task, generate `PROGRESS_CHECKPOINT_MEMBER3.md` using the format in `00_CHECKPOINT_AND_INTEGRATION_PROTOCOL.md`.

### Verification Commands:
```bash
# 1. Test telemetry generation locally
python simulation/swarm_runner.py --target-url http://localhost:3000 --bots 3

# 2. Check if Laptop 2 received the packets
curl http://localhost:8000/api/graph | jq .nodes
```
