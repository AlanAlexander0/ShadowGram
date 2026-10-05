# Role 2: Visual Command Center & 3D WebGL Lead
**Assignee:** Aiswarya Kallayil Rajesh  
**Hardware & Station:** 🎮 Gaming Laptop #2 (Dedicated GPU for 60 FPS Three.js Bloom) • Station: Laptop 2 (Shared Display Cockpit)  
**Role Title:** Visual Command Center & 3D WebGL Lead (Frontend Architecture)  
**Core Responsibility:** Next.js 14 dashboard, 3D WebGL particle graph, dark liquid-glass UI styling, live simulation controls, and the "Why Card" modal.

---

## 🤖 MANDATORY INSTRUCTION BLOCK FOR AI CODING ASSISTANTS
> **INSTRUCTION FOR CHATGPT / CLAUDE / CURSOR / COPILOT:**  
> You are an elite Next.js and Three.js frontend engineer assisting **Aiswarya** in building the ShadowGram Command Cockpit.
> 
> **STRICT COMPLIANCE RULES:**
> 1. You **MUST** strictly adhere to the frozen API schemas in `00_CHECKPOINT_AND_INTEGRATION_PROTOCOL.md`. Do NOT invent custom API routes, query parameters, or payload keys.
> 2. You **MUST NOT** hardcode static mock data inside components. All graph data must be fetched dynamically from `http://localhost:8000/api/graph` or received via WebSocket `ws://localhost:8000/ws/telemetry`.
> 3. Implement the exact theme and CSS classes specified in `shadowgram-template by ais.md` (dark blue-purple `260 87% 3%`, `.liquid-glass`, Geist/General Sans).
> 4. At the end of every response, you **MUST generate a `PROGRESS_CHECKPOINT_AISWARYA.md`** report summarizing modified files, components created, and code snippets for the Lead Architect to review.

---

## 1. Role Mission & System Scope
Your mission is to build the visual centerpiece of ShadowGram that runs on **Laptop 2** (displayed on the main screen/projector for the judges). When the Red Team attacks, your dashboard must visually convey the threat: legitimate users float as calm blue stars, red laser-like connection lines snap across the bot swarm in 3D space, and a single click opens the plain-English "Why Card".

---

## 2. Dashboard Layout & Component Hierarchy

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ NAVBAR: Logo [SHADOWGRAM]  |  Live Telemetry: [CONNECTED]  |  Mode: [3D/2D] │
├─────────────────────────────────────────────────────────────────────────────┤
│ HERO METRICS BAR:                                                           │
│ [ Accounts: 100 ] [ Relationships: 248 ] [ Clusters: 1 ] [ Modularity: 0.72]│
├──────────────────────────────────────┬──────────────────────────────────────┤
│ 3D WEBGL GRAPH CANVAS (Center-Left)   │ KINETIC SPECTROGRAM PANEL (Top-Right)│
│ • react-force-graph-3d               │ • Dynamic 2D mouse trajectory canvas │
│ • Blue Nodes: Organic human users    │ • Live CNN score: "99.4% Synthetic"  │
│ • Red Nodes: AI bot accounts         ├──────────────────────────────────────┤
│ • Glowing red edges between bots     │ SIMULATION & RED-TEAM CONTROLS       │
│ • Orbital camera controls            │ • Button: [ 🔥 Deploy 20 AI Bots ]   │
│ • 1-Click Toggle: [ Switch to 2D ]   │ • Button: [ 🛑 QUARANTINE CLUSTER ]  │
├──────────────────────────────────────┴──────────────────────────────────────┤
│ MODAL: "WHY ARE THESE ACCOUNTS LINKED?" (Pops open on cluster click)         │
│ • Explains 4-step route overlap (/auth -> /kyc -> /loan_submit)             │
│ • Shows Δt = 38ms ingress arrival synchronization                            │
│ • Shows 0.89 semantic intent cosine similarity                               │
│ • Button: [ 📄 Export Legal SAR Report PDF ] (Calls Laptop 4 API)           │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Atomic Task Specifications

### Task 2.1: Project Setup & Liquid-Glass Theme System
* **Directory:** `frontend/`
* **Stack:** Next.js 14 (App Router), Tailwind CSS, Framer Motion, `@fontsource/geist-sans`.
* **Requirements:**
  * Configure `index.css` with the CSS variables from `shadowgram-template by ais.md`:
    * Background: `hsl(260, 87%, 3%)` (deep dark blue-purple).
    * Foreground: `hsl(40, 6%, 95%)` (off-white).
    * Accent: Indigo / violet / cyan gradients.
  * Implement the `.liquid-glass` CSS utility class:
```css
.liquid-glass {
  background: rgba(255, 255, 255, 0.015);
  backdrop-filter: blur(12px);
  box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.08);
}
```

