"""
stations/station1_alan_swarm/swarm_runner.py - Red-Team Swarm Runner for ShadowGram
Assignee: Alan E Alexander (Role 3: Red-Team Swarm Runner & Client Telemetry Lead)
Document Code: SG-PROTO-00 / Task 3.2

High-Performance Architecture:
1. Single Chromium browser instance with N isolated BrowserContexts.
2. Intercepts and aborts images/fonts/css to keep total RAM strictly < 600MB.
3. Neuromotor human trajectory emulation using Flash & Hogan minimum-jerk polynomials.
4. Synchronizes 20 bot submissions within a tight 1.4-second arrival window.
5. Dual-Mode execution:
   - Full Playwright Browser Mode: Drives live DOM on Laptop 3.
   - Direct Synthetic Telemetry Mode: Dispatches compliant telemetry to Laptop 2 for instant testing.
6. Two Sophistication Modes:
   - --mode naive: Triggers Key 1 Fast Automation Filter (<5ms).
   - --mode stealth: Evades Key 1, intercepted by Key 2 Relational Physics Graph.
"""

import argparse
import asyncio
import hashlib
import hmac
import json
import math
import os
import random
import sys
import time
import uuid
from pathlib import Path
from typing import Any, Dict, List, Optional

# Add parent directory to path so trajectory module can be imported
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from trajectory import generate_human_trajectory
except ImportError:
    from simulation.trajectory import generate_human_trajectory

SESSION_SALT = "shadowgram-hackathena-2026-salt"


def compute_telemetry_hmac(session_id: str, timestamp: float, salt: str = SESSION_SALT) -> str:
    """Computes session-salted HMAC-SHA256 signature matching telemetry.js."""
    sign_payload = f"{session_id}:{timestamp:.3f}".encode("utf-8")
    return hmac.new(salt.encode("utf-8"), sign_payload, hashlib.sha256).hexdigest()


def load_personas(cache_path: Optional[Path] = None, count: int = 20, live_ai: bool = False, force_live_ai: bool = False) -> List[Dict[str, Any]]:
    """
    Loads personas with dual-mode support:
    1. Static / Pre-Generated JSON Mode (Default):
       Loads instantly from personas_cache.json for sub-second, 100% offline-safe hackathon execution.
    2. Live NVIDIA NIM GenAI Mode (--live-ai):
       Connects to NVIDIA NIM (meta/llama-3.2-11b-vision-instruct) using NVIDIA_API_KEY from .env,
       dynamically synthesizes fresh synthetic Indian personas on the fly, and updates cache.
    """
    if force_live_ai:
        live_ai = True
    if cache_path is None:
        cache_path = Path(__file__).resolve().parent / "personas_cache.json"
    if live_ai:
        try:
            from generate_personas import get_nvidia_api_key, generate_personas_via_nvidia_nim
        except ImportError:
            from simulation.generate_personas import get_nvidia_api_key, generate_personas_via_nvidia_nim

        api_key = get_nvidia_api_key()
        if api_key:
            print(f"\n[NVIDIA NIM AI] Live AI Mode enabled (--live-ai)!")
            print(f"[NVIDIA NIM AI] Contacting NVIDIA NIM (meta/llama-3.2-11b-vision-instruct)...")
            try:
                live_personas = generate_personas_via_nvidia_nim(api_key, count=count)
                if live_personas and len(live_personas) >= count:
                    print(f"[NVIDIA NIM AI] Successfully generated {len(live_personas)} fresh AI synthetic identities!")
                    sample = live_personas[0]
                    print(f"  -> AI Sample #1: {sample.get('full_name')} ({sample.get('occupation')} in {sample.get('city')}) - INR {sample.get('requested_loan_inr')}")
                    print(f"  -> AI Narrative: \"{sample.get('loan_purpose_narrative')}\"\n")
                    if cache_path.exists():
                        try:
                            with open(cache_path, "r", encoding="utf-8") as f:
                                existing = json.load(f)
                            if isinstance(existing, list) and len(existing) > len(live_personas):
                                to_save = live_personas + existing[len(live_personas):]
                            else:
                                to_save = live_personas
                        except Exception:
                            to_save = live_personas
                    else:
                        to_save = live_personas
                    with open(cache_path, "w", encoding="utf-8") as f:
                        json.dump(to_save, f, indent=2)
                    return live_personas[:count]
            except Exception as e:
                print(f"[WARN] Live NVIDIA NIM generation failed: {e}. Falling back to cached personas.")
        else:
            print("[WARN] --live-ai requested, but NVIDIA_API_KEY was not found in .env. Falling back to cached personas.")

    # Default Fast / Cached Mode
    if cache_path.exists():
        with open(cache_path, "r", encoding="utf-8") as f:
            personas = json.load(f)
            if len(personas) >= count:
                print(f"[PERSONAS] Loaded {count} pre-generated synthetic personas from {cache_path.name} (Instant Mode).")
                return personas[:count]

    # Fallback inline generation if file not found
    try:
        from generate_personas import generate_offline_personas
    except ImportError:
        from simulation.generate_personas import generate_offline_personas
    personas = generate_offline_personas(count)
    with open(cache_path, "w", encoding="utf-8") as f:
        json.dump(personas, f, indent=2)
    return personas


