# ShadowGram: Master Checkpoint, Quality Gate & Integration Protocol
**Document Code:** `SG-PROTO-00`  
**Target Event:** HackAthena 2.0  
**Authority:** Principal Systems Architect (Lead)  
**Applicability:** All 4 Team Members & Autonomous AI Assistants

---

## 1. Purpose & The "Anti-Hallucination" Mandate

In hackathons where team members use AI coding assistants (ChatGPT, Claude, Cursor, Copilot), the single greatest failure mode is **"Architectural Drift & Hallucination."** 

An AI given an isolated prompt will often:
1. Invent custom, incompatible API endpoints (e.g., using `/api/v2/user_telemetry` instead of the locked `/telemetry`).
2. Hardcode fake mock data inside UI components instead of connecting to the real FastAPI backend.
3. Introduce conflicting dependencies (e.g., pulling in heavy cloud libraries when the system is strictly local CPU).
4. Shift variable names (e.g., `user_id` vs `account_id`, `flight_time` vs `ft_delta`).

**This protocol enforces an unbreakable contract.** Every team member and every AI assistant working on ShadowGram must adhere to the data schemas, verification gates, and checkpoint reporting defined in this document.

---

## 2. The Checkpoint Reporting Lifecycle

Every team member has a dedicated role document with assigned milestones. At each milestone, the member (or their AI assistant) **MUST generate a standardized markdown checkpoint report** along with their working code files before anything is merged into the master repository.

```
┌────────────────────────────────────────────────────────────────────────┐
│                        MILESTONE EXECUTION CYCLE                       │
├────────────────────────────────────────────────────────────────────────┤
│ 1. READ ROLE SPECIFICATION: Read assigned atomic module & schemas.     │
│ 2. CODE & TEST LOCALLY: Write code and run local verification tests.  │
│ 3. GENERATE PROGRESS REPORT: Compile `PROGRESS_CHECKPOINT_<NAME>.md`.  │
│ 4. SUBMIT TO LEAD ARCHITECT: Hand over code + checkpoint file.         │
│ 5. ARCHITECTURAL AUDIT: Lead Architect runs the verification suite.    │
│ 6. MERGE TO MASTER: Module is integrated into the live cyber-range.    │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Mandatory Format for `PROGRESS_CHECKPOINT_<NAME>.md`

Whenever a team member completes a task, their AI assistant must generate this exact progress report file:

```markdown
# Progress Checkpoint Report: [ROLE NAME / MEMBER NAME]
**Checkpoint ID:** CP-[ROLE]-[MILESTONE_NUMBER] (e.g., CP-REDTEAM-01)  
**Date & Time:** [ISO Timestamp]  
**Assigned Module:** [e.g., Playwright Swarm Engine / 3D Force Graph / SQLite Schema]

### 1. Deliverables Created / Modified
- `path/to/file1.py` (New / Modified) - [Brief description of what was coded]
- `path/to/file2.tsx` (New / Modified) - [Brief description of what was coded]

### 2. API Contract Compliance Audit
- [ ] Confirmed: All endpoints match the schemas in `00_CHECKPOINT_AND_INTEGRATION_PROTOCOL.md`.
- [ ] Confirmed: No hardcoded mock data bypasses the backend API.
- [ ] Confirmed: Zero cloud dependencies (runs 100% locally on CPU).
- [ ] Confirmed: All variable names match the global dictionary.

### 3. Local Verification & Test Output
[Paste terminal output of the test command here, e.g., pytest results, curl response, or console log]

### 4. Code Excerpts for Lead Architect Audit
```python
# Paste the core logic functions here for rapid inspection
```

