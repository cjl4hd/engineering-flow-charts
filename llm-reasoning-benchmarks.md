# LLM Reasoning Benchmark Tier Flowcharts

Quickly compare open-weight LLMs for reasoning by reviewing results across multiple publicly published benchmarks. Single benchmarks are insufficient: small models score 0 on advanced tests, large models saturate simple ones. This flowchart creates **tiers of models** and identifies **benchmarks that separate tiers** with clear pass/fail boundaries.

---

## Benchmark Comparison Table

| Benchmark | Full Name | Focus | Difficulty | Questions | Key Skill Tested |
|-----------|-----------|-------|------------|-----------|------------------|
| **MMLU** | Massive Multitask Language Understanding | 57 subjects (STEM, humanities, social sciences) | Medium | ~16K | Broad knowledge + basic reasoning |
| **GSM8K** | Grade School Math 8K | Multi-step arithmetic word problems | Easy–Medium | 8.5K | Basic multi-step reasoning |
| **BBH** | BIG-Bench Hard | 23 challenging BIG-Bench tasks | Hard | ~6.5K | Chain-of-thought multi-step reasoning |
| **MATH** | Mathematics Dataset | Competition-level math (precalc, algebra, geometry, etc.) | Hard | 12.5K | Advanced mathematical problem solving |
| **GPQA** | Graduate-Level Google-Proof Q&A | PhD-level physics, chemistry, biology | Very Hard | 448 | Expert scientific reasoning |
| **HumanEval** | Hand-Written Evaluation Set | Code generation (Python) | Medium–Hard | 164 | Programming reasoning |
| **ARC** | AI2 Reasoning Challenge | Grade-school science questions | Easy–Medium | 7.8K | Basic scientific reasoning |
| **HellaSwag** | Commonsense Reasoning | Sentence completion with commonsense | Easy | 70K | World knowledge / commonsense |

---

## Tier Thresholds (Soft Boundaries)

*Thresholds are approximate based on public leaderboard data (Open LLM Leaderboard, Papers With Code, HF Spaces). Models may fall in different tiers on different benchmarks—this is expected and informative.*

| Tier | Param Range | MMLU | GSM8K | BBH | MATH | GPQA | HumanEval | Representative Models |
|------|-------------|------|-------|-----|------|------|-----------|----------------------|
| **T0: Tiny** | < 3B | 40–55% | 20–40% | 0–10% | 0–5% | ~25% (random) | 5–15% | Qwen3-0.5B, Phi-3-mini-3.8B, Gemma-2-2B, Llama-3.2-1B |
| **T1: Small** | 3–7B | 55–65% | 50–75% | 20–35% | 10–20% | 30–35% | 20–35% | Qwen3-1.5B, Qwen3-4B, Mistral-7B, Llama-3.2-3B, Phi-3.5-mini |
| **T2: Medium** | 8–30B | 65–75% | 80–90% | 40–55% | 25–40% | 35–45% | 40–55% | Qwen3-8B, Qwen3-14B, Llama-3.1-8B, Nemotron-3-8B, Gemma-2-9B |
| **T3: Large** | 30–70B | 75–85% | 90–95% | 55–70% | 40–55% | 40–50% | 55–70% | Qwen3-32B, Llama-3.1-70B, Nemotron-3-Ultra, Qwen2.5-72B |
| **T4: Frontier** | 70B+ / Closed | 85–92% | 95–98% | 70–85% | 55–75% | 50–65% | 70–85% | **Open:** Qwen3-72B, Llama-3.1-405B<br/>**Closed:** GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro |

> **Note on Qwen 3.x:** The Qwen 3 family spans all tiers (0.5B → 72B), making it an ideal "ruler" for calibrating these thresholds.

---

## Diagram 1: Decision Tree Flowchart (Diamond Gates)

Progressive gating: each benchmark acts as a filter. Soft thresholds with overlap zones noted in parentheses.

