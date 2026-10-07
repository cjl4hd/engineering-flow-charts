#!/usr/bin/env python3
"""Generate HTML table with tier-colored cells for the reference table.

Tier bands mirror the "Tier Thresholds" table in llm-reasoning-benchmarks.md.
Scores are classified by the *documented* ranges (lower <= score <= upper);
boundary scores resolve to the tier closest to the model's modal tier so each
row keeps a coherent classification (see get_tier).
"""

import csv
from collections import Counter
from pathlib import Path

# Tier color mapping (matches Diagram 1 classDefs in llm-reasoning-benchmarks.md)
TIER_COLORS = {
    'T0': '#ffcccc',  # red
    'T1': '#ffe6cc',  # orange
    'T2': '#ffffcc',  # yellow
    'T3': '#ccffcc',  # green
    'T4': '#cce6ff',  # blue
}

TIER_NAMES = {'T0': 'Entry', 'T1': 'Basic', 'T2': 'Competent', 'T3': 'Advanced', 'T4': 'Expert'}

TIERS = ['T0', 'T1', 'T2', 'T3', 'T4']

# Documented tier ranges: (lower, upper) inclusive, mirroring the Tier
# Thresholds table. Adjacent tiers share boundary values by design ("soft
# boundaries"): e.g. MMLU 55 is listed as both T0 and T1. T4's upper bound is
# 100 (the doc's descriptive ceiling, e.g. "85-92%", is not a hard cap) so
# super-frontier scores (HumanEval 88, MMLU 93.3) still classify as Expert.
# Gaps between bands (e.g. BBH 10-20) resolve to the nearest band.
THRESHOLDS = {
    'MMLU': {
        'T0': (0, 55),
        'T1': (55, 65),
        'T2': (65, 75),
        'T3': (75, 85),
        'T4': (85, 92),
    },
    'GSM8K': {
        'T0': (0, 40),
        'T1': (50, 75),
        'T2': (80, 90),
        'T3': (90, 95),
        'T4': (95, 100),
    },
    'BBH': {
        'T0': (0, 10),
        'T1': (20, 35),
        'T2': (40, 55),
        'T3': (55, 70),
        'T4': (70, 100),
    },
    'MATH': {
        'T0': (0, 5),
        'T1': (10, 20),
        'T2': (25, 40),
        'T3': (40, 55),
        'T4': (55, 100),
    },
    'GPQA': {
        'T0': (0, 30),
        'T1': (30, 35),
        'T2': (35, 45),
        'T3': (40, 50),
        'T4': (50, 100),
    },
    'HumanEval': {
        'T0': (0, 15),
        'T1': (20, 35),
        'T2': (40, 55),
        'T3': (55, 70),
        'T4': (70, 100),
    },
}


def parse_score(value):
    """Parse a score cell like '88.7%' or '80%+' to a float, else None."""
    try:
        return float(str(value).replace('%', '').replace('+', '').strip())
    except (TypeError, ValueError):
        return None


def matching_tiers(benchmark, val):
    """All documented tiers whose range contains val (boundaries overlap)."""
    return [t for t in TIERS
            if THRESHOLDS[benchmark][t][0] <= val <= THRESHOLDS[benchmark][t][1]]


def _modal_tier(row):
    """Most common tier across a model row (ties average toward the middle)."""
    tiers = [t for b, v in row.items() if (t := get_tier(b, v))]
    if not tiers:
        return None
    counts = Counter(tiers)
    best = max(counts.values())
    tied = [t for t, c in counts.items() if c == best]
    if len(tied) == 1:
        return tied[0]
    avg = sum(TIERS.index(t) for t in tied) / len(tied)
    return TIERS[round(avg)]


