# engineering-flow-charts

Useful decision making charts for engineering.

## LLM Reasoning Benchmark Tier Flowcharts

Quickly compare open-weight LLMs for reasoning by reviewing results across multiple publicly published benchmarks. Single benchmarks are insufficient: small models score 0 on advanced tests, large models saturate simple ones. This flowchart creates **tiers of models** and identifies **benchmarks that separate tiers** with clear pass/fail boundaries.

📄 **[View Full Analysis → llm-reasoning-benchmarks.md](llm-reasoning-benchmarks.md)**

### Tier Summary

| Tier | Params | MMLU | GSM8K | BBH | MATH | GPQA | Example Models |
|------|--------|------|-------|-----|------|------|----------------|
| **T0: Tiny** | < 3B | 40–55% | 20–40% | 0–10% | 0–5% | ~25% | Qwen3-0.5B, Phi-3-mini, Gemma-2-2B |
| **T1: Small** | 3–7B | 55–65% | 50–75% | 20–35% | 10–20% | 30–35% | Qwen3-1.5B/4B, Mistral-7B, Llama-3.2-3B |
| **T2: Medium** | 8–30B | 65–75% | 80–90% | 40–55% | 25–40% | 35–45% | Qwen3-8B/14B, Llama-3.1-8B, Nemotron-3-8B |
| **T3: Large** | 30–70B | 75–85% | 90–95% | 55–70% | 40–55% | 40–50% | Qwen3-32B, Llama-3.1-70B, Nemotron-3-Ultra |
| **T4: Frontier** | 70B+ | 85–92% | 95–98% | 70–85% | 55–75% | 50–92% (85–92% for frontier models) | **Open:** Qwen3-72B, Llama-3.1-405B<br/>**Closed:** GPT-4o, Claude 3.5 Sonnet |

### Key Insight

The **BBH (BIG-Bench Hard)** benchmark shows the largest tier separation—it's the best single discriminator for CoT reasoning capability. GSM8K saturates early (T2+ all >80%). GPQA compresses at the top (T2–T4 only 15–30pp spread).

> The Qwen 3.x family (0.5B → 72B) spans all five tiers, making it an ideal internal "ruler" for calibrating thresholds.

---

## Analog vs Digital DSP Decision Flowchart

A decision tree for choosing between analog and digital signal processing implementations. Based on [DSP Guide Chapter 21](https://www.dspguide.com/ch21/1.htm), it evaluates requirements in sequence: dynamic range (>10,000), real-time frequency range (>10,000), latency (<1ns), ripple (<1%), roll-off/stopband needs, and linear phase. Digital wins for precision, linear phase, and steep roll-offs; analog wins for extreme dynamic range, ultra-low latency, and high-frequency real-time processing.

📄 **[View Flowchart → analog-v-digital-dsp.md](analog-v-digital-dsp.md)**

---

*More engineering decision charts coming soon...*