```mermaid
flowchart TD
    %% ===== LEFT COLUMN: Decision Gates =====
    Start([Start: New Model\nRun MMLU First])
    
    MMLU{MMLU Score}
    GSM8K{GSM8K Score}
    BBH{BBH Score}
    MATH{MATH Score}
    GPQA{GPQA Score}
    
    Overlap1{{Overlap Zone:\nStrong basics,\nweak reasoning}}
    Overlap2{{Overlap Zone:\nGood CoT,\nlimited math}}
    Overlap3{{Overlap Zone:\nStrong math,\nGPQA boundary}}
    
    %% ===== RIGHT COLUMN: Tier Results (aligned vertically) =====
    subgraph TIERS["Model Tiers"]
        direction TB
        T0[T0: Tiny\n<3B params\nQwen3-0.5B, Phi-3-mini, Gemma-2-2B]
        T1[T1: Small\n3–7B params\nQwen3-1.5B/4B, Mistral-7B, Llama-3.2-3B]
        T2[T2: Medium\n8–30B params\nQwen3-8B/14B, Llama-3.1-8B, Nemotron-3-8B]
        T3[T3: Large\n30–70B params\nQwen3-32B, Llama-3.1-70B, Nemotron-3-Ultra]
        T4open["T4: Frontier (Open)\n70B+ params\nQwen3-72B, Llama-3.1-405B"]
        T4closed["T4: Frontier (Closed)\nGPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro"]
    end
    
    %% ===== EDGES =====
    Start --> MMLU
    
    MMLU -- "< 50%" --> T0
    MMLU -- "50–65%" --> GSM8K
    MMLU -- "65–75%" --> MATH
    MMLU -- "75–85%" --> T3
    MMLU -- "> 85%" --> T4closed
    
    GSM8K -- "< 50%" --> Overlap1
    GSM8K -- "50–75%" --> BBH
    GSM8K -- "> 75% (rare)" --> Overlap1
    
    Overlap1 --> T1
    
    BBH -- "< 30%" --> T1
    BBH -- "30–55%" --> T2
    BBH -- "> 55% (rare)" --> Overlap2
    
    Overlap2 --> T2
    
    MATH -- "< 25%" --> Overlap2
    MATH -- "25–55%" --> GPQA
    MATH -- "> 55% (rare)" --> Overlap3
    
    Overlap3 --> T3
    
    GPQA -- "< 40%" --> T3
    GPQA -- "40–65%" --> T4open
    GPQA -- "> 65%" --> T4closed
    
    %% ===== STYLING =====
    classDef tier0 fill:#ffcccc,stroke:#cc0000,stroke-width:2px,color:#333;
    classDef tier1 fill:#ffe6cc,stroke:#cc6600,stroke-width:2px,color:#333;
    classDef tier2 fill:#ffffcc,stroke:#ccaa00,stroke-width:2px,color:#333;
    classDef tier3 fill:#ccffcc,stroke:#00aa00,stroke-width:2px,color:#333;
    classDef tier4 fill:#cce6ff,stroke:#0066cc,stroke-width:2px,color:#333;
    classDef gate fill:#f0f0f0,stroke:#666,stroke-width:1.5px,stroke-dasharray: 5 5,color:#333;
    classDef overlap fill:#fff0f0,stroke:#cc3333,stroke-width:1.5px,stroke-dasharray: 3 3,color:#333;
    classDef start fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#333;
    classDef tierBox fill:none,stroke:none;
    
    class T0 tier0;
    class T1 tier1;
    class T2 tier2;
    class T3 tier3;
    class T4open,T4closed tier4;
    class MMLU,GSM8K,BBH,MATH,GPQA gate;
    class Overlap1,Overlap2,Overlap3 overlap;
    class Start start;
    class TIERS tierBox;
```

**How to read:** Enter at **MMLU**. Follow the branch matching the model's score. Overlap zones (dashed pink) indicate models that pass one gate but fail the next—these are the most informative for understanding specific capability gaps.

---

## Diagram 2: Swimlane Diagram (Horizontal Tier Bands)

Each tier is a horizontal band. Benchmarks form vertical "gates" showing where each tier typically falls. Gaps between bands = benchmark discriminative power.