def get_tier(benchmark, value, row=None):
    """Determine tier for a benchmark score using the documented bands.

    A boundary score (e.g. MMLU 55) matches two tiers. With no row context it
    resolves to the higher tier; with a row it resolves to the candidate tier
    closest to the row's modal tier, keeping each model row coherent
    (e.g. DeepSeek-V2's GSM8K 90 -> T3, matching the rest of its row).
    A score in a gap between bands (the doc leaves e.g. BBH 10-20 unassigned)
    takes the nearest band; ties resolve like boundaries. Scores outside
    0-100 are unclassifiable.
    """
    if benchmark not in THRESHOLDS:
        return None
    val = parse_score(value)
    if val is None or not (0 <= val <= 100):
        return None
    candidates = matching_tiers(benchmark, val)
    if not candidates:
        def band_dist(tier):
            lo, hi = THRESHOLDS[benchmark][tier]
            return max(lo - val, val - hi, 0)
        nearest = min(band_dist(t) for t in TIERS)
        candidates = [t for t in TIERS if band_dist(t) == nearest]
    if len(candidates) == 1:
        return candidates[0]
    if row:
        modal = _modal_tier(row)
        if modal:
            return min(candidates, key=lambda t: abs(TIERS.index(t) - TIERS.index(modal)))
    return candidates[-1]


def get_cell_html(benchmark, value, row=None):
    """Generate HTML td with tier-colored background."""
    tier = get_tier(benchmark, value, row)
    color = TIER_COLORS.get(tier, '#ffffff')
    return f'<td style="background-color: {color}; padding: 4px 8px; text-align: center;">{value}</td>'


# Model data
models = [
    # (Model, Params, MMLU, GSM8K, BBH, MATH, GPQA, HumanEval, Source)
    ('Qwen Family', '', '', '', '', '', '', '', ''),
    ('Qwen3-0.6B', '0.6B', '40%+', '25%+', '5%+', '2%+', '25%+', '10%+', 'HF Leaderboard'),
    ('Qwen3-1.7B', '1.7B', '55%+', '50%+', '20%+', '12%+', '30%+', '20%+', 'HF Leaderboard'),
    ('Qwen3-4B', '4B', '60%+', '65%+', '28%+', '18%+', '33%+', '28%+', 'HF Leaderboard'),
    ('Qwen3-8B', '8B', '68%+', '82%+', '42%+', '30%+', '38%+', '45%+', 'HF Leaderboard'),
    ('Qwen3-14B', '14B', '72%+', '87%+', '48%+', '35%+', '42%+', '50%+', 'HF Leaderboard'),
    ('Qwen3-32B', '32B', '78%+', '92%+', '58%+', '45%+', '45%+', '60%+', 'HF Leaderboard'),
    ('Qwen3-30B-A3B', '30B (MoE)', '80%+', '93%+', '60%+', '48%+', '47%+', '62%+', 'HF Leaderboard'),
    ('Qwen3.6-35B-A3B', '35B (MoE)', '93.3%', '95%+', '70%+', '55%+', '86.0%', '75%+', 'Qwen Blog'),
    ('Qwen3.8-27B', '27B', '82%+', '94%+', '65%+', '50%+', '89.2%', '70%+', 'HF Model Card'),
    ('Qwen3.8-Max', '2.4T (95B act)', '88%+', '96%+', '75%+', '60%+', '90%+', '80%+', 'Qwen Blog'),
    ('Qwen3-235B-A22B', '235B (MoE)', '90%+', '97%+', '80%+', '65%+', '85%+', '85%+', 'HF Leaderboard'),
    ('Llama Family', '', '', '', '', '', '', '', ''),
    ('Llama-3.1-8B', '8B', '68%+', '80%+', '40%+', '28%+', '36%+', '42%+', 'HF Leaderboard'),
    ('Llama-3.1-70B', '70B', '82%+', '94%+', '62%+', '48%+', '46%+', '65%+', 'HF Leaderboard'),
    ('Llama-3.1-405B', '405B', '88%+', '96%+', '72%+', '58%+', '55%+', '80%+', 'HF Leaderboard'),
    ('Llama-3.2-1B', '1B', '45%+', '30%+', '8%+', '3%+', '25%+', '12%+', 'HF Leaderboard'),
    ('Llama-3.2-3B', '3B', '58%+', '55%+', '22%+', '14%+', '32%+', '25%+', 'HF Leaderboard'),
    ('Nemotron Family', '', '', '', '', '', '', '', ''),
    ('Nemotron-3-8B', '8B', '70%+', '85%+', '45%+', '32%+', '40%+', '48%+', 'HF Leaderboard'),
    ('Nemotron-3-Ultra', '53B', '80%+', '93%+', '58%+', '45%+', '45%+', '60%+', 'HF Leaderboard'),
    ('Phi Family', '', '', '', '', '', '', '', ''),
    ('Phi-3-mini-3.8B', '3.8B', '60%+', '62%+', '25%+', '16%+', '34%+', '28%+', 'HF Leaderboard'),
    ('Phi-3.5-mini', '3.8B', '62%+', '65%+', '28%+', '18%+', '35%+', '30%+', 'HF Leaderboard'),
    ('Gemma Family', '', '', '', '', '', '', '', ''),
    ('Gemma-2-2B', '2B', '50%+', '40%+', '12%+', '6%+', '28%+', '15%+', 'HF Leaderboard'),
    ('Gemma-2-9B', '9B', '68%+', '82%+', '42%+', '30%+', '38%+', '45%+', 'HF Leaderboard'),
    ('Mistral Family', '', '', '', '', '', '', '', ''),
    ('Mistral-7B', '7B', '62%+', '68%+', '30%+', '20%+', '35%+', '32%+', 'HF Leaderboard'),
    ('GLM Family', '', '', '', '', '', '', '', ''),
    ('GLM-4-9B', '9B', '72%+', '85%+', '48%+', '35%+', '42%+', '50%+', 'HF Leaderboard'),
    ('GLM-4-32B', '32B', '80%+', '92%+', '58%+', '45%+', '45%+', '60%+', 'HF Leaderboard'),
    ('DeepSeek Family', '', '', '', '', '', '', '', ''),
    ('DeepSeek-V2', '236B (MoE)', '78%+', '90%+', '55%+', '42%+', '44%+', '58%+', 'HF Leaderboard'),
    ('DeepSeek-V3', '671B (MoE)', '88%+', '96%+', '72%+', '58%+', '55%+', '82%+', 'DeepSeek Blog'),
    ('DeepSeek-R1', '671B (MoE)', '89%+', '97%+', '75%+', '62%+', '58%+', '85%+', 'DeepSeek Blog'),
    ('Closed-Source', '', '', '', '', '', '', '', ''),
    ('GPT-4o*', '—', '88.7%', '96%', '80%', '60%', '58%', '85%', 'OpenAI'),
    ('GPT-4o-mini*', '—', '82%+', '92%+', '55%+', '40%+', '42%+', '70%+', 'OpenAI'),
    ('Claude 3.5 Sonnet*', '—', '89%', '96%', '82%', '62%', '60%', '88%', 'Anthropic'),
    ('Claude 3.5 Haiku*', '—', '85%+', '93%+', '60%+', '45%+', '48%+', '75%+', 'Anthropic'),
    ('Gemini 1.5 Pro*', '—', '88%', '95%', '78%', '58%', '55%', '82%', 'Google'),
    ('Gemini 1.5 Flash*', '—', '82%+', '91%+', '58%+', '42%+', '44%+', '72%+', 'Google'),
]

