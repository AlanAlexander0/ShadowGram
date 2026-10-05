import os
import asyncio
import requests
from typing import Dict, Any
from backend.fallback_sar import deterministic_sar_narrative

NVIDIA_NIM_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
NVIDIA_MODEL = "meta/llama-3.3-70b-instruct"

async def generate_sar_report_narrative(cluster_data: Dict[str, Any]) -> str:
    """
    Generates a formal legal SAR narrative using NVIDIA NIM (Llama-3.3-70B).
    Enforces a strict 1500ms timeout circuit breaker; falls back to deterministic template immediately.
    """
    api_key = os.getenv("NVIDIA_API_KEY", "").strip()
    if not api_key:
        print("[NIM Client] No NVIDIA_API_KEY configured. Using deterministic legal template.")
        return deterministic_sar_narrative(cluster_data)

    def _sync_nim_call() -> str:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        prompt = f"""You are a Senior AML & Financial Fraud Compliance Officer.
Draft an official Suspicious Activity Report (SAR) executive summary for Syndicate Cluster #{cluster_data.get('cluster_id', 1)}
containing {cluster_data.get('size', 20)} synthetic applicant accounts.
Topological Louvain Modularity: Q = {cluster_data.get('modularity_q', 0.72):.4f}.
Formulate four specific, factual adverse action reason codes complying with CFPB Circular 2023-03 and ECOA Regulation B (12 CFR § 1002.9).
Include: 1) FSM Navigation Route Invariance, 2) Micro-temporal Arrival Sync (delta_t < 40ms), 3) Non-human Bézier constant jerk kinetics, and 4) Semantic intent prompt homogeneity.
Avoid generic or uncalibrated risk scores."""

        payload = {
            "model": NVIDIA_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 800,
            "temperature": 0.2
        }

        resp = requests.post(NVIDIA_NIM_URL, headers=headers, json=payload, timeout=1.4)
        if resp.status_code == 200:
            data = resp.json()
            return data["choices"][0]["message"]["content"]
        else:
            raise RuntimeError(f"NVIDIA NIM error {resp.status_code}: {resp.text}")

    try:
        # Strict 1500ms Circuit Breaker
        narrative = await asyncio.wait_for(asyncio.to_thread(_sync_nim_call), timeout=1.5)
        return narrative
    except (asyncio.TimeoutError, Exception) as e:
        print(f"[NIM Client] Circuit breaker triggered ({e}). Returning deterministic legal narrative.")
        return deterministic_sar_narrative(cluster_data)