# Alias for test runners and external scripts
get_synthetic_personas = load_personas


async def direct_telemetry_agent(
    bot_id: int,
    persona: Dict[str, Any],
    telemetry_url: str,
    burst_barrier: asyncio.Event,
    burst_delay: float,
    session: Any,
    mode: str = "stealth"
):
    """
    Simulates bot interaction and dispatches compliant telemetry packets directly.
    - naive: Triggers Key 1 Fast Automation Filter (zero pre-click moves, zero dwell variance).
    - stealth: Evades Key 1 (Gaussian dwell, pre-hover mouse stream), caught by Key 2 (relational graph).
    """
    session_id = str(uuid.uuid4())
    account_id = persona.get("account_id", f"ACC-{random.randint(10000, 99999)}")
    route_state = "/auth -> /kyc -> /loan_details -> /submit"

    # 1. Navigation Event
    t0 = time.time()
    nav_packet = {
        "session_id": session_id,
        "account_id": account_id,
        "timestamp": t0,
        "event_type": "route_change",
        "telemetry_hmac": compute_telemetry_hmac(session_id, t0),
        "payload": {
            "route_path": route_state
        }
    }

    # 2. Keystroke Dynamics & Biometric Digraphs
    t1 = t0 + 0.25
    if mode == "naive":
        key_flight = 15.0  # Robotic static timing
        key_dwell = 10.0
        digraph_flight = 12.0
        is_digraph = False
    elif mode == "dynamic-jitter":
        key_flight = round(random.gauss(78.0, 15.0), 2)
        key_dwell = round(random.gauss(68.0, 9.0), 2)
        digraph_flight = round(random.gauss(70.0, 11.0), 2)
        is_digraph = True
    else:  # stealth
        key_flight = round(random.gauss(75.0, 12.0), 2)
        key_dwell = round(random.gauss(65.0, 8.0), 2)
        digraph_flight = round(random.gauss(68.0, 10.0), 2)
        is_digraph = True

    key_packet = {
        "session_id": session_id,
        "account_id": account_id,
        "timestamp": t1,
        "event_type": "keydown",
        "telemetry_hmac": compute_telemetry_hmac(session_id, t1),
        "payload": {
            "key_flight_time_ms": key_flight,
            "key_dwell_time_ms": key_dwell,
            "digraph_flight_time_ms": digraph_flight,
            "is_common_digraph": is_digraph,
            "route_path": route_state
        }
    }

    # 3. Kinetic Trajectory
    start_pos = (random.randint(50, 200), random.randint(50, 200))
    target_pos = (random.randint(600, 900), random.randint(400, 700))
    waypoints = generate_human_trajectory(start_pos, target_pos, duration=0.45)
    
    t2 = t1 + 0.35
    if mode == "naive":
        pre_click_moves = 0
        click_dwell = 1.0  # Instant script click -> triggers Key 1!
        jerk_score = 0.0
    else:
        pre_click_moves = random.randint(12, 28)
        click_dwell = round(random.gauss(92.0, 14.0), 2)
        jerk_score = 0.012

    pointer_packet = {
        "session_id": session_id,
        "account_id": account_id,
        "timestamp": t2,
        "event_type": "pointerdown",
        "telemetry_hmac": compute_telemetry_hmac(session_id, t2),
        "payload": {
            "pointer_curvature_jerk": jerk_score,
            "pointer_coordinates": [[p[0], p[1], round(t2 + p[2], 3)] for p in waypoints[-15:]],
            "click_dwell_duration_ms": click_dwell,
            "mousemove_pre_click_count": pre_click_moves,
            "route_path": route_state
        }
    }

    # Wait for the synchronized burst window release
    await burst_barrier.wait()
    await asyncio.sleep(burst_delay)

    # 4. Final Submission Telemetry (Burst phase with Dense Semantic Narrative)
    t_submit = time.time()
    submit_packet = {
        "session_id": session_id,
        "account_id": account_id,
        "timestamp": t_submit,
        "event_type": "loan_submit",
        "telemetry_hmac": compute_telemetry_hmac(session_id, t_submit),
        "payload": {
            "route_path": route_state,
            "key_flight_time_ms": key_flight,
            "key_dwell_time_ms": click_dwell,
            "digraph_flight_time_ms": digraph_flight,
            "pointer_curvature_jerk": jerk_score,
            "narrative_text": persona.get("loan_purpose_narrative", "Urgent micro-loan needed for domestic repair expenditures."),
            "client_canvas_hash": "e4a8b71d9f02c6"  # Shared syndicate canvas hash
        }
    }

    # Dispatch packets asynchronously via thread pool
    import urllib.request

    def _post_packet(pkt_dict):
        try:
            req = urllib.request.Request(
                telemetry_url,
                data=json.dumps(pkt_dict).encode("utf-8"),
                headers={"Content-Type": "application/json"},
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=0.3) as response:
                return response.status
        except Exception:
            return None

    # Asynchronously dispatch all packets without stalling the event loop
    for pkt in [nav_packet, key_packet, pointer_packet, submit_packet]:
        asyncio.create_task(asyncio.to_thread(_post_packet, pkt))

    return {
        "bot_id": bot_id,
        "account_id": account_id,
        "name": persona.get("full_name"),
        "loan_inr": persona.get("requested_loan_inr"),
        "submit_timestamp": t_submit,
        "mode": mode
    }


