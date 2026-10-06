# Station 4: Data Engineering, NVIDIA LLM & Legal SAR Lead
**Assignee:** Mohammed Nihad PC & Ashlin Theres James (Role 4)  
**Target:** Laptop 4 (Compliance Station)  
**Repository:** `shadowgram-station4-nihad-compliance`

---

## 🎯 What This Station Does
This station owns regulatory compliance, statutory legal reason codes, and automated Suspicious Activity Report (SAR) paperwork:
1. **Automated 2-Page SAR PDF Generator (`sar_generator.py`):**
   - Pure Python ReportLab compiler (runs 100% locally on CPU in $<2\text{s}$).
   - **Page 1:** Executive Summary, Modularity $Q$, Permutation null model significance ($p < 0.001$), Pre-KYC Denial-of-Wallet (DoW) savings ledger (₹1,220.00 saved), and statutory Equal Credit Opportunity Act (ECOA) Regulation B legal basis.
   - **Page 2:** Evidence Ledger with 20 flagged synthetic accounts, interaction physics metrics, adverse action reason codes (CR-01 to CR-04), and officer HMAC audit seal.
2. **NVIDIA NIM Legal Scribe Client (`nim_client.py`):**
   - Calls `meta/llama-3.3-70b-instruct` to synthesize formal compliance narratives.
   - **Strict 1500ms Circuit Breaker:** Falls back instantaneously ($<1\text{ms}$) to `fallback_sar.py` if mobile hotspot drops or times out.
3. **Statutory Fallback Narrative (`fallback_sar.py`):**
   - Deterministic legal template complying strictly with 12 CFR § 1002.9 and EU AI Act Articles 13 & 14.
4. **Compliance Station UI (`page.tsx`):**
   - Next.js / React dashboard displaying the active incident ledger, DoW savings ticker, and one-click SAR PDF compilation button.

---

## 🚀 Quickstart Commands

### 1. Test Standalone SAR PDF Generation
```bash
python3 -m venv venv
source venv/bin/activate
pip install reportlab requests
python -c "from sar_generator import generate_sar_pdf; pdf = generate_sar_pdf({'cluster_id': 1, 'size': 20, 'modularity_q': 0.7241}); open('SAR_Test.pdf', 'wb').write(pdf); print('Generated SAR_Test.pdf successfully!')"
```

### 2. Verify NVIDIA NIM or Deterministic Fallback
```bash
export NVIDIA_API_KEY=""  # Leave empty to test instant offline fallback
python -c "import asyncio; from nim_client import generate_sar_report_narrative; print(asyncio.run(generate_sar_report_narrative({'cluster_id': 1, 'size': 20})))"
```

---

## 📦 Git Repository Setup
To publish this station to your dedicated GitHub repository:
```bash
cd stations/station4_nihad_compliance
git init
git add .
git commit -m "feat(station4): Legal Compliance SAR Engine & ReportLab PDF Exporter v2.0"
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/shadowgram-station4-compliance.git
git push -u origin main
```