### Task 2.2: High-Performance 3D WebGL Force-Directed Graph (`react-force-graph-3d`)
* **File:** `frontend/components/GraphCanvas.tsx` & `frontend/materials/LaserEdgeMaterial.ts`
* **Performance Architecture:**
  * **Single `THREE.InstancedMesh`:** Use instanced geometry to render all nodes in a single GPU draw call. Update positions via dynamic transformation matrices (`setMatrixAt`).
  * **Single-Pass Emissive Laser Edge Shader (Zero Bloom Overhead):** Use this self-contained shader material that creates an optical bloom illusion in a single forward pass without needing heavy post-processing buffers:
```typescript
// frontend/materials/LaserEdgeMaterial.ts - Single-Pass Emissive Shader (Zero Bloom Lag)
import * as THREE from 'three';

export function createLaserEdgeMaterial(laserColor = 0xef4444, speed = 2.5, frequency = 4.0) {
  return new THREE.ShaderMaterial({
    uniforms: {
      uTime: { value: 0.0 },
      uColor: { value: new THREE.Color(laserColor) },
      uSpeed: { value: speed },
      uFrequency: { value: frequency },
      uPulseWidth: { value: 0.35 },
    },
    vertexShader: `
      varying vec2 vUv;
      void main() {
        vUv = uv;
        gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
      }
    `,
    fragmentShader: `
      uniform float uTime;
      uniform vec3 uColor;
      uniform float uSpeed;
      uniform float uFrequency;
      uniform float uPulseWidth;
      varying vec2 vUv;

      void main() {
        float d = abs(vUv.y - 0.5) * 2.0;
        float core = exp(-d * d * 32.0);          // High-energy Gaussian core filament
        float halo = 1.0 / (1.0 + 14.0 * d * d);  // Lorentzian atmospheric scattering mantle
        
        float wave = sin(vUv.x * uFrequency * 6.28318 - uTime * uSpeed);
        float pulse = smoothstep(1.0 - uPulseWidth, 1.0, wave);
        float dash = step(0.15, fract(vUv.x * uFrequency - uTime * (uSpeed * 0.15)));
        
        float energy = (0.25 + 0.75 * pulse) * dash;
        vec3 finalRgb = (uColor * halo + vec3(1.0) * core * 1.5) * energy;
        float alpha = clamp(core + halo * 0.6, 0.0, 1.0) * energy;

        gl_FragColor = vec4(finalRgb, alpha);
      }
    `,
    transparent: true,
    blending: THREE.AdditiveBlending,
    depthWrite: false,
    side: THREE.DoubleSide,
  });
}
```
  * **Automated Catmull-Rom Spline Camera Path:** When a cluster is detected, smoothly swoop the orbital camera into a focused dramatic fly-around of the syndicate centroid:
    `camera.position.copy(spline.getPoint(t)); camera.lookAt(clusterCentroid);`
  * Node colors:
    * `risk_label === "normal_organic"` $\to$ Soft glowing cyan/blue (`#22d3ee`).
    * `risk_label === "suspicious_syndicate"` $\to$ Pulsing crimson red (`#ef4444`).
    * `status === "quarantined"` $\to$ Locked grey shield (`#64748b`).
  * **2D Fallback Toggle:** Add a top-right button `[ 2D / 3D ]` that dynamically switches between `ForceGraph3D` and `ForceGraph2D` if hardware ever lags.

### Task 2.3: Interactive "Why Card" Modal & 4-Stage Quarantine Shockwave
* **File:** `frontend/components/WhyCardModal.tsx` & `frontend/components/QuarantineShockwave.ts`
* **Requirements:**
  * When a user clicks any node or cluster, a frosted `.liquid-glass` modal slides into view.
  * Displays:
    * Cluster ID and count of involved accounts (e.g., *"Cluster #01 — 20 Accounts Detected"*).
    * Visual progress meters for the 4 evidence dimensions:
      1. Navigation Sequence Overlap (e.g., 96%).
      2. Micro-Temporal Arrival Sync (e.g., $\Delta t < 40\text{ms}$).
      3. Semantic Loan Narrative Similarity (e.g., 0.89 Cosine).
      4. Kinetic Jerk Biomechanical Score (e.g., 0.04 Constant Jerk).
    * Plain-English explanation text: *"Signals consistent with coordinated multi-agent automation."*
    * Button: **`[ 🛑 Quarantine Entire Cluster ]`** (Dispatches `POST /api/quarantine`).
    * Button: **`[ 📄 Download Legal SAR Dossier ]`** (Dispatches `GET /api/sar/export`).
  * **4-Stage Quarantine Shockwave Sequence:**
    1. $T = 0\text{ms}$: Crimson shockwave ring expands from cluster center.
    2. $T = 200\text{ms}$: Swarm nodes shudder and repel slightly from organic nodes.
    3. $T = 400\text{ms}$: Translucent wireframe geometric containment sphere renders around syndicate.
    4. $T = 600\text{ms}$: Nodes desaturate to slate grey with shield icon; SAR download badge glows.