async def run_direct_swarm(
    personas: List[Dict[str, Any]],
    telemetry_url: str,
    burst_window: float = 1.4,
    mode: str = "stealth"
) -> List[Dict[str, Any]]:
    """Runs high-speed direct telemetry swarm simulation."""
    print(f"\n[SWARM] Launching direct swarm simulation for {len(personas)} agents (Mode: {mode.upper()})...")
    print(f"[SWARM] Target Telemetry Ingress: {telemetry_url}")
    print(f"[SWARM] Arrival synchronization window: {burst_window:.2f}s\n")

    burst_barrier = asyncio.Event()
    tasks = []

    if mode == "dynamic-jitter":
        print(f"[SWARM JITTER] Generating Poisson-distributed inter-arrival intervals Delta_t ~ Exp(lambda)...")
        mean_delta = burst_window / max(len(personas), 1)
        lambd = 1.0 / max(mean_delta, 0.001)
        current_offset = 0.0
        for i, persona in enumerate(personas):
            # Poisson point process inter-arrival delay
            inter_arrival = random.expovariate(lambd)
            current_offset += inter_arrival
            tasks.append(
                direct_telemetry_agent(i + 1, persona, telemetry_url, burst_barrier, current_offset, None, mode=mode)
            )
    else:
        # Distribute bot submission delays uniformly within the burst window
        for i, persona in enumerate(personas):
            delay = (i / len(personas)) * burst_window + random.uniform(-0.04, 0.04)
            delay = max(0.0, min(burst_window, delay))
            tasks.append(
                direct_telemetry_agent(i + 1, persona, telemetry_url, burst_barrier, delay, None, mode=mode)
            )

    # Release all agents simultaneously
    start_time = time.time()
    burst_barrier.set()
    results = await asyncio.gather(*tasks)
    elapsed = time.time() - start_time

    # Calculate empirical arrival deltas
    submits = sorted([r["submit_timestamp"] for r in results])
    deltas = [submits[i] - submits[i - 1] for i in range(1, len(submits))]
    avg_delta_ms = (sum(deltas) / len(deltas) * 1000) if deltas else 0

    print(f"\n[SWARM COMPLETE] Dispatched {len(results)} agents in {elapsed:.3f}s total.")
    print(f"[SWARM TELEMETRY] Micro-temporal arrival mean delta: {avg_delta_ms:.1f}ms (Synchronized Phase-Lock)")
    for r in results[:4]:
        print(f"  - Bot #{r['bot_id']} [{r['account_id']}]: {r['name']} requested INR {r['loan_inr']} [Mode: {r['mode']}]")
    print("  ...")
    return results


