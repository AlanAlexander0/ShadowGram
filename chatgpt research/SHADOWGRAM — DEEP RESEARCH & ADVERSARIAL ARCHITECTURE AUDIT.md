PART 1 — RESEARCH POSITIONING AND THE CORE THESIS
1. Audit objective

This audit evaluates ShadowGram as a proposed fraud-defense system for digital lending and high-speed application funnels.

The objective is not to prove that ShadowGram is already superior to commercial fraud systems.

The objective is to determine:

Which parts of the original ShadowGram architecture are technically defensible.
Which claims are supported by published research or official documentation.
Which claims are assumptions.
Which architectural components are already common in commercial systems.
Where a genuine technical gap may exist.
Which proposed innovations are worth implementing for the hackathon.
Which claims should be removed from the presentation.
Which experiments can demonstrate ShadowGram's value without requiring access to real bank data.
2. The most important architectural correction

The original ShadowGram thesis was:

"Traditional fraud systems evaluate accounts independently, while ShadowGram detects the relationship between accounts."

This is too broad.

It is not defensible to claim that existing fraud vendors cannot perform relational analysis.

Modern fraud systems already use:

device relationships
identity relationships
behavioral relationships
network relationships
shared attributes
consortium intelligence
graph/link analysis
machine learning
behavioral biometrics

The new 2026 research landscape makes this particularly clear.

A recent peer-reviewed study on synthetic-identity fraud explicitly evaluates heterogeneous identity graphs connecting clients to shared SSNs, email addresses and phone numbers. It found that graph structure can improve detection when the relationships are complete and useful.

Therefore:

❌ Do NOT claim

"ShadowGram invented relational fraud detection."

❌ Do NOT claim

"BioCatch/Sift/DataVisor cannot detect relationships."

❌ Do NOT claim

"Existing vendors only inspect accounts individually."

✅ Instead claim

"ShadowGram investigates whether low-cost, pre-verification behavioral relationships can be used as an additional early-stage signal for coordinated application attacks."

That is substantially stronger.

It is narrower.

It is testable.

And importantly, it is something you can actually demonstrate at a hackathon.

3. The strongest version of the ShadowGram thesis

The research-backed version should become:

Fraud detection does not have to depend exclusively on the risk of an individual applicant. Some attacks create relationships between otherwise low-risk sessions. ShadowGram attempts to detect those relationships before expensive downstream verification by combining early behavioral telemetry with lightweight relational analysis.

This distinction is critical.

ShadowGram is no longer claiming:

"Everyone else is doing fraud detection wrong."

Instead, it asks:

"Can we detect coordinated application behavior earlier and more cheaply?"

That is a much more interesting engineering question.

4. Why "individually legitimate, collectively suspicious" is still valuable

Consider three applications.

Account A
normal-looking name
normal typing
normal IP
normal browser
normal loan request

Nothing obviously fraudulent.

Account B

Almost the same situation.

Nothing obviously fraudulent.

Account C

Again, individually plausible.

Traditional per-session detection may therefore assign:

A → low risk
B → low risk
C → low risk

But suppose the following relationships exist:

A ─────┐
       │
B ─────┼── very similar application sequence
       │
C ─────┘

And:

A → same unusual field order
B → same unusual field order
C → same unusual field order

A → same unusual timing distribution
B → same unusual timing distribution
C → same unusual timing distribution

A → same unusual navigation sequence
B → same unusual navigation sequence
C → same unusual navigation sequence

None of these features necessarily proves fraud.

But their joint relationship can become interesting.

That is the actual basis for ShadowGram.

5. Important distinction: correlation ≠ fraud

This is one of the biggest weaknesses in the original design.

Suppose 100 students apply for a loan during a college campaign.

They may all:

use the same Wi-Fi
open the same page
follow the same navigation path
apply within the same hour
enter similar information
use the same mobile network

A naive graph detector could interpret this as:

HIGH CONNECTIVITY
      ↓
FRAUD

That would be wrong.

Therefore ShadowGram must instead implement:

RELATIONSHIP
      ↓
ANOMALY
      ↓
MULTI-SIGNAL EVIDENCE
      ↓
RISK / STEP-UP

not:

RELATIONSHIP
      ↓
BAN

This is why your common-cause protection is actually an important research direction.

6. A better mental model for ShadowGram

The system should have three questions.

Question 1 — Does this session look automated?
Session A
   ↓
automation evidence

This is the first key.

Examples:

missing expected interaction events
impossible event ordering
abnormal event timing
automation fingerprints
unrealistic interaction patterns
Question 2 — Does this session resemble other sessions?
A ↔ B
A ↔ C
B ↔ C

This is the relational layer.

It can compare:

temporal behavior
navigation sequence
interaction-event distributions
semantic application content
device/environment signals
Question 3 — Could the relationship have a legitimate common cause?

For example:

100 students
     ↓
same campus
     ↓
same Wi-Fi
     ↓
same campaign

If yes:

DOWN-WEIGHT RELATIONSHIP

If instead:

100 accounts
     ↓
same strange interaction sequence
     ↓
same unusual timing
     ↓
same semantic structure
     ↓
same device characteristics
     ↓
no legitimate common cause

then:

ESCALATE FOR REVIEW / STEP-UP

That is a much more defensible architecture.

7. Major research validation: graph-based fraud detection is real

This is one of the strongest pieces of evidence for ShadowGram.

A paper published in Discover Informatics in October 2026 evaluated synthetic-identity fraud using a heterogeneous graph connecting:

Client
 ↓
SSN
 ↓
Email
 ↓
Phone

The researchers compared:

rule-based detection
traditional machine learning
propagation methods
graph models
hybrid rule + graph models

Their key conclusion was particularly relevant:

Graph learning's value came from structural relationships, rather than simply making the final score more complicated.

Their Rule + HGT + SVM hybrid achieved average PR-AUC of 0.835, compared with 0.777 for their rule-only baseline in that benchmark.

Why this matters to ShadowGram

It supports the fundamental idea that:

relationships between entities can contain fraud information that is not obvious from an isolated entity score.

But it does not prove that ShadowGram's particular five behavioral layers work.

That still requires your own experiment.

8. This suggests a major improvement to ShadowGram

Your current design treats the graph almost as:

behavior similarity
       ↓
weighted similarity score
       ↓
edge
       ↓
Leiden

The research suggests something more interesting.

Instead of making ShadowGram a giant weighted-score machine, consider:

Evidence graph

Each edge should retain why the relationship exists.

For example:

A ───────── B

Relationship evidence:

Temporal similarity     0.94
Navigation similarity   0.91
Semantic similarity     0.87
Kinetic similarity      0.72
Environment similarity  0.83

Common-cause score      0.12

Then:

Relationship = explainable evidence

rather than:

Relationship = mysterious 0.84

This makes your Why Card much stronger.

9. New concept: Evidence-Carrying Edges

I recommend adding this to ShadowGram.

Current idea
A ─── 0.82 ─── B
Improved idea
A ───────────── B
│
├── temporal:     0.91
├── navigation:   0.88
├── semantic:     0.84
├── kinetic:      0.76
├── environment:  0.81
│
└── common-cause: 0.09

Now the graph is not simply saying:

"These accounts are similar."

It says:

"These accounts are similar for these measurable reasons."

That is much better for:

judges
debugging
research
explainability
false-positive investigation
future patent work
reproducibility
10. Another important correction: the "AI swarm" narrative

Your original document repeatedly says:

"Modern scammers use autonomous multi-agent AI swarms."

That is currently too strong as a universal statement.

There is good evidence that AI agents and vision-language models can automate tasks previously difficult for bots.

For example, the USENIX Security 2025 Halligan research demonstrated generalized automated CAPTCHA solving using an agentic VLM. It achieved 60.7% across 2,600 challenges and 70.6% on previously unseen real-world challenges.

That supports:

AI-assisted automation is becoming more capable.

It does not establish:

"Most modern financial fraud is now conducted by autonomous AI swarms."

Therefore the ShadowGram threat model should say:

"ShadowGram stress-tests against coordinated automated agents, including AI-assisted browser agents, rather than assuming that every real-world fraud attack already uses autonomous AI swarms."

This is scientifically much safer.

11. Why this actually makes the hackathon story stronger

You don't need to prove:

"This exact attack is happening everywhere."

You can demonstrate:

"We constructed a controlled adversarial environment where individually plausible automated sessions attempt to evade single-session detection, and we test whether relational behavioral evidence can identify the coordinated group."

That is a legitimate cybersecurity experiment.

Your live demonstration becomes:

NORMAL HUMAN
      ↓
normal behavioral evidence
      ↓
GREEN

BOT 1 ─┐
BOT 2 ─┤
BOT 3 ─┤
BOT 4 ─┤
BOT 5 ─┤
        ↓
similar behavioral relationships
        ↓
GRAPH
        ↓
COMMUNITY
        ↓
WHY CARD
        ↓
STEP-UP / QUARANTINE

That is compelling without making an unverifiable real-world claim.

12. Research direction emerging from the audit

The most interesting version of ShadowGram is therefore becoming:

Pre-verification behavioral coordination detection

Not:

AI fraud detector.

Not:

AI swarm detector.

Not:

replacement for BioCatch.

Not:

replacement for KYC.

Instead:

A lightweight early-stage coordination-analysis layer that identifies suspicious relationships among application sessions before expensive identity verification and downstream decisioning.

This is a much cleaner innovation claim.

13. Current research confidence map
ShadowGram claim	Audit status
Fraud can involve relationships between accounts	✅ Strong
Graph analysis can help fraud detection	✅ Strong
Synthetic identity fraud can create identity relationships	✅ Strong
Graph models can complement rule-based detection	✅ Supported
AI/VLMs can automate CAPTCHA solving	✅ Strong evidence
AI-assisted automation is an emerging threat	✅ Supported
Every modern fraud attack uses AI swarms	🔴 Unsupported
Existing vendors only inspect accounts individually	🔴 False/overstated
Existing vendors cannot perform graph analysis	🔴 False
ShadowGram's exact five-layer graph is superior	🧪 Must test
ShadowGram can detect coordinated application attacks	🧪 Must test
Pre-KYC behavioral analysis can reduce verification calls	🧪 Must demonstrate
Leiden is automatically better for ShadowGram	🟡 Needs benchmark
Q > 0.60 means fraud	🔴 Incorrect
p < 0.001 automatically proves a fraud cluster	🔴 Incorrect
Evidence-carrying graph edges improve explainability	💡 Strong design direction
Common-cause controls reduce false positives	💡 Strong research hypothesis
14. Critical warning about your current mathematical claims

These should not remain in the final architecture as currently written:

Modularity Q > 0.60
        ↓
syndicate

and:

p < 0.001
        ↓
fraud

Neither follows mathematically.

A high modularity score means something about community structure, not that the community is fraudulent.

A low permutation-test p-value means that a statistic is unusual under the chosen null model.

It does not mean:

"The accounts are definitely fraudulent."

This is a major place where we can improve ShadowGram.

The correct chain is:

Graph structure
      ↓
statistical anomaly
      ↓
behavioral evidence
      ↓
risk score
      ↓
step-up / analyst review

rather than:

Q > 0.6
      ↓
FRAUD
15. The next research parts

I suggest we build the remaining audit in this order:

PART 2

Threat landscape audit

synthetic identity
coordinated applications
AI browser agents
CAPTCHA automation
bot farms
device farms
residential/mobile proxies
account farming
mule networks
flash attacks
PART 3

Competitor audit

We will investigate individually:

BioCatch
Sift
LexisNexis ThreatMetrix
DataVisor
Arkose
Cloudflare
reCAPTCHA
Featurespace
Feedzai
Sardine
Socure

And determine exactly what ShadowGram can legitimately claim as different.

PART 4

Five-layer telemetry audit

We will test whether:

temporal rhythm
navigation sequence
kinetic dynamics
semantic similarity
environment/device signals

are actually useful, redundant, spoofable, privacy-safe, and computationally feasible.

PART 5

Graph algorithm audit

Compare:

pairwise graph
blocking
ANN
Louvain
Leiden
connected components
label propagation
heterogeneous graphs
temporal graphs
GNNs

and determine what is actually worth implementing on your laptops.

PART 6

Statistical validation

We will redesign:

thresholds
null models
permutation tests
false-positive controls
precision/recall
PR-AUC
ROC-AUC
detection latency
cost saved
PART 7

Denial-of-Wallet hypothesis

We will independently verify the actual India verification costs instead of using the current ₹33.50–₹118.50 table blindly.

PART 8

Regulatory/legal audit

We will verify:

RBI Digital Lending Directions
PMLA claims
ECOA / Regulation B
EU AI Act
SAR terminology
adverse-action claims
UPI step-up idea
what ShadowGram must not claim legally
PART 9

Adversarial red-team

We will actively try to break ShadowGram:

random delays
random navigation
different semantic text
device spoofing
shared Wi-Fi
mobile networks
human-assisted bots
AI browser agents
bridge accounts
slow-drip attacks
legitimate traffic surges
PART 10

New cutting-edge architecture

Only after the audit will we decide what genuinely deserves to be called:

ShadowGram 2.0

This is where we can potentially introduce things such as:

evidence-carrying temporal graphs
adaptive relationship discovery
common-cause inference
adversarially robust behavioral fingerprints
temporal community evolution
uncertainty-aware graph scoring
explainable edge provenance
cost-aware pre-KYC decisioning
adversarial simulation
human-in-the-loop step-up orchestration

I recommend we do NOT implement all of these blindly. The point of the next parts is to discover which ones actually survive the evidence audit.

And importantly: the audit is already finding useful directions rather than turning ShadowGram into a generic research paper. The 2026 synthetic-identity graph research gives us a real external basis for the relational part, while the USENIX CAPTCHA research gives us a strong basis for stress-testing against increasingly capable automation.

PART 2 — THREAT LANDSCAPE & ADVERSARIAL MODEL AUDIT

Purpose of this section: Determine what threat ShadowGram should actually defend against.
Important: This section deliberately separates documented threats from future/adversarial scenarios. ShadowGram should not claim that every attacker already uses autonomous AI swarms.

2.1 Executive Finding

The original ShadowGram document describes the threat as:

"Modern scammers use autonomous multi-agent AI swarms."

That statement is too absolute.

The evidence supports a more careful conclusion:

Automation is becoming increasingly capable, including AI-assisted browser automation and vision-language-model-based interaction. Financial fraud already involves identity abuse, coordinated activity, account creation abuse, and automated attacks. However, there is insufficient evidence to claim that most real-world digital-lending fraud is currently performed by autonomous multi-agent AI swarms.

This distinction matters.

ShadowGram does not need to prove that AI swarms are already responsible for a particular percentage of fraud.

For the hackathon, the stronger approach is:

ShadowGram is adversarially tested against increasingly capable automated agents, including agents capable of human-like browser interaction.

