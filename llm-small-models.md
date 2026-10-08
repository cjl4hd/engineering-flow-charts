# Small LLM Benchmarks — Reported Results

Reported benchmark results for open-weight models under **50B total parameters**.

- **Vendor-reported values only** — a cell is filled only when the model card
  or technical report publishes that exact number. No estimates.
- **"—" means not reported** by the vendor for that benchmark (not zero).
- Source of truth: [`data/models.csv`](data/models.csv), which also carries
  per-model source links and protocol notes (avg@k, eval sweep, harness
  caveats). Regenerate with `python generate_table.py`.

<!-- GENERATED-SMALL-TABLES-START -->
<p style="font-weight: bold; margin: 14px 0 4px;">Math &amp; reasoning</p>
<table style="border-collapse: collapse; width: 100%; font-family: monospace; font-size: 12px;">
  <thead>
    <tr style="background-color: #f0f0f0;">
      <th style="padding: 6px 8px; text-align: left; border-bottom: 2px solid #666;">Model</th>
      <th style="padding: 6px 8px; text-align: left; border-bottom: 2px solid #666;">Org</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">Params</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">Ctx</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">Released</th>
      <th style="padding: 6px 8px; text-align: left; border-bottom: 2px solid #666;">License</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">GPQA-D</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">AIME25</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">AIME26</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">HMMT Feb25</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">HMMT Feb26/Nov25</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">HLE</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">MATH-500</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">AMC23</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">AIME24</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">CritPt</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">BBEH</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">KOR-Bench</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">MMLU-Pro</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">MMLU-Redux</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">BBH</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen3.5-0.8B">Qwen3.5-0.8B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">0.8B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-09</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="background-color: #ffcccc; padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">11.9</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">42.3</td>
      <td style="background-color: #ffe6cc; padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">59.5</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen3.5-2B">Qwen3.5-2B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-03</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="background-color: #cce6ff; padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">51.6</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">22.9</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">19.6</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">66.5</td>
      <td style="background-color: #ccffcc; padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">79.6</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen3.5-4B">Qwen3.5-4B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">4B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-03</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="background-color: #cce6ff; padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">76.2</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">74.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">76.8</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">79.1</td>
      <td style="background-color: #cce6ff; padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">88.8</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen3-4B-Thinking-2507">Qwen3-4B-Thinking-2507</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">4B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2025-07</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="background-color: #cce6ff; padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">65.8</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">57.5</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">69.6</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">74.0</td>
      <td style="background-color: #cce6ff; padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">86.1</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/IFM/K2-Horizon-7B">K2-Horizon-7B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">IFM</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">7B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">512K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-09</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="background-color: #cce6ff; padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">77.1</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">84.2</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">73.3</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">18.6</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/MiniMaxAI/SynLogic-7B">SynLogic-7B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">MiniMaxAI</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">7B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2025-06</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">MIT</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">71.8</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">55.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">10.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">8.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">48.1</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="background-color: #ccffcc; padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">66.5</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct">Qwen2.5-Coder-7B-Instruct</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">7.6B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">128K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2024-09</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">83.9</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B">MiMo-V2.6-Distill-Qwen-9B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Xiaomi MiMo</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">9B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-09</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">MIT</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">18.3</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen3.5-9B">Qwen3.5-9B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">9B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-03</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="background-color: #cce6ff; padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">81.7</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">83.2</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">82.9</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">82.5</td>
      <td style="background-color: #cce6ff; padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">91.1</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/ornith-ai/Ornith-1.5-9B">Ornith-1.5-9B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">ornith-ai</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">9B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-08</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">MIT</td>
      <td style="background-color: #cce6ff; padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">86.4</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">20.2</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen3.6-27B">Qwen3.6-27B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">27B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-04</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="background-color: #cce6ff; padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">87.8</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">94.1</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">93.8</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">84.3</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">24.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">86.2</td>
      <td style="background-color: #cce6ff; padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">93.5</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/poolside/Laguna-XS-2.1">Laguna-XS-2.1</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">poolside</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">33B (3B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-08</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">OpenMDW-1.1</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B">Ornith-1.5-35B-A3B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">ornith-ai</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">35B (3B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-08</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">MIT</td>
      <td style="background-color: #cce6ff; padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">89.2</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">25.6</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Kwaipilot/KAT-Coder-V2.5-Dev">KAT-Coder-V2.5-Dev</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Kwaipilot</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">35B (3B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-07</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen3.6-35B-A3B">Qwen3.6-35B-A3B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">35B (3B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-04</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="background-color: #cce6ff; padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">86.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">92.7</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">90.7</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">83.6</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">21.4</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">85.2</td>
      <td style="background-color: #cce6ff; padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">93.3</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4">Qwen3.6-35B-A3B-NVFP4</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">nvidia</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">35B (3B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-05</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="background-color: #cce6ff; padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">84.8</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">88.8</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">85.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/unsloth/Qwen3.6-35B-A3B-NVFP4">Qwen3.6-35B-A3B-NVFP4</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">unsloth</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">35B (3B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-04</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="background-color: #cce6ff; padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">86.74</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">92.29</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">85.85</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/unsloth/Qwen3.6-35B-A3B-NVFP4-Fast">Qwen3.6-35B-A3B-NVFP4-Fast</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">unsloth</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">35B (3B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-07</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="background-color: #cce6ff; padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">87.75</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">91.67</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">85.58</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/IFM/K2-Horizon-MoVA-36B-A4B">K2-Horizon-MoVA-36B-A4B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">IFM</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">36B (4B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">512K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-09</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="background-color: #cce6ff; padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">80.8</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">25.2</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2.1</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
  </tbody>