```mermaid
flowchart LR
    %% Benchmark columns (vertical gates)
    subgraph B_MMLU["MMLU\n(Broad Knowledge)"]
        direction TB
        M0[T0: 40–55%]
        M1[T1: 55–65%]
        M2[T2: 65–75%]
        M3[T3: 75–85%]
        M4[T4: 85–92%]
    end
    
    subgraph B_GSM8K["GSM8K\n(Basic Reasoning)"]
        direction TB
        G0[T0: 20–40%]
        G1[T1: 50–75%]
        G2[T2: 80–90%]
        G3[T3: 90–95%]
        G4[T4: 95–98%]
    end
    
    subgraph B_BBH["BBH\n(CoT Reasoning)"]
        direction TB
        B0[T0: 0–10%]
        B1[T1: 20–35%]
        B2[T2: 40–55%]
        B3[T3: 55–70%]
        B4[T4: 70–85%]
    end
    
    subgraph B_MATH["MATH\n(Advanced Math)"]
        direction TB
        H0[T0: 0–5%]
        H1[T1: 10–20%]
        H2[T2: 25–40%]
        H3[T3: 40–55%]
        H4[T4: 55–75%]
    end
    
    subgraph B_GPQA["GPQA\n(Expert Science)"]
        direction TB
        P0[T0: ~25%]
        P1[T1: 30–35%]
        P2[T2: 35–45%]
        P3[T3: 40–50%]
        P4[T4: 50–65%]
    end
    
    %% Invisible edges to align columns
    M0 -.-> G0 -.-> B0 -.-> H0 -.-> P0
    M1 -.-> G1 -.-> B1 -.-> H1 -.-> P1
    M2 -.-> G2 -.-> B2 -.-> H2 -.-> P2
    M3 -.-> G3 -.-> B3 -.-> H3 -.-> P3
    M4 -.-> G4 -.-> B4 -.-> H4 -.-> P4
    
    %% Styling
    classDef tier0 fill:#ffcccc,stroke:#cc0000;
    classDef tier1 fill:#ffe6cc,stroke:#cc6600;
    classDef tier2 fill:#ffffcc,stroke:#ccaa00;
    classDef tier3 fill:#ccffcc,stroke:#00aa00;
    classDef tier4 fill:#cce6ff,stroke:#0066cc;
    classDef bench fill:#f5f5f5,stroke:#999,stroke-dasharray: 5 5;
    
    class M0,G0,B0,H0,P0 tier0;
    class M1,G1,B1,H1,P1 tier1;
    class M2,G2,B2,H2,P2 tier2;
    class M3,G3,B3,H3,P3 tier3;
    class M4,G4,B4,H4,P4 tier4;
    class B_MMLU,B_GSM8K,B_BBH,B_MATH,B_GPQA bench;
```

**Key insight:** The **BBH column** shows the largest tier separation (T0→T1: 20–35pp gap, T1→T2: 15–20pp). **GSM8K** saturates early (T2+ all >80%). **GPQA** compresses at top (T2–T4 only 15–30pp spread).

---

## Diagram 3: Sankey-Style Model Flow

Models flow left-to-right through benchmark gates, landing in tier buckets. Qwen 3.x family (all sizes) traces through as a calibration ruler.