That turns the "AI swarm" from an unsupported factual claim into a controlled threat model.

2.2 Threat Class A — Identity Abuse

Identity-related abuse is not hypothetical.

FinCEN analyzed identity-related suspicious activity reported by financial institutions and found approximately 1.6 million reports in 2021, representing about 42% of all reports filed that year, associated with approximately $212 billion in suspicious activity. FinCEN described identity processes during account creation, account access, and transaction processing as important areas of exploitation.

This supports ShadowGram's focus on the application/identity stage.

However:

It does NOT prove
identity fraud
      ↓
AI swarm
      ↓
micro-loan attack

That causal chain must not be presented as an established fact.

What it does establish
identity process
      ↓
important fraud attack surface

That is enough to justify investigating early-stage signals.

2.3 Threat Class B — Synthetic Identity Fraud

Synthetic identity fraud is particularly relevant.

A synthetic identity can combine:

real information
       +
fabricated information
       +
stolen information
       ↓
apparently legitimate identity

This is different from simply stealing somebody's complete identity.

That distinction is important for ShadowGram.

A synthetic identity may not produce an obvious red flag when examined independently.

The interesting detection opportunity is therefore:

Applicant A → plausible

Applicant B → plausible

Applicant C → plausible

       BUT

A ↔ B ↔ C

where the relationships between applicants reveal something unusual.

2.4 Strong 2026 Evidence for the Relational Approach

A particularly relevant 2026 study evaluated synthetic-identity fraud using a heterogeneous graph.

The researchers modeled:

Client
  │
  ├── SSN
  ├── Email
  └── Phone

The resulting graph allowed multiple client nodes to converge on shared identifiers.

The study found that a hybrid approach combining transparent rule-based scoring with graph learning achieved an average PR-AUC of 0.835, compared with 0.777 for the rule-only baseline in its experimental setting. Removing individual identity relationships consistently reduced performance.

This is extremely relevant to ShadowGram.

It provides independent evidence for the general proposition:

Relationships between entities can contain fraud information that is not captured by looking at each entity independently.

However, there is an important limitation.

The researchers used:

synthetic/benchmark data
explicit identity relationships
SSN
email
phone

They did not prove that:

mouse dynamics
+
navigation
+
semantic vectors
+
timing
+
hardware entropy

will produce the same result.

Therefore ShadowGram still needs its own experiment.

2.5 New Research Direction: Behavioral Relationship Graph

This suggests that ShadowGram should distinguish two kinds of graph relationships.

Identity graph
User
 ↓
Phone
 ↓
Email
 ↓
Address
 ↓
Identity
Behavioral graph
Session A
   ↕
Session B
   ↕
Session C

relationships based on:

timing
navigation
interaction
semantic behavior
environment

The second graph is where ShadowGram can potentially differentiate itself.

The research evidence already supports the value of relational fraud analysis.

ShadowGram's research question becomes:

Can behavioral relationships provide useful early-warning signals before expensive identity verification?

That is a much stronger research question than:

"Can graphs detect fraud?"

Graph-based fraud detection is already established.

2.6 Threat Class C — Increasingly Capable Automated Agents

This is where the "AI swarm" concept becomes relevant.

AI systems are becoming increasingly capable of interacting with websites and completing multi-step tasks.

But ShadowGram should distinguish:

Traditional scripted automation
HTTP requests
Selenium
Playwright
fixed scripts

from:

Adaptive automation
agent
 ↓
browser
 ↓
observe page
 ↓
reason
 ↓
choose action
 ↓
continue

The second category is much more difficult to identify using simple rules.

2.7 CAPTCHA Is No Longer a Sufficient Threat Model

This part of the original ShadowGram document is supported by strong academic evidence.

A USENIX Security 2025 paper introduced Halligan, a generalized visual CAPTCHA solver based on a vision-language model.

The researchers evaluated it on 2,600 CAPTCHA challenges across 26 types and reported a 60.7% solving rate. They also evaluated previously unseen CAPTCHA challenges in the wild and reported an average 70.6% solving rate over a 30-day period.

This does not mean:

"CAPTCHA is completely broken."

It means:

The assumption that visual CAPTCHA challenges are inherently difficult for modern automated systems is becoming less reliable.

That is directly relevant to ShadowGram.

2.8 Implication for ShadowGram

ShadowGram should not depend on:

CAPTCHA
   ↓
bot defeated

Instead:

CAPTCHA
   +
session telemetry
   +
behavior
   +
relationships

should be considered separate layers.

This gives ShadowGram an important architectural principle:

Do not assume that successfully completing a challenge proves that the actor is human.

A sufficiently capable agent may solve the challenge.

The question becomes:

What behavioral evidence does the agent leave behind while completing the workflow?

2.9 Threat Class D — Bot Traffic Is Already Significant

The 2026 Thales Bad Bot Report reports that bots accounted for 53% of internet traffic in its analysis of 2025 activity, with 40% classified as bad bots. It also reports that AI-enabled bot attacks increased 12.5× year over year in its dataset.

These figures come from a commercial vendor's telemetry rather than neutral academic measurement.

Therefore:

Use in presentation

You can say:

"Commercial security telemetry indicates rapid growth in AI-enabled automated traffic."

Avoid saying

"53% of all Internet traffic is malicious."

The report itself distinguishes:

53% = bots
40% = bad bots
47% = human traffic

So the numbers must not be conflated.

2.10 Threat Class E — Financial Services Are a Relevant Target

The same Thales report states that:

24% of bot attacks in its dataset targeted financial services.
46% of account takeover attacks targeted financial services.
27% of bot attacks targeted APIs.

Again, these are vendor telemetry figures.

They should be treated as industry evidence, not universal measurements.

But they support the general threat model:

financial services
       ↓
high-value automated attack surface
2.11 Threat Class F — API Abuse

This is particularly relevant to your Denial-of-Wallet hypothesis.

Modern applications increasingly depend on API calls for:

identity verification
credit checks
document verification
liveness
risk scoring
account creation

Therefore an attacker does not necessarily need to steal money directly.

They may instead generate large amounts of:

application traffic
       ↓
verification requests
       ↓
API expenditure
       ↓
operational load

This is a valid attack hypothesis.

But ShadowGram currently has a problem:

You have not yet established that
₹33.50–₹118.50

is a universal or representative cost for an Indian lending application.

That must be separately audited.

Do not use the current cost table as verified evidence yet.

2.12 Threat Class G — Coordinated Application Bursts

This is one of the most useful threats for the hackathon because it is easy to simulate safely.

Example:

09:00:00
Bot A
Bot B
Bot C
Bot D
...
Bot T

All initiate an application within a short window.

A conventional rate limiter might detect:

20 requests
↓
high request rate
↓
block

But ShadowGram can test a harder scenario:

Bot A → 09:00:00
Bot B → 09:00:07
Bot C → 09:00:13
Bot D → 09:00:21
...

Now the attack deliberately avoids a simple burst threshold.

This is where the temporal relationship becomes interesting.

2.13 Threat Class H — Slow-Drip Coordination

This should be added to your red-team test suite.

Instead of:

20 bots
↓
30 seconds

use:

Bot A → 09:00
Bot B → 09:03
Bot C → 09:07
Bot D → 09:12
Bot E → 09:16
...

The attack remains coordinated but does not produce an obvious burst.

This tests whether ShadowGram's graph actually captures relationships rather than merely detecting rate spikes.

2.14 Threat Class I — Behavioral Randomization

Your original design assumes attackers may produce identical behavior.

That is too easy to defeat.

A sophisticated red-team simulation should randomize:

typing speed
pause duration
navigation timing
field order
mouse movement
scroll timing
loan explanation
application start time

The attacker should deliberately attempt to reduce pairwise similarity.

Example:

Bot 1:
A → B → C → D

Bot 2:
A → C → B → D

Bot 3:
A → B → D → C

If ShadowGram still detects the group through independent evidence layers, that is much more interesting.

2.15 Threat Class J — Semantic Randomization

Your semantic layer currently proposes:

Cosine similarity ≥ 0.88

This is a dangerous fixed assumption.

An attacker can simply ask an LLM to generate different wording.

For example:

"I need this loan for tuition."

"I require financial assistance for my educational expenses."

"I am seeking short-term funding to cover college fees."

The semantic vectors may remain related.

But an attacker could deliberately ask for substantially different narratives.

Therefore semantic similarity should never be the primary detection mechanism.

It should be one piece of evidence.

2.16 Threat Class K — Common-Cause Events

This is one of the most important threats to ShadowGram itself.

Imagine:

College campaign
       ↓
5,000 students
       ↓
same Wi-Fi
       ↓
same URL
       ↓
same application workflow

The graph becomes extremely dense.

A naive graph detector might report:

FRAUD RING

That would be catastrophic.

Therefore legitimate coordinated behavior must be part of your adversarial test set.

ShadowGram should explicitly test:
college application drives
marketing campaigns
salary-day application spikes
new-product launches
geographic events
network outages followed by retry bursts
shared corporate networks
shared campus networks

This is more important than demonstrating a pretty graph.

2.17 Threat Class L — Shared Device / Shared Network

Another false-positive source:

family
 ↓
same Wi-Fi
 ↓
multiple legitimate applicants

or:

college
 ↓
shared NAT
 ↓
hundreds of students

or:

office
 ↓
shared network
 ↓
multiple employees

Therefore:

IP address should never be treated as identity.

Likewise:

A shared device/network signal should be treated as contextual evidence, not proof of coordination.

This is especially important because Carrier-Grade NAT and other shared-network architectures can cause unrelated users to appear network-related.

2.18 Threat Class M — Bridge Accounts

This is a particularly useful adversarial test.

Suppose:

BOT A ───── BOT B
   \          /
    \        /
     CLEAN ACCOUNT

The clean account is deliberately inserted between fraudulent accounts.

The purpose is to reduce graph density and break obvious clustering.

ShadowGram should therefore test:

direct connections
+
indirect connections
+
community structure
+
edge provenance

rather than only:

pairwise similarity > threshold

This makes your graph research substantially more interesting.

2.19 Threat Class N — Adversarial Graph Pollution

An attacker could deliberately generate legitimate-looking accounts to alter the graph.

For example:

Fraud A
Fraud B
Fraud C
Fraud D

        ↓

Inject 50 normal-looking accounts

        ↓

Fraud cluster becomes less obvious

This is a real research problem for graph-based detection systems.

Your response should therefore not be:

"The graph will always find the attackers."

Instead:

"ShadowGram evaluates how robust its relational signals remain when adversarial sessions attempt to dilute or distort the graph."

That is a much stronger research statement.

2.20 Threat Class O — AI Agent vs. Scripted Bot

This distinction should become part of your architecture.

Test Group 1 — Scripted
Playwright
fixed timings
fixed paths
fixed inputs
Test Group 2 — Randomized script
Playwright
random timing
random navigation
random text
Test Group 3 — Human-emulation
synthetic cursor
variable typing
scroll variation
Test Group 4 — Agentic automation
observe page
 ↓
LLM/VLM
 ↓
choose action
 ↓
browser interaction
 ↓
observe again
Test Group 5 — Human baseline
real person
 ↓
real browser
 ↓
real application

This creates a much better benchmark.

2.21 The Most Important Experimental Matrix

ShadowGram should eventually produce something like:

Attack	Key 1	Key 2	Detection	False Positive
Fixed scripted bots	?	?	?	?
Randomized bots	?	?	?	?
Human-emulation bots	?	?	?	?
Agentic browser bots	?	?	?	?
Slow-drip bots	?	?	?	?
Bridge-account attack	?	?	?	?
Shared-campus users	?	?	?	?
Marketing surge	?	?	?	?
Normal users	?	?	—	?

This table would be far more convincing to judges than claiming "100% detection."

2.22 The Core Research Hypothesis

After this threat audit, ShadowGram's central hypothesis should be:

H1: Coordinated automated application sessions produce measurable relational patterns across multiple behavioral dimensions that remain informative even when individual sessions are designed to appear legitimate.

And the null hypothesis:

H0: After controlling for legitimate common causes, the relational patterns of coordinated automated sessions are not distinguishable from those of legitimate sessions.

This is now a proper experiment.

2.23 Secondary Hypotheses
H2 — Multi-signal evidence

Combining multiple weak behavioral signals provides better discrimination than any single behavioral signal.

H3 — Relational advantage

Relational analysis identifies some coordinated attacks that single-session analysis misses.

H4 — Early-stage advantage

Detecting suspicious coordination before downstream verification can reduce unnecessary verification attempts in the simulated environment.

H5 — Robustness

Detection remains useful when attackers introduce timing and behavioral randomization.

H6 — False-positive protection

Common-cause controls reduce false positives during legitimate synchronized events.

These hypotheses give ShadowGram something extremely valuable:

a way to prove itself wrong.

That is good research.

2.24 What ShadowGram Should NOT Claim After This Audit

Remove or rewrite claims such as:

🔴 "AI swarms are currently stealing ₹20 lakh in 15 minutes."

Unless you have a real documented incident supporting that exact number.

Your ₹20 lakh example is a simulation.

Call it:

Simulated adversarial exposure: ₹20 lakh

not:

Real-world incident: ₹20 lakh.

🔴 "Existing vendors cannot detect this."

Unsupported.

Replace with:

"ShadowGram explores an early-stage behavioral coordination layer that complements existing fraud and identity systems."

🔴 "Graph detection is missing from existing systems."

False.

The research and commercial landscape clearly show graph/link analysis is already used.

🔴 "Q > 0.60 proves fraud."

Incorrect.

Remove.

🔴 "p < 0.001 proves a syndicate."

Incorrect.

Replace with:

"The permutation test measures whether the observed coordination statistic is unlikely under the chosen null model."

Then use the result as one component of the decision.

2.25 What Becomes ShadowGram's Potential Innovation

After this threat audit, I see a much cleaner opportunity:

Evidence-Carrying Early Coordination Graph

The system does not simply say:

ACCOUNT = FRAUD

It says:

SESSION GROUP
     ↓
COORDINATION EVIDENCE
     ↓
┌─────────────────────┐
│ Temporal             │
│ Navigation           │
│ Interaction          │
│ Semantic             │
│ Environment          │
└─────────────────────┘
     ↓
COMMON-CAUSE CHECK
     ↓
STATISTICAL TEST
     ↓
RISK / STEP-UP

Every suspicious relationship retains its evidence.

This makes the graph:

auditable + explainable + experimentally testable.

