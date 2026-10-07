# Small LLM Benchmarks — Reported Results

Reported benchmark results for open-weight models under **50B total parameters**.

- **Vendor-reported values only** — a cell is filled only when the model card
  or technical report publishes that exact number. No estimates.
- **"—" means not reported** by the vendor for that benchmark (not zero).
- Source of truth: [`data/models.csv`](data/models.csv), which also carries
  per-model source links and protocol notes (avg@k, eval sweep, harness
  caveats). Regenerate with `python generate_table.py`.

<!-- GENERATED-SMALL-TABLES-START -->
<p style="font-weight: bold; margin: 14px 0 4px;">Reasoning &amp; knowledge</p>
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
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">IFEval</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">AIME25</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">AIME26</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">HMMT25</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">HMMT26</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">HLE</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">AA-LCR</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/IFM/K2-Horizon-7B">K2-Horizon-7B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">IFM</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">7B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">512K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-09</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="background-color: #cce6ff; padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">77.1</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">88.7</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">91.9</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">90.1</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">84.2</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">73.3</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">18.6</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">68.0</td>
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
    </tr>
  </tbody>
</table>
<p style="font-weight: bold; margin: 14px 0 4px;">Coding &amp; agentic</p>
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
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">SciCode</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">Terminal-Bench</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">BrowseComp</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">tau3-Banking</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">Toolathlon</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">OfficeQA</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">JobBench</th>
      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">AutomationBench</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;"><a href="https://huggingface.co/IFM/K2-Horizon-7B">K2-Horizon-7B</a></td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">IFM</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">7B</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">512K</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">2026-09</td>
      <td style="padding: 4px 8px; text-align: left; border-bottom: 1px solid #eee;">Apache-2.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">70.6</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">31.6</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">39.1</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">59.0</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">25.8</td>
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
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">37.1</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">—</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">35.2</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">19.5</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">18.3</td>
      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">30.3</td>
    </tr>
  </tbody>
</table>
<p style="font-size: 11px; color: #666; margin-top: 8px;">
All values are vendor-reported exactly as published (no estimates). "—" = not reported for that benchmark. Metric/protocol details in <a href="data/models.csv">data/models.csv</a>. Sources: 
K2-Horizon-7B (IFM model card); MiMo-V2.6-Distill-Qwen-9B (MiMo-V2.6 technical report (model card))
.</p>
<!-- GENERATED-SMALL-TABLES-END -->
