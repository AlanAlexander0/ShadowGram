"""
stations/station1_alan_swarm/generate_personas.py - Persona Generator for ShadowGram Swarm
Dual-Mode Generation:
1. Live GenAI: Queries NVIDIA NIM (meta/llama-3.2-11b-vision-instruct) using NVIDIA_API_KEY from .env.
2. Offline Algorithmic Fallback: High-speed deterministic generator for offline hackathon demos.
Saves personas to personas_cache.json.
"""

import os
import json
import math
import random
import argparse
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional

NAMES = [
    ("Aarav", "Sharma"), ("Priya", "Nair"), ("Rohan", "Mehta"), ("Ananya", "Iyer"),
    ("Vikram", "Patel"), ("Neha", "Deshmukh"), ("Aditya", "Verma"), ("Pooja", "Reddy"),
    ("Karan", "Malhotra"), ("Sneha", "Kulkarni"), ("Arjun", "Bose"), ("Divya", "Menon"),
    ("Siddharth", "Choudhury"), ("Ritu", "Agarwal"), ("Manish", "Saxena"), ("Kavita", "Joshi"),
    ("Naveen", "Pillai"), ("Swati", "Chatterjee"), ("Deepak", "Rao"), ("Sunita", "Gupta")
]

CITIES = [
    ("Bengaluru", "Karnataka"), ("Mumbai", "Maharashtra"), ("Pune", "Maharashtra"),
    ("Hyderabad", "Telangana"), ("Chennai", "Tamil Nadu"), ("Kochi", "Kerala"),
    ("Delhi", "Delhi"), ("Gurugram", "Haryana"), ("Noida", "Uttar Pradesh"),
    ("Kolkata", "West Bengal"), ("Ahmedabad", "Gujarat"), ("Jaipur", "Rajasthan")
]

OCCUPATIONS = [
    "Software Engineer", "Operations Executive", "Accountant", "Graphic Designer",
    "Digital Marketer", "Logistics Coordinator", "Sales Representative", "Customer Success Lead"
]

LOAN_PURPOSES = [
    "Urgent laptop display and motherboard repair required for remote work deliverables.",
    "Emergency dental root canal treatment and prescription antibiotic expenses.",
    "Advance deposit payment for semester college tuition fees due this Friday.",
    "Unplanned two-wheeler engine overhaul and clutch replacement for daily commute.",
    "Emergency hospitalization advance for mother post acute viral bronchitis.",
    "Quarterly society maintenance charges and impending water pipeline plumbing repair.",
    "Replacement of faulty compressor unit for commercial kitchen refrigerator.",
    "Immediate home inverter battery replacement prior to scheduled monsoon power outages."
]


def get_nvidia_api_key() -> str:
    """Retrieves NVIDIA_API_KEY from os.environ or searching up parent dirs for .env."""
    key = os.getenv("NVIDIA_API_KEY", "").strip()
    if key:
        return key

    current = Path(__file__).resolve().parent
    search_paths = [
        current / ".env",
        current.parent / ".env",
        current.parent.parent / ".env",
        current.parent.parent.parent / ".env",
        Path("D:/ATHENA/ShadowGram/.env")
    ]
    for env_path in search_paths:
        if env_path.exists():
            try:
                with open(env_path, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith("NVIDIA_API_KEY=") and not line.startswith("#"):
                            k = line.split("=", 1)[1].strip()
                            if k:
                                os.environ["NVIDIA_API_KEY"] = k
                                return k
            except Exception:
                pass
    return ""


def generate_random_pan() -> str:
    """Generates standard 10-character Indian PAN (5 letters + 4 digits + 1 letter)."""
    letters = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=5))
    digits = "".join(random.choices("0123456789", k=4))
    last_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return f"{letters}{digits}{last_letter}"


def generate_offline_personas(count: int = 20) -> List[Dict[str, Any]]:
    """Fast algorithmic persona generator for 100% offline hackathon operation."""
    personas = []
    for i in range(count):
        first, last = NAMES[i % len(NAMES)]
        city, state = CITIES[i % len(CITIES)]
        occupation = OCCUPATIONS[i % len(OCCUPATIONS)]
        loan_purpose = LOAN_PURPOSES[i % len(LOAN_PURPOSES)]
        monthly_income = random.randint(35, 95) * 1000
        requested_amount = random.choice([8000, 10000, 12000, 15000, 20000])

        personas.append({
            "persona_id": f"PERS-{i + 1:03d}",
            "account_id": f"ACC-{random.randint(10000, 99999)}",
            "full_name": f"{first} {last}",
            "pan": generate_random_pan(),
            "phone": f"+91 {random.choice(['7', '8', '9'])}{random.randint(100000000, 999999999)}",
            "email": f"{first.lower()}.{last.lower()}{random.randint(10, 99)}@gmail.com",
            "city": city,
            "state": state,
            "occupation": occupation,
            "monthly_income_inr": monthly_income,
            "requested_loan_inr": requested_amount,
            "loan_duration_months": random.choice([3, 6, 9, 12]),
            "loan_purpose_narrative": loan_purpose
        })
    return personas


