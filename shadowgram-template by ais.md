Create a full-screen dark cinematic landing page and interactive fraud-detection dashboard for **SHADOWGRAM**, a behavioral graph detection system that identifies coordinated AI-fraud accounts and hidden groups by analyzing behavioral fingerprints, timing, navigation, interaction patterns, content similarity, and environment signals.

The design should feel like a **cyber-forensics / behavioral intelligence platform** rather than a generic AI website. Use a premium, futuristic, minimal interface with dark blue-purple backgrounds, subtle glass effects, glowing graph connections, animated data points, and smooth motion.

## Theme & Colors (index.css CSS variables)

Background: 260 87% 3% (deep dark blue-purple)

Foreground: 40 6% 95% (off-white)

Secondary text: 40 6% 75%

Muted text: 40 6% 55%

Primary accent: indigo / violet / cyan

Alert accent: soft red / orange for suspicious activity

Success accent: emerald / green for normal activity

Body font: Geist Sans (via @fontsource/geist-sans)

Headline font: General Sans (loaded from Fontshare: https://api.fontshare.com/v2/css?f[]=general-sans@400,500,600,700&display=swap)

Use subtle gradients between indigo, violet, and cyan for important interactive elements.

Avoid excessive neon colors. The interface should feel professional, technical, and suitable for a cybersecurity / fraud-detection product.

***

# HERO SECTION

Create a full-screen hero section with a dark animated behavioral-network background.

The background should visually represent a network of accounts:

- Small glowing circular nodes representing accounts
- Thin lines connecting related accounts
- A few clusters of strongly connected nodes
- Slowly moving particles
- Subtle pulsing activity around suspicious clusters
- Occasional animated data trails between nodes
- Randomized but deterministic movement
- No distracting text inside the background

The network should feel like a live behavioral graph being analyzed.

The hero wrapper should use:

min-h-screen flex flex-col

overflow-hidden

The animated graph remains behind all content.

Add a very subtle blurred radial shape behind the main headline:

w-[984px] h-[527px]

opacity-70

bg-gray-950

blur-[82px]

Absolutely positioned at:

top-1/2

left-1/2

-translate-x-1/2

-translate-y-1/2

pointer-events-none

***

# NAVBAR

Full width:

py-5 px-8

display flex

justify-between

Left:

ShadowGram logo / wordmark.

Logo text:

"SHADOWGRAM"

Use a minimal geometric icon representing interconnected nodes or a behavioral graph.

Center navigation:

"Overview"

"Detection"

"ShadowGraph"

"Evidence"

Each item should be a button with:

text-foreground/90

subtle hover transition

active state using indigo/cyan glow

Right:

Primary button:

"Launch Detection"

rounded-full

px-5

py-2

The navbar should remain minimal and premium.

Below the navbar:

1px divider line with gradient:

transparent → foreground/20 → transparent

***

# HERO CONTENT

Center the content vertically in the remaining hero space.

Small eyebrow text:

"BEHAVIORAL GRAPH INTELLIGENCE"

Use:

uppercase

tracking-wide

text-sm

text-indigo/cyan

Headline:

"Detect the"

followed by:

"Shadow."

The word "Shadow." should use a gradient:

linear-gradient(to right, #6366f1, #a855f7, #22d3ee)

Use:

text-[150px] on large desktop screens

font-normal

leading-[0.95]

tracking-[-0.03em]

font-family: General Sans

Responsive sizing should reduce the headline on tablets and mobile.

Below the headline:

"Uncover coordinated behavior hiding in plain sight."

Use:

text-lg

leading-8

max-w-xl

opacity-80

Then a secondary description:

"ShadowGram analyzes behavioral fingerprints across accounts, connects related activity into a graph, and identifies suspicious coordinated clusters with explainable evidence."

Use:

text-base

leading-7

max-w-2xl

text-foreground/60

***

# HERO CTA

Primary CTA:

"Explore ShadowGraph"

rounded-full

px-[29px]

py-[18px]

Use a subtle indigo-to-violet gradient.

Hover:

slight scale

soft glow

arrow moves slightly to the right

Secondary CTA:

"View Detection Demo"

transparent / liquid-glass style

rounded-full

px-[29px]

py-[18px]

The two buttons should appear next to each other on desktop and stack on mobile.

***

# LIVE BEHAVIORAL GRAPH PREVIEW

Directly below the hero content, create a compact animated graph preview.

Display approximately 12–16 account nodes.

Example nodes:

A-104

A-117

A-203

A-211

A-304

A-319

A-402

A-417

Normal accounts should have subtle neutral nodes.

Suspicious accounts should form a visually connected cluster.

Example:

```text
            A-104
             |
      A-117--A-203
         \    |
          \   |
          A-211
         /    \
    A-304     A-319
```

When connections are created, animate the lines smoothly.

Show one highlighted cluster with a small floating label:

"SHADOW CLUSTER"

"6 accounts"

"0.91 coordination score"

Do not imply that the accounts belong to the same person.

Use wording such as:

"signals consistent with coordinated operation"

***

# BEHAVIORAL SIGNALS SECTION

Create a section titled:

"Every action leaves a fingerprint."

Subtitle:

"ShadowGram combines multiple behavioral signals instead of relying on a single indicator."

Create five interactive glass cards.

## Card 1 — INTERACTION

Icon:

keyboard / pointer

Title:

"Interaction Fingerprint"

Description:

"Typing rhythm, keystroke timing, hesitation, mouse movement, click intervals, scrolling, and pointer behavior."

Small metrics:

Dwell Time

Flight Time

Pointer Curvature

Click Interval

***

## Card 2 — NAVIGATION

Icon:

route / compass

Title:

"Navigation Pattern"

Description:

"Analyzes the sequence of pages and actions taken by accounts."

Show a miniature route:

Login → Feed → Profile → Search → Post

Represent the navigation sequence as a finite-state-machine style path.

***

## Card 3 — TIMING

Icon:

clock

Title:

"Temporal Coordination"

Description:

"Compares action timestamps and repeated activity intervals between accounts."

Show example:

Account A: 10:42:13.2

Account B: 10:42:14.0

Δt = 0.8s

Add a small label:

"Coordinated timing signal"

***

## Card 4 — CONTENT

Icon:

document / text

Title:

"Semantic Similarity"

Description:

"Compares the meaning of account content using sentence embeddings."

Show:

all-MiniLM-L6-v2

384-dimensional embedding

Cosine similarity

Use a simple vector visualization.

***

## Card 5 — ENVIRONMENT

Icon:

browser / monitor

Title:

"Environment Signals"

Description:

"Browser, operating system, screen resolution, timezone, language, Canvas/WebGL and simulated device/network signals."

Add a small label:

"Prototype • Consent-based"

***

# MULTI-SIGNAL CONVERGENCE

Create a large centered section titled:

"One signal is not enough."

Subtitle:

"ShadowGram looks for convergence across multiple behavioral categories."

Show five signals flowing into a central node:

INTERACTION

NAVIGATION

TIMING

CONTENT

ENVIRONMENT

↓

"COMPOSITE SIMILARITY"

↓

"BEHAVIORAL RELATIONSHIP"

Use animated lines connecting each signal.

Display an example composite score:

S_comp = 0.86

Show:

3+ signal categories aligned

Use the visual language of an analytical system rather than a marketing statistic.

***

# SHADOWGRAPH SECTION

Create a large interactive section titled:

"From behavior to relationships."

Subtitle:

"Accounts become nodes. Behavioral similarity becomes edges. Coordinated groups emerge as communities."

Create a large graph visualization using:

React-Force-Graph

Display:

- account nodes
- weighted edges
- suspicious cluster
- normal accounts
- edge strength
- hover information
- selected account state

When a node is selected, show a side panel:

ACCOUNT

A-203

Behavioral Activity

High

Related Accounts

A-117

A-211

A-319

Coordination Score

0.91

Do not label the account as "fraudster" or claim identity attribution.

Use:

"Suspicious behavioral relationship"

and

"Signals consistent with coordinated operation"

***

# COMMUNITY DETECTION

Create a section titled:

"Find the hidden community."

Explain:

"ShadowGram builds a weighted behavioral graph and applies community detection to identify groups that are more strongly connected internally than externally."

Display:

NetworkX

Louvain Community Detection

Show a graph separating into:

Cluster A

Cluster B

Normal Accounts

Suspicious Cluster

Use animated transitions when communities are detected.

***

# WHY ARE THESE ACCOUNTS LINKED?

This should be one of the most prominent sections of the website.

Create a large interactive investigation panel.

Heading:

"Why are these accounts linked?"

Selected accounts:

A-117

A-203

A-211

Show an evidence breakdown.

### Timing

"Repeated actions occurred within short time intervals."

Example:

Δt < 1.4s

### Navigation

"Similar page and action sequences were observed."

Example:

Feed → Search → Profile → Post

### Interaction

"Similar interaction cadence was observed."

Example:

Typing rhythm similarity: 0.87

### Content

"Content embeddings show high semantic similarity."

Example:

Cosine similarity: 0.91

### Environment

"Shared simulated environment characteristics were observed."

Example:

Browser

OS

Timezone

Screen resolution

At the bottom show:

"Evidence converges across 4 behavioral categories."

Use an explainability visualization showing how each signal contributes to the relationship.

***

# TIMELINE

Create a section titled:

"Coordination, over time."

Display a horizontal or vertical event timeline.

Example:

10:42:13

A-117 opens feed

↓

10:42:14

A-203 opens feed

↓

10:42:15

A-211 opens feed

↓

10:42:17

All three navigate to the same profile

↓

10:42:20

Similar content interaction detected

Use animated timeline markers.

Add filters:

All

Timing

Navigation

Interaction

Content

***

# ANOMALY DETECTION

Create a section titled:

"Spot unusual behavior."

Explain:

"Isolation Forest identifies unusual individual behavior patterns. An anomaly is a signal for investigation, not proof of fraud."

Show a simple two-dimensional visualization:

Normal Behavior

Suspicious / Unusual Behavior

Use:

scikit-learn

Isolation Forest

Include an informational label:

"Anomaly ≠ Fraud"

This distinction should be visually clear.

***

# DETECTION PIPELINE

Create a horizontal animated pipeline:

SIMULATED USERS

↓

BROWSER TELEMETRY

↓

FEATURE ENGINEERING

↓

BEHAVIORAL VECTORS

↓

SIMILARITY

↓

BEHAVIORAL GRAPH

↓

LOUVAIN

↓

SHADOW CLUSTER

↓

WHY / EVIDENCE

↓

PREVENTION

Each stage should be represented by a compact glass card.

Animate a small data pulse travelling through the pipeline.

***

# PREVENTION / CONTAINMENT

Create a section titled:

"Detection is only the beginning."

Show three response cards.

### Additional Verification

"Request additional verification for suspicious activity."

### Restrict Suspicious Links

"Temporarily limit interactions between highly connected suspicious accounts."

### Human Review

"Send explainable evidence to an analyst for investigation."

Add an optional future capability:

"WebAuthn / FIDO2"

with label:

"Future containment layer"

Do not automatically ban or permanently identify users based only on behavioral similarity.

***

# LIVE DETECTION DEMO

Create an interactive demo section titled:

"Run a ShadowGram simulation."

Include controls:

"Start Simulation"

"Generate Normal Accounts"

"Generate Coordinated Accounts"

"Analyze"

"Reset"

When "Start Simulation" is clicked:

1. Generate normal accounts.
2. Generate a small group of coordinated accounts.
3. Simulate browser interactions.
4. Generate telemetry.
5. Extract behavioral features.
6. Calculate similarity.
7. Create graph edges.
8. Detect communities.
9. Highlight the suspicious cluster.
10. Populate the WHY panel.

Show a status indicator:

"Telemetry Collection"

then:

"Feature Extraction"

then:

"Similarity Analysis"

then:

"Graph Construction"

then:

"Community Detection"

then:

"Evidence Generated"

Finally:

"Shadow Cluster Detected"

Use smooth animated transitions between states.

***

# DASHBOARD STATISTICS

Create a compact analytics bar containing:

Accounts Analyzed

100

Behavioral Relationships

248

Shadow Clusters

3

Evidence Signals

5

Use these as demo values only.

Do not present them as real-world benchmark results.

***

# DATA FLOW VISUALIZATION

Create a technical architecture section titled:

"How ShadowGram works."

Show:

Browser

↓

JavaScript Telemetry

↓

POST /telemetry

↓

FastAPI

↓

Feature Engineering

↓

Python ML Layer

↓

Sentence Transformers

↓

Cosine Similarity

↓

NetworkX

↓

Louvain

↓

Next.js Dashboard

Use glowing animated connection lines.

Add a small label:

"Local / Offline Prototype"

***

# FOOTER

Footer should contain:

SHADOWGRAM

"Behavioral Graph Intelligence"

Navigation:

Overview

Detection

ShadowGraph

Evidence

Technology

Footer text:

"Prototype for coordinated behavior detection and explainable fraud analysis."

Add:

"Built for HackAthena 2.0"

Do not include fake company logos or fake customer names.

***

# LIQUID GLASS UTILITY

Use the following liquid-glass style throughout cards, panels, buttons, and floating elements:

```css
.liquid-glass {
  background: rgba(255, 255, 255, 0.01);
  background-blend-mode: luminosity;
  backdrop-filter: blur(8px);
  border: none;
  box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.1);
  position: relative;
  overflow: hidden;
}

.liquid-glass::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: 1.4px;
  background: linear-gradient(
    180deg,
    rgba(255,255,255,0.45) 0%,
    rgba(255,255,255,0.15) 20%,
    rgba(255,255,255,0) 40%,
    rgba(255,255,255,0) 60%,
    rgba(255,255,255,0.15) 80%,
    rgba(255,255,255,0.45) 100%
  );
  -webkit-mask:
    linear-gradient(#fff 0 0) content-box,
    linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  pointer-events: none;
}
```

***

# MOTION & INTERACTION

Use subtle premium animations.

Do not over-animate.

Use:

Framer Motion where appropriate.

Animations:

- graph nodes gently pulse
- graph edges appear progressively
- data particles travel along edges
- cards fade and slide upward on scroll
- numbers count up
- evidence bars animate from zero
- cluster detection highlights nodes
- timeline events appear sequentially
- CTA buttons have subtle hover movement
- navigation transitions smoothly
- sections use smooth scroll

All animations should respect:

prefers-reduced-motion

***

# RESPONSIVE DESIGN

Desktop:

Large graph visualizations.

Large typography.

Multi-column layouts.

Tablet:

Reduce graph size and typography.

Mobile:

Stack all cards vertically.

Navigation collapses into a mobile menu.

Graph remains interactive but scales down.

Hero headline becomes approximately:

text-[64px]

Ensure no horizontal overflow.

***

# TECHNICAL STACK

Frontend:

Next.js

React

Tailwind CSS

JavaScript / TypeScript

React-Force-Graph

Framer Motion

Backend-ready architecture:

FastAPI

Python

REST API

WebSocket-ready telemetry connection

ML:

scikit-learn

Isolation Forest

Sentence Transformers

all-MiniLM-L6-v2

Cosine Similarity

Graph:

NetworkX

Louvain Community Detection

Data:

Synthetic behavioral data

JSON / CSV / optional SQLite

The frontend should be structured so the simulated data can later be replaced by real FastAPI API responses without redesigning the interface.

***

# IMPORTANT PRODUCT FRAMING

ShadowGram is a behavioral coordination detection prototype.

Do NOT describe an account as definitively belonging to a particular person.

Do NOT claim that behavioral similarity proves fraud.

Use language such as:

"Suspicious behavioral relationship"

"Signals consistent with coordinated operation"

"Candidate shadow cluster"

"Evidence for analyst review"

"Behavioral similarity"

"Coordination signal"

"Anomaly requiring investigation"

The interface should emphasize:

"Collect behavior → turn it into numbers → compare accounts → build relationships → find groups → explain evidence → contain suspicious activity."

The final experience should feel like a **real-time behavioral intelligence command center**, while remaining understandable to a hackathon judge seeing the system for the first time.