### Task 2.4: Kinetic Trajectory Spectrogram Canvas
* **File:** `frontend/components/KineticSpectrogram.tsx`
* **Requirements:**
  * Renders a 128x128 live canvas showing the mouse coordinates $(x, y, t)$ of the selected account.
  * Shows acceleration heatmap colors (blue = low acceleration, yellow/red = peak acceleration).
  * Displays a live CNN prediction tag: *"Kinetic Trajectory: SYNTHETIC BÉZIER (99.2% Confidence)"*.

### Task 2.5: Live Simulation Controls & Fallback Bar
* **File:** `frontend/components/ControlBar.tsx`
* **Requirements:**
  * Button `[ 🔥 Deploy 20 AI Bots ]`: Calls `POST /api/simulate_swarm` to populate the graph in-memory if LAN Wi-Fi fails.
  * Button `[ 🔄 Reset Environment ]`: Clears the graph state via `POST /api/reset`.

### Task 2.6: Procedural Web Audio Engine (`CyberAudioEngine`)
* **File:** `frontend/utils/CyberAudioEngine.ts`
* **Implementation:** Zero external sound files. Uses native W3C `AudioContext` with zero latency:
```typescript
// frontend/utils/CyberAudioEngine.ts - Zero Asset Procedural Audio
export function playProceduralSFX(ctx: AudioContext, type: 'subbass' | 'glitch'): void {
  const now = ctx.currentTime, master = ctx.createGain();
  master.connect(ctx.destination);
  
  if (type === 'subbass') {
    // Cinematic Sub-Bass Drop (120 Hz -> 30 Hz logarithmic decay)
    const osc = ctx.createOscillator();
    osc.frequency.setValueAtTime(120, now);
    osc.frequency.exponentialRampToValueAtTime(30, now + 1.2);
    master.gain.setValueAtTime(1.0, now);
    master.gain.exponentialRampToValueAtTime(0.001, now + 1.2);
    osc.connect(master);
    osc.start(now); osc.stop(now + 1.2);
  } else {
    // Cyber-Glitch Telemetry Chirp (Chowning FM modulation at 2400 Hz -> 800 Hz)
    const carrier = ctx.createOscillator(), mod = ctx.createOscillator(), modGain = ctx.createGain();
    carrier.frequency.setValueAtTime(2400, now);
    carrier.frequency.linearRampToValueAtTime(800, now + 0.015);
    mod.frequency.setValueAtTime(850, now);
    modGain.gain.setValueAtTime(1200, now);
    mod.connect(modGain);
    modGain.connect(carrier.frequency);
    master.gain.setValueAtTime(0.7, now);
    master.gain.exponentialRampToValueAtTime(0.001, now + 0.015);
    carrier.connect(master);
    mod.start(now); carrier.start(now);
    mod.stop(now + 0.015); carrier.stop(now + 0.015);
  }
}
```
  * Includes a mute toggle button in the navbar for noisy hackathon venues.

---

## 4. Aiswarya's Hotspot Hub Setup & Windows Defender Settings

### A. Aiswarya's Dedicated Phone Hotspot Setup (Google Pixel / Jio SIM)
As the owner of the hotspot phone, you provide the local LAN foundation for all 4 laptops:
1. **Continuous Power:** Keep your phone connected to a dedicated USB-C power bank for the entire hackathon.
2. **Android Developer Options (One-Time Setup):**
   * Enable **"Stay Awake While Charging"** (Settings $\to$ System $\to$ Developer Options). Prevents Android Wi-Fi sleep.
   * Enable **"Tethering Hardware Acceleration"**.
   * Turn OFF **"Wi-Fi Power Saving Mode"**.
3. **Hotspot Configuration:**
   * Hotspot Name / SSID: `ShadowGram-AP` (or similar).
   * AP Band: 5 GHz (preferred for lowest latency) or 2.4 GHz.
   * Confirm AP Isolation is OFF (default on Android).
   * *Zero Data Cost Note:* Intra-laptop LAN traffic (`192.168.43.x`) communicates directly through your phone's Wi-Fi router chip; it does NOT consume cellular data when laptops communicate locally with each other!

### B. Windows Defender Firewall Rule (Administrative PowerShell)
If developing on Windows, run this in an **Administrative PowerShell** so incoming dashboard and WebSocket requests are never blocked:
```powershell
netsh advfirewall firewall add rule name="ShadowGram Frontend" dir=in action=allow protocol=TCP localport=3000
netsh advfirewall firewall add rule name="ShadowGram Backend" dir=in action=allow protocol=TCP localport=8000
```
*(If the Windows popup asks: "Allow app to communicate on Private networks?" $\to$ **Check 'Private networks' and click 'Allow'**).*

---

## 5. Quality Gate & Checkpoint Deliverable: `PROGRESS_CHECKPOINT_AISWARYA.md`

Whenever you complete a component, generate `PROGRESS_CHECKPOINT_AISWARYA.md` using the format in `00_CHECKPOINT_AND_INTEGRATION_PROTOCOL.md`.

### Verification Commands:
```bash
cd frontend
npm install
npm run build
npm run dev
# Open http://localhost:3000 and verify 3D graph and modals render smoothly
```