2.26 Current Threat-Model Verdict
Threat	Evidence	ShadowGram relevance
Identity abuse	✅ Strong	🔥 Very high
Synthetic identities	✅ Strong	🔥 Very high
Relational fraud	✅ Strong research support	🔥 Very high
Automated bots	✅ Strong	🔥 Very high
AI-assisted automation	🟢 Emerging/strong	🔥 High
VLM CAPTCHA solving	✅ Strong academic evidence	🔥 High
Coordinated application bursts	🟢 Plausible/known pattern	🔥 Very high
Slow-drip coordination	🟡 Adversarial hypothesis	🔥 High
Behavioral randomization	🟡 Adversarial hypothesis	🔥 Very high
Bridge accounts	🟡 Research threat	🔥 High
Graph pollution	🟡 Research threat	🔥 High
Common-cause traffic	✅ Real operational problem	🔥 Extremely high
"All fraud is AI swarm fraud"	🔴 Unsupported	Remove
"Existing vendors cannot use graphs"	🔴 False	Remove
"Q > .60 = fraud"	🔴 Incorrect	Remove
"p < .001 = fraud"	🔴 Incorrect	Remove
2.27 Most Important Conclusion for the Hackathon

The strongest ShadowGram story is not:

"We built an AI that detects AI fraud."

It is:

"We built an adversarial testbed for coordinated application fraud and designed a lightweight relational defense that looks for evidence distributed across sessions rather than relying only on the risk of one applicant."

Then demonstrate:

NORMAL HUMAN
       ↓
individual evidence
       ↓
no suspicious relationship
       ↓
PASS


COORDINATED ATTACK
       ↓
each session individually plausible
       ↓
cross-session evidence accumulates
       ↓
graph emerges
       ↓
common-cause check
       ↓
statistical validation
       ↓
Why Card
       ↓
STEP-UP

That is a much more defensible and potentially more innovative hackathon project than the original "existing vendors fail against 2026 AI swarms" story.

Sources for this section
USENIX Security 2025 — generalized agentic VLM CAPTCHA solving.
Springer/Discover Informatics, October 2026 — rule-anchored graph learning for synthetic-identity fraud.
FinCEN, January 2024 — identity-related suspicious activity analysis.
Thales 2026 Bad Bot Report — commercial telemetry on bot and AI-enabled automation trends

PART 3 — EXISTING TECHNOLOGY & COMPETITOR AUDIT
3.0 Purpose

This section audits whether ShadowGram's claimed innovation is actually different from existing fraud-detection technology.

The objective is not to prove that competitors are weak.

The objective is to identify:

what already exists;
what ShadowGram should not claim as new;
what ShadowGram can reasonably claim as its contribution;
where the prototype can demonstrate something genuinely interesting.
3.1 The Most Important Finding

The original ShadowGram documentation treated relational fraud detection as if it were largely absent from commercial fraud systems.

That is incorrect.

Modern fraud platforms already use combinations of:

behavioral biometrics;
device intelligence;
identity networks;
consortium data;
graph/link analysis;
machine learning;
anomaly detection;
risk scoring;
bot detection;
account-link analysis.

Therefore:

"ShadowGram uses graphs to detect fraud rings" is not, by itself, an innovation.

This must be removed from the project's novelty argument.

The innovation must come from where, when, how, and with what evidence ShadowGram applies these techniques.

3.2 BioCatch Audit

BioCatch is an important competitor because it demonstrates that behavioral biometrics are already commercially established.

BioCatch's technology uses behavioral signals to help identify suspicious activity.

Its product ecosystem also includes network/link-analysis capabilities.

Therefore, this statement should NOT be used:

"BioCatch cannot cluster accounts."

That is directly vulnerable to a judge's challenge.

Better statement

"ShadowGram is not proposing behavioral biometrics or relational fraud analysis as new technologies. It investigates their use as an early pre-verification coordination layer in a controlled digital-lending workflow."

This is much safer.

3.3 DataVisor Audit

DataVisor is another important competitor.

DataVisor has publicly described unsupervised machine-learning approaches for detecting coordinated fraud attacks.

This means ShadowGram cannot claim:

"We invented unsupervised fraud-ring detection."

It already exists.

ShadowGram differentiation

A defensible distinction is:

Existing enterprise approach
        ↓
Large-scale fraud/risk infrastructure
        ↓
Enterprise deployment
        ↓
Cross-platform / transaction / account analysis

versus:

ShadowGram prototype
        ↓
Application-form event stream
        ↓
Pre-verification analysis
        ↓
Local graph
        ↓
Human-readable evidence

The second architecture can be presented as a prototype research direction, not proof that commercial products cannot do it.

3.4 Sift Audit

Sift provides machine-learning-based fraud prevention and behavioral signals.

Therefore, claims such as:

"Sift only looks at IP addresses."

or:

"Sift evaluates users independently."

should be removed.

Modern fraud platforms generally combine multiple signals.

Better framing

ShadowGram should say:

"ShadowGram explores whether application-stage behavioral relationships can complement existing identity, device, and transaction risk signals."

This positions ShadowGram as a complementary layer.

That is much harder to attack.

3.5 LexisNexis / ThreatMetrix Audit

LexisNexis Risk Solutions operates technology that can connect identity, device, network, and behavioral information.

Therefore the original statement:

"ThreatMetrix matches shared IP addresses, hardware MACs and device hashes."

is oversimplified.

In particular, browser applications generally cannot simply obtain a user's physical hardware MAC address through normal web APIs.

The architecture should not depend on MAC-address collection.

Recommended replacement

Use privacy-conscious browser/device signals such as:

browser characteristics;
device configuration;
rendering characteristics;
event timing;
session behavior;
network metadata where legally appropriate.
3.6 Arkose Labs Audit

Arkose Labs is primarily relevant to the bot-defense portion of ShadowGram.

The original documentation stated that:

"Arkose uses 3D puzzles."

and therefore:

"Vision-LLMs bypass Arkose."

This is too simplistic.

Modern bot-defense systems use more than one visual challenge.

They can combine:

risk assessment;
behavioral signals;
device/network signals;
challenge mechanisms;
session intelligence.

Therefore ShadowGram should not present itself as:

"A better CAPTCHA."

It is solving a different problem:

CAPTCHA-style defense
        ↓
"What is happening in this session?"

ShadowGram
        ↓
"What relationship exists between these sessions?"

That distinction is useful.

3.7 Cloudflare Turnstile Audit

Cloudflare Turnstile should also not be described as simply:

"A CAPTCHA that checks mouse movement."

Turnstile is designed as a broader challenge/risk mechanism intended to distinguish legitimate visitors from automated traffic while reducing traditional CAPTCHA friction.

Therefore:

"ghost-cursor defeats Turnstile"

is not a defensible blanket claim.

A mouse trajectory generator may demonstrate that one behavioral signal can be imitated.

That does not demonstrate that an entire bot-defense platform has been defeated.

ShadowGram lesson

This actually strengthens the project.

If one behavioral signal can be copied, then:

ShadowGram should avoid depending on one behavioral feature.

This supports the multi-signal architecture.

3.8 Why Multi-Modal Evidence Matters

Suppose an attacker successfully imitates mouse movement.

Then:

Kinetic similarity
       ↓
Attacker wins

But if ShadowGram also evaluates:

Timing
+
Navigation
+
Semantic behavior
+
Interaction events
+
Environmental characteristics

the attacker must reproduce multiple dimensions simultaneously.

This does not make ShadowGram impossible to evade.

It increases the adversarial cost and gives the detector more evidence.

That is the correct security argument.

3.9 ShadowGram Should Stop Using the Word "Physics" Too Literally

The phrase:

"Five layers of interaction physics"

sounds impressive but can create technical problems.

Not every signal is actually physics.

For example:

semantic embeddings are computational linguistics;
navigation sequences are behavioral sequences;
timing is temporal statistics;
browser characteristics are environment/device signals;
touch movement contains physical interaction information.

A more technically accurate name would be:

Five-Layer Behavioral Evidence Model

or:

Multi-Modal Interaction Evidence Model

Recommended:

Multi-Modal Behavioral Evidence Stack

This is easier to defend academically.

3.10 Layer-by-Layer Novelty Audit
Layer	Already Exists?	ShadowGram Novelty
Timing analysis	Yes	Combining it with other application-stage signals
Navigation similarity	Yes	Application-session relational modeling
Mouse/touch behavior	Yes	Multi-modal integration
Semantic similarity	Yes	Linking semantic behavior to session relationships
Device/environment signals	Yes	Supporting evidence rather than sole identity
Graph analysis	Yes	Applying it to the proposed pre-verification workflow
Community detection	Yes	Not novel itself
Leiden	Yes	Not novel
Permutation testing	Yes	Statistical validation of the prototype
Explainable evidence	Yes	Useful integration into the proposed workflow
Pre-KYC triage	Potentially differentiating	Strongest application-level opportunity
Verification-cost protection	Potentially differentiating	Strong business/use-case angle
Local/on-premise prototype	Potentially differentiating	Strong deployment constraint
Multi-modal early coordination detection	Research-worthy	Strongest technical research direction
3.11 The Real ShadowGram Innovation

After removing exaggerated competitor claims, the strongest ShadowGram idea becomes:

Use multiple low-cost behavioral signals to construct a temporary relational graph of application sessions before expensive identity/credit verification, then provide statistically testable evidence for why a group deserves additional scrutiny.

This contains several components.

Component 1 — Early observation

The detector operates before downstream verification.

Component 2 — Relational analysis

It evaluates relationships between sessions.

Component 3 — Multi-modal evidence

It does not depend on one feature.

Component 4 — Statistical validation

It tests whether observed coordination is unusual.

Component 5 — Human-review workflow

It exposes the evidence rather than simply returning:

risk = 0.97
Component 6 — Cost-aware routing

It potentially reduces unnecessary expensive downstream operations.

Together, these make a much stronger project.

3.12 Important: Do Not Claim "Zero Cloud"

The current pitch says:

"Zero cloud bills."

This should be changed.

Your prototype can run locally.

That does not mean a production deployment has zero cloud cost.

A better statement is:

"The prototype can perform the initial behavioral and graph analysis locally without requiring a third-party fraud-scoring API."

That is precise.

3.13 Important: Do Not Claim "100% Explainable"

The current pitch says:

"100% explainable."

This is too strong.

A machine-learning system containing:

CNNs;
embeddings;
graph algorithms;

is not literally 100% explainable.

Instead use:

"Evidence-based and auditable decision support."

The Why Card can expose:

Cluster ID
Number of sessions
Time similarity
Navigation similarity
Semantic similarity
Interaction similarity
Environmental similarity
Statistical significance
Decision/action

That is genuinely useful.

3.14 Important: Do Not Call the Output a "SAR" Automatically

A major regulatory/documentation issue is the use of the term:

SAR — Suspicious Activity Report

A SAR is a specific regulatory filing concept.

A generated PDF containing graph evidence should not automatically be described as an official SAR.

The safer architecture is:

ShadowGram
      ↓
Evidence Report
      ↓
Analyst Review
      ↓
Regulatory workflow
      ↓
Official filing if required

The prototype should therefore call its PDF something like:

Suspicious Activity Investigation Report

or:

Fraud Cluster Investigation Report

unless the exact regulatory filing requirements are actually being implemented.

This is an important correction.

3.15 Recommended Competitor Table

Replace the previous competitor table with something closer to this:

System	Established Capability	What ShadowGram Should Acknowledge	ShadowGram Research Position
BioCatch	Behavioral biometrics and fraud-risk analysis	Behavioral detection is already commercial	Explore early application-session coordination as an additional layer
DataVisor	Unsupervised/ML-based fraud and attack-ring detection	Graph/unsupervised fraud detection already exists	Focus on lightweight pre-verification prototype workflow
Sift	Digital trust, behavioral and fraud-risk signals	Multi-signal fraud scoring already exists	Study cross-session application coordination
LexisNexis Risk Solutions / ThreatMetrix	Identity/device/network risk intelligence	Device/network correlation already exists	Avoid claiming these signals are novel
Arkose Labs	Bot and automated-abuse detection	Bot detection is mature	ShadowGram focuses on relationships between sessions
Cloudflare Turnstile	Automated-abuse/risk detection	Challenge/risk systems already exist	ShadowGram is not a CAPTCHA replacement

This table is much more defensible than claiming each competitor "fails."

3.16 What Judges Can Ask

The team should expect these questions.

Judge Question 1

"Doesn't BioCatch already do behavioral analysis?"

Answer:

"Yes. We are not claiming behavioral biometrics are new. Our research focuses on combining early application-session behavior into a temporary relational graph before downstream verification, with explicit statistical evidence and cost-aware routing."

Judge Question 2

"Doesn't DataVisor already detect fraud rings?"

Answer:

"Yes. Graph-based fraud-ring detection already exists. Our contribution is the proposed lightweight application-stage workflow and the controlled evaluation of whether early behavioral relationships can provide useful signals before expensive verification."

Judge Question 3

"Why can't the attacker simply imitate the behavior?"

Answer:

"They can. ShadowGram does not assume any individual signal is impossible to imitate. The system combines several independent evidence sources and measures whether their joint relationship is statistically unusual."

This is a much stronger security answer than claiming the system is impossible to bypass.

3.17 The Adversarial Principle

ShadowGram should explicitly adopt:

No single feature is trusted as proof of fraud.

For example:

Same IP
       ≠ fraud
Same timing
       ≠ fraud
Same navigation
       ≠ fraud
Same semantic meaning
       ≠ fraud
Similar touch behavior
       ≠ fraud

Instead:

Multiple independent signals
              +
Unusual relational structure
              +
Statistical significance
              +
Context
              ↓
       Investigation signal

This is one of the most important principles for the final architecture.

3.18 Recommended Terminology

Replace exaggerated terminology with these terms:

Current Term	Recommended Term
AI swarm attack	Coordinated multi-session attack
AI swarm detector	Coordinated-session detector
Interaction physics	Behavioral evidence
Physics engine	Behavioral evidence engine
Fraud proof	Fraud-risk evidence
100% explainable	Auditable evidence
100% detectable	Detectable under tested conditions
Official SAR	Investigation report / SAR-support report
Denial-of-Wallet attack	Verification-cost exhaustion scenario
Existing vendors fail	Existing systems address adjacent problems
Competitor blind spot	Potential deployment/application gap
Guaranteed detection	Experimentally evaluated detection

This language will make ShadowGram look more credible, not less impressive.

3.19 Competitive Positioning After Audit

The final positioning should be:

ShadowGram is not a replacement for enterprise fraud platforms.

It is:

A research prototype for early, relational behavioral screening of coordinated application sessions before expensive downstream verification.

The system can sit conceptually in front of:

Identity verification
Document verification
Liveness
Credit bureau
Manual review

rather than competing directly with those systems.

3.20 Hackathon Strategy

For winning a hackathon, this distinction is extremely important.

A judge does not need to believe:

"We defeated BioCatch."

They need to believe:

"This team identified a real problem, researched existing solutions, found a specific gap, built a working system, and experimentally demonstrated why their approach is useful."

The strongest presentation therefore becomes:

Problem