### 5. Identified Blockers or Cross-Laptop Dependencies
[State any questions or dependencies on other laptops/modules]
```

---

## 4. Master Data Dictionaries & Global API Contracts

All modules across all 4 laptops must communicate using these **frozen JSON schemas**:

### A. Ingress Telemetry Endpoint: `POST /telemetry`
* **Consumer:** Laptop 2 (FastAPI Server)
* **Producers:** Laptop 3 (AthenaPay Web Portal) & Laptop 1 (Playwright Swarm Runner)
* **Payload Specification:**
```json
{
  "session_id": "string (UUIDv4)",
  "account_id": "string (e.g., ACC-89412)",
  "timestamp": "float (Unix timestamp with millisecond precision)",
  "event_type": "string (keydown | pointerdown | route_change | honey_dom_trip)",
  "telemetry_hmac": "string (hex HMAC-SHA256 signature generated with session salt)",
  "payload": {
    "key_flight_time_ms": "float (optional, delta between key releases)",
    "key_dwell_time_ms": "float (optional, keydown to keyup)",
    "pointer_curvature_jerk": "float (optional, d3x/dt3 derivative value)",
    "pointer_coordinates": "array of [x, y, t] (optional, max 100 points)",
    "route_path": "string (optional, e.g., /auth -> /kyc -> /loan_submit)",
    "tripwire_id": "string (optional, e.g., #honey-dom-profile-sync)",
    "client_canvas_hash": "string (hex hash, optional)"
  }
}
```
*Note on `telemetry_hmac`:* Generated client-side using `HMAC_SHA256(session_id + timestamp, session_salt)`. Disallows forged cURL injection or synthetic replay from outside the client runtime.

### B. Graph Query Endpoint: `GET /api/graph`
* **Producer:** Laptop 2 (FastAPI Server)
* **Consumer:** Laptop 2 (Next.js Dashboard) & Laptop 4 (Compliance Station)
* **Response Specification:**
```json
{
  "nodes": [
    {
      "id": "ACC-89412",
      "session_id": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
      "cluster_id": 1,
      "risk_label": "suspicious_syndicate | normal_organic | anomaly_outlier",
      "kinetic_jerk_score": 0.04,
      "semantic_intent_vector": [0.12, -0.45, "... 384 dims ..."]
    }
  ],
  "links": [
    {
      "source": "ACC-89412",
      "target": "ACC-89415",
      "weight": 0.89,
      "converged_layers": ["timing", "navigation", "semantic", "kinetics"],
      "delta_t_seconds": 0.038
    }
  ],
  "clusters": [
    {
      "cluster_id": 1,
      "size": 20,
      "modularity_q": 0.72,
      "status": "active | quarantined",
      "factual_reasons": [
        "96% FSM route overlap (/auth -> /kyc -> /loan_submit)",
        "38ms inter-arrival synchronization across 20 accounts",
        "0.89 semantic cosine similarity on loan text"
      ]
    }
  ]
}
```

### C. Cluster Quarantine Endpoint: `POST /api/quarantine`
* **Producer:** Laptop 4 (Compliance Station) or Laptop 2 (Dashboard Button)
* **Consumer:** Laptop 2 (FastAPI Server)
* **Payload:**
```json
{
  "cluster_id": 1,
  "action": "isolate | step_up_challenge | release",
  "reason": "Coordinated multi-agent swarm detected via Louvain community clustering",
  "operator_id": "OFFICER-04"
}
```

---

## 5. Milestone Integration Schedule

| Milestone | Target Objective | Verification Command / Quality Gate |
| :--- | :--- | :--- |
| **M1: Ingestion Pipeline** | Laptop 2 receives telemetry from local test script; SQLite logs events in `shadowgram.db`. | `curl -X POST http://localhost:8000/telemetry -H "Content-Type: application/json" -d @test_payload.json` $\to$ Returns `200 OK`. |
| **M2: Relational Graph & Louvain** | NetworkX builds adjacency matrix from active sessions and isolates test cluster with modularity $Q > 0.60$. | `pytest tests/test_graph_engine.py` $\to$ Passes with 100% assertion on 20-node synthetic swarm. |
| **M3: 3D Visualization & "Why Card"** | Next.js dashboard connects via WebSocket, renders nodes in 3D WebGL, and pops the "Why Card" on click. | Visual inspection on `http://localhost:3000`: Nodes pulse, red laser links snap between bots, camera rotates. |
| **M4: Red-Team LAN Attack** | Laptop 1 dispatches 20 Playwright agents across local Wi-Fi to Laptop 3; Laptop 2 detects and quarantines in <3s. | Live 4-laptop dry run: Judge on Laptop 3 stays unaffected while Laptop 1 bots are locked in grey shields. |
| **M5: Legal SAR PDF Export** | Laptop 4 clicks `[Export SAR]` $\to$ NVIDIA NIM formats legal narrative (<1500ms timeout circuit breaker) $\to$ 2-page PDF downloads cleanly. | Verify downloaded PDF contains cluster graph snapshot, timestamp, and 3 CFPB reason codes. Fallback deterministic generator triggers if NIM takes >1.5s. |

---

## 7. Cross-Platform Environment: Linux vs. Windows (Zero Docker)

* **Decision: NO DOCKER.**  
  Docker Desktop on Windows requires BIOS virtualization (VT-x), WSL2, and 4GB+ RAM. Setting it up on teammates' Windows laptops during a hackathon is prone to errors and creates bridge network isolation.
