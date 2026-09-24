# engineering-flow-charts

Useful decision making charts for engineering.

## LLM Reasoning Benchmark Tier Flowcharts

Quickly compare open-weight LLMs for reasoning by reviewing results across multiple publicly published benchmarks. Single benchmarks are insufficient: small models score 0 on advanced tests, large models saturate simple ones. This flowchart creates **tiers of models** and identifies **benchmarks that separate tiers** with clear pass/fail boundaries.

📄 **[View Full Analysis → llm-reasoning-benchmarks.md](llm-reasoning-benchmarks.md)**

### What's Inside

| Diagram | Purpose | Best For |
|---------|---------|----------|
| **Decision Tree** (Diagram 1) | Progressive gating: MMLU → GSM8K → BBH → MATH → GPQA | Evaluating a new model step-by-step; finding its tier ceiling |
| **Swimlane** (Diagram 2) | Horizontal tier bands (T0–T4) with benchmark score ranges | Seeing which benchmarks best discriminate at each tier level |
| **Sankey Flow** (Diagram 3) | Models flowing through gates into tier buckets; Qwen 3.x as calibration ruler | Comparing model families; understanding capability gaps |

### Tier Summary

| Tier | Params | MMLU | GSM8K | BBH | MATH | GPQA | Example Models |
|------|--------|------|-------|-----|------|------|----------------|
| **T0: Tiny** | < 3B | 40–55% | 20–40% | 0–10% | 0–5% | ~25% | Qwen3-0.5B, Phi-3-mini, Gemma-2-2B |
| **T1: Small** | 3–7B | 55–65% | 50–75% | 20–35% | 10–20% | 30–35% | Qwen3-1.5B/4B, Mistral-7B, Llama-3.2-3B |
| **T2: Medium** | 8–30B | 65–75% | 80–90% | 40–55% | 25–40% | 35–45% | Qwen3-8B/14B, Llama-3.1-8B, Nemotron-3-8B |
| **T3: Large** | 30–70B | 75–85% | 90–95% | 55–70% | 40–55% | 40–50% | Qwen3-32B, Llama-3.1-70B, Nemotron-3-Ultra |
| **T4: Frontier** | 70B+ | 85–92% | 95–98% | 70–85% | 55–75% | 50–65% | **Open:** Qwen3-72B, Llama-3.1-405B<br/>**Closed:** GPT-4o, Claude 3.5 Sonnet |

### Key Insight

The **BBH (BIG-Bench Hard)** benchmark shows the largest tier separation—it's the best single discriminator for CoT reasoning capability. GSM8K saturates early (T2+ all >80%). GPQA compresses at the top (T2–T4 only 15–30pp spread).

> The Qwen 3.x family (0.5B → 72B) spans all five tiers, making it an ideal internal "ruler" for calibrating thresholds.

---

## Other Charts

*More engineering decision charts coming soon...*