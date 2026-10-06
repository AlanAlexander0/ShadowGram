# Station 3: Visual Command Center & AthenaPay Loan Portal
**Assignee:** Aiswarya Kallayil Rajesh (Role 2)  
**Target:** Laptop 3 (AthenaPay Live Loan App) & Command Cockpit  
**Repository:** `shadowgram-station3-aiswarya-frontend`

---

## 🎯 What This Station Does
This station runs the user-facing web applications:
1. **AthenaPay Instant Loan Portal (`athenapay_portal.html`):**
   - The application where a **live judge** or teammate applies for a ₹10,000 micro-credit loan.
   - **6-Second Test Rule:** Only requires typing 3 words (e.g., *"Laptop repair fee"*). Keystroke flight time and mouse jitter are collected naturally in $<6\text{s}$.
   - **Hidden Honey-DOM Tripwire:** Catches naive headless bots that crawl hidden fields.
   - **Reversible Step-Up Challenge (UPI Penny-Drop):** Demonstrates live that quarantined users can clear challenges in 10 seconds without permanent bans.
2. **Interactive Command Cockpit (`cockpit.html`):**
   - High-performance particle visualizer. Shows 80 calm blue human nodes and 20 red pulsing bot nodes snapping together with laser links.
   - 1-Click Blast-Radius Quarantine button.
   - Why Card modal inspection with live SVG Permutation Histogram.
3. **React/Next.js Why Card Component (`WhyCardModal.tsx`):**
   - Reusable modal component for the Next.js App Router.
   - Displays statutory Equal Credit Opportunity Act (ECOA) Regulation B reason codes (CR-01 to CR-04).
   - Live Denial-of-Wallet (DoW) savings counter (₹1,220.00 saved).
4. **Client-Side Behavioral Telemetry SDK (`telemetry.js`):**
   - Collects sub-millisecond dwell times, pre-click movement counts, and touch dynamics without recording personal data.

---

## 🚀 Quickstart Commands

### 1. Serve AthenaPay for Live Testing
Serve the directory with any local static HTTP server (e.g. Python):
```bash
python3 -m http.server 3000
```
Open in browser:
- **AthenaPay Portal:** `http://localhost:3000/athenapay_portal.html`
- **Command Cockpit:** `http://localhost:3000/cockpit.html`

### 2. Live Judge Walkthrough (10-Second Test)
1. Hand Laptop 3 to the judge.
2. Tell them: *"Type 3 words in Loan Purpose and click Apply."*
3. Point to Laptop 2's screen: The judge's account appears as an isolated **green/blue node**.
4. Alan triggers the red-team swarm on Laptop 1: 20 red nodes snap together in a tight cluster.
5. Demonstrate the **Step-Up Challenge button**: Show the judge how a ₹1 UPI penny-drop clears quarantine in 10 seconds!

---

## 📦 Git Repository Setup
To publish this station to your dedicated GitHub repository:
```bash
cd stations/station3_aiswarya_frontend
git init
git add .
git commit -m "feat(station3): AthenaPay Live Loan Portal & Visual Command Cockpit v2.0"
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/shadowgram-station3-frontend.git
git push -u origin main
```
