# ShadowGram NotebookLM Slide Generation Guide

This directory contains three meticulously structured source documents designed specifically to feed into **Google NotebookLM** (or Gemini Slide Deck creation) to generate three separate, highly visual, 11-slide presentations for your team and the HackAthena judges.

---

## 📁 Source Decks Overview

| File | Theme / Deck Purpose | Number of Slides | Target Audience |
| :--- | :--- | :--- | :--- |
| [**`DECK_1_THE_PROBLEM_AND_THREAT_LANDSCAPE.md`**](file:///home/paradoxpete/Documents/ATHENA/NotebookLM_Slide_Packs/DECK_1_THE_PROBLEM_AND_THREAT_LANDSCAPE.md) | **The Problem & Threat Landscape:** 2026 AI bot swarms, synthetic identities, why accounts look innocent in isolation, 3 banking case studies (Micro-lending, BNPL, KYC Denial-of-Wallet), competitor failures (BioCatch, Arkose, Sift), CFPB circular 2023-03. | 11 Slides | Team briefing & Opening Pitch Hook |
| [**`DECK_2_SHADOWGRAM_SOLUTION_AND_ARCHITECTURE.md`**](file:///home/paradoxpete/Documents/ATHENA/NotebookLM_Slide_Packs/DECK_2_SHADOWGRAM_SOLUTION_AND_ARCHITECTURE.md) | **The Solution & Technical Architecture:** Relational graph paradigm, 5-layer interaction physics, 2D-CNN kinetic spectrograms, Sentence-Transformers NLP, Louvain modularity clustering, the "Why Card", 1-click quarantine, NVIDIA SAR PDF export, zero-cost stack. | 11 Slides | Technical Deep-Dive & Architecture Defense |
| [**`DECK_3_TEAM_ROLES_HARDWARE_AND_LIVE_DEMO.md`**](file:///home/paradoxpete/Documents/ATHENA/NotebookLM_Slide_Packs/DECK_3_TEAM_ROLES_HARDWARE_AND_LIVE_DEMO.md) | **Team Execution, Hardware & Live Cyber-Range:** 4-laptop cyber-range setup, hardware matching (2 gaming + 2 normal), local phone hotspot networking, 4 individual role dossiers, 3-minute pitch choreography, live judge interaction, milestone checkpoints. | 11 Slides | Internal Team War-Room & Demo Execution |

---

## 🚀 How to Generate the Visual Slide Decks in NotebookLM

1. **Open Google NotebookLM:** Navigate to [notebooklm.google.com](https://notebooklm.google.com).
2. **Create a New Notebook:** Name it e.g. `ShadowGram - Deck 1: The Problem`.
3. **Upload the Source File:** Upload `DECK_1_THE_PROBLEM_AND_THREAT_LANDSCAPE.md`.
4. **Prompt NotebookLM to Generate the Slides:**
   Paste this exact prompt into the chat box:
   > *"Using the uploaded source document, create a compelling, visual 11-slide presentation deck. Follow the exact slide outline provided in the document. For each slide, output the Slide Title, Visual Layout Recommendation, Key High-Impact Bullet Points, Bold Metrics/Callouts, and Speaker Notes. Keep the tone authoritative, technical, and urgent."*
5. **Repeat for Decks 2 and 3:**
   - Create a second notebook for `DECK_2_SHADOWGRAM_SOLUTION_AND_ARCHITECTURE.md`.
   - Create a third notebook for `DECK_3_TEAM_ROLES_HARDWARE_AND_LIVE_DEMO.md`.
6. **Export / Share:** You can copy the generated slide content directly into Google Slides, Canva, or PowerPoint, or export it using NotebookLM's built-in sharing features.