benchmarks = ['MMLU', 'GSM8K', 'BBH', 'MATH', 'GPQA', 'HumanEval']


def build_html():
    """Build the tier-colored table HTML (without writing any file)."""
    html_lines = []
    html_lines.append('<table style="border-collapse: collapse; width: 100%; font-family: monospace; font-size: 12px;">')
    html_lines.append('  <thead>')
    html_lines.append('    <tr style="background-color: #f0f0f0;">')
    html_lines.append('      <th style="padding: 6px 8px; text-align: left; border-bottom: 2px solid #666;">Model</th>')
    html_lines.append('      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">Params</th>')
    for b in benchmarks:
        html_lines.append(f'      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">{b}</th>')
    html_lines.append('      <th style="padding: 6px 8px; text-align: left; border-bottom: 2px solid #666;">Source</th>')
    html_lines.append('    </tr>')
    html_lines.append('  </thead>')
    html_lines.append('  <tbody>')

    for row in models:
        model, params, *scores, source = row

        if not any(scores):  # Family header row
            html_lines.append('    <tr style="background-color: #f5f5f5;">')
            html_lines.append(f'      <td colspan="9" style="padding: 6px 8px; font-weight: bold; border-top: 1px solid #ddd; border-bottom: 1px solid #ddd;">{model}</td>')
            html_lines.append('    </tr>')
            continue

        row_scores = dict(zip(benchmarks, scores))
        html_lines.append('    <tr>')
        html_lines.append(f'      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;">{model}</td>')
        html_lines.append(f'      <td style="padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;">{params}</td>')

        for benchmark in benchmarks:
            html_lines.append(get_cell_html(benchmark, row_scores[benchmark], row_scores))

        html_lines.append(f'      <td style="padding: 4px 8px; border-bottom: 1px solid #eee;">{source}</td>')
        html_lines.append('    </tr>')

    html_lines.append('  </tbody>')
    html_lines.append('</table>')
    html_lines.append('')
    html_lines.append('<p style="font-size: 11px; color: #666; margin-top: 8px;">')
    html_lines.append('  <strong>Color legend:</strong> ')
    for tier, color in TIER_COLORS.items():
        html_lines.append(f'  <span style="display: inline-block; width: 12px; height: 12px; background-color: {color}; border: 1px solid #999; margin-right: 4px; vertical-align: middle;"></span>{TIER_NAMES[tier]}: {tier}')
        if tier != 'T4':
            html_lines.append(' |')
    html_lines.append('  <br>')
    html_lines.append('  <strong>Scores with + are estimates</strong>. <strong>* = Closed-source (API only)</strong>.')
    html_lines.append('</p>')
    return '\n'.join(html_lines)