Coordinated applications can be difficult to identify when each session is evaluated separately.

Existing technology

Commercial systems already perform sophisticated behavioral, device, identity, and graph-based fraud detection.

Gap being investigated

Can a lightweight local behavioral-relational layer detect suspicious coordination before expensive verification?

Innovation

Multi-modal session relationships + temporary graph + statistical testing + evidence interface.

Demonstration

Controlled attacks with progressively stronger evasion.

Result

Show:

Detection rate
False-positive rate
Latency
Verification calls avoided
Cluster quality
Robustness under evasion

That is a research-backed engineering story.

3.21 Audit Verdict
❌ Not novel by itself
Graph fraud detection
Fraud-ring detection
Behavioral biometrics
Device fingerprinting
Semantic similarity
Leiden clustering
Louvain clustering
Bot detection
CAPTCHA alternatives
Explainable fraud scores
🟡 Potentially interesting
Combining these signals at the application stage
Local temporary graph
Pre-verification risk routing
Statistical testing of coordination
Cost-aware verification routing
Human-readable relational evidence
Controlled adversarial evaluation
🟢 Strongest research direction

Early relational behavioral detection under adversarial conditions, evaluated against controlled evasion strategies and measured using detection quality, false positives, latency, and avoided downstream verification.

That is where ShadowGram should concentrate its engineering effort.

3.22 Decision for the Next Architecture Iteration

The research should now move ShadowGram away from:

"We built a fraud graph."

toward:

"We built and experimentally tested an early-warning
relational behavioral layer."

The next research section should therefore audit the five proposed behavioral layers individually.

For each layer, we need to answer:

Is the signal technically measurable in a browser?
Is it privacy-safe?
Can a normal user naturally produce it?
Can an attacker imitate it?
Is the proposed mathematical metric valid?
Does it actually add information beyond the other layers?
Can it run on your laptop in real time?
How should it be tested?
What should be removed from the current implementation?

That layer-by-layer audit is likely to produce the largest practical improvements to the actual ShadowGram prototype.


Part: Architecture Improvements and Innovation Opportunities
1. The most important correction: ShadowGram is NOT the first system to use relational fraud detection

This is now firmly established.

Your original claim:

“Existing fraud vendors inspect accounts individually. ShadowGram is the first to detect relationships between accounts.”

Do not use this claim.

BioCatch publicly describes Scout as a graph/link-analysis system that connects accounts, devices and individuals to expose criminal networks.

DataVisor also explicitly describes combining behavioral, device, identity, transaction and network signals to detect coordinated behavior that can appear normal when individual events are viewed separately.

So your innovation cannot simply be:

“We use graphs to detect fraud rings.”

That already exists.

Better ShadowGram positioning

The defensible statement is:

ShadowGram explores whether lightweight, privacy-preserving behavioral telemetry collected before expensive identity verification can be combined with relational analysis to identify coordinated application activity early in a digital-lending funnel.

That is much stronger because it describes a specific architecture and deployment point, rather than claiming invention of graph fraud detection.

2. The real innovation opportunity: Early-Funnel Relational Detection

This is where I think ShadowGram has a potentially strong hackathon story.

Existing commercial systems already perform graph analysis.

Therefore, don't compete with them on:

“Our graph is better.”

Instead compete on:

WHEN the graph is created and WHAT evidence feeds it.

Your architecture is:

Applicant opens loan form
        ↓
Low-cost telemetry collection
        ↓
Behavioral feature extraction
        ↓
Relational similarity
        ↓
Small candidate graph
        ↓
Early coordination score
        ↓
┌─────────────────────────┐
│       Decision          │
├─────────────────────────┤
│ Low risk → continue     │
│ Suspicious → step-up    │
│ Strong cluster → hold   │
└─────────────────────────┘
        ↓
Expensive KYC / verification

This is a much more credible innovation claim.

Important: You still need an actual experiment demonstrating that early behavioral evidence provides useful incremental detection value. Otherwise it remains an architecture hypothesis.

3. New principle: Separate "bot detection" from "coordination detection"

Your current Two-Key Defense is conceptually good, but one part needs clarification.

Key 1
Is this individual session automated?
Key 2
Are multiple sessions behaving in a coordinated way?

These are different questions.

A human-operated fraud farm can pass Key 1.

An AI agent deliberately designed to imitate human input can pass Key 1.

But several supposedly independent sessions may still exhibit:

unusually similar navigation;
similar timing patterns;
similar interaction sequences;
similar semantic intent;
unusual shared environmental characteristics;
coordinated arrival patterns.

Therefore:

Key 1 does not need to defeat sophisticated attackers.

Its purpose is to remove obvious automation cheaply.

Key 2 handles the harder problem.

This makes the architecture much more defensible.

4. Replace the "5 physics layers" language

I would change this.

Calling everything “interaction physics” sounds impressive, but it creates a technical vulnerability during judging.

Your five layers are actually different classes of evidence:

Layer	Better name
Timing	Temporal behavior
Navigation	Sequential behavior
Mouse/touch	Interaction dynamics
Text embeddings	Semantic behavior
Browser/device signals	Environment/device signals

So instead of:

Five Layers of Interaction Physics

use:

Five Behavioral Evidence Layers

This is technically cleaner.

5. Do NOT claim that any single signal identifies a fraudster

This is one of the most important changes.

For example:

Same IP → suspicious

is weak.

Same navigation → suspicious

is weak.

Similar text → suspicious

is weak.

Similar timing → suspicious

is weak.

But:

timing
+
navigation
+
interaction dynamics
+
semantic similarity
+
environmental similarity

may provide substantially stronger evidence.

Therefore ShadowGram should explicitly implement:

Evidence diversity

An edge should not be created merely because two users are similar.

Instead:

Edge(A,B) exists only when:

multiple independent evidence families
support the relationship

This also gives you a powerful judge explanation:

“We do not flag people because they share one characteristic. We look for agreement between independent behavioral signals.”

6. A much better graph architecture

Your current architecture calculates pairwise similarity.

That becomes problematic as N grows.

For 100,000 sessions:

$$ \frac{100000(99999)}{2} \approx 5\times10^9 $$

possible pairs.

Your original concern about quadratic growth is therefore mathematically correct.

But this statement:

“Traditional servers crash under this load.”

should be removed.

That is too absolute.

Modern fraud systems obviously process very large datasets.

Instead say:

Naively comparing every session with every other session creates unnecessary \(O(N^2)\) candidate comparisons. ShadowGram therefore uses candidate generation before expensive similarity calculation.

That is technically defensible.

7. Add a "candidate generation" stage

This could become one of the strongest engineering improvements.

Instead of:

100,000 sessions
       ↓
compare everything
       ↓
5 billion comparisons

use:

100,000 sessions
       ↓
cheap blocking
       ↓
candidate pairs
       ↓
expensive similarity
       ↓
graph edges

Possible blocking dimensions:

Temporal block

Only compare sessions occurring within a relevant window.

Route block

Only compare sessions visiting similar application states.

Device/environment block

Only compare compatible environmental signatures.

Semantic block

Use approximate nearest-neighbor retrieval to identify semantically related text.

Behavioral block

Only compare sessions with compatible interaction patterns.

Then:

N sessions
      ↓
Blocking
      ↓
k candidate neighbors/session
      ↓
O(kN)
      ↓
graph construction

This is a much more realistic architecture.

8. Add a crucial concept: "Evidence aging"

This is one area where ShadowGram can become much more interesting.

A relationship from:

5 seconds ago

should not necessarily have the same importance as:

20 hours ago.

You already proposed an exponential decay kernel.

Formalize it.

For an evidence relationship:

$$ W(t)=W_0e^{-\lambda\Delta t} $$

where:

\(W_0\) = original evidence strength
\(\Delta t\) = time since interaction
\(\lambda\) = decay rate

Now the graph becomes temporal, rather than static.

Example:

09:00
A ─── B
    strong

09:30
A ─── B
    weaker

18:00
A ─── B
    historical

This is better than simply saying:

“A and B are connected.”

You can say:

“A and B were strongly coordinated during the attack window.”

That is much more useful to investigators.

9. Add "relationship types" instead of one generic edge

Your current graph uses:

A ───── B

I recommend:

A ── temporal ── B
A ── navigation ── B
A ── semantic ── B
A ── interaction ── B
A ── environment ── B

Then your graph becomes a multiplex graph.

For example:

             temporal
          ─────────────
        /                \
      A                    B
        \                /
          ─────────────
             semantic

This gives the judge a much stronger visual explanation:

“These accounts are not connected because they share one IP. They are connected because several independent behavioral relationships agree.”

10. This also fixes your campus-Wi-Fi problem

This is important.

Suppose 100 students apply for a loan from the same college Wi-Fi.

A naive system sees:

100 users
     ↓
same IP
     ↓
FRAUD

Bad.

ShadowGram should treat common infrastructure as a shared-cause signal rather than independent evidence.

For example:

Campus Wi-Fi
     │
 ┌───┼───┬───┐
 A   B   C   D

The shared IP should contribute little or nothing.

But if:

A B C D

same Wi-Fi
+
same navigation
+
similar timing
+
similar semantic text
+
similar interaction sequence

then the relationship becomes stronger.

This gives you a much better principle:

Common-cause discounting

A signal that can easily be explained by a legitimate common cause should receive lower evidentiary weight.

That is more defensible than your current phrase “common-cause immunity.”

11. Your p < 0.001 claim needs major correction

This is one of the biggest statistical problems in the current document.

You currently say:

“Any cluster with Modularity Q > 0.60 and node count ≥3 is mathematically isolated as a syndicate (p < 0.001).”

Remove this.

Modularity \(Q\) and statistical significance are not the same thing.

A high modularity score does not automatically mean:

$$ p < 0.001 $$

Community detection can find apparently strong communities even in networks without meaningful structure, which is exactly why statistical significance of communities has to be evaluated separately.

Instead:

Correct architecture
Community detection
       ↓
candidate cluster
       ↓
statistical validation
       ↓
permutation/null-model test
       ↓
confidence / significance

Then your system can honestly say:

“This cluster was unusually cohesive compared with our empirical null model.”

That is much stronger than inventing a universal p-value.

12. Make the permutation test actually meaningful

Your idea of permutation testing is good.

But don't simply say:

“Shuffle 1,000 times and p < 0.001.”

Define what is being tested.

For example:

Null hypothesis

The observed relationships between sessions can be explained by independent behavior drawn from the observed population.

Then calculate a statistic such as:

$$ T = \text{within-cluster edge density} $$

or:

$$ T = \text{weighted community score} $$

Then:

Observed T
     ↓
Compare against 1,000 null networks
     ↓
How many null networks ≥ observed T?
     ↓
empirical p-value

That becomes an actual statistical experiment.

13. Don't make the LLM responsible for the decision

This should become a hard architectural rule.

Bad:

Graph
 ↓
LLM
 ↓
"Looks fraudulent"

Good:

Telemetry
 ↓
deterministic feature extraction
 ↓
graph algorithm
 ↓
statistical validation
 ↓
structured evidence
 ↓
LLM
 ↓
human-readable explanation

The LLM should be an explanation layer, not the fraud classifier.

This is one of the strongest improvements you can make.

14. The "Why Card" should become an Evidence Card

Your current Why Card idea is excellent.

But improve it.

Instead of:

Why suspicious?

show:

Evidence Card
CLUSTER: C-017
Members: 18

Evidence

Temporal
█████████░ 0.91

Navigation
████████░░ 0.84

Semantic
█████████░ 0.89

Interaction
███████░░░ 0.76

Environment
████░░░░░░ 0.43

Common-cause adjustment
-0.17

Cluster significance
p = 0.004

Decision
STEP-UP VERIFICATION

Most importantly:

Show exactly which evidence contributed to the decision.

This is far more defensible than a generic AI-generated explanation.

15. Change the "SAR" terminology

Another important correction.

A generated PDF does not automatically become an official Suspicious Activity Report.

ShadowGram should not claim:

“ShadowGram generates an official SAR.”

Instead:

“ShadowGram generates an investigator evidence report that can support a regulated entity's internal review and, where appropriate, subsequent regulatory reporting.”

This is safer and more accurate.

The same applies to:

“official adverse action reason.”

Don't claim that your graph output is automatically legally sufficient.

Your system can provide decision evidence.

The lender's compliance/legal process determines the actual regulatory action.

16. Your Regulation B reasoning needs another correction

Your document says:

“Regulation B prohibits unexplained loan denials.”

The basic idea is directionally correct for U.S. covered credit decisions, but ShadowGram must be careful about jurisdiction and scope.

Regulation B requires specific principal reasons for adverse action, and the reasons must correspond to factors actually considered or scored.

Therefore the useful ShadowGram principle is:

Every automated risk decision must preserve the underlying evidence that produced the decision.

That is an excellent architecture requirement even outside the U.S.

17. Your RBI section should also be rewritten

The 2025 RBI Digital Lending Directions did exist and were issued May 8, 2025. They addressed issues including third-party involvement, data privacy, borrower protection and digital-lending arrangements.

However, your document currently treats them as if they specifically mandate:

“ShadowGram-style explainable graph audit trails.”

They don't.

Therefore say:

“The RBI digital-lending framework provides regulatory context for responsible digital-credit operations, data handling, outsourcing and borrower protection. ShadowGram's auditability is a design response to these governance requirements, not a feature explicitly mandated by the Directions.”

That's much safer.

18. Your KrazyBee case should NOT be used as proof of AI-swarm fraud

This needs to remain very clear.

The Telangana High Court case involved proceedings connected to allegations concerning digital lending operations and 43 FIRs. The court ultimately quashed the relevant proceedings because of the absence of the required predicate offence in the circumstances before it.

It does not establish:

AI swarm
      ↓
48 synthetic identities
      ↓
micro-loan theft

That story should never appear as a factual incident.

You can instead use it as:

Regulatory context demonstrating that digital-lending operations can face significant legal scrutiny.

19. The OnlyFake incident is actually useful—but for a different reason

The OnlyFake incident is genuine and well documented.

404 Media reported that the service generated convincing fake ID images for approximately $15 and demonstrated that one generated ID could pass an identity verification check at a cryptocurrency exchange.

But don't turn it into:

“OnlyFake proves AI swarms are attacking micro-lenders.”

It doesn't.

Instead:

Correct ShadowGram relevance
Generative AI
      ↓
Cheap synthetic identity artifacts
      ↓
Identity verification becomes less reliable
      ↓
Early behavioral/relational evidence becomes
potentially more valuable

That's a legitimate connection.

20. Your CAPTCHA research is genuinely useful

This part of your research has good empirical support.

USENIX Security 2025 research reported that Halligan achieved 60.7% success across 2,600 visual CAPTCHA challenges and 70.6% on previously unseen challenges in real-world CAPTCHA environments.

