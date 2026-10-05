"""
simulation/generate_personas.py - Persona Generator for ShadowGram Adversarial Swarm
Uses NVIDIA NIM (meta/llama-3.3-70b-instruct) when NVIDIA_API_KEY is available,
or falls back to an algorithmic generator to guarantee 100% offline hackathon operation.
Saves output to simulation/personas_cache.json.
"""

import json
import math
import os
import random
import sys
from pathlib import Path
from typing import Any, Dict, List

# Realistic seed databases for offline fallback generation
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
    "Digital Marketer", "Logistics Coordinator", "Sales Representative", "Customer Success Lead",
    "High School Teacher", "Laboratory Technician", "Data Entry Specialist", "Pharmacy Assistant"
]

LOAN_PURPOSES = [
    "Urgent laptop display and motherboard repair required for remote work deliverables.",
    "Emergency dental root canal treatment and prescription antibiotic expenses.",
    "Advance deposit payment for semester college tuition fees due this Friday.",
    "Unplanned two-wheeler engine overhaul and clutch replacement for daily commute.",
    "Emergency hospitalization advance for mother post acute viral bronchitis.",
    "Quarterly society maintenance charges and impending water pipeline plumbing repair.",
    "Replacement of faulty compressor unit for commercial kitchen refrigerator.",
    "Immediate home inverter battery replacement prior to scheduled monsoon power outages.",
    "Urgent medical diagnostic ultrasound and specialized pathology blood work.",
    "Urgent payment for certification exam voucher required for employment promotion.",
    "Sudden rental lease renewal deposit shortfall for residential accommodation.",
    "Replacement of stolen mobile device essential for two-factor authentication and work.",
    "Purchase of critical specialized pediatric asthma nebulizer and medication refills.",
    "Down payment for mandatory emergency electrical rewiring after power surge trip.",
    "Urgent repair of damaged water purifier RO filtration membrane unit.",
    "Emergency veterinarian consultation and surgical medication for household pet.",
    "Purchase of specialized orthopedic cervical spine support pillow and physical therapy.",
    "Pending installment clearance for domestic cooking gas pipeline connection.",
    "Immediate procurement of emergency inventory raw materials for catering contract.",
    "Sudden outstation travel expenses to attend family medical emergency."
]

def generate_random_pan() -> str:
    letters = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=5))
    digits = "".join(random.choices("0123456789", k=4))
    last_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return f"{letters}{digits}{last_letter}"

def generate_random_phone() -> str:
    return f"+91 {random.choice(['6', '7', '8', '9'])}{random.randint(100000000, 999999999)}"

def generate_offline_personas(count: int = 20) -> List[Dict[str, Any]]:
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
            "phone": generate_random_phone(),
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


def load_env():
    """Loads key-value pairs from .env in project root if present."""
    base_dir = Path(__file__).resolve().parent.parent
    env_file = base_dir / ".env"
    if env_file.exists():
        with open(env_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    os.environ.setdefault(key.strip(), val.strip())


def generate_personas_via_nvidia_nim(api_key: str, count: int = 20) -> List[Dict[str, Any]]:
    """Calls NVIDIA NIM API in fast chunks of 5 personas to prevent timeout."""
    import urllib.request
    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    all_personas = []
    chunk_size = 5
    batches = math.ceil(count / chunk_size)

    for b in range(batches):
        current_req = min(chunk_size, count - len(all_personas))
        print(f"[INFO] Requesting batch {b + 1}/{batches} ({current_req} personas) from NVIDIA NIM...")
        prompt = (
            f"Generate exactly {current_req} distinct, realistic Indian personas for an emergency micro-loan application. "
            "Each persona must have keys: full_name, pan (format ABCDE1234F), phone, city, occupation, "
            "monthly_income_inr (int between 35000 and 85000), requested_loan_inr (int between 8000 and 20000), "
            "and loan_purpose_narrative (a realistic 1-sentence emergency loan reason). "
            "Return strictly a raw JSON array of objects. Do not include markdown codeblocks or explanation."
        )

        payload = {
            "model": "meta/llama-3.2-11b-vision-instruct",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 1200
        }

        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=35) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                content = data["choices"][0]["message"]["content"].strip()

                start_idx = content.find("[")
                end_idx = content.rfind("]")
                if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
                    json_str = content[start_idx:end_idx + 1]
                else:
                    json_str = content

                parsed = json.loads(json_str)
                all_personas.extend(parsed)
                print(f"  [+] Received {len(parsed)} personas from Llama-3.2-11B")
        except Exception as e:
            err_msg = str(e).encode('ascii', errors='ignore').decode('ascii')
            print(f"  [-] Batch {b + 1} issue ({err_msg}). Using deterministic fallback for remaining.")
            remaining = count - len(all_personas)
            fallback = generate_offline_personas(remaining)
            all_personas.extend(fallback)
            break

    # Ensure IDs and PAN compliance
    for i, p in enumerate(all_personas):
        if "account_id" not in p:
            p["account_id"] = f"ACC-{random.randint(10000, 99999)}"
        p["persona_id"] = f"PERS-{i + 1:03d}"
        
        # Enforce standard 10-character Indian PAN: 5 letters + 4 digits + 1 letter
        raw_pan = str(p.get("pan", "")).upper()
        if not (len(raw_pan) == 10 and raw_pan[:5].isalpha() and raw_pan[5:9].isdigit() and raw_pan[9].isalpha()):
            p["pan"] = generate_random_pan()

    return all_personas[:count]


def main():
    load_env()
    base_dir = Path(__file__).resolve().parent
    cache_path = base_dir / "personas_cache.json"
    api_key = os.getenv("NVIDIA_API_KEY", "").strip()

    if api_key:
        print("[INFO] Attempting to query live NVIDIA NIM API (meta/llama-3.3-70b-instruct) for 20 personas...")
        personas = generate_personas_via_nvidia_nim(api_key, count=20)
    else:
        print("[INFO] No NVIDIA_API_KEY provided. Using deterministic offline generator for 20 personas...")
        personas = generate_offline_personas(count=20)

    with open(cache_path, "w", encoding="utf-8") as f:
        json.dump(personas, f, indent=2)

    print(f"[SUCCESS] Successfully generated and cached {len(personas)} personas to {cache_path}")
    print(f"Sample Persona #1: {personas[0].get('full_name')} ({personas[0].get('occupation')} in {personas[0].get('city')}) - INR {personas[0].get('requested_loan_inr')}")
    print(f"Reason: {personas[0].get('loan_purpose_narrative')}")


if __name__ == "__main__":
    main()