def update_markdown_embed(html):
    """Refresh the table embedded between markers in llm-reasoning-benchmarks.md."""
    md_path = Path(__file__).resolve().parent / 'llm-reasoning-benchmarks.md'
    if not md_path.exists():
        return
    text = md_path.read_text()
    start, end = '<!-- GENERATED-TABLE-START -->', '<!-- GENERATED-TABLE-END -->'
    if start in text and end in text:
        head, rest = text.split(start, 1)
        _, tail = rest.split(end, 1)
        md_path.write_text(f'{head}{start}\n{html}\n{end}{tail}')


# ---------------------------------------------------------------------------
# Small-model reported-benchmarks table (data/models.csv -> llm-small-models.md)
#
# Policy: vendor-reported values only. A cell is filled only when the model's
# card/technical report publishes that exact number; blank = not reported.
# ---------------------------------------------------------------------------

CSV_PATH = Path(__file__).resolve().parent / 'data' / 'models.csv'
SMALL_PAGE_PATH = Path(__file__).resolve().parent / 'llm-small-models.md'
SMALL_START = '<!-- GENERATED-SMALL-TABLES-START -->'
SMALL_END = '<!-- GENERATED-SMALL-TABLES-END -->'

# CSV column -> THRESHOLDS key for legacy benchmarks (tier-colored cells)
TIER_KEY = {'mmlu': 'MMLU', 'gsm8k': 'GSM8K', 'bbh': 'BBH', 'math': 'MATH',
            'gpqa': 'GPQA', 'humaneval': 'HumanEval'}

BENCH_GROUPS = [
    ('Math &amp; reasoning', ['gpqa', 'aime25', 'aime26', 'hmmt25', 'hmmt26', 'hle',
                              'math', 'math500', 'amc23', 'aime24', 'critpt', 'bbeh',
                              'kor_bench', 'mmlu_pro', 'mmlu', 'bbh', 'gsm8k']),
    ('Instruction &amp; long context', ['ifeval', 'ifbench', 'multichallenge',
                                        'aalcr', 'longbench_v2', 'mmmlu']),
    ('Code generation &amp; review', ['swe_verified', 'swe_pro', 'swe_multilingual',
                                      'nl2repo', 'swe_atlas_qna', 'livecodebench',
                                      'humaneval', 'ojbench', 'scicode',
                                      'pinch_bench', 'kat_code_bench', 'deepswe',
                                      'frontier_bench']),
    ('Agentic tool use &amp; search', ['terminal_bench', 'mcp_atlas', 'bfcl_v4',
                                       'tau2_bench', 'tau3_banking', 'toolathlon',
                                       'officeqa', 'jobbench', 'automation_bench',
                                       'claw_eval', 'wide_search', 'browsecomp']),
]

# Flatten all rendered benchmark columns in group order.
BENCH_COLS = [c for _, cols in BENCH_GROUPS for c in cols]

