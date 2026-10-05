# Role 4: Data Engineering, NVIDIA LLM & Legal SAR Lead
**Assignee:** Teammate 4 (Mohammed Nihad PC / Ashlin Theres James)  
**Hardware & Station:** 💻 Normal Laptop #2 (Basic Office Specs / Lightweight) • Station: Laptop 4 (Compliance Station) • Heavy AI runs via NVIDIA Cloud API  
**Role Title:** Data Engineering, NVIDIA LLM & Legal SAR Lead (Compliance & Data Architecture)  
**Core Responsibility:** SQLite database models, NVIDIA NIM API legal narrative generation, automated ReportLab SAR PDF exporter, and lightweight KYC ID image artifact scanner.

---

## 🤖 MANDATORY INSTRUCTION BLOCK FOR AI CODING ASSISTANTS
> **INSTRUCTION FOR CHATGPT / CLAUDE / CURSOR / COPILOT:**  
> You are an elite Python backend and data compliance engineer assisting **Teammate 4** in building the data persistence and legal compliance engine for ShadowGram.
> 
> **STRICT COMPLIANCE RULES:**
> 1. You **MUST** strictly adhere to the SQLite database schema defined in `00_CHECKPOINT_AND_INTEGRATION_PROTOCOL.md`.
> 2. The PDF report generator must use Python's `ReportLab` library (runs 100% locally with zero cloud dependencies).
> 3. The NVIDIA NIM API calls must handle rate limits gracefully and include a local fallback cache if internet is slow during the hackathon.
> 4. At the end of every task, you **MUST generate a `PROGRESS_CHECKPOINT_MEMBER4.md`** report summarizing modified files, test outputs, and code snippets for the Lead Architect to review.

---

## 1. Role Mission & System Scope
Your mission is to handle the **data persistence and legal credibility** of ShadowGram:
* **On Laptop 2/4:** You maintain the single-file database (`shadowgram.db`) that records every incoming session and cluster.
* **On Laptop 4:** When a cluster is quarantined, your script takes the raw graph metrics, feeds them to the free **NVIDIA NIM API (Llama-3.3-70B)**, and auto-generates a formal, 2-page **Suspicious Activity Report (SAR) PDF** formatted for bank compliance officers and regulators under **CFPB Circular 2023-03**.
* **On Laptop 3:** You deploy a lightweight image scanner that inspects uploaded KYC identity cards for synthetic generation artifacts.

---

## 2. Compliance & Data Flow Pipeline

```
[ Incoming Telemetry Stream ]
             │
             ▼
[ SQLite Database: shadowgram.db ]
  ├── Table: sessions (id, account_id, ip_hash, created_at)
  ├── Table: telemetry_events (session_id, event_type, ft, dt, jerk)
  └── Table: clusters (cluster_id, size, modularity_q, status)
             │
             ▼ (When Operator clicks [ Export Legal SAR Report ])
[ NVIDIA NIM API (Llama-3.3-70B) ]
  • Input: Raw cluster telemetry metrics (96% route overlap, 38ms Δt, 0.89 cosine)
  • Prompt: Formats factual legal reason codes satisfying CFPB Circular 2023-03
  • Output: Structured executive legal narrative
             │
             ▼
[ ReportLab PDF Engine (generate_sar_pdf.py) ]
  • Compiles formal 2-page Suspicious Activity Report (SAR)
  • Embeds cluster topology snapshot, timestamp, and audit trail
  • Downloads instantly to Laptop 4 / Laptop 2 as a crisp PDF
```

---

## 3. Atomic Task Specifications

### Task 4.1: SQLite Database Models via SQLAlchemy
* **File:** `backend/database.py` & `backend/models.py`
* **Requirements:**
  * Define SQLAlchemy models:
    * `SessionModel`: `id` (UUID), `account_id`, `created_at`, `status` (active/quarantined).
    * `TelemetryEventModel`: `id`, `session_id`, `event_type`, `flight_time`, `dwell_time`, `jerk`, `route`.
    * `ClusterLogModel`: `id`, `cluster_id`, `node_count`, `modularity_q`, `quarantined_at`, `reasons_json`.
  * Creates `shadowgram.db` automatically on first run with zero configuration.