```mermaid
flowchart LR
    %% Source
    AllModels[("All Models\nEnter Here")]
    
    %% Gates
    GateMMLU[[MMLU Gate\n(50% / 65% / 75% / 85%)]]
    GateGSM8K[[GSM8K Gate\n(50% / 75%)]]
    GateBBH[[BBH Gate\n(30% / 55%)]]
    GateMATH[[MATH Gate\n(25% / 55%)]]
    GateGPQA[[GPQA Gate\n(40% / 65%)]]
    
    %% Tier Buckets
    BucketT0["T0: Tiny\nQwen3-0.5B\nPhi-3-mini-3.8B\nGemma-2-2B\nLlama-3.2-1B"]
    BucketT1["T1: Small\nQwen3-1.5B\nQwen3-4B\nMistral-7B\nLlama-3.2-3B\nPhi-3.5-mini"]
    BucketT2["T2: Medium\nQwen3-8B\nQwen3-14B\nLlama-3.1-8B\nNemotron-3-8B\nGemma-2-9B"]
    BucketT3["T3: Large\nQwen3-32B\nLlama-3.1-70B\nNemotron-3-Ultra"]
    BucketT4open["T4: Frontier (Open)\nQwen3-72B\nLlama-3.1-405B"]
    BucketT4closed["T4: Frontier (Closed)\nGPT-4o\nClaude 3.5 Sonnet\nGemini 1.5 Pro"]
    
    %% Flow paths
    AllModels --> GateMMLU
    
    GateMMLU -- "Fail <50%" --> BucketT0
    GateMMLU -- "50–65%" --> GateGSM8K
    GateMMLU -- "65–75%" --> GateMATH
    GateMMLU -- "75–85%" --> BucketT3
    GateMMLU -- ">85%" --> BucketT4closed
    
    GateGSM8K -- "Fail <50%" --> BucketT1
    GateGSM8K -- "50–75%" --> GateBBH
    
    GateBBH -- "Fail <30%" --> BucketT1
    GateBBH -- "30–55%" --> BucketT2
    GateBBH -- ">55%" --> GateMATH
    
    GateMATH -- "Fail <25%" --> BucketT2
    GateMATH -- "25–55%" --> GateGPQA
    GateMATH -- ">55%" --> BucketT3
    
    GateGPQA -- "Fail <40%" --> BucketT3
    GateGPQA -- "40–65%" --> BucketT4open
    GateGPQA -- ">65%" --> BucketT4closed
    
    %% Qwen 3.x calibration trace (highlighted path)
    QwenTrace[["Qwen 3.x Family\n(Calibration Ruler)"]]
    QwenTrace -.-> GateMMLU
    QwenTrace -.-> GateGSM8K
    QwenTrace -.-> GateBBH
    QwenTrace -.-> GateMATH
    QwenTrace -.-> GateGPQA
    QwenTrace -.-> BucketT0
    QwenTrace -.-> BucketT1
    QwenTrace -.-> BucketT2
    QwenTrace -.-> BucketT3
    QwenTrace -.-> BucketT4open
    
    %% Styling
    classDef source fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef gate fill:#fff3e0,stroke:#e65100,stroke-width:2px;
    classDef bucket0 fill:#ffcccc,stroke:#cc0000,stroke-width:2px;
    classDef bucket1 fill:#ffe6cc,stroke:#cc6600,stroke-width:2px;
    classDef bucket2 fill:#ffffcc,stroke:#ccaa00,stroke-width:2px;
    classDef bucket3 fill:#ccffcc,stroke:#00aa00,stroke-width:2px;
    classDef bucket4 fill:#cce6ff,stroke:#0066cc,stroke-width:2px;
    classDef trace fill:#f3e5f5,stroke:#7b1fa2,stroke-width:3px,stroke-dasharray: 5 5;
    
    class AllModels source;
    class GateMMLU,GateGSM8K,GateBBH,GateMATH,GateGPQA gate;
    class BucketT0 bucket0;
    class BucketT1 bucket1;
    class BucketT2 bucket2;
    class BucketT3 bucket3;
    class BucketT4open,BucketT4closed bucket4;
    class QwenTrace trace;
```

**Reading the flow:** The **Qwen 3.x trace** (purple dashed) shows how a single model family spans all tiers—use it to calibrate where new models land. Models hitting BucketT1 at BBH gate have "basic reasoning but weak CoT"; models reaching BucketT3 at MATH gate have "strong math but not expert science."

---

## Usage Guide

### For Evaluating a New Model
1. Run **MMLU** first (cheap, broad signal)
2. Follow the decision tree (Diagram 1) to know which benchmark to run next
3. Stop when the model fails a gate—that's its tier ceiling
4. Check Diagram 2 to see which benchmarks best discriminate at that tier
5. Use Diagram 3 to find similar models for comparison

### Interpreting Overlap Zones
| Zone | Meaning | Action |
|------|---------|--------|
| MMLU 50–65% + GSM8K <50% | Memorizes facts, can't reason | Don't trust on multi-step tasks |
| GSM8K 50–75% + BBH <30% | Good arithmetic, weak CoT | Fine for simple math, fails complex reasoning |
| BBH 30–55% + MATH <25% | Reasoning works, math knowledge gaps | Supplement with tool use / calculator |
| MATH 25–55% + GPQA <40% | Strong STEM, not expert-level | Good for coding/engineering, not research |

### Updating Thresholds
Thresholds are soft. When new models are released:
1. Run the 5 core benchmarks (MMLU, GSM8K, BBH, MATH, GPQA)
2. Plot results on Diagram 2 swimlanes
3. Adjust gate thresholds in Diagram 1/3 if tier boundaries shift
4. The Qwen 3.x family provides a stable internal ruler

---

## Data Sources & References

- **Open LLM Leaderboard** (Hugging Face H4): https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard
- **LMSYS Chatbot Arena** (Elo ratings): https://huggingface.co/spaces/lmarena-ai/arena-leaderboard
- **Papers With Code** (benchmark SOTA): https://paperswithcode.com/
- **EleutherAI LM Evaluation Harness**: https://github.com/EleutherAI/lm-evaluation-harness
- **Original benchmark papers**: MMLU (Hendrycks et al. 2021), GSM8K (Cobbe et al. 2021), BBH (Suzgun et al. 2022), MATH (Hendrycks et al. 2021), GPQA (Rein et al. 2023)

---

*Generated for quick LLM reasoning comparison. Thresholds approximate—verify with current leaderboard data before making deployment decisions.*