USENIX Security 2026's ViPer work reported up to 93.2% success against several visual reasoning CAPTCHA providers.

This supports a useful ShadowGram design decision:

CAPTCHA success should not be treated as strong evidence that a session is human.

That's much more defensible than claiming:

“CAPTCHAs are completely broken.”

21. New ShadowGram innovation: "Coordination-before-identity"

This is the idea I would emphasize most heavily for the hackathon.

Traditional conceptual pipeline:

IDENTITY
   ↓
KYC
   ↓
CREDIT
   ↓
FRAUD

ShadowGram:

BEHAVIOR
   ↓
COORDINATION
   ↓
RISK
   ↓
KYC
   ↓
CREDIT

The system doesn't have to determine:

“Who is this person?”

before asking:

“Are these application sessions behaving like independent applicants?”

That is an interesting security research question.

22. New metric: Coordination Lift

I recommend adding a new evaluation metric.

Don't just measure:

Accuracy

Measure:

$$ \text{Coordination Lift} = P(\text{fraud evidence}|\text{relational features}) - P(\text{fraud evidence}|\text{individual features}) $$

In plain English:

How much better can we identify coordinated attacks when relationships between sessions are included, compared with examining each session separately?

This directly tests your core thesis.

23. New experiment: Ablation Study

This is probably the single most valuable experiment you can add.

Run the detector several ways:

Experiment A
Individual features only
Experiment B
Individual + temporal
Experiment C
Individual + temporal + navigation
Experiment D
All five layers
Experiment E
All five + relational graph

Then compare:

Model	Precision	Recall	False positives
Individual only	?	?	?
+ Temporal	?	?	?
+ Navigation	?	?	?
+ All behavioral	?	?	?
+ Relational graph	?	?	?

If:

Individual = mediocre

Graph + behavioral =
substantially better

you have experimental evidence supporting ShadowGram's central thesis.

That is far more impressive to judges than 20 pages of theoretical claims.

24. New experiment: Human-like swarm

Don't only test obvious Playwright bots.

Build three attack classes in your safe local cyber-range:

Level 1 — Scripted
identical automation
identical routes
identical timing
Level 2 — Randomized
different timing
different routes
different text
different browser sessions
Level 3 — Human-emulation
randomized timing
natural navigation
human-like pointer/touch patterns
different semantic text
different environment signatures

Then test:

Key 1

against all three.

You will probably see:

Level 1 → easy
Level 2 → moderate
Level 3 → harder

Then test:

Key 2 relational analysis

This creates a very compelling demonstration:

“The attacker can make one session look human. The question is whether they can make an entire population behave independently.”

That sentence is much closer to a defensible ShadowGram thesis.

25. One more innovation: attack adaptation loop

Your current system is mostly:

attacker
   ↓
detector

Make it:

attacker
   ↓
detector
   ↓
evidence
   ↓
attacker changes strategy
   ↓
detector adapts

This creates an adversarial evaluation framework.

For example:

Attack V1
↓
detected because timing similarity

Attack V2
↓
timing randomized
↓
detected because navigation similarity

Attack V3
↓
navigation randomized
↓
semantic + interaction relationship remains

Attack V4
↓
multiple layers randomized
↓
detection confidence falls

Now you can measure the robustness boundary of ShadowGram.

That is research-grade engineering.

26. Your ultimate architecture should therefore become
                    SHADOWGRAM
                         │
                ┌────────┴────────┐
                │                 │
        KEY 1: SESSION       KEY 2: RELATIONAL
        ANALYSIS              ANALYSIS
                │                 │
       Automation signals     Candidate generation
       Interaction signals    ↓
       Device signals        Multiplex graph
                │             ↓
                │       Temporal weighting
                │             ↓
                │       Community detection
                │             ↓
                │       Statistical validation
                │             ↓
                └───────┬───────┘
                        │
                 EVIDENCE ENGINE
                        │
             ┌──────────┼──────────┐
             │          │          │
           PASS       STEP-UP    HOLD
             │          │          │
             └──────────┼──────────┘
                        │
                  Evidence Card
                        │
                 Investigator UI
                        │
                 Optional report
27. The strongest final ShadowGram thesis

I would replace your current Core Axiom with this:

Fraudulent coordination may be difficult to identify from an individual session alone. ShadowGram tests whether combining low-cost behavioral evidence across multiple sessions can reveal coordination before expensive identity and credit-verification steps occur.

That is:

technically defensible;
experimentally testable;
much harder for a judge to attack;
compatible with your graph architecture;
compatible with your hackathon demonstration;
and does not falsely claim that commercial fraud vendors have no graph capabilities.
The most important takeaway for the team

Your project does not need to beat BioCatch, DataVisor, Sift, etc.

That would be an enormous and unrealistic claim.

Your hackathon objective should instead be:

Build a convincing experimental prototype demonstrating that early, low-cost behavioral relationships can provide useful additional evidence of coordinated application activity before expensive downstream verification.

And prove it with:

Ablation study
Scripted vs randomized vs human-emulated attack
Individual vs relational detection
False-positive campus/common-cause test
Temporal decay experiment
Statistical validation
Explainable evidence card
Live 20-agent local demonstration

If those experiments work, that is your innovation story.

And importantly, the fact that commercial systems such as BioCatch and DataVisor already use graph/behavioral correlation does not kill ShadowGram. It forces you to make the claim narrower and much stronger. BioCatch explicitly markets network/link analysis, while DataVisor explicitly markets unsupervised coordinated-behavior detection.

Your differentiator should therefore be the early-funnel, lightweight, privacy-conscious, experimentally validated combination and the way you demonstrate its incremental value, not “we invented relational fraud detection.”


PART — Experimental Validation Plan

This is where ShadowGram can move from “interesting architecture” to “we have evidence that our architecture works.”

28. Build the experiment before claiming the innovation

The biggest weakness in the current document is that many numbers are presented as if ShadowGram has already proven them.

For example:

S_comp ≥ 0.78

Q > 0.60

p < 0.001

<5 ms

<10 ms

<15 ms

These should initially be treated as engineering targets, not facts.

The correct wording is:

“Prototype target: evaluate whether...”

Then measure the actual result.

For the hackathon, this is much safer.

29. Create a controlled synthetic dataset

You don't need real borrower data.

In fact, you should not use real people's financial or identity data for the prototype.

Create a synthetic dataset containing:

Legitimate users

Example:

H001
H002
H003
...
H500

Generate realistic variation:

different typing speed;
different navigation;
different time between actions;
different text;
different devices;
different screen sizes;
different interaction patterns.

The important property is:

Legitimate users should NOT all behave identically.

Otherwise the detector becomes artificially easy.

30. Create multiple attack populations

Don't create only one "bot."

Create different attacker populations.

Attack A — Identical automation
A001
A002
A003
...
A020

Almost everything is identical.

Expected:

Very easy to detect.

This proves the system can catch basic automation.

Attack B — Randomized automation

Each bot gets:

different name;
different timing;
different route order;
different text;
different browser characteristics.

Expected:

Key 1 becomes weaker.

This is important.

Attack C — Coordinated swarm

Now deliberately make the individual sessions appear more independent.

But preserve coordination at the population level.

For example:

Bot A
Bot B
Bot C
...
Bot T

Each has different:

timing;
text;
browser profile;
interaction variation.

But they share statistically unusual patterns such as:

related navigation sequences;
unusual application-state transitions;
coordinated arrival distribution;
semantic intent;
recurring interaction structures.

This is the dataset that actually tests your thesis.

31. Add a legitimate "flash crowd"

This is essential.

Otherwise your demo is biased.

Create something like:

Campus Event
────────────

100 legitimate users
        ↓
same Wi-Fi
        ↓
same 30-minute period
        ↓
same loan product

Your system must not automatically classify them as a fraud ring.

This tests your common-cause protection.

Your graph might initially look like:

              Campus Wi-Fi
                   │
       ┌───────────┼───────────┐
       │           │           │
      H01         H02         H03
       │           │           │
      H04         H05         H06

But the system should recognize:

Shared infrastructure is an insufficient explanation for coordinated fraud.

32. Add a second legitimate correlated population

One flash crowd isn't enough.

Create another scenario:

Marketing campaign

A lender sends the same promotional message to 200 people.

Therefore:

same loan product;
similar text;
similar time period.

Again:

semantic similarity ↑
temporal similarity ↑

But they are legitimate.

This tests whether ShadowGram blindly treats correlation as fraud.

33. Your graph must distinguish correlation from coordination

This should become a fundamental design rule.

Correlation
People behave similarly
because something external caused it.
Coordination
People behave similarly
in ways difficult to explain by the same external cause.

That distinction is much more important than simply detecting similarity.

34. Introduce a Common-Cause Score

Instead of simply:

$$ S_{comp} $$

consider an adjustment:

$$ S_{final}=S_{comp}-C $$

where:

$$ C = \text{common-cause contribution} $$

For example:

Same IP
      ↓
High common-cause probability
      ↓
discount

while:

Same unusual navigation sequence
+
same timing structure
+
same interaction pattern
      ↓
low common-cause explanation
      ↓
stronger evidence

This is a conceptual improvement.

You don't need to pretend that the formula is scientifically validated yet.

35. Measure false-positive rate

Your system should report:

$$ FPR = \frac{\text{legitimate sessions incorrectly flagged}} {\text{all legitimate sessions}} $$

This is critical.

A fraud detector that catches every attacker but blocks 30% of genuine customers is not a good product.

For the demo, you could show:

Legitimate users: 500
False positives: 4

FPR = 0.8%

Only show numbers actually produced by your experiment.

Never manufacture them beforehand.

36. Measure recall

For the attack population:

$$ Recall = \frac{TP}{TP+FN} $$

In simple language:

Of all the attackers, how many did ShadowGram detect?

Example:

Attack sessions = 100
Detected = 93

Recall = 93%

Again, that is an example—not a result you should claim until measured.

37. Most important metric: precision
$$ Precision = \frac{TP}{TP+FP} $$

This answers:

When ShadowGram says "suspicious," how often is it actually correct?

For a hackathon fraud system, this is extremely important because your system is supposed to avoid mass-quarantining legitimate users.

38. Add "graph lift"

This should be one of your headline experimental metrics.

Run:

Baseline

Individual-session features only.

Then:

ShadowGram

Individual features + relational graph.

Calculate:

$$ Lift = Metric_{graph}-Metric_{individual} $$

For example:

Individual-only F1: 0.71
Graph-enhanced F1: 0.84

Lift: +0.13

Those numbers are illustrative only.

If your actual experiment produces a meaningful improvement, you have something extremely useful for the judges:

“The graph did not replace conventional detection. It added measurable detection value.”

That is a much stronger claim.

39. Perform an ablation study

Your final paper/demo dashboard should show something like:

                    DETECTION PERFORMANCE

Individual signals        ███████
+ Temporal                ████████
+ Navigation              █████████
+ Semantic               █████████
+ Interaction             ██████████
+ Environment             ██████████
+ RELATIONAL GRAPH        ███████████

But the graph must earn its place through actual data.

This answers the judge's likely question:

“Why do you need the graph?”

Your answer becomes:

“We experimentally removed the graph and measured the change.”

That is far more convincing than explaining it theoretically.

40. Test each layer independently

Create a layer contribution table.

Experiment	Temporal	Navigation	Interaction	Semantic	Environment	Graph
Baseline	❌	❌	❌	❌	❌	❌
E1	✅	❌	❌	❌	❌	❌
E2	❌	✅	❌	❌	❌	❌
E3	❌	❌	✅	❌	❌	❌
E4	❌	❌	❌	✅	❌	❌
E5	❌	❌	❌	❌	✅	❌
Full	✅	✅	✅	✅	✅	✅

Then measure performance.

This lets you discover something potentially interesting:

Maybe one of your five layers isn't actually useful.

That's okay.

Removing a useless feature is a research result.

41. Don't assume MiniLM semantic similarity works for fraud

Your current:

$$ Cosine(A,B)\geq0.88 $$

is an arbitrary threshold unless experimentally calibrated.

Instead:

Step 1

Generate legitimate loan explanations.

Step 2

Generate attacker explanations.

Step 3

Calculate similarity distributions.

You may discover:

Legitimate pairs

0.35
0.42
0.51
0.63
...

Attack pairs

0.61
0.72
0.78
0.83
...

Then select a threshold based on the observed distributions.

Maybe it's:

0.81

Maybe:

0.87

Maybe semantic similarity isn't useful enough.

Let the experiment decide.

42. Same principle applies to your graph threshold

Your current:

$$ S_{comp}\geq0.78 $$

should not be treated as a universal truth.

Run:

Threshold = 0.60
Threshold = 0.65
Threshold = 0.70
Threshold = 0.75
Threshold = 0.80
Threshold = 0.85
Threshold = 0.90

Measure:

precision;
recall;
false positives;
cluster size;
processing time.

Then choose the threshold that gives the best trade-off.

This gives you a genuine engineering justification for your final number.

43. Same for Leiden

Do not claim:

“Leiden is automatically better than Louvain for ShadowGram.”

Instead benchmark:

Same dataset
      │
 ┌────┴────┐
Louvain   Leiden
 │          │
 Q          Q
runtime    runtime
cluster    cluster
quality    quality

Then compare.

Your final statement can become:

“On our benchmark dataset, Leiden produced [X] while Louvain produced [Y].”

That is much stronger.

44. Don't over-engineer the 2D CNN yet

This is another important recommendation.

Your current architecture has:

2D-CNN + ONNX + motion matrices + <10 ms

That's a lot.

For the hackathon, first build:

raw interaction events
        ↓
feature extraction
        ↓
simple classifier

Then benchmark.

Only add the CNN if the experiment demonstrates that it provides meaningful improvement.

Otherwise you risk spending your development time training a model that contributes little to the actual ShadowGram thesis.

45. Your strongest architecture may actually be simpler

Potential final pipeline:

                TELEMETRY
                    │
                    ▼
           Feature Extraction
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
   Session Risk          Candidate Links
          │                   │
          │             Multiplex Graph
          │                   │
          │             Community Detection
          │                   │
          └──────────┬────────┘
                     ▼
              Evidence Engine
                     │
             Statistical Test
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
        PASS      STEP-UP      HOLD

That's easier to build, easier to explain and easier to defend.

46. The live demo should demonstrate the experiment

Don't make the demo simply:

“Look, 20 red dots appeared.”

Instead:

Stage 1

Judge behaves normally.

Human → GREEN
Stage 2

Launch basic bots.

20 bots → Key 1 catches many
Stage 3

Launch randomized bots.

Key 1 catches fewer
Stage 4

Graph activates.

multiple weak relationships
        ↓
cluster emerges
Stage 5

Click cluster.

Show:

18 sessions

Temporal evidence     0.87
Navigation evidence   0.82
Semantic evidence     0.79
Interaction evidence  0.74

