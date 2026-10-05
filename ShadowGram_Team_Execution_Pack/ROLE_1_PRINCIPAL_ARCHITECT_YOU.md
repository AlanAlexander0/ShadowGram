# Role 1: Principal Systems Architect & Graph Engine Lead
**Assignee:** Principal Architect (ParadoxPete)  
**Hardware & Station:** 🎮 Gaming Laptop #2 (Dedicated GPU) • Station: Laptop 2 (Command Cockpit)  
**Role Title:** Principal Systems Architect & Graph Engine Lead (Lead Developer / Orchestrator)  
**Core Responsibility:** End-to-end backend orchestration (`uvicorn main:app --host 0.0.0.0`), relational graph modeling, Louvain community detection, 2D-CNN ONNX integration, and master judge defense.

---

## 1. Role Mission & System Scope
You are the master builder of the ShadowGram engine. Your job is to construct the central processing hub on **Laptop 2** that receives real-time telemetry from both Laptop 1 (Red Team Swarm) and Laptop 3 (AthenaPay App), constructs the dynamic multi-layer relationship graph, clusters the syndicate using Louvain modularity, and serves live WebSockets to the 3D dashboard.

---

## 2. Master Component Architecture

```
[ Ingress WebSockets / REST: /telemetry ]
                  │
                  ▼
         [ FastAPI Dispatcher ]
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
 [ Kinetic 2D-CNN ]  [ Local Embeddings ]
 (ONNX Jerk Model)   (all-MiniLM-L6-v2)
        │                   │
        └─────────┬─────────┘
                  ▼
      [ Feature Vector Builder ] (x in R^D)
                  │
                  ▼
 [ Relational Multi-Layer Graph Engine ]
  • S_comp(u, v) = sum w_k * S_k(u, v)
  • Dynamic Adjacency Matrix (NetworkX)
                  │
                  ▼
   [ Louvain Modularity Clustering ]
  • Q-Optimization without fixed k
  • Isolates Coordinated Syndicates
                  │
                  ▼
[ WebSocket Broadcast to Next.js Cockpit ] (/ws/graph_live)
```

---

## 3. Atomic Task Specifications

### Task 1.1: FastAPI Core Server & Routing Skeleton
* **File:** `backend/main.py`
* **Requirements:**
  * Configure FastAPI app with CORS middleware enabled for all local LAN IPs (`192.168.*.*` and `localhost`).
  * Cryptographic anti-tamper middleware: Verify `telemetry_hmac` using session salt; reject raw cURL forge attempts with `401 Unauthorized`.
  * Register endpoints:
    * `POST /telemetry` (Ingests raw telemetry packets conforming to `00_CHECKPOINT_AND_INTEGRATION_PROTOCOL.md`).
    * `GET /api/graph` (Returns current nodes, edges, clusters, and modularity score $Q$).
    * `POST /api/quarantine` (Executes cluster quarantine state update).
    * `WebSocket /ws/telemetry` (Streams live events to dashboard).
    * `GET /health` (Quick heartbeat probe).

### Task 1.2: Relational Graph Engine & Louvain Clustering
* **File:** `backend/graph_engine.py`
* **Requirements:**
  * Build class `ShadowGraphEngine`:
    * Maintains an active in-memory `networkx.Graph()`.
    * **Sliding Temporal Window ($T = 10\text{ min}$):** Purges sessions older than 10 minutes to bound total edge count $m \le 500$, mathematically nullifying the Fortunato-Barthélemy (2007) modularity resolution limit.
    * Computes pairwise composite similarity across active sessions:
      $$S_{\text{comp}}(u, v) = w_{\text{time}} S_{\text{time}} + w_{\text{nav}} S_{\text{nav}} + w_{\text{sem}} S_{\text{sem}} + w_{\text{kin}} S_{\text{kin}} + w_{\text{env}} S_{\text{env}}$$
    * **3-Layer Sparsification Filter:** Instantiate edge $(u, v)$ if and only if $S_{\text{comp}} \ge 0.78$ across $\ge 3$ active layers (pruning $>98\%$ of background edges).
    * Executes `community.louvain_communities(G, weight='weight')` to partition graph in sub-5ms CPU time ($O(E \log V)$).
    * Formats plain-English factual reasons for any cluster with size $\ge 3$:
      * Path overlap % (LCS reduction).
      * Arrival synchronization $\Delta t$.
      * Semantic cosine similarity.