def generate_personas_via_nvidia_nim(api_key: str, count: int = 20) -> List[Dict[str, Any]]:
    """
    Calls NVIDIA NIM API (meta/llama-3.2-11b-vision-instruct) to synthesize live AI personas.
    Batches in chunks of 5 personas to ensure fast response times and avoid timeouts.
    """
    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    all_personas: List[Dict[str, Any]] = []
    chunk_size = 5
    batches = math.ceil(count / chunk_size)

    for b in range(batches):
        current_req = min(chunk_size, count - len(all_personas))
        print(f"  [+] Requesting batch {b + 1}/{batches} ({current_req} personas) from NVIDIA NIM...")

        prompt = (
            f"Generate exactly {current_req} distinct, realistic Indian synthetic identities applying for emergency micro-loans. "
            "Each identity must have keys: full_name (diverse Indian names), pan (valid 10-char format like ABCDE1234F), "
            "phone (+91 10-digit number), city (Indian city), state (Indian state), occupation, "
            "monthly_income_inr (int between 35000 and 85000), requested_loan_inr (int between 8000 and 20000), "
            "and loan_purpose_narrative (a realistic, specific 1-sentence emergency loan reason). "
            "Return strictly a raw JSON array of objects. Do not include markdown codeblocks or explanation."
        )

        payload = {
            "model": "meta/llama-3.2-11b-vision-instruct",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.75,
            "max_tokens": 1200
        }

        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode("utf-8"),
                headers=headers,
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=25) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                content = data["choices"][0]["message"]["content"].strip()

                # Clean markdown fencing if model outputs ```json ... ```
                if content.startswith("```"):
                    lines = content.splitlines()
                    if lines[0].startswith("```"):
                        lines = lines[1:]
                    if lines and lines[-1].startswith("```"):
                        lines = lines[:-1]
                    content = "\n".join(lines).strip()

                start_idx = content.find("[")
                end_idx = content.rfind("]")
                if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
                    json_str = content[start_idx:end_idx + 1]
                else:
                    json_str = content

                parsed = json.loads(json_str)
                all_personas.extend(parsed)
                print(f"      -> Received {len(parsed)} personas from Llama-3.2")
        except Exception as e:
            err_msg = str(e).encode('ascii', errors='ignore').decode('ascii')
            print(f"      -> Batch {b + 1} notice: {err_msg}. Using deterministic fallback for remaining.")
            remaining = count - len(all_personas)
            fallback = generate_offline_personas(remaining)
            all_personas.extend(fallback)
            break

    # Standardize IDs, PAN formats, and structure
    for i, p in enumerate(all_personas):
        if "account_id" not in p:
            p["account_id"] = f"ACC-{random.randint(10000, 99999)}"
        p["persona_id"] = f"PERS-{i + 1:03d}"

        # Enforce valid 10-character Indian PAN format
        raw_pan = str(p.get("pan", "")).upper().strip()
        if not (len(raw_pan) == 10 and raw_pan[:5].isalpha() and raw_pan[5:9].isdigit() and raw_pan[9].isalpha()):
            p["pan"] = generate_random_pan()
        else:
            p["pan"] = raw_pan

    return all_personas[:count]


def main():
    parser = argparse.ArgumentParser(description="ShadowGram Persona Generator (Role 3 - Alan E Alexander)")
    parser.add_argument("--count", type=int, default=20, help="Number of personas to generate (default: 20)")
    parser.add_argument("--live-ai", action="store_true", help="Generate live using NVIDIA NIM API instead of offline generator")
    parser.add_argument("--output", type=str, default="", help="Output cache JSON path")
    args = parser.parse_args()

    cache_path = Path(args.output) if args.output else (Path(__file__).resolve().parent / "personas_cache.json")
    api_key = get_nvidia_api_key()

    if args.live_ai:
        if not api_key:
            print("[WARN] --live-ai requested, but NVIDIA_API_KEY was not found in .env or environment.")
            print("[INFO] Falling back to deterministic offline persona generator...")
            personas = generate_offline_personas(args.count)
        else:
            print(f"[INFO] Connecting to NVIDIA NIM API (meta/llama-3.2-11b-vision-instruct) to generate {args.count} live personas...")
            personas = generate_personas_via_nvidia_nim(api_key, count=args.count)
    else:
        print(f"[INFO] Using deterministic offline persona generator for {args.count} personas (Instant & Offline)...")
        personas = generate_offline_personas(args.count)

    with open(cache_path, "w", encoding="utf-8") as f:
        json.dump(personas, f, indent=2)

    print(f"\n[SUCCESS] Saved {len(personas)} personas to {cache_path}")
    print(f"Sample Persona #1: {personas[0].get('full_name')} ({personas[0].get('occupation')} in {personas[0].get('city')}) - INR {personas[0].get('requested_loan_inr')}")
    print(f"Reason: \"{personas[0].get('loan_purpose_narrative')}\"")


if __name__ == "__main__":
    main()