Common-cause discount  -0.11

Cluster confidence     [actual measured value]

Then:

Step-up verification

rather than immediately saying:

“These are criminals.”

That distinction makes the system look much more mature.

47. The judge's strongest possible attack

Expect someone to ask:

“What stops a sufficiently advanced AI swarm from randomizing all of these signals?”

Do not claim that ShadowGram makes this impossible.

Answer:

“Nothing makes behavioral detection impossible to evade. Our goal is to increase the cost of making many independent sessions statistically independent. We therefore evaluate robustness under progressively stronger adversarial simulations.”

That's an excellent cybersecurity answer.

It acknowledges the adversarial nature of the problem.

48. This creates another valuable metric: Evasion Cost

Instead of claiming:

“Our detector cannot be bypassed.”

measure:

How much attacker randomization is required before detection performance drops below an acceptable level?

For example:

Attack sophistication

Level 1 ─────────────── 95% detected
Level 2 ─────────────── 88%
Level 3 ─────────────── 79%
Level 4 ─────────────── 64%
Level 5 ─────────────── 48%

Those are hypothetical values.

But the experiment itself would be excellent.

It tells the judge:

“Here is exactly where our system starts to fail.”

That is much more credible than claiming perfect detection.

49. ShadowGram should have a defined "failure boundary"

Every serious security system needs one.

For example:

ShadowGram is designed to detect:

coordinated multi-session behavior
       ↓
within an observable application window
       ↓
when sufficient behavioral evidence exists

It is not designed to guarantee detection when:

every attacker behaves independently;
there is insufficient telemetry;
there are too few sessions;
the attacker perfectly reproduces legitimate population variance;
the common-cause explanation is stronger than the coordination evidence.

This actually strengthens the project.

50. Final research question

Your entire project can now be expressed as one experimentally testable question:

Can low-cost behavioral evidence collected before expensive identity verification provide measurable additional value for detecting coordinated application activity when individual sessions are designed to appear legitimate?

That's the research question I would put near the beginning of the ShadowGram documentation.

And your hackathon answer becomes:

We built a prototype and tested it under increasingly difficult adversarial conditions.

That's considerably stronger than:

“We invented an AI swarm detector.”

Where we are now

Completed audit areas:

❌ false competitor claims identified
❌ unsupported legal claims identified
❌ unsupported statistical claims identified
❌ questionable performance claims identified
✅ early-funnel positioning
✅ relational detection thesis
✅ multiplex graph concept
✅ temporal graph concept
✅ common-cause protection
✅ evidence-card architecture
✅ LLM-as-explanation rather than decision-maker
✅ adversarial evaluation framework
✅ ablation methodology

The key shift is now clear: don't make ShadowGram impressive by adding more buzzwords; make it impressive by experimentally proving which parts actually improve detection.

PART — Graph & Model Engineering Audit

This is the most important technical audit because the graph is the actual heart of ShadowGram. The five signals should feed the graph; they should not become five unrelated AI models just for complexity.

51. Recommended architecture: multiplex evidence graph

Instead of one graph containing one mysterious S_comp, represent different relationships separately.

                 SHADOWGRAM
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       Session     Session    Session
       features    features   features
          │          │          │
          └──────┬───┴──────┬───┘
                 ▼
          MULTIPLEX GRAPH
        ┌────────┼────────┐
        ▼        ▼        ▼
      TIME      NAV      SEMANTIC
        │        │        │
        └────┬───┴───┬────┘
             ▼       ▼
          KINETIC   ENVIRONMENT
                │
                ▼
          COMMUNITY MODEL
                │
                ▼
          EVIDENCE ENGINE

This is better than hiding everything inside:

$$ S_{comp}=w_1S_1+w_2S_2+\cdots+w_5S_5 $$

because a judge can actually see why two sessions became related.

52. Don't make every similarity an edge

This is a major engineering safeguard.

Suppose:

A ↔ B

because they both used the same IP.

That should not automatically create a strong fraud relationship.

Instead, maintain evidence channels:

A ── temporal ── B
A ── navigation ── B
A ── semantic ── B
A ── kinetic ── B
A ── environment ── B

Then the system can say:

"These two sessions are related across four independent evidence channels."

That is much more meaningful.

53. Separate infrastructure similarity from behavioral similarity

This should become a core design principle.

Infrastructure

Examples:

IP;
ASN;
network;
device characteristics;
browser characteristics.

These can be shared legitimately.

Behavioral

Examples:

event timing;
navigation sequence;
interaction dynamics;
unusual application flow;
semantic behavior.

The system should generally give more evidentiary weight to combinations of independent behavioral signals than to a shared IP.

For example:

Same IP
      ↓
weak relationship

Same IP
+
same unusual route sequence
+
same timing structure
+
same unusual interaction pattern
      ↓
stronger relationship

This also helps with your campus-Wi-Fi false-positive scenario.

54. Use a heterogeneous graph if the implementation supports it

A future version could represent different entities:

Session
Device
Network
Application
Event pattern
Semantic cluster

For example:

Session A
   │
   ├── used → Device X
   │
   ├── network → ASN Y
   │
   ├── followed → Route Pattern Z
   │
   └── belongs to → Semantic Cluster 4

Then:

Session B
   │
   ├── used → Device Q
   ├── network → ASN Y
   ├── followed → Route Pattern Z
   └── belongs to → Semantic Cluster 4

The devices are different.

The network may be shared.

But the combination of relationships becomes interesting.

This is closer to actual graph-based fraud reasoning than simply drawing red lines between accounts.

55. Candidate generation is more important than brute-force comparison

Your document correctly noticed the \(O(N^2)\) problem, but one statement needs changing:

"Traditional servers crash under this load."

That is too broad.

Large fraud systems can process enormous datasets using distributed systems, indexing, blocking, approximate search, streaming architectures, etc.

Your legitimate innovation is therefore not:

"Other systems cannot process 100,000 users."

Instead:

"ShadowGram uses aggressive candidate generation so that a lightweight prototype does not need to compare every session with every other session."

That's defensible.

56. Candidate blocking

Suppose:

$$ N=100,000 $$

Full pairwise comparison:

$$ \frac{N(N-1)}{2}\approx5\times10^9 $$

Instead, first create candidate buckets.

Example:

100,000 sessions
       │
       ├── time bucket
       │
       ├── route fingerprint
       │
       ├── coarse semantic cluster
       │
       └── interaction signature
       │
       ▼
candidate pairs
       ↓
5 billion → much smaller set

Then run expensive similarity only on candidates.

This is one of the most practical engineering improvements for ShadowGram.

57. But don't use overly aggressive blocking

There's a hidden danger.

Suppose two attackers intentionally differ in:

route;
timing;
text.

If your blocking requires them to share all three, you'll never compare them.

Therefore:

Blocking should be permissive. Final scoring should be strict.

Think:

Blocking = "Could these two be related?"

Scoring = "Are they actually related?"

That's a very useful distinction.

58. Your graph should be temporal

A fraud ring isn't necessarily permanent.

Use:

Graph(t)

rather than:

Graph

For example:

02:00 ─────── 03:00 ─────── 04:00
   │             │             │
 sparse       dense          sparse

A cluster that appears suddenly and disappears may be more interesting than a permanent relationship.

This also supports your original "flash syndicate" concept without assuming that every synchronized event is fraudulent.

59. Add graph velocity

A useful experimental feature:

$$ V_g(t)=\frac{\Delta E}{\Delta t} $$

where \(E\) is the number of suspicious relationships.

In simple terms:

How quickly is a suspicious network forming?

Example:

10:00 → 3 related sessions
10:02 → 11
10:04 → 24
10:06 → 41

That growth pattern can become another evidence layer.

Don't call it proof of fraud.

Call it:

rapid relational growth

and combine it with other evidence.

60. Add motif detection

This could become one of ShadowGram's more interesting technical additions.

A graph doesn't only contain communities.

It contains patterns.

For example:

A ─── B
│     │
C ─── D

or:

      A
     / \
    B   C
     \ /
      D

These structures can represent recurring coordination patterns.

Instead of only asking:

"Is this community dense?"

ask:

"Does this community contain suspicious recurring interaction structures?"

This gives you a future research direction beyond simple Louvain/Leiden clustering.

61. Don't make modularity Q your fraud detector

This line in your current document is particularly dangerous:

Any cluster with Modularity Q > 0.60 and node count ≥3 is mathematically isolated as a syndicate (p < 0.001).

That is not valid.

A high modularity score does not automatically mean:

$$ p<0.001 $$

And:

$$ Q>0.60 $$

doesn't mean "fraud."

Modularity measures graph community structure.

It does not prove malicious coordination.

Replace the idea with:

Graph clustering
      ↓
candidate community
      ↓
evidence aggregation
      ↓
statistical validation
      ↓
risk assessment

This is a critical correction.

62. Statistical significance must test a specific hypothesis

Your permutation test is potentially useful, but define what it tests.

For example:

Null hypothesis

The observed relationship between sessions could arise from random assignment of behavioral observations to sessions within the same observation window.

Then shuffle the relevant labels while preserving appropriate structure.

If:

$$ p < 0.001 $$

you can say:

"The observed structure is unlikely under this particular null model."

You cannot say:

"Therefore these accounts are fraudulent."

That's a huge difference.

63. Use multiple-testing correction if you test many clusters

Suppose ShadowGram evaluates:

1,000 candidate clusters

and uses:

$$ p<0.001 $$

for each.

You are performing many statistical tests.

That increases the chance of false discoveries.

For a research-grade implementation, investigate:

Benjamini-Hochberg FDR;
Bonferroni correction where appropriate;
hierarchical testing.

For the hackathon prototype, you don't necessarily need a sophisticated statistical framework, but you should know this limitation if a judge asks.

64. Replace "Why Card proves fraud"

Your Why Card should not say:

❌ "This proves the accounts are fraudulent."

It should say:

✅ "Evidence associated with this cluster."

For example:

SHADOWGRAM EVIDENCE

Cluster: C-014
Sessions: 18

Temporal similarity       HIGH
Navigation similarity    HIGH
Semantic similarity      MEDIUM
Interaction similarity   HIGH
Infrastructure overlap   LOW

Common-cause analysis    PASSED

Statistical test:
Observed structure differs
from permutation baseline.

Result:
ESCALATE FOR STEP-UP REVIEW

This is significantly safer and more professional.

65. Use a three-state decision

Instead of:

SAFE / FRAUD

use:

ALLOW
   │
   ├── insufficient evidence
   │
   ▼
STEP-UP
   │
   ├── stronger evidence
   │
   ▼
REVIEW / QUARANTINE

This is especially important for a lending system.

ShadowGram should be presented as a triage system, not an autonomous criminality judge.

66. Your "Step 2" idea is potentially strong

The actual positioning should be:

Application begins
       ↓
ShadowGram telemetry
       ↓
cheap pre-KYC assessment
       ↓
┌──────┼────────┐
│      │        │
ALLOW STEP-UP  HOLD
│      │        │
▼      ▼        ▼
KYC    extra    review
       check

The key innovation claim becomes:

Use low-cost relational behavioral evidence before expensive downstream verification.

That's much more defensible than:

"Existing fraud vendors don't detect swarms."

67. Don't claim ShadowGram replaces KYC

It doesn't.

It should be:

ShadowGram
     +
KYC
     +
credit assessment
     +
human review

not:

ShadowGram
     ↓
loan decision

This distinction matters enormously.

68. Don't claim "Denial-of-Wallet" is an established attack category unless sourced

Your concept is useful:

Attackers deliberately trigger expensive downstream verification.

But distinguish:

Established fact

Verification services can incur costs.

ShadowGram hypothesis

An attacker could exploit that cost structure through application flooding.

Experimental claim

Your simulation demonstrates the potential cost under specified assumptions.

Use those labels.

That prevents the project from accidentally presenting a proposed threat model as a documented widespread attack.

69. Your architecture should have an evidence ledger

This could be a genuinely nice feature.

For every cluster:

Cluster C-014
────────────────────────

Evidence ID E001
Temporal relationship
weight: 0.81

Evidence ID E002
Navigation relationship
weight: 0.76

Evidence ID E003
Semantic relationship
weight: 0.83

Evidence ID E004
Common-cause factor
weight: -0.17

Statistical test
permutation p = [actual result]

Timestamp
[actual timestamp]

Model version
v0.4.2

Now your Why Card isn't just UI.

It is a reproducible evidence record.

That is a much stronger innovation for a cybersecurity hackathon.

70. Freeze the evidence before the LLM sees it

Your LLM should receive something like:

{
  "cluster_id": "C-014",
  "node_count": 18,
  "temporal_similarity": 0.81,
  "navigation_similarity": 0.76,
  "semantic_similarity": 0.83,
  "common_cause_adjustment": -0.17,
  "permutation_p": 0.0007
}

The LLM's job:

JSON
 ↓
human-readable explanation

Not:

raw sessions
 ↓
LLM
 ↓
decide fraud

This is an important architectural boundary.

71. Your NVIDIA component should therefore be positioned differently

Don't say:

"NVIDIA AI detects the fraud."

Say:

"The detection engine produces structured evidence. NVIDIA NIM converts that evidence into an operator-readable explanation."

That gives the LLM a controlled role.

It also makes the demo more impressive because you can demonstrate:

Graph
  ↓
Evidence
  ↓
Structured JSON
  ↓
NVIDIA model
  ↓
Why Card / report
72. One more innovation: counterfactual Why Card

This could be excellent for judges.

Instead of only:

"Why was this cluster flagged?"

show:

"What would have caused this cluster not to be flagged?"

Example:

WHY FLAGGED?

✓ unusual temporal coordination
✓ unusual navigation similarity
✓ interaction similarity
✓ low common-cause explanation

WHAT WOULD REDUCE RISK?

If only the shared network remained:
→ cluster would not cross threshold.

If navigation similarity disappeared:
→ evidence becomes insufficient.

If interaction similarity disappeared:
→ STEP-UP instead of QUARANTINE.

This is a much better explanation interface than a generic AI-generated paragraph.

73. This also gives ShadowGram a strong "human-in-the-loop" story

The operator isn't asked to blindly trust AI.

They see:

OBSERVATION
    ↓
RELATIONSHIP
    ↓
STATISTICAL EVIDENCE
    ↓
MODEL INTERPRETATION
    ↓
HUMAN DECISION

That's a very strong architecture for a cybersecurity competition.

74. Revised technical thesis

I would now describe ShadowGram like this:

ShadowGram is a pre-verification behavioral triage system that detects potentially coordinated application activity by combining low-cost session telemetry with a temporal, multi-signal relational graph. It does not assume that a single suspicious account is fraudulent. Instead, it searches for groups whose combined behavioral relationships are difficult to explain by legitimate common causes.

That's considerably stronger than the original "AI swarm detector" wording.