async def run_playwright_swarm(
    personas: List[Dict[str, Any]],
    target_url: str,
    telemetry_url: str,
    headless: bool = True,
    burst_window: float = 1.4,
    mode: str = "stealth"
):
    """
    Runs full Playwright browser swarm.
    Strictly keeps memory <600MB by using 1 Chromium process and aborting media routes.
    """
    from playwright.async_api import async_playwright

    print(f"\n[PLAYWRIGHT SWARM] Launching Playwright engine...")
    print(f"[PLAYWRIGHT SWARM] Target Web App: {target_url}")
    print(f"[PLAYWRIGHT SWARM] Concurrency: {len(personas)} isolated browser contexts (1 Chromium process)")
    print(f"[PLAYWRIGHT SWARM] Media route aborting enabled (<600MB RAM guarantee)\n")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=headless)
        burst_barrier = asyncio.Event()

        async def bot_worker(bot_id: int, persona: Dict[str, Any], delay: float):
            # Create isolated context
            context = await browser.new_context(
                viewport={"width": 1280, "height": 800},
                user_agent=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.{bot_id} Safari/537.36"
            )
            # Route-abort media to preserve RAM
            await context.route(
                "**/*.{png,jpg,jpeg,svg,woff,woff2,css,gif}",
                lambda route: route.abort()
            )
            page = await context.new_page()

            try:
                # 1. Navigate to target portal
                await page.goto(target_url, timeout=15000)
                await page.wait_for_load_state("domcontentloaded")

                # 2. Emulate realistic cursor trajectory to inputs
                path_to_input = generate_human_trajectory((100, 100), (350, 240), duration=0.4)
                for pt in path_to_input[::3]:
                    await page.mouse.move(pt[0], pt[1])

                # 3. Fill personal details if inputs exist and are editable
                name_input = await page.query_selector("#input-name")
                if name_input and await name_input.is_editable():
                    await page.fill("#input-name", persona["full_name"])

                pan_input = await page.query_selector("#input-pan")
                if pan_input and await pan_input.is_editable():
                    await page.fill("#input-pan", persona["pan"])

                amt_input = await page.query_selector("#input-amount")
                if amt_input and await amt_input.is_editable():
                    await page.fill("#input-amount", str(persona["requested_loan_inr"]))

                reason_input = await page.query_selector("#input-reason")
                if reason_input and await reason_input.is_editable():
                    # Type loan justification with natural keystroke timing
                    type_delay = 20 if mode != "naive" else 1
                    await page.type("#input-reason", persona["loan_purpose_narrative"][:35], delay=type_delay)

                # Wait for synchronized submission burst
                await burst_barrier.wait()
                await asyncio.sleep(delay)

                # 4. Click Submit button
                if await page.query_selector("#btn-apply"):
                    await page.click("#btn-apply")
                elif await page.query_selector("button[type='submit']"):
                    await page.click("button[type='submit']")

                return {
                    "bot_id": bot_id,
                    "account_id": persona.get("account_id"),
                    "name": persona.get("full_name"),
                    "status": "submitted",
                    "timestamp": time.time()
                }
            except Exception as ex:
                print(f"[WARN] Bot #{bot_id} encountered browser issue: {ex}")
                return {"bot_id": bot_id, "status": "fallback_direct", "error": str(ex)}
            finally:
                await context.close()

        # Build workers
        tasks = []
        if mode == "dynamic-jitter":
            mean_delta = burst_window / max(len(personas), 1)
            lambd = 1.0 / max(mean_delta, 0.001)
            current_offset = 0.0
            for i, persona in enumerate(personas):
                inter_arrival = random.expovariate(lambd)
                current_offset += inter_arrival
                tasks.append(bot_worker(i + 1, persona, current_offset))
        else:
            for i, persona in enumerate(personas):
                delay = (i / len(personas)) * burst_window
                tasks.append(bot_worker(i + 1, persona, delay))

        # Trigger synchronized burst
        burst_barrier.set()
        results = await asyncio.gather(*tasks)
        await browser.close()

        print(f"\n[PLAYWRIGHT SWARM] Finished {len(results)} browser bot executions.")
        return results