### Task 4.2: NVIDIA NIM Legal Narrative Generator & 1500ms Circuit Breaker
* **File:** `backend/sar_generator.py`
* **Requirements:**
  * Uses the team's free NVIDIA NIM API key (`meta/llama-3.3-70b-instruct`).
  * Function `generate_legal_narrative(cluster_data: dict) -> str`:
    * Inputs: Cluster size, Louvain modularity $Q$, average $\Delta t$, FSM route overlap, semantic cosine similarity.
    * Prompt:
      > *"You are a senior AML/Fraud compliance officer. Draft an official Suspicious Activity Report (SAR) executive summary for Syndicate Cluster #{cluster_id} containing {node_count} synthetic accounts. Formulate three specific, verifiable factual reason codes that strictly comply with CFPB Circular 2023-03 and ECOA Regulation B. Avoid generic risk scores."*
  * **Strict 1500ms Timeout Circuit-Breaker:**
    * Wrap invocation in `asyncio.wait_for(nim_request(), timeout=1.5)`.
    * If timeout occurs or HTTP 429/500 is returned, immediately fallback to local deterministic template:
      ```python
      # Deterministic fallback returns in <5ms:
      return deterministic_sar_narrative(cluster_data)
      ```
    * Guarantees the judge never sees a hanging spinner on Laptop 4 during the live demo.

### Task 4.3: Automated 2-Page SAR PDF Generator (ReportLab)
* **File:** `backend/generate_sar_pdf.py`
* **Requirements:**
  * Uses `reportlab.platypus` (`SimpleDocTemplate`, `Paragraph`, `Spacer`, `Table`, `Image`).
  * Page 1:
    * Official Bank Compliance Header: *"FINANCIAL CRIMES ENFORCEMENT & COMPLIANCE DOSSIER"*.
    * Incident Metadata table: Date, Cluster ID, Involved Accounts, Risk Modality ($Q = 0.72$).
    * Executive Summary generated by NVIDIA NIM (or instantaneous deterministic fallback).
    * Embedded visual snapshot of the clustered network graph.
  * Page 2:
    * Evidence Matrix Table (Interaction, Navigation, Timing, Content, Environment).
    * Factual Adverse Action Reason Codes (CFPB Circular 2023-03 compliant).
    * Compliance Officer Signature & Quarantine Timestamp block.

### Task 4.4: Lightweight KYC Document Artifact Scanner
* **File:** `backend/kyc_scanner.py`
* **Requirements:**
  * Runs on Laptop 3 when an applicant uploads an ID card.
  * Analyzes the image using Python `PIL` / `OpenCV`:
    * Error Level Analysis (ELA) to check compression differences.
    * Sharpness / high-frequency noise variance to detect diffusion model generation.
  * Outputs a float score: `synthetic_image_score` $\in [0.0, 1.0]$.
  * Included in the telemetry packet under `client_id_artifact_score`.

---

## 4. Station Networking & Windows Defender Firewall Configuration

### A. Windows Defender Firewall Rule (Administrative PowerShell)
If developing on Windows, run this in an **Administrative PowerShell** on Laptop 4 to guarantee communication with Laptop 2 is never dropped:
```powershell
netsh advfirewall firewall add rule name="ShadowGram Port 8000" dir=in action=allow protocol=TCP localport=8000
netsh advfirewall firewall add rule name="ShadowGram Port 8501" dir=in action=allow protocol=TCP localport=8501
```
*(If the Windows popup asks: "Allow app to communicate on Private networks?" $\to$ **Check 'Private networks' and click 'Allow'**).*

### B. Hotspot LAN Connection Guide (Connecting to Aiswarya's Phone)
1. **Connect to Wi-Fi:** Connect Laptop 4 to **Aiswarya's phone hotspot** (`ShadowGram-AP`).
2. **Lead Server Static IP:** On Linux Laptop 2 (ParadoxPete), the static IP is `192.168.43.2`.
3. **Endpoint Routing:**
   * Query graph metrics: `GET http://192.168.43.2:8000/api/graph`.
   * Submit quarantine action: `POST http://192.168.43.2:8000/api/quarantine`.
   * Trigger SAR download: `GET http://192.168.43.2:8000/api/sar/export`.

---

## 5. Quality Gate & Checkpoint Deliverable: `PROGRESS_CHECKPOINT_MEMBER4.md`

Whenever you complete a task, generate `PROGRESS_CHECKPOINT_MEMBER4.md` using the format in `00_CHECKPOINT_AND_INTEGRATION_PROTOCOL.md`.

### Verification Commands:
```bash
# 1. Test database table creation
python -c "from backend.database import init_db; init_db()"

# 2. Test NVIDIA SAR PDF generation
python backend/generate_sar_pdf.py --cluster-id 1

# 3. Verify PDF was generated cleanly
ls -lh generated_reports/SAR_Cluster_1.pdf
```