75. What I would actually build for the hackathon

Don't attempt every feature in the document.

MUST BUILD
1. Synthetic loan application
2. Telemetry collector
3. Session feature extraction
4. Temporal features
5. Navigation features
6. At least one interaction feature
7. Semantic similarity
8. Candidate graph
9. Leiden/Louvain comparison
10. Evidence/Why Card
11. Step-up flow
12. Attack simulator
13. Legitimate flash-crowd simulator
14. Evaluation dashboard
NICE TO HAVE
15. Environment signals
16. Graph velocity
17. Motif detection
18. Permutation testing
19. Counterfactual Why Card
20. NVIDIA explanation
CUT IF TIME IS SHORT
❌ 2D CNN
❌ WebGL complexity
❌ elaborate SAR automation
❌ five different ML models
❌ complicated legal automation
❌ claims of autonomous decision-making

A working graph + strong experiment beats ten unfinished AI components.

The biggest upgrade from this audit

Your project is no longer:

"Look at our complicated AI architecture."

It becomes:

"Here is a controlled adversarial experiment. Here is a legitimate correlated population. Here is the baseline. Here is what happens when we add relational evidence. Here is where the detector succeeds. Here is where it fails. Here is the evidence an operator sees."

That is exactly the kind of story that can make a hackathon project feel like real cybersecurity engineering rather than an AI buzzword demo.

Next part: the adversarial/red-team audit — how to attack ShadowGram itself, what a strong 2026 swarm simulation should look like, and how to prove that the detector isn't simply winning because the bots were unrealistically easy.

PART — Adversarial / Red-Team Audit

This is probably the most important part for hackathon credibility.

If ShadowGram only detects bots that you deliberately make similar, a judge can reasonably say:

“Of course it works. You created the attack.”

So the red-team experiment should deliberately try to break ShadowGram.

76. Define attacker capability levels

Don't define the attacker as simply "AI swarm."

Create progressively stronger adversaries.

Level 0
Normal human traffic

Level 1
Simple scripted automation

Level 2
Randomized automation

Level 3
Human-emulating automation

Level 4
Coordinated heterogeneous swarm

Level 5
Adaptive adversary

This gives you a clean experimental ladder.

77. Level 1 — obvious automation

Example:

Bot 1
Bot 2
Bot 3
...
Bot 20

All execute almost identical actions.

Expected:

Key 1 → strong detection
Graph → strong cluster

This validates the basic pipeline.

But do not use this as your main evidence.

It's too easy.

78. Level 2 — randomized bots

Now introduce variation.

Each bot receives:

random delays;
different names;
slightly different navigation;
different text;
different viewport;
different browser settings.

Conceptually:

Bot A → 1.2s → /loan → /profile → /submit
Bot B → 2.8s → /loan → /profile → /submit
Bot C → 1.7s → /loan → /help → /loan → /submit

The individual sessions should become harder to classify.

This tests whether ShadowGram can still find relationships.

79. Level 3 — human-emulation

Now assume the attacker knows your Key 1.

They intentionally generate:

pointer events;
variable click delays;
scrolling;
realistic pauses;
touch-like interaction patterns.

The goal is:

Individual session
       ↓
looks reasonably human

This is where your original thesis becomes useful.

The question changes from:

"Can I detect this bot?"

to:

"Can I detect that many apparently human sessions are behaving as a coordinated population?"

80. Level 4 — heterogeneous swarm

This should be your flagship adversarial test.

Don't make 20 bots identical.

Give them different profiles:

Agent A → browser profile 1
Agent B → browser profile 2
Agent C → browser profile 3
...
Agent T → browser profile 20

Vary:

timing;
text;
routes;
device characteristics;
interaction patterns.

But preserve selected coordination relationships.

For example:

                 coordination
                       │
       ┌───────────────┼───────────────┐
       ↓               ↓               ↓
    timing          workflow        semantic
       │               │               │
       └───────────────┼───────────────┘
                       ↓
                    graph

This tests the actual ShadowGram proposition.

81. Don't assume all layers remain correlated

A sophisticated adversary may deliberately attack your assumptions.

For example:

Temporal similarity → LOW
Navigation similarity → MEDIUM
Semantic similarity → HIGH
Interaction similarity → LOW
Infrastructure similarity → LOW

ShadowGram should not automatically reject this group simply because one layer is strong.

This is why your graph should treat each signal as separate evidence.

82. Attack the semantic layer

Your current architecture assumes similar intent produces similar embeddings.

Attack that assumption.

Generate semantically equivalent but lexically different explanations.

For example, conceptually:

"I need money for tuition."

"I require financial assistance
to cover my educational expenses."

"My immediate funding requirement
is related to college fees."

The wording differs.

The semantic representation may still be similar.

Then go further:

"I need money for tuition."

"I am currently enrolled in college
and need temporary financial support."

Then introduce irrelevant details.

Your experiment should measure how robust the semantic detector is.

83. Attack the temporal layer

Your original system relied heavily on synchronized activity.

An attacker can deliberately introduce jitter.

Instead of:

12:00:00
12:00:01
12:00:02
12:00:03

you might simulate:

12:00:03
12:00:19
12:01:04
12:01:47
12:02:31

The purpose is not to create a real attack.

It is to ask:

How much timing randomization is required before temporal evidence stops being useful?

This gives you a measurable robustness curve.

84. Attack the navigation layer

Make bots take different routes.

For example:

Bot A:
/home → /loan → /profile → /submit

Bot B:
/home → /faq → /loan → /profile → /submit

Bot C:
/home → /loan → /help → /loan → /submit

Now test:

Does ShadowGram still recognize structural similarity?

This is where LCS can be compared against simpler route matching.

85. Attack the interaction layer

This is particularly important.

Do not claim:

"Bots cannot generate human-like mouse movement."

They can generate sophisticated synthetic movement.

Instead:

"ShadowGram tests whether interaction-event distributions provide additional discriminatory information under our simulated adversaries."

Then measure it.

Your experiment can vary:

human-like variance
       ↓
low ─────────────── high

and observe detector performance.

86. Attack the environment layer

Suppose attackers deliberately vary:

screen dimensions;
browser configuration;
rendering characteristics;
clock characteristics.

Your system should treat environmental signals as supporting evidence, not identity proof.

This is important because hardware/browser fingerprints can collide among legitimate users.

For example:

100 students
      ↓
same laptop lab
      ↓
similar browser fingerprint

That should not create a fraud ring.

87. Attack the graph itself

This is where the project becomes much more interesting.

Suppose an attacker inserts legitimate-looking nodes between malicious nodes.

Conceptually:

Malicious A
     │
  clean-looking
     │
Malicious B
     │
  clean-looking
     │
Malicious C

The purpose is to make the malicious community less obvious.

Your system should identify whether those nodes are:

genuine bridge nodes

or

anomalous bridge nodes.

This is why your "boundary repair" idea can be tested experimentally.

88. But don't claim Leiden solves adversarial graph attacks

Leiden gives you well-connected communities.

It does not magically defeat adversarial graph manipulation.

The correct architecture is:

Graph construction
       ↓
Community detection
       ↓
Boundary analysis
       ↓
Evidence validation

Leiden is one component.

Not the security mechanism itself.

89. Test graph poisoning

Another experiment:

Start with:

20 malicious nodes

Then gradually add:

5 legitimate-looking nodes
10
20
50
100

Measure whether the malicious community remains detectable.

This produces a robustness curve.

For example:

Detection
100% │████████████
 80% │██████████
 60% │████████
 40% │████
 20% │██
     └──────────────
       injected nodes

Again, actual values must come from your experiment.

90. Test swarm fragmentation

Instead of one large group:

A B C D E F G H I J

split it:

A B C
      D E F

G H I
      J K L

Now ask:

Can ShadowGram identify related subcommunities?

This is important because attackers don't have to create one obvious giant cluster.

91. Test slow attacks

Your current "20 bots in 3 seconds" demo is visually impressive but unrealistic as the only threat model.

Create:

Day 1 → 5 sessions
Day 2 → 7
Day 3 → 3
Day 4 → 8

or within a sliding observation window.

The question becomes:

Can temporal decay preserve useful evidence without keeping suspicious relationships forever?

This tests your time-kernel design.

92. Test legitimate synchronized activity

This must be one of the hardest tests.

Create:

200 legitimate students
      ↓
same campus
      ↓
same Wi-Fi
      ↓
same marketing campaign
      ↓
same application
      ↓
same 30-minute period

A naive system could scream:

FRAUD RING!

ShadowGram should instead produce something like:

High common-cause probability
+
insufficient independent behavioral evidence

→ NO SYNDICATE QUARANTINE

If your system genuinely does this, show it to the judges.

That may be more impressive than catching the bots.

93. Add an adversarial scorecard

Your dashboard could display:

SHADOWGRAM RED-TEAM SCORECARD

                         Detection    False Positive
Simple automation          98%            0.2%
Randomized automation      91%            0.4%
Human-emulated             78%            0.7%
Heterogeneous swarm        74%            0.9%

Campus flash crowd          —             0.3%
Marketing campaign         —             0.5%

These numbers are examples only.

Your actual results should populate the table.

This is excellent hackathon material because judges can immediately see that you tested the system against its own weaknesses.

94. Compare against a baseline

This is critical.

Don't only show:

ShadowGram = 84%

Show:

                       Baseline    ShadowGram
Individual model          X%          X%
Rule-based                X%          X%
Graph only                X%          X%
Full system               X%          X%

Now you can answer:

"What does ShadowGram add?"

95. Your strongest experiment may be "graph contribution"

Run the exact same attack dataset twice.

Experiment A
Individual session classifier
Experiment B
Individual classifier
+
relational graph

Then compare.

If the graph gives a measurable improvement against the harder attack classes, that becomes your strongest technical evidence.

96. Test whether the graph creates false positives

This is the other side.

Run:

100 legitimate users

then:

100 legitimate users
+
same Wi-Fi

then:

100 legitimate users
+
same Wi-Fi
+
same campaign

Then:

100 legitimate users
+
same Wi-Fi
+
same campaign
+
similar application reason

Your system should progressively recognize that those relationships can be explained by common causes.

97. Introduce a "common-cause explanation engine"

Conceptually:

Observed relationship
        │
        ▼
Can a legitimate external
cause explain it?
        │
    ┌───┴───┐
   YES      NO
    │        │
 discount   retain
 evidence   evidence

Potential common causes:

same Wi-Fi;
same campus;
same campaign;
same event;
same application deadline;
same device lab;
same public network.

This is an important anti-false-positive mechanism.

98. Do not use "common-cause immunity" as an absolute rule

Your current terminology:

"Common-Cause Immunity"

sounds stronger than the actual mechanism.

A shared cause doesn't make a relationship immune.

For example:

Same campus
+
same Wi-Fi
+
same route
+
same unusual interaction structure
+
same coordinated timing

There could still be a problem.

I'd rename it:

Common-Cause Adjustment

or:

Common-Cause Evidence Discount

Much easier to defend scientifically.

99. Build an attack generator that has knobs

This would be an excellent live demo feature.

For example:

ATTACK SOPHISTICATION

Timing randomization     [██████░░░░]
Navigation variation     [████░░░░░░]
Semantic variation       [███████░░░]
Interaction variation    [████████░░]
Infrastructure diversity [█████████░]

             [RUN TEST]

Then:

Detection rate: 76%
False positive rate: 0.8%

The judges can literally see that you are testing the detector against increasingly difficult conditions.

100. This changes the pitch dramatically

Instead of saying:

"ShadowGram detects AI swarms."

say:

"We built an adversarial test harness that progressively makes coordinated sessions look more independent. ShadowGram is evaluated against those increasingly difficult conditions rather than only against obvious bots."

That sounds much more serious.

101. One major correction to your current pitch

Your current script says:

"Autonomous AI swarms drained ₹20 Lakhs in 15 minutes from digital lenders."

Don't say this as a real-world fact unless you have a source documenting exactly that incident.

Instead say:

"Our stress-test scenario models a ₹20 lakh exposure: 200 simulated applications × ₹10,000."

That is completely different.

The first is a factual claim.

The second is your experiment.

102. Same rule for the "50 accounts approved" claim

Don't say:

"Traditional systems approve all 50 accounts."

Unless you've experimentally demonstrated it against a specific baseline.

Say:

"Our baseline simulation is designed so that individual sessions remain below the baseline detector's alert threshold, allowing us to test whether relational evidence adds detection value."

That is scientifically honest.

103. Your red-team objective

Put this directly into your project documentation:

Red-Team Objective: Attempt to reduce ShadowGram detection performance by increasing behavioral diversity while preserving coordinated activity. The purpose is to identify the conditions under which relational evidence remains useful and the conditions under which the system fails.

That sentence is extremely valuable.

104. What counts as success?

Not:

"ShadowGram detects everything."

Instead:

Success condition

ShadowGram demonstrates that:

relational information provides measurable additional value;
increasingly sophisticated simulated attackers reduce performance gradually rather than immediately;
legitimate common-cause events do not automatically become fraud clusters;
every high-risk cluster has inspectable evidence;
the system clearly identifies its own uncertainty and failure boundary.

That is a much more credible innovation claim.

105. The final innovation direction

After the audit, I would not position the innovation as:

"AI swarm detection."

That's too broad and there are already graph/behavioral fraud systems.

I'd position the technical contribution as:

A low-cost, pre-verification relational triage layer that combines session-level behavioral evidence, temporal relationships, common-cause adjustment, and explainable community evidence to identify potentially coordinated application activity before expensive downstream verification.

And then your genuinely interesting research question becomes:

Does relational behavioral evidence provide useful incremental detection power against coordinated sessions that are individually designed to resemble legitimate users?

That is something you can actually test.

Next part

The next part is the final architecture + hackathon optimization audit:

what to keep;
what to remove;
what is actually innovative;
what should be called experimental rather than proven;
how the 4 laptops should work;
what the judge should see in 3 minutes;
what metrics should appear on the dashboard;
what claims you can safely put on the poster;
and the final ShadowGram architecture I would recommend building.

PART — Final ShadowGram Architecture + Hackathon Optimization Audit

This is the part where I would stop adding features and decide what ShadowGram should actually be.

The goal is not to make the architecture sound advanced. The goal is to make the smallest system that can produce convincing, measurable evidence in front of judges.

106. First: What ShadowGram should NOT claim

Remove or soften these claims from the current document.