* **The Reality:** Python and Node.js are already 100% cross-platform:
  * Linux Lead: `python3 -m venv venv && source venv/bin/activate` | `npm run dev`
  * Windows Teammates: `py -m venv venv && .\venv\Scripts\activate` | `npm run dev`
* **Two Strict Cross-Platform Rules:**
  1. **Path Handling:** In Python, **never** hardcode slashes like `"data/file.json"`. Always use `pathlib.Path("data") / "file.json"` or `os.path.join("data", "file.json")`.
  2. **Windows Defender Firewall Rule (Administrative PowerShell):**  
     To prevent Windows from silently dropping incoming hotspot packets, Windows teammates should run this single command in an Administrative PowerShell:
     ```powershell
     netsh advfirewall firewall add rule name="ShadowGram Port 8000" dir=in action=allow protocol=TCP localport=8000
     ```
     *(If the graphical prompt appears: "Allow app to communicate on Private networks?" $\to$ **Check 'Private networks' and click 'Allow'**).*

---

## 8. Hotspot & Local LAN Networking Guide (Aiswarya's Phone / Jio SIM Dedicated AP)

To connect the 4 laptops seamlessly without venue Wi-Fi:

1. **FastAPI Host Binding (`0.0.0.0`):**  
   On Laptop 2 (Linux Server), you **MUST** run:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
   *(Binding to `127.0.0.1` or `localhost` blocks external laptops. `0.0.0.0` allows all hotspot laptops to connect).*
2. **Dedicated Aiswarya Phone Hotspot Setup (Google Pixel / Jio):**  
   * **Power Management:** Connect Aiswarya's phone to a dedicated USB-C power bank continuously.
   * **Developer Options Settings:**
     * Enable **"Stay Awake While Charging"** (prevents Wi-Fi radio sleep).
     * Enable **"Tethering Hardware Acceleration"**.
     * Turn OFF "Wi-Fi Power Saving Mode".
   * **Lead Laptop Static IP:** Assign static IP `192.168.43.2` to Laptop 2 (Linux Host). All client laptops connect to: `http://192.168.43.2:8000`.
3. **Hotspot AP Isolation Warning:**  
   * **Android Hotspot (Google Pixel):** Does NOT enable client isolation; laptops ping each other with sub-2ms latency.
   * **iPhone Hotspot:** Often forces "Client Isolation" (blocks laptop-to-laptop traffic). If using iPhone, bring an offline portable home Wi-Fi router (no internet needed, just plug into wall power so all 4 laptops share the same router network).
4. **No CI/CD Pipeline:**  
   Do not set up GitHub Actions or automated cloud build pipelines. Version control uses a standard GitHub repository with individual branches (`git checkout -b feature-frontend`), merged locally on the Lead's Linux machine.

---

## 9. Hardware Allocation Matrix (2 Gaming + 2 Normal Laptops)

Only two roles require heavy hardware; the other two run on standard, basic laptops:

| Station | Assigned Role | Required Hardware Tier | Workload / Why |
| :--- | :--- | :--- | :--- |
| **Laptop 1** | **Red Team Attacker** | 🎮 **Gaming Laptop #1** (Multi-Core CPU) | Spawns 20 parallel Playwright Chromium browser contexts. **Resource Optimization Rule:** Single Chromium instance with 20 browser contexts + route-abort media (`context.route("**/*.{png,jpg,jpeg,svg,woff,woff2,css,gif}", lambda route: route.abort())`) keeping RAM strictly **< 600MB**. |
| **Laptop 2** | **ShadowGram Cockpit** | 🎮 **Gaming Laptop #2** (Dedicated GPU) | Hosts FastAPI + SQLite + ONNX 2D-CNN + **3D WebGL Three.js Particle Universe**. Uses `THREE.InstancedMesh` and half-resolution selective bloom (`w/2, h/2`) for rock-solid 60 FPS. |
| **Laptop 3** | **AthenaPay Portal** | 💻 **Normal Laptop #1** (Basic Office Specs) | Renders standard loan web form for live judge testing (< 200MB RAM). Form is 95% pre-filled with single 3-word reason box to ensure <6s test cycle. |
| **Laptop 4** | **Compliance Station** | 💻 **Normal Laptop #2** (Basic Office Specs) | Displays compliance list and downloads SAR PDF via ReportLab. Heavy LLM runs on NVIDIA's cloud with a 1500ms circuit breaker (< 300MB RAM). |
