# ShadowGram: Deep Research Note v2 (web-verified, 6 Oct 2026)

*This version replaces v1. I ran about 25 searches and read one 2026 paper in full. Each claim is tagged **VERIFIED** (found in a primary or strong source), **SECONDARY** (blog or vendor summary), or **FROM MEMORY** (not re-checked). Lines marked "our reasoning" are my analysis, not findings.*

---

## 1. Ten findings that change your pitch

1. **BioCatch already ships a graph product.** BioCatch Scout (Sept 2023) draws link-analysis graphs of connected mule accounts, supports 50,000+ nodes and 250,000+ edges, fuses 3,000+ signals, and uses a "galaxy" interface. Its Account Opening Protection page says it detects fraud on applicants it has never seen, including bots and AI-driven agents. **Remove "BioCatch fails on day zero" and "BioCatch cannot cluster".** BioCatch also published an agentic-AI fraud report in June 2026, so it is moving toward your space. *(VERIFIED)*
2. **DataVisor already does unsupervised ring detection.** It holds patents on "unsupervised attack ring detection" that clusters accounts, uses graph analysis, and outputs "detection reasons". DataVisor's own blog warns that some coordinated groups are legitimate (it uses a phone application centre as the example). That is the same flash-crowd false-positive problem you face, so cite it as shared ground. *(VERIFIED)*
3. **Your core idea is established science.** SynchroTrap (ACM CCS 2014, Facebook/Instagram) clusters accounts by loosely synchronized actions. It found 2M+ malicious accounts and about 1,156 campaigns in one month. Your novelty is the *application and combination*, not the thesis. *(VERIFIED)*
4. **Per-session mouse detection is an arms race, and attackers have matching tools.** GAN-generated trajectories (Iliou et al.; BeCAPTCHA-Mouse) are published. A July 2026 workshop paper (TUM/Kontext) found Playwright-driven agents were caught 100% of the time even after Bézier, GAN and human-replay evasion. The signal was not the cursor path. It was missing raw event streams (no raw mousemove before clicks, no wheel events, near-zero click-duration variance). The authors state that OS-level input (xdotool, PyAutoGUI, hardware emulators, Anthropic's Computer Use) is outside their results. *(VERIFIED)*
5. **Your own demo may be caught without a graph.** Alan's swarm runs on Playwright, which that paper shows is separable per session by event-stream artifacts. A sharp judge will ask why you need a graph. Section 7, Q5 gives the answer.
6. **The Krazybee case undercuts how you used it.** The Telangana High Court quashed *all* proceedings against Krazybee on 11 March 2025. The company's own filings show attachment amounts of ₹3,305.31 lakh plus ₹1,606.53 lakh, not ₹65.87 Cr. The case also concerned alleged predatory-app conduct, not bot attacks on lenders. *(VERIFIED)*
7. **Sift's +211% is old and narrow.** It is BNPL *merchant payment fraud*, 2022 vs 2021, from Sift's Q1 2023 index. It is not a 2025 figure and not about swarms. *(VERIFIED)*
8. **Three legal citations are wrong or stale.** CFPB Circular 2023-03 was withdrawn on 12 May 2025. The RBI 2022 guidelines were replaced by the RBI (Digital Lending) Directions, 2025. The EU AI Act fine "€35M / 7%" applies to *prohibited practices*, not high-risk duties. See Section 8.
9. **The CAPTCHA citation is mis-sourced.** The real paper is "Are CAPTCHAs Still Bot-hard?" (Halligan), USENIX Security 2025: 60.7% solve rate across 26 CAPTCHA types, and 70.6% on unseen challenges from human CAPTCHA farms. *(VERIFIED)*
10. **Louvain has documented defects.** It can return disconnected communities (Leiden paper: up to 25% badly connected, up to 16% disconnected in tests), and modularity has a resolution limit. Use Leiden. *(VERIFIED)*

---

## 2. Fact-check ledger

| Claim in your decks | Verdict | Evidence | Say instead |
|---|---|---|---|
| "USENIX Security 2024: Threat of VLMs to CAPTCHAs", 70–85% on Arkose | Not found | Halligan, USENIX Sec 2025: 60.7% (26 types), 70.6% (in the wild). ViPer (USENIX Sec 2026, arXiv 2601.06461): up to 93.2% on visual-reasoning CAPTCHAs; GPT-4o zero-shot 31% on those. | "Generalist VLM solvers now beat visual CAPTCHAs (USENIX Sec 2025)." Do not name Arkose. |
| BNPL +211% (Sift 2025) | Mis-dated | Sift Q1 2023 index, BNPL merchants, 2022 vs 2021 | "Sift 2023: BNPL payment fraud +211% YoY." |
| "+340% agent-driven attacks" | No source found | Thales 2026 Bad Bot Report (2025 data): AI-driven bot attacks up **12.5×** YoY, all industries; financial services = 46% of account-takeover incidents. *(SECONDARY listing)* | Use Thales, labelled "all industries". |
| "85% of new fraudulent accounts are synthetic, globally" | Over-stated | Widely repeated "80–85%" is a US, vendor-origin estimate (ID Analytics, repeated in Fed-related literature). *(SECONDARY)* | "Industry estimates put synthetic identities at 80%+ of new-account fraud (US, vendor estimates)." |
| Agentic fraud context | New, usable | BioCatch June 2026 survey (reported via FinTech News): 89% of LatAm institutions saw agentic attacks; 76% say fraud losses rose in 2026. *(SECONDARY, vendor survey)* | Cite as "vendor survey". |
| Krazybee / ₹65.87 Cr | Misleading | HC quashed proceedings 11 Mar 2025 (Indian Kanoon; company's SEBI filings) | Drop it, or say "regulatory scrutiny of digital lenders is intense". |
| ghost-cursor "bypassed Cloudflare at 0.9" (Black Hat/DEF CON 31) | Unsupported | It is an open-source Puppeteer library using Bézier curves and Fitts's law. Multiple scraping vendors say it does *not* beat Cloudflare or DataDome. No conference talk found. | "Open-source tools like ghost-cursor generate Bézier cursor paths." |
| Aadhaar gate cost ₹15–30 (deck 1) | Outdated | UIDAI cut the fee from ₹20 to ₹3 in 2021 (CEO statement, Sept 2021). Master book's "₹3 + routing" is right. | Use the master-book table only. |
| CFPB Circular 2023-03 as law | Withdrawn | Withdrawn 12 May 2025 in a batch of 67 documents, including Circular 2022-03 | Cite ECOA (15 U.S.C. §1691) and Reg B (12 CFR §1002.9) only. |
| RBI guidelines RBI/2022-23/111 | Superseded | RBI (Digital Lending) Directions, 2025 (RBI/2025-26/36, 8 May 2025) replaced them | Cite the 2025 Directions. |
| EU AI Act €35M / 7% | Wrong tier | Art. 99(4): up to €15M or 3% for most operator duties. 7% applies to Art. 5 prohibited practices. | "Up to €15M or 3% of turnover." |
| EU AI Act Annex III credit AI is high-risk | Incomplete | Point 5(b) *excludes* AI used to detect financial fraud. The carve-out is narrow if fraud output feeds a creditworthiness model. | See Section 8. |
| "Zero-PII" | Over-claim | DPDP Act treats all personal data uniformly. Behavioral data tied to an applicant is personal data. | "Data-minimized; no raw text or credentials stored." |
| 8–12 Hz physiological tremor | *(FROM MEMORY)* | Not re-checked this round | Keep, but do not build the whole kinetic claim on it. |
| OnlyFake ($15/ID) and 815M Indian records breach | *(FROM MEMORY)* | Not re-checked this round | Re-verify before presenting. |

---

## 3. Competitor reality

| Vendor | What I verified | Where you win | Where they challenge you |
|---|---|---|---|
| **BioCatch** | Scout graph (50k nodes / 250k edges, 3,000+ signals, galaxy UI). Account Opening Protection targets bots, scripts, AI agents, and synthetic identities on unseen users. | Local, zero-cloud, per-lender; open evidence trail; explicit regulator artifacts (SAR). | They have the graph, the data and the scale. Your claim cannot be "they can't". |
| **DataVisor** | Patented unsupervised ring detection, clustering plus graph analysis, outputs "detection reasons". 15,000+ queries/sec and sub-100 ms decisions claimed. | Behavioral-physics layers and pre-KYC cost gating story. | They already explain clusters and handle application fraud. |
| **Featurespace (ARIC)** | Visa completed the acquisition on 19 Dec 2024. Models each customer's own behavior; on-prem option exists. | Application-side, cross-session. | Largely transaction-side, so partly complementary. |
| **Sift / ThreatMetrix** | *(Not re-researched.)* Sift markets cross-dimensional identity signals across its network. | Behavior edges survive proxy rotation. | Consortium data you cannot match. |

**Safest positioning (our reasoning):** you are not the first graph defense. You are an **open, explainable, pre-KYC triage layer for a lender**, with regulator-ready evidence and a quantified cost-saving story.

---

## 4. Academic landscape (what to cite, and what each one gives you)

- **Coordination detection lineage:** SynchroTrap (CCS 2014); a 2024 survey of coordinated online behavior (arXiv 2408.01257); Iannucci et al., ICWSM 2026, whose multiplex time-aware model uses an exponential-decay time kernel and beats earlier methods. *(VERIFIED)* Use these to justify your multi-layer design and your long time windows.
- **Graph-model attacks:** BOCLOAK (ICML 2026, arXiv 2602.00318) attacks GNN bot detectors with sparse edge edits and reports up to 80.13% higher attack success than prior graph attacks. *(VERIFIED)* **Our reasoning:** BOCLOAK edits *declared* graph links (social follows). Your edges are *computed by the defender from observed telemetry*. The attacker cannot add an edge. They must change real behavior. That is a structural advantage over social-graph Sybil attacks, and it holds only while the five layers stay independent.
- **Mouse-evasion literature:** BeCAPTCHA-Mouse (Pattern Recognition, 2022) uses neuromotor (Sigma-Lognormal) features and reports 93% accuracy from one trajectory against GAN fakes. The Bournemouth GAN-evasion study shows attackers can generate human-like mouse and touch trajectories. The 2026 TUM/Kontext paper (a workshop paper, single LLM, Playwright only) shows event-stream artifacts beat trajectory realism. *(VERIFIED)* **Implication:** replace "third-derivative jerk" with neuromotor-model features and event-stream features. Raw jerk is noise-dominated at about 60 Hz sampling.
- **Community detection:** Leiden (Scientific Reports, 2019): guaranteed connected communities and faster than Louvain. Fortunato and Barthélemy (PNAS, 2007): modularity can miss modules smaller than roughly √(L/2) internal edges (the abstract states the scale as order √(2L)). With L = 1,000,000 edges, that is about 700–1,400 edges. A 10-bot clique has only 45. *(VERIFIED)*

---

## 5. Technical stress test (updated)

**Timing.** Random sleeps or Poisson jitter defeat a fixed Δt < 100 ms rule, and slow-drip attacks defeat any short window. Defense: 24 h sliding window with decay kernel (Iannucci et al.), and a baseline-rate model: p = P(Poisson(λw) ≥ k) for k arrivals in window w. Treat timing as one weak vote.

**Kinetic.** Noise on a Bézier path breaks "jerk ≈ 0". GAN and replay break trajectory realism. What survives:
1. **Event-stream artifacts** (raw-event rate, click-duration variance, teleport-before-click, wheel presence). These beat Playwright and likely other CDP-driven tools, but not OS-level input.
2. **Same-generator test (our reasoning):** i.i.d. noise makes each trace unique but leaves the *distribution* unchanged. Compare sessions with a two-sample test (MMD or energy distance) on motion features.
3. **Mobile gap:** Indian lending is mostly mobile, and there is no cursor on touch. Name touch dynamics as the mobile equivalent.

**Graph poisoning.** Decoy bots, bridge nodes and dilution lower Q. Defense: Leiden per connected component after sparsification, ranking by density and permutation p-value, not raw Q. Note that Q scores a whole partition. Per-community contribution is L_c/m − (d_c/2m)². That is still not a significance test.

**Flash crowd (the real danger).** A trending loan creates synchronized arrivals, similar semantics and identical routes, all from one common cause. DataVisor's own blog concedes that benign coordinated groups exist. Separation (our reasoning): an external event correlates only the layers it drives (time, semantics, route). It does not correlate hand motion or hardware. So:
1. Require at least one common-cause-immune layer per edge (event-stream/kinetic distribution).
2. Weight route and semantic similarity by rarity against the population baseline. Your 3-step funnel gives every honest user near-identical routes, so use field-level events (focus order, paste, backspace rate).
3. Compute significance by permutation: shuffle session labels inside the time window 1,000 times and report the empirical p-value.
4. Treat `S_env` as weak. A campus full of identical laptops shares WebGL and Audio hashes.

---

## 6. Reinforcements, ranked by value per hour

1. **Two-key detection (new, do tonight).**
   - **Key 1:** per-session automation artifacts (cheap, strong against CDP tools).
   - **Key 2:** relational graph (survives when attackers hide artifacts).
   - Add an **artifact-masked swarm mode**: dense raw pointer events, human-sampled click durations, random sleeps, unique personas. Show the graph still clusters them via semantic, route-field, timing-distribution and generator-parameter edges. This answers the strongest critique in Finding 5.
2. **Statistical Proof Card (do tonight).** Replace "P < 10⁻⁵" with a live permutation-null histogram and an empirical p-value. A regulator can re-run it.
3. **Graph-triggered adaptive friction (roadmap).** Plain PoW is weak. 2 s CPU × 100,000 sessions is about 55 CPU-hours, roughly $2 on cloud (our arithmetic). Practitioners also flag low-end phones, GPU asymmetry for attackers, and memory cost (ALTCHA's Argon2id guidance suggests 64–128 MB). GeeTest already applies PoW adaptively, so the idea is not new. Your angle: the *trigger* is cluster membership, so honest users never pay.
4. **Spectral add-on (roadmap).** Cheeger inequality: λ₂/2 ≤ h(G) ≤ √(2λ₂) links the Laplacian's second eigenvalue to cluster conductance. It gives an independent isolation certificate. Hypergraphs fit burst arrivals (one hyperedge per 50 ms window).
5. **Skip:** persistent homology and full causal discovery. Use conditional independence across layers instead.

---

## 7. Judge battlecards

**Q1. "Bots just add `sleep(random(1,10))`."**
That removes Δt only. Route-field sequence, text semantics and motion distribution remain. Uniform(1,10) delays also differ from heavy-tailed human think times (a KS test separates them). For slow-drip attacks we keep a 24 h decay-weighted window. We show this live in the masked mode.

**Q2. "Louvain is O(N log N) or O(N²). It will crash at 100,000 sessions."**
The O(N²) cost is pairwise scoring, which we avoid via blocking (ANN/LSH on embeddings, time buckets, hash buckets). The graph stays sparse. Leiden is faster than Louvain in the published benchmarks. As an industry reference, BioCatch Scout visualizes 50k-node / 250k-edge graphs, and SynchroTrap ran at Facebook scale on Hadoop/Giraph (our design is smaller and single-lender). Do not claim a measured 100k number until you run the benchmark tonight.

**Q3. "Why can't BioCatch or Cloudflare add this tomorrow?"**
Concede they already have graph analytics (Scout). The moat is position and artifact: pre-KYC inside one lender's funnel, local zero-PII-minimized inference, an auditable Why Card and SAR, and the verification-cost savings story. Do not say they cannot.

**Q4. "How do you legally deny a loan based on someone else's mouse movements?"**
The evidence is about the applicant's own session and its statistical match to an automated cluster. The action is quarantine plus step-up verification, not a permanent ban, and an officer reviews it. Under Reg B (12 CFR §1002.9) a specific reason is required for adverse action; a reason like "identity could not be verified; session matched an automated cluster" is specific and checkable. *(Not legal advice.)*

**Q5. "Playwright is detectable per session. Why do you need a graph?"**
Per-session detectors are brittle: in the TUM study, binary MLP and SAINT detectors let 39.1% and 34.5% of real agents through as human, and the strong signal vanishes if attackers use OS-level input or hardware emulation, which the authors explicitly exclude. Coordination across sessions does not depend on how events are generated. We run both keys and show the masked mode.

**Q6. "Isn't this BioCatch Scout or DataVisor?"**
Same family, different deployment. Concede the lineage (SynchroTrap, DataVisor). Differentiators: local and open, pre-KYC cost gating, regulator-ready evidence, and a statistical proof you can re-run.

---

## 8. Regulatory pack

- **US:** ECOA and Reg B remain. Circular 2023-03 and Circular 2022-03 were withdrawn (12 May 2025). The agency also said it would deprioritize enforcement of conduct that departs from withdrawn guidance, so do not describe the statute as unenforceable either.
- **India:** RBI (Digital Lending) Directions, 2025, effective 8 May 2025, replace the 2022 Guidelines. They require documented borrower assessment (para 7) and explicit, audit-trailed consent for data collection (para 12). The DPDP Rules were notified 13 Nov 2025; most substantive duties start about 18 months later (around May 2027), consent-manager registration earlier. I found no source confirming an explicit "no black-box credit assessment" rule in the Directions, so drop that sentence from the book unless you can cite a clause. One secondary source claimed a DPDP "Section 11 right against automated decisions"; I could not confirm it and I doubt it, so do not repeat it.
- **EU:** Annex III 5(b) lists creditworthiness AI as high-risk but *excludes* AI used to detect financial fraud. Narrow rule: if fraud output is fused into a creditworthiness model, the exemption may not apply. Fines for high-risk operator duties are up to €15M or 3% (Art. 99(4)). A secondary source reports the Digital Omnibus delayed standalone Annex III obligations from 2 Aug 2026 to 2 Dec 2027; verify before stating.

---

## 9. What to do tonight (priority order)

1. **Rewrite the claims** (30 min, Nihad): apply Sections 1–2 and 8. Remove "world's first", "zero-PII", the BioCatch "fails day zero" line, Krazybee, the unsourced stats, and the wrong fine tier.
2. **Permutation Proof Card** (1.5 h, Pete): null histogram plus empirical p-value in the Why Card.
3. **Leiden swap** (45 min, Pete): per-component clustering; rank by density and p-value.
4. **Artifact-masked swarm mode** (2 h, Alan): raw pointer events, human-sampled click durations, random sleeps, unique personas.
5. **Human control group** (30 min, team): 5 people fill the form at once and stay unclustered.
6. **Field-level route layer** (1 h, Pete): focus order, paste events, backspace rate, weighted by rarity.
7. **100k-node benchmark** (45 min, Pete): planted-partition graph, quote the real time.
8. **"SIMULATION MODE" label** on the Tier 3 fallback screen.

---

## 10. Sources

**Verified this round**
- Halligan CAPTCHA solver, USENIX Security 2025: https://www.usenix.org/conference/usenixsecurity25/presentation/teoh
- ViPer, USENIX Security 2026: https://arxiv.org/abs/2601.06461
- TUM/Kontext agent-detection paper (2026 workshop): https://arxiv.org/abs/2607.26935
- BeCAPTCHA-Mouse: https://arxiv.org/abs/2005.00890
- BOCLOAK (ICML 2026): https://arxiv.org/abs/2602.00318
- Iannucci et al., ICWSM 2026: https://ojs.aaai.org/index.php/ICWSM/article/view/42682
- Coordinated-behavior survey: https://arxiv.org/abs/2408.01257
- SynchroTrap (CCS 2014): https://scholars.duke.edu/publication/1050883
- Leiden algorithm: https://arxiv.org/abs/1810.08473
- Resolution limit: https://arxiv.org/abs/physics/0607100
- BioCatch Scout: https://www.biocatch.com/press-release/biocatch-announces-biocatch-scout
- BioCatch Account Opening Protection: https://www.biocatch.com/account-opening-protection
- DataVisor UML and cluster-quality blog: https://www.datavisor.com/wiki/unsupervised-machine-learning and https://www.datavisor.com/blog/quantifying-cluster-quality-with-unsupervised-machine-learning
- Visa/Featurespace: https://investor.visa.com/news/news-details/2024/Visa-Completes-Acquisition-of-Featurespace/default.aspx
- Krazybee judgment: https://indiankanoon.org/doc/103009550/
- CFPB withdrawal: https://kriegdevault.com/insights/cfpb-withdraws-67-guidance-documents
- Sift BNPL +211%: https://sift.com/blog/digital-trust-safety-roundup-payment-fraud-targets-fintech/
- UIDAI fee cut: https://www.businesstoday.in/latest/economy/story/aadhaar-authentication-charge-slashed-to-rs-3-uidai-ceo-307903-2021-09-29
- ghost-cursor repo: https://github.com/xetera/ghost-cursor
- RBI Digital Lending Directions 2025 explainers: https://synergialegal.com/an-overview-of-the-rbis-digital-lending-direction-2025/
- DPDP Rules 2025: https://www.jsalaw.com/wp-content/uploads/2025/11/JSA-Prism-InfoTech-November-2025-DPDP-Rules.Final_.pdf
- EU AI Act Art. 99: https://ai-act-service-desk.ec.europa.eu/de/ai-act/article-99

**Secondary or vendor sources (treat as indicative)**
- Thales 2026 Bad Bot Report listing: https://www.techtarget.com/hub/asset/1787288698_197
- BioCatch June 2026 agentic survey coverage: https://fintechnews.sg/133560/ai/the-rise-of-agentic-ai-in-cyber-fraud-and-scams/
- Annex III 5(b) fraud exemption and Omnibus delay (law-firm and consultancy blogs): https://www.deepinspect.ai/blog/finance-eu-ai-act and https://ai2.work/blog/eu-delays-ai-credit-scoring-rules-16-months-what-lenders-do-now
- PoW CAPTCHA trade-offs: https://www.kevnu.com/en/posts/21 and https://altcha.org/docs/v2/proof-of-work-captcha/

**Not re-verified (from memory):** CopyCatch (WWW 2013), Fraudar (KDD 2016), Elble and Randall tremor work, OnlyFake and the 815M breach, Cheeger inequality statement, Hawkes-process baseline suggestion.