Current claim	Recommendation
“AI swarms are draining ₹20 lakh from lenders”	❌ Don't present as a real incident. Make it your simulated scenario.
“Traditional systems inspect accounts individually”	⚠️ Too broad. Modern fraud platforms also use graph/link analysis.
“BioCatch cannot cluster accounts”	❌ False. BioCatch has link-analysis capabilities.
“DataVisor operates primarily post-submission”	⚠️ Needs evidence. Don't claim without vendor-specific proof.
“Traditional servers crash at 100k pairwise comparisons”	❌ False/overstated. 5 billion comparisons are expensive, but servers don't simply “crash.”
“Western vendors don't support India”	❌ Too broad.
“ECOA prohibits unexplained loan denials”	⚠️ Oversimplified. Regulation B requires specific reasons for adverse action; don't frame your graph as automatically legally sufficient.
“SAR generated by NVIDIA = official regulatory SAR”	❌ Don't call it official. Call it a demonstration/report draft.
“p < 0.001 proves coordination”	❌ A p-value doesn't prove coordination. It measures incompatibility with a specified null model.
“Leiden guarantees fraud detection”	❌ No. Leiden gives useful community structure; it doesn't establish fraud.
“100% explainable”	❌ Replace with “evidence traceable to recorded signals.”
“Zero cloud bills”	⚠️ Only true for the local components. NVIDIA NIM API is still a cloud/API dependency unless you run it locally.

This actually makes ShadowGram stronger, because a judge cannot easily attack exaggerated claims.

107. The core architecture I recommend

Keep the system as:

                 ATHENAPAY
                     │
                     ▼
          ┌────────────────────┐
          │  STEP 2 TELEMETRY  │
          └──────────┬─────────┘
                     │
                     ▼
          ┌────────────────────┐
          │ KEY 1              │
          │ Session Signals    │
          └──────────┬─────────┘
                     │
            suspicious / uncertain
                     │
                     ▼
          ┌────────────────────┐
          │ KEY 2              │
          │ Relational Engine  │
          └──────────┬─────────┘
                     │
                     ▼
          ┌────────────────────┐
          │ Evidence Graph     │
          └──────────┬─────────┘
                     │
                     ▼
          ┌────────────────────┐
          │ Community +        │
          │ Boundary Analysis  │
          └──────────┬─────────┘
                     │
                     ▼
          ┌────────────────────┐
          │ Risk / Evidence    │
          │ Decision           │
          └──────────┬─────────┘
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
       CLEAR                 STEP-UP
                              │
                              ▼
                         HUMAN REVIEW

This is enough.

Don't turn it into a giant AI platform.

108. Key 1 should be extremely simple

Your current Key 1 is over-engineered in wording.

You don't need to prove:

“We can detect all Playwright bots.”

Instead:

Key 1 = cheap session-level screening.

Collect things such as:

pointer events
click timing
focus events
paste events
scroll events
touch events
automation indicators

Then produce:

session_signal_score

The purpose is:

Don't waste graph computation on obviously normal sessions.

That's a better architectural justification.

109. Key 1 should NOT make the final decision

This is important.

Imagine:

Bot A

looks perfectly human.

Key 1:

LOW RISK

That's okay.

It can still enter Key 2 because the relationship may be suspicious.

Therefore:

Key 1 = filter / feature generator

not:

Key 1 = final bot detector

This directly supports your thesis.

110. Key 2 becomes the innovation focus

The interesting part is:

Account A
Account B
Account C
Account D
        ↓
relationships
        ↓
graph

Instead of:

A → score
B → score
C → score
D → score

You calculate:

A ↔ B
A ↔ C
B ↔ C
B ↔ D
...

But don't compare every possible pair.

111. Keep your blocking idea

Your O(N²) discussion should become:

Naively comparing every session with every other session becomes expensive as traffic grows. ShadowGram therefore uses candidate blocking to compare only potentially related sessions.

Candidate blocking can use inexpensive properties such as:

time window
route family
event signature
coarse semantic bucket

Then expensive similarity calculations happen only on candidates.

This is much more defensible than:

“Traditional servers crash.”

112. The graph edge should contain evidence

This is one of the best improvements.

Don't create:

A ───── B

Create:

A ───── B

time       0.91
navigation 0.83
semantic   0.88
kinetic    0.74
environment 0.31

Then your UI can literally show:

Why are these two sessions connected?

That is your strongest explainability mechanism.

113. Don't make one arbitrary composite threshold your truth

Current:

S_comp >= 0.78

is okay for a prototype.

But don't say:

“0.78 mathematically means fraud.”

Instead:

“0.78 is an experimentally selected prototype threshold.”

Even better, allow it to be configured.

threshold = 0.70
threshold = 0.75
threshold = 0.80
threshold = 0.85

Then evaluate performance.

114. Use ablation testing

This is probably the single most valuable research feature you can add.

Run the detector with:

ALL 5 LAYERS

Then:

WITHOUT temporal
WITHOUT navigation
WITHOUT semantic
WITHOUT kinetic
WITHOUT environment

Compare results.

Example:

Configuration          Detection
All layers                87%
No temporal               82%
No navigation             79%
No semantic               84%
No kinetic                76%
No environment            86%

Those numbers are only examples.

Your experiment determines the real values.

This lets you say:

“We measured which signals actually contribute to detection.”

That's much more impressive than simply claiming five layers are innovative.

115. Add adversarial ablation

Then attack individual layers.

For example:

Attack                     Result
────────────────────────────────────
Timing randomization       ?
Route variation            ?
Text variation             ?
Fingerprint variation      ?
Interaction variation      ?
Combined variation         ?

This creates a real robustness evaluation.

116. Make the "Why Card" the centerpiece

Your Why Card should not say:

AI says this is suspicious.

It should show:

WHY THIS CLUSTER WAS FLAGGED

Cluster: SG-042

Accounts: 18

Evidence:

Temporal relationship
█████████░ 0.91

Navigation similarity
████████░░ 0.83

Semantic similarity
████████░░ 0.88

Interaction similarity
███████░░░ 0.74

Environment similarity
███░░░░░░░ 0.31

Common-cause adjustment
Applied: SAME CAMPUS NETWORK

Permutation test
p = [actual experiment result]

Decision
STEP-UP REQUIRED

Now the judge can understand your system without reading your architecture document.

117. Don't let the LLM decide fraud

This is another major architectural correction.

Bad:

Graph
 ↓
LLM
 ↓
"Fraud!"

Good:

Telemetry
 ↓
Statistics
 ↓
Graph
 ↓
Evidence
 ↓
Deterministic decision
 ↓
LLM
 ↓
Human-readable explanation

The LLM should be a reporting layer, not the detection engine.

118. NVIDIA NIM should therefore be optional

Your architecture should work without NVIDIA.

Detection
    ↓
always local

Then:

NVIDIA NIM
    ↓
optional explanation/report generation

If the network fails:

local template
    ↓
report

This makes your demo resilient.

And it supports the legitimate claim:

Core detection does not depend on an external LLM.

119. Don't call the generated document an official SAR

Use:

Suspicious Activity Report Demonstration

or:

Compliance Evidence Report

unless you have actually implemented the requirements and workflow for a legally valid SAR.

This prevents an easy judge challenge:

“Are you actually filing SARs?”

You can answer:

“No. This is a demonstration of how our evidence can be exported into a structured compliance-oriented report.”

Much safer.

120. The 1-rupee UPI challenge needs reconsideration

I would not make the ₹1 UPI penny-drop the central step-up mechanism.

It introduces:

banking integration complexity;
privacy considerations;
dependency on external infrastructure;
demo failure risk.

Instead, your demo can use:

STEP-UP REQUIRED

[ Verify Identity ]

and simulate the result.

If you later have a legitimate sandbox/payment integration, you can demonstrate it.

121. Your actual decision pipeline

I recommend:

                 session
                    │
                    ▼
            Session screening
                    │
                    ▼
          Candidate relationships
                    │
                    ▼
             Evidence edges
                    │
                    ▼
          Community detection
                    │
                    ▼
        Statistical validation
                    │
             ┌──────┴──────┐
             ▼             ▼
         insufficient    strong
             │             │
             ▼             ▼
           CLEAR       STEP-UP

Not:

cluster → automatic ban
122. Three possible outcomes are better

Use:

GREEN
No meaningful coordinated evidence.
AMBER
Some relational evidence.
Additional verification recommended.
RED
Strong coordinated evidence.
Cluster requires investigation / quarantine.

This is far more realistic than binary:

human / fraud
123. Your graph visualization should reflect uncertainty

Don't make every red line mean:

“This is definitely fraud.”

Instead:

Green node = normal
Yellow node = requires attention
Red node = strong evidence
Grey edge = weak relationship
Orange edge = moderate relationship
Red edge = strong relationship

And the Why Card explains the actual evidence.

124. Your strongest visual demo

The judge enters:

Nihad

and sees:

       HUMAN
         ●
         │
         │
     ────┼────
    /    │    \
   ●     ●     ●
  BOT   BOT   BOT

Then Alan launches your controlled swarm.

The graph dynamically becomes:

             ●
           / | \
          ●──●──●
         / \ | / \
        ●───●───●
             │
             ●

Then:

Cluster detected

Click it.

Why Card opens.

Then:

Step-up cluster: 20 sessions

Then the report.

That's your 3-minute story.

125. Your judge shouldn't need to understand Leiden

This is a critical presentation rule.

Don't say:

“We use Leiden modularity optimization.”

as your headline.

Say:

“We turn relationships between sessions into a graph and find groups that behave unusually similarly.”

Then:

“The prototype uses Leiden for community detection.”

Technical judges can ask about it afterward.

126. Your actual innovation claim

I would use this:

ShadowGram

Pre-verification relational fraud triage for coordinated application attacks.

Then:

Instead of asking whether one application looks fraudulent, ShadowGram asks whether multiple apparently legitimate sessions exhibit statistically unusual relationships before expensive downstream verification.

That is clear.

127. What makes it innovative enough for a hackathon?

Not:

“Nobody has ever used graphs for fraud.”

That's demonstrably vulnerable.

Instead:

Your combination
PRE-KYC
   +
LOW-COST TELEMETRY
   +
MULTI-SIGNAL RELATIONSHIPS
   +
COMMON-CAUSE ADJUSTMENT
   +
ADVERSARIAL TESTING
   +
EXPLAINABLE EVIDENCE GRAPH

The innovation is the system design and demonstrated workflow, not claiming invention of graph fraud detection itself.

128. Your most valuable research result

If you have limited time, prioritize this experiment:

Experiment

Create:

100 legitimate sessions
100 coordinated simulated sessions

Then progressively make the coordinated sessions more diverse.

Test:

Individual-only detector
vs.
ShadowGram relational detector

Measure:

Precision
Recall
F1
False-positive rate
Detection latency

Then produce:

               Individual    ShadowGram
Precision         XX%           XX%
Recall            XX%           XX%
F1                XX%           XX%
FPR               XX%           XX%
Latency           XX ms         XX ms

That table is worth more than ten pages of futuristic claims.

129. Second experiment: legitimate crowd

Run:

50 students
same Wi-Fi
same application
same time

Then test ShadowGram.

Your target isn't:

100% detection.

Your target is:

low false-positive clustering under a known common cause.

That demonstrates maturity.

130. Third experiment: adversarial swarm

Take the same malicious group.

Increase:

timing diversity
+
route diversity
+
semantic diversity
+
device diversity
+
interaction diversity

Plot:

                Sophistication →
Detection %
100 ┤████████
 80 ┤███████
 60 ┤█████
 40 ┤███
 20 ┤█
    └────────────────────

Again, populate with real measurements.

That becomes your adversarial robustness result.

131. Your final research question

I would put this into the project:

Can relational behavioral evidence improve detection of coordinated application activity when individual sessions are deliberately constructed to resemble legitimate users?

That's a legitimate engineering/research question.

And importantly:

You don't already know the answer.

You test it.

132. Your final architecture in one sentence

ShadowGram is a local pre-verification triage system that converts low-cost session telemetry into an evidence-weighted relational graph, identifies unusual communities, adjusts for legitimate common causes, and presents traceable evidence for human review or step-up verification.

That's the sentence I'd build the entire project around.

133. What I would cut before the hackathon

If time is limited, remove or simplify:

❌ 3D WebGL galaxy complexity
❌ complicated legal SAR generation
❌ real UPI integration
❌ five sophisticated ML models
❌ claims about defeating every commercial vendor
❌ claims about AI swarms being universally autonomous
❌ 100k-user production-scale performance claims
❌ exact vendor pricing unless verified
❌ unsupported legal claims

Keep:

✅ live swarm simulation
✅ telemetry collection
✅ relational graph
✅ community detection
✅ Why Card
✅ common-cause test
✅ adversarial test modes
✅ baseline comparison
✅ measurable metrics
✅ offline fallback

134. The 4-laptop setup becomes much cleaner
Laptop 1 — Attacker
Swarm generator
↓
20 controlled simulated sessions
Laptop 2 — ShadowGram engine
FastAPI
↓
Telemetry
↓
feature extraction
↓
graph
↓
community detection
Laptop 3 — Human / AthenaPay
Judge
↓
normal application
Laptop 4 — Analyst
Why Card
↓
cluster investigation
↓
report

That is enough.

135. The 3-minute story
0:00–0:30

Judge submits an ordinary application.

You say:

“This is the legitimate user.”

0:30–1:00

Launch the controlled swarm.

You say:

“These sessions are deliberately designed to look less identical than simple scripted bots.”

1:00–1:45

Graph forms.

You say:

“None of the individual signals is treated as proof. ShadowGram looks for relationships across sessions.”

1:45–2:20

Click cluster.

Show:

Timing
Navigation
Semantics
Interaction
Environment
Common-cause adjustment
2:20–2:45

Run step-up.

Human:

GREEN

Suspicious cluster:

AMBER/RED
2:45–3:00

Show your experiment results.

“We also attacked our own detector by randomizing timing, routes, language and interaction patterns. These are our measured results.”

That last sentence is what makes the project feel like engineering rather than a scripted demo.

136. Final verdict on ShadowGram

After the audit, I would rate the project like this:

Area	Current direction
Problem relevance	🟢 Strong
Graph-based concept	🟢 Established but useful
Pre-verification positioning	🟢 Potentially interesting
Multi-signal telemetry	🟢 Good
Adversarial evaluation	🟢 Very strong opportunity
Explainability	🟢 Strong
Local/on-premise angle	🟢 Useful
“AI swarm” claim	🟡 Needs careful wording
Legal claims	🔴 Need tightening
Competitor claims	🔴 Need tightening
Current numerical claims	🔴 Many need empirical validation
Hackathon demo potential	🟢🟢 Very high
My recommendation

Do not rebuild ShadowGram into something completely different.

The core idea is worth keeping.

But shift the project from:

“We invented a system that defeats AI swarms and existing fraud vendors.”

to:

“We built and adversarially evaluated a pre-verification relational fraud-triage system, and we measure whether relationships between individually plausible sessions provide additional evidence of coordination.”

That version is less flashy on paper but much harder for judges to destroy during Q&A.

And if your experiments show a meaningful improvement, then you have the evidence to make the stronger innovation claim.