def main():
    parser = argparse.ArgumentParser(description="ShadowGram Red-Team Swarm Runner (Role 3 - Alan E Alexander)")
    parser.add_argument("--target-url", type=str, default="http://localhost:3000", help="AthenaPay target web portal")
    parser.add_argument("--telemetry-url", type=str, default="http://localhost:8000/telemetry", help="ShadowGram Core Ingress")
    parser.add_argument("--bots", type=int, default=20, help="Number of concurrent bots to deploy (default: 20)")
    parser.add_argument("--burst-window", type=float, default=1.4, help="Micro-temporal synchronization window in seconds (default: 1.4s)")
    parser.add_argument("--direct", action="store_true", help="Force direct synthetic telemetry dispatch without opening Chromium")
    parser.add_argument("--headed", action="store_true", help="Run browser in visible mode (default: headless)")
    parser.add_argument(
        "--mode",
        type=str,
        choices=["stealth", "naive", "dynamic-jitter", "dynamic_jitter"],
        default="stealth",
        help="Bot sophistication mode: stealth (bypasses Key 1, caught by Key 2), naive (caught by Key 1), or dynamic-jitter (Poisson inter-arrival jitter)"
    )
    parser.add_argument(
        "--live-ai",
        action="store_true",
        help="Generate fresh synthetic personas live using NVIDIA NIM API (Llama-3.2) instead of cached JSON"
    )
    args = parser.parse_args()
    if args.mode == "dynamic_jitter":
        args.mode = "dynamic-jitter"

    cache_file = Path(__file__).resolve().parent / "personas_cache.json"
    personas = load_personas(cache_file, count=args.bots, live_ai=args.live_ai)

    # Check Playwright availability
    playwright_available = False
    if not args.direct:
        try:
            import playwright
            playwright_available = True
        except ImportError:
            playwright_available = False

    if playwright_available and not args.direct:
        try:
            asyncio.run(
                run_playwright_swarm(
                    personas,
                    target_url=args.target_url,
                    telemetry_url=args.telemetry_url,
                    headless=not args.headed,
                    burst_window=args.burst_window,
                    mode=args.mode
                )
            )
        except Exception as e:
            err_msg = str(e).encode('ascii', errors='ignore').decode('ascii')
            print(f"[INFO] Playwright error encountered: {err_msg[:120]}... Falling back to direct telemetry.")
            asyncio.run(
                run_direct_swarm(
                    personas,
                    telemetry_url=args.telemetry_url,
                    burst_window=args.burst_window,
                    mode=args.mode
                )
            )
    else:
        print(f"[INFO] Operating in Direct Synthetic Telemetry Mode ({args.mode.upper()})...")
        asyncio.run(
            run_direct_swarm(
                personas,
                telemetry_url=args.telemetry_url,
                burst_window=args.burst_window,
                mode=args.mode
            )
        )


if __name__ == "__main__":
    main()
