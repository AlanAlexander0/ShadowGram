"""
stations/station1_alan_swarm/generate_personas.py - Persona Generator for ShadowGram Swarm
Uses algorithmic seed generation for 100% offline hackathon operation.
Saves personas to personas_cache.json.
"""

import json
import random
from pathlib import Path
from typing import Any, Dict, List

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

def generate_random_pan() -> str:
    letters = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=5))
    digits = "".join(random.choices("0123456789", k=4))
    last_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return f"{letters}{digits}{last_letter}"

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

if __name__ == "__main__":
    cache_path = Path(__file__).resolve().parent / "personas_cache.json"
    p = generate_offline_personas(20)
    with open(cache_path, "w") as f:
        json.dump(p, f, indent=2)
    print(f"Generated {len(p)} personas into {cache_path}")