### Task 1.3: Kinetic Trajectory Classifier Integration (ONNX Runtime)
* **File:** `backend/kinetic_classifier.py`
* **Requirements:**
  * Load pre-exported lightweight 2D-CNN ONNX model (`models/kinetic_jerk_cnn.onnx`) via `onnxruntime.InferenceSession`.
  * Input: 128x128 2D trajectory image / acceleration spectrogram matrix.
  * Output: Float probability score $P_{\text{synthetic}} \in [0.0, 1.0]$.
  * Performance constraint: Inference latency must be $< 10\text{ms}$ on CPU.

### Task 1.4: Local Sentence Embeddings Worker
* **File:** `backend/embedding_worker.py`
* **Requirements:**
  * Load HuggingFace model `sentence-transformers/all-MiniLM-L6-v2` locally on CPU.
  * Encodes loan request narratives / profile bios into 384-dimensional dense float vectors.
  * Calculates pairwise cosine similarity:
    $$\text{Cosine}(A, B) = \frac{A \cdot B}{\|A\| \|B\|}$$

### Task 1.5: In-Memory 1-Click Simulation Fallback
* **File:** `backend/mock_simulation.py`
* **Requirements:**
  * Pre-bakes a deterministic dataset of 80 legitimate human sessions and 20 synchronized AI bot sessions.
  * Triggered via `POST /api/simulate_swarm`.
  * Instantly populates the graph engine to guarantee a flawless live demo if LAN Wi-Fi fails.

### Task 1.6: NVIDIA NIM Integration & 1500ms Circuit Breaker
* **File:** `backend/nim_client.py`
* **Requirements:**
  * Connect to NVIDIA NIM Free API (`meta/llama-3.3-70b-instruct`).
  * Enforce strict timeout wrapper: `asyncio.wait_for(nim_call(), timeout=1.5)`.
  * If the API call times out or returns HTTP 429/500, immediately fall back to local deterministic rule-based generator (`backend/fallback_sar.py`). The frontend will never stall waiting for cloud response.

---

## 4. Master Station Networking & Hotspot Architecture (Linux Lead Machine)

### A. Local Network Binding & IP Configuration
Your machine (Laptop 2) is the central server for all 4 laptops:
1. **Connect to Hotspot:** Connect your Linux laptop to **Aiswarya's phone hotspot** (`ShadowGram-AP`).
2. **Find Your Hotspot IP:**
   ```bash
   hostname -I
   # Identifies your local IP (e.g., 192.168.43.2)
   ```
3. **Mandatory Uvicorn Host Binding (`0.0.0.0`):**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
   *(Never bind to `127.0.0.1` or `localhost`, as that blocks external incoming requests from Alan's and Nihad's laptops).*
4. **Linux Firewall Verification:**
   If your Linux distribution has `ufw` or `firewalld` active, permit port 8000:
   ```bash
   sudo ufw allow 8000/tcp
   ```

---

## 5. Quality Gate & Checkpoint Deliverable: `PROGRESS_CHECKPOINT_LEAD.md`

At each milestone, compile `PROGRESS_CHECKPOINT_LEAD.md` using the format in `00_CHECKPOINT_AND_INTEGRATION_PROTOCOL.md`.

### Verification Suite:
```bash
# 1. Run backend unit tests
pytest tests/test_backend.py -v

# 2. Test live telemetry ingestion via curl
curl -X POST http://localhost:8000/telemetry \
  -H "Content-Type: application/json" \
  -d '{"session_id":"test-1","account_id":"ACC-001","timestamp":1727999999.1,"event_type":"keydown","payload":{"key_flight_time_ms":42.5}}'

# 3. Verify graph output
curl -X GET http://localhost:8000/api/graph | jq .
```