BENCH_LABELS = {
    'gpqa': 'GPQA-D', 'ifeval': 'IFEval', 'aime25': 'AIME25', 'aime26': 'AIME26',
    'hmmt25': 'HMMT Feb25', 'hmmt26': 'HMMT Feb26/Nov25', 'hle': 'HLE', 'aalcr': 'AA-LCR',
    'mmlu_pro': 'MMLU-Pro', 'aime24': 'AIME24', 'livecodebench': 'LiveCodeBench',
    'mmlu': 'MMLU-Redux', 'gsm8k': 'GSM8K', 'bbh': 'BBH', 'math': 'MATH',
    'humaneval': 'HumanEval', 'swe_verified': 'SWE-bench Verified',
    'swe_pro': 'SWE-bench Pro', 'scicode': 'SciCode',
    'terminal_bench': 'Terminal-Bench', 'browsecomp': 'BrowseComp',
    'tau3_banking': 'tau3-Banking', 'toolathlon': 'Toolathlon',
    'math500': 'MATH-500', 'amc23': 'AMC23', 'bbeh': 'BBEH',
    'kor_bench': 'KOR-Bench', 'swe_multilingual': 'SWE-bench Multi',
    'nl2repo': 'NL2Repo', 'swe_atlas_qna': 'SWE-Atlas QnA',
    'deepswe': 'DeepSWE', 'frontier_bench': 'Frontier-Bench',
    'mcp_atlas': 'MCP-Atlas', 'wide_search': 'WideSearch',
    'claw_eval': 'ClawEval', 'bfcl_v4': 'BFCL-V4', 'tau2_bench': 'TAU2-Bench',
    'longbench_v2': 'LongBench-v2', 'ifbench': 'IFBench',
    'multichallenge': 'MultiChallenge', 'ojbench': 'OJBench',
    'mmmlu': 'MMMLU', 'critpt': 'CritPt', 'pinch_bench': 'PinchBench',
    'kat_code_bench': 'KAT-Code-Bench',
}

TD_BASE = 'padding: 4px 8px; text-align: center; border-bottom: 1px solid #eee;'


def load_models_csv(path=CSV_PATH):
    """Load the verified reported-benchmarks data (blank cell = not reported)."""
    with open(path, newline='') as f:
        return [{k: (v.strip() if isinstance(v, str) else '') for k, v in row.items()}
                for row in csv.DictReader(f)]


def _params_label(row):
    total = row.get('params_total_B', '')
    if not total:
        return '—'
    label = f'{total}B'
    if row.get('arch') == 'moe' and row.get('params_active_B'):
        label += f' ({row["params_active_B"]}B act.)'
    return label


def _model_cell(row):
    name, repo = row.get('model', ''), row.get('hf_repo', '')
    if repo:
        return f'<a href="https://huggingface.co/{repo}">{name}</a>'
    return name


def _bench_cell(col, row, legacy_ctx):
    """Benchmark cell; tier-colored only for benchmarks with documented bands."""
    val = row.get(col, '')
    if not val:
        return f'<td style="{TD_BASE}">—</td>'
    bg = ''
    tier_key = TIER_KEY.get(col)
    if tier_key:
        tier = get_tier(tier_key, val, legacy_ctx)
        if tier:
            bg = f'background-color: {TIER_COLORS[tier]}; '
    return f'<td style="{bg}{TD_BASE}">{val}</td>'