</table>
<p style="font-weight: bold; margin: 14px 0 4px;">Instruction &amp; long context</p>
<table style="border-collapse: collapse; width: 100%; font-family: monospace; font-size: 12px;">
  <thead>
    <tr style="background-color: #f0f0f0;">
      <th style="padding: 6px 8px; text-align: left; border-bottom: 2px solid #666;">Model</th>
      <th style="padding: 6px 8px; text-align: left; border-bottom: 2px solid #666;">Org</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">Params</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">Ctx</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">Released</th>
      <th style="padding: 6px 8px; text-align: left; border-bottom: 2px solid #666;">License</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">IFEval</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">IFBench</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">MultiChallenge</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">AA-LCR</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">LongBench-v2</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">MMMLU</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen3.5-0.8B">Qwen3.5-0.8B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">0.8B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-09</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">44.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">21.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">18.9</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">4.7</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">26.1</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">44.3</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen3.5-2B">Qwen3.5-2B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-03</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">78.6</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">41.3</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">33.7</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">25.6</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">38.7</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">63.1</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen3.5-4B">Qwen3.5-4B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">4B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-03</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">89.8</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">59.2</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">49.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">57.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">50.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">76.1</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen3-4B-Thinking-2507">Qwen3-4B-Thinking-2507</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">4B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2025-07</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">87.4</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">50.4</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">41.7</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">32.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">42.8</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">70.8</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/IFM/K2-Horizon-7B">K2-Horizon-7B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">IFM</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">7B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">512K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-09</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">88.7</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">68.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/MiniMaxAI/SynLogic-7B">SynLogic-7B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">MiniMaxAI</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">7B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2025-06</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">MIT</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct">Qwen2.5-Coder-7B-Instruct</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">7.6B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">128K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2024-09</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B">MiMo-V2.6-Distill-Qwen-9B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Xiaomi MiMo</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">9B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-09</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">MIT</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen3.5-9B">Qwen3.5-9B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">9B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-03</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">91.5</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">64.5</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">54.5</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">63.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">55.2</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">81.2</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/ornith-ai/Ornith-1.5-9B">Ornith-1.5-9B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">ornith-ai</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">9B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-08</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">MIT</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen3.6-27B">Qwen3.6-27B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">27B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-04</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/poolside/Laguna-XS-2.1">Laguna-XS-2.1</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">poolside</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">33B (3B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-08</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">OpenMDW-1.1</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B">Ornith-1.5-35B-A3B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">ornith-ai</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">35B (3B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-08</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">MIT</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Kwaipilot/KAT-Coder-V2.5-Dev">KAT-Coder-V2.5-Dev</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Kwaipilot</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">35B (3B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-07</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen3.6-35B-A3B">Qwen3.6-35B-A3B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">35B (3B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-04</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4">Qwen3.6-35B-A3B-NVFP4</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">nvidia</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">35B (3B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-05</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">62.8</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">62.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/unsloth/Qwen3.6-35B-A3B-NVFP4">Qwen3.6-35B-A3B-NVFP4</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">unsloth</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">35B (3B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-04</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/unsloth/Qwen3.6-35B-A3B-NVFP4-Fast">Qwen3.6-35B-A3B-NVFP4-Fast</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">unsloth</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">35B (3B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-07</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/IFM/K2-Horizon-MoVA-36B-A4B">K2-Horizon-MoVA-36B-A4B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">IFM</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">36B (4B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">512K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-09</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">66.3</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
  </tbody>
</table>
<p style="font-weight: bold; margin: 14px 0 4px;">Code generation &amp; review</p>
<table style="border-collapse: collapse; width: 100%; font-family: monospace; font-size: 12px;">
  <thead>
    <tr style="background-color: #f0f0f0;">
      <th style="padding: 6px 8px; text-align: left; border-bottom: 2px solid #666;">Model</th>
      <th style="padding: 6px 8px; text-align: left; border-bottom: 2px solid #666;">Org</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">Params</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">Ctx</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">Released</th>
      <th style="padding: 6px 8px; text-align: left; border-bottom: 2px solid #666;">License</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">SWE-bench Verified</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">SWE-bench Pro</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">SWE-bench Multi</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">NL2Repo</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">SWE-Atlas QnA</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">LiveCodeBench</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">HumanEval</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">OJBench</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">SciCode</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">PinchBench</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">KAT-Code-Bench</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">DeepSWE</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">Frontier-Bench</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen3.5-0.8B">Qwen3.5-0.8B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">0.8B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-09</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen3.5-2B">Qwen3.5-2B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-03</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen3.5-4B">Qwen3.5-4B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">4B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-03</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">55.8</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">24.1</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen3-4B-Thinking-2507">Qwen3-4B-Thinking-2507</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">4B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2025-07</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/IFM/K2-Horizon-7B">K2-Horizon-7B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">IFM</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">7B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">512K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-09</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">69.2</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">71.5</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">29.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">31.6</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/MiniMaxAI/SynLogic-7B">SynLogic-7B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">MiniMaxAI</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">7B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2025-06</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">MIT</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct">Qwen2.5-Coder-7B-Instruct</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">7.6B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">128K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2024-09</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">37.6</td>
      <td style="background-color: #cce6ff; padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">88.4</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B">MiMo-V2.6-Distill-Qwen-9B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Xiaomi MiMo</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">9B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-09</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">MIT</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">61.1</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">44.6</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen3.5-9B">Qwen3.5-9B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">9B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-03</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">65.6</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">29.2</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/ornith-ai/Ornith-1.5-9B">Ornith-1.5-9B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">ornith-ai</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">9B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-08</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">MIT</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">70.6</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">47.5</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">54.4</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">32.4</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">20.6</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen3.6-27B">Qwen3.6-27B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">27B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-04</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">77.2</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">53.5</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">71.3</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">36.2</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">83.9</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/poolside/Laguna-XS-2.1">Laguna-XS-2.1</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">poolside</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">33B (3B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-08</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">OpenMDW-1.1</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">70.9</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">47.6</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">63.1</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B">Ornith-1.5-35B-A3B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">ornith-ai</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">35B (3B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-08</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">MIT</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">79</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">59.6</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">71.4</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">46.2</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">39.8</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">22</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">5.1</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Kwaipilot/KAT-Coder-V2.5-Dev">KAT-Coder-V2.5-Dev</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Kwaipilot</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">35B (3B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-07</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">69.40</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">45.96</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">63.00</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">44.20</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">93.43</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">46.21</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen3.6-35B-A3B">Qwen3.6-35B-A3B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">35B (3B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-04</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">73.4</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">49.5</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">67.2</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">29.4</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">80.4</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4">Qwen3.6-35B-A3B-NVFP4</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">nvidia</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">35B (3B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-05</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">40.6</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/unsloth/Qwen3.6-35B-A3B-NVFP4">Qwen3.6-35B-A3B-NVFP4</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">unsloth</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">35B (3B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-04</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/unsloth/Qwen3.6-35B-A3B-NVFP4-Fast">Qwen3.6-35B-A3B-NVFP4-Fast</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">unsloth</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">35B (3B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-07</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/IFM/K2-Horizon-MoVA-36B-A4B">K2-Horizon-MoVA-36B-A4B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">IFM</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">36B (4B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">512K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-09</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">38.9</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
  </tbody>
</table>
<p style="font-weight: bold; margin: 14px 0 4px;">Agentic tool use &amp; search</p>
<table style="border-collapse: collapse; width: 100%; font-family: monospace; font-size: 12px;">
  <thead>
    <tr style="background-color: #f0f0f0;">
      <th style="padding: 6px 8px; text-align: left; border-bottom: 2px solid #666;">Model</th>
      <th style="padding: 6px 8px; text-align: left; border-bottom: 2px solid #666;">Org</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">Params</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">Ctx</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">Released</th>
      <th style="padding: 6px 8px; text-align: left; border-bottom: 2px solid #666;">License</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">Terminal-Bench</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">MCP-Atlas</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">BFCL-V4</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">TAU2-Bench</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">tau3-Banking</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">Toolathlon</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">ClawEval</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">WideSearch</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">BrowseComp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen3.5-0.8B">Qwen3.5-0.8B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">0.8B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-09</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">25.3</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">11.6</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen3.5-2B">Qwen3.5-2B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-03</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">43.6</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">48.8</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen3.5-4B">Qwen3.5-4B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">4B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-03</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">50.3</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">79.9</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen3-4B-Thinking-2507">Qwen3-4B-Thinking-2507</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">4B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2025-07</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">39.9</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">43.2</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/IFM/K2-Horizon-7B">K2-Horizon-7B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">IFM</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">7B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">512K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-09</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">39.7</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">62.3</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">25.8</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">59.0</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/MiniMaxAI/SynLogic-7B">SynLogic-7B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">MiniMaxAI</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">7B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2025-06</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">MIT</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct">Qwen2.5-Coder-7B-Instruct</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">7.6B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">128K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2024-09</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B">MiMo-V2.6-Distill-Qwen-9B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Xiaomi MiMo</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">9B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-09</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">MIT</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">37.1</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">35.2</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">30.3</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen3.5-9B">Qwen3.5-9B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">9B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-03</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">66.1</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">79.1</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/ornith-ai/Ornith-1.5-9B">Ornith-1.5-9B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">ornith-ai</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">9B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-08</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">MIT</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">46.2</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">54.2</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">41.2</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">66.5</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">59.5</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">56.4</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen3.6-27B">Qwen3.6-27B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">27B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-04</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">59.3</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">72.4</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/poolside/Laguna-XS-2.1">Laguna-XS-2.1</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">poolside</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">33B (3B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-08</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">OpenMDW-1.1</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">37.5</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B">Ornith-1.5-35B-A3B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">ornith-ai</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">35B (3B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-08</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">MIT</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">67.8</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">70.2</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">48.7</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">72.5</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">67.8</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">67.6</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Kwaipilot/KAT-Coder-V2.5-Dev">KAT-Coder-V2.5-Dev</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Kwaipilot</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">35B (3B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-07</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">41.02</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/Qwen/Qwen3.6-35B-A3B">Qwen3.6-35B-A3B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Qwen</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">35B (3B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-04</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">51.5</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">62.8</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">26.9</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">68.7</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">60.1</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4">Qwen3.6-35B-A3B-NVFP4</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">nvidia</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">35B (3B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-05</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">94.7</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/unsloth/Qwen3.6-35B-A3B-NVFP4">Qwen3.6-35B-A3B-NVFP4</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">unsloth</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">35B (3B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-04</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/unsloth/Qwen3.6-35B-A3B-NVFP4-Fast">Qwen3.6-35B-A3B-NVFP4-Fast</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">unsloth</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">35B (3B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">262K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-07</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/IFM/K2-Horizon-MoVA-36B-A4B">K2-Horizon-MoVA-36B-A4B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">IFM</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">36B (4B act.)</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">512K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-09</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">58.6</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">26.8</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
    </tr>
  </tbody>
</table>
<p style="font-size: 11px; color: #666; margin-top: 8px;">
All values are vendor-reported exactly as published (no estimates). "—" = not reported for that benchmark. Metric/protocol details in <a href="data/models.csv">data/models.csv</a>. Sources: 
Qwen3.5-0.8B (Qwen model card (thinking mode, via Qwen3.5-2B table)); Qwen3.5-2B (Qwen model card (thinking mode)); Qwen3.5-4B (Qwen model card (thinking mode)); Qwen3-4B-Thinking-2507 (Qwen model card (via Qwen3.5-2B comparison column)); K2-Horizon-7B (IFM model card (full eval sweep + FTPO table)); SynLogic-7B (MiniMaxAI model card); Qwen2.5-Coder-7B-Instruct (Qwen2.5-Coder technical report (arXiv 2409.12186)); MiMo-V2.6-Distill-Qwen-9B (MiMo-V2.6 technical report (model card)); Qwen3.5-9B (Qwen model card (thinking mode)); Ornith-1.5-9B (Ornith model card (avg over 5 independent runs)); Qwen3.6-27B (Qwen model card); Laguna-XS-2.1 (poolside model card); Ornith-1.5-35B-A3B (Ornith model card (avg over 5 independent runs)); KAT-Coder-V2.5-Dev (Kwaipilot model card); Qwen3.6-35B-A3B (Qwen model card); Qwen3.6-35B-A3B-NVFP4 (NVIDIA model card (quant accuracy table)); Qwen3.6-35B-A3B-NVFP4 (Unsloth model card (NVFP4 accuracy benchmarks)); Qwen3.6-35B-A3B-NVFP4-Fast (Unsloth model card (NVFP4 accuracy benchmarks)); K2-Horizon-MoVA-36B-A4B (IFM model card)
.</p>
<!-- GENERATED-SMALL-TABLES-END -->