def build_small_models_html(rows=None):
    """Build grouped tables from data/models.csv (without writing any file).

    Only rows with at least one reported benchmark cell are rendered, so the
    tables stay as compact as the data allows (CSV bookkeeping rows stay in
    data/models.csv). Rows are sorted by total params ascending. Benchmark
    columns with no data for any shown row are omitted.
    """
    if rows is None:
        rows = load_models_csv()
    rows = [r for r in rows if r.get('include', 'core') != 'excluded']
    rows = [r for r in rows if any(r.get(c) for c in BENCH_COLS)]
    rows.sort(key=lambda r: float(r.get('params_total_B') or 0))

    shown_groups = []
    for title, cols in BENCH_GROUPS:
        shown = [c for c in cols if any(r.get(c) for r in rows)]
        if shown:
            shown_groups.append((title, shown))
    if not shown_groups:
        return '<p>No benchmark data.</p>'

    parts = []
    for title, cols in shown_groups:
        parts.append(f'<p style="font-weight: bold; margin: 14px 0 4px;">{title}</p>')
        parts.append('<table style="border-collapse: collapse; width: 100%; font-family: monospace; font-size: 12px;">')
        parts.append('  <thead>')
        parts.append('    <tr style="background-color: #f0f0f0;">')
        for header, align in [('Model', 'left'), ('Org', 'left'), ('Params', 'center'),
                              ('Ctx', 'center'), ('Released', 'center'), ('License', 'left')]:
            parts.append(f'      <th style="padding: 6px 8px; text-align: {align}; border-bottom: 2px solid #666;">{header}</th>')
        for c in cols:
            parts.append(f'      <th style="padding: 6px 8px; text-align: center; border-bottom: 2px solid #666;">{BENCH_LABELS.get(c, c)}</th>')
        parts.append('    </tr>')
        parts.append('  </thead>')
        parts.append('  <tbody>')

        for row in rows:
            parts.append('    <tr>')
            parts.append(f'      <td style="padding: 4px 8px; font-weight: bold; border-bottom: 1px solid #eee;">{_model_cell(row)}</td>')
            ctx = f"{row['context_k']}K" if row.get('context_k') else '—'
            identity = [
                (row.get('org', '') or '—', 'left'),
                (_params_label(row), 'center'),
                (ctx, 'center'),
                (row.get('released', '') or '—', 'center'),
                (row.get('license', '') or '—', 'left'),
            ]
            for value, align in identity:
                parts.append(f'      <td style="padding: 4px 8px; text-align: {align}; border-bottom: 1px solid #eee;">{value}</td>')
            legacy_ctx = {TIER_KEY[c]: row.get(c, '') for c in TIER_KEY if row.get(c)}
            for c in cols:
                parts.append('      ' + _bench_cell(c, row, legacy_ctx))
            parts.append('    </tr>')

        parts.append('  </tbody>')
        parts.append('</table>')

    parts.append('<p style="font-size: 11px; color: #666; margin-top: 8px;">')
    parts.append('All values are vendor-reported exactly as published (no estimates). '
                 '"—" = not reported for that benchmark. Metric/protocol details in '
                 '<a href="data/models.csv">data/models.csv</a>. Sources: ')
    parts.append('; '.join(f'{r.get("model", "")} ({r.get("source_name", "")})'
                           for r in rows))
    parts.append('.</p>')
    return '\n'.join(parts)


def update_small_models_page(html):
    """Refresh llm-small-models.md between markers, creating the page if needed."""
    if SMALL_PAGE_PATH.exists():
        text = SMALL_PAGE_PATH.read_text()
        if SMALL_START in text and SMALL_END in text:
            head, rest = text.split(SMALL_START, 1)
            _, tail = rest.split(SMALL_END, 1)
            SMALL_PAGE_PATH.write_text(f'{head}{SMALL_START}\n{html}\n{SMALL_END}{tail}')
            return
    intro = (
        '# Small LLM Benchmarks — Reported Results\n'
        '\n'
        'Reported benchmark results for open-weight models under **50B total parameters**.\n'
        '\n'
        '- **Vendor-reported values only** — a cell is filled only when the model card\n'
        '  or technical report publishes that exact number. No estimates.\n'
        '- **"—" means not reported** by the vendor for that benchmark (not zero).\n'
        '- Source of truth: [`data/models.csv`](data/models.csv), which also carries\n'
        '  per-model source links and protocol notes (avg@k, eval sweep, harness\n'
        '  caveats). Regenerate with `python generate_table.py`.\n'
    )
    SMALL_PAGE_PATH.write_text(f'{intro}\n{SMALL_START}\n{html}\n{SMALL_END}\n')


def main():
    html = build_html()
    print(html)
    out_path = Path(__file__).resolve().parent / 'table_html.txt'
    with open(out_path, 'w') as f:
        f.write(html)
    update_markdown_embed(html)

    small_rows = load_models_csv()
    update_small_models_page(build_small_models_html(small_rows))
    print(f'Small-models page: {SMALL_PAGE_PATH.name} ({len(small_rows)} models)')


if __name__ == '__main__':
    main()
