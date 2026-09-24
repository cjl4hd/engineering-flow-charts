"""Tests for generate_table.py tier classification and HTML generation.

Tier bands mirror the Tier Thresholds table in llm-reasoning-benchmarks.md
(soft boundaries: adjacent tiers share edge values).
"""

import re
from pathlib import Path

import pytest

import generate_table as gt

PROJECT_ROOT = Path(__file__).resolve().parent


# ---------------------------------------------------------------------------
# Basic classification
# ---------------------------------------------------------------------------

class TestGetTier:
    @pytest.mark.parametrize('benchmark, score, expected', [
        # Mid-band scores
        ('MMLU', '40%+', 'T0'),
        ('MMLU', '60%+', 'T1'),
        ('MMLU', '68%+', 'T2'),
        ('MMLU', '78%+', 'T3'),
        ('MMLU', '88.7%', 'T4'),
        ('GSM8K', '25%+', 'T0'),
        ('GSM8K', '50%+', 'T1'),
        ('GSM8K', '82%+', 'T2'),
        ('GSM8K', '92%+', 'T3'),
        ('GSM8K', '96%', 'T4'),
        ('BBH', '5%+', 'T0'),
        ('BBH', '20%+', 'T1'),
        ('BBH', '42%+', 'T2'),
        ('BBH', '58%+', 'T3'),
        ('BBH', '80%', 'T4'),
        ('MATH', '2%+', 'T0'),
        ('MATH', '12%+', 'T1'),
        ('MATH', '30%+', 'T2'),
        ('MATH', '45%+', 'T3'),
        ('MATH', '62%+', 'T4'),
        ('GPQA', '25%+', 'T0'),
        ('GPQA', '30%+', 'T1'),
        ('GPQA', '38%+', 'T2'),
        ('GPQA', '45%+', 'T3'),
        ('GPQA', '58%', 'T4'),
        ('HumanEval', '10%+', 'T0'),
        ('HumanEval', '20%+', 'T1'),
        ('HumanEval', '45%+', 'T2'),
        ('HumanEval', '60%+', 'T3'),
        ('HumanEval', '80%+', 'T4'),
    ])
    def test_mid_band(self, benchmark, score, expected):
        assert gt.get_tier(benchmark, score) == expected

    def test_unparseable_returns_none(self):
        assert gt.get_tier('MMLU', 'n/a') is None
        assert gt.get_tier('MMLU', '') is None
        assert gt.get_tier('MMLU', None) is None

    def test_unknown_benchmark_returns_none(self):
        assert gt.get_tier('ARC', '50%') is None

    def test_out_of_range_returns_none(self):
        assert gt.get_tier('MMLU', '101%') is None
        assert gt.get_tier('HumanEval', '-1%') is None


# ---------------------------------------------------------------------------
# Boundary scores (documented soft boundaries overlap between adjacent tiers)
# ---------------------------------------------------------------------------

class TestBoundaries:
    def test_boundary_resolves_to_higher_tier_without_row(self):
        # MMLU 55 is documented as both T0 and T1 -> defaults to T1
        assert gt.get_tier('MMLU', '55%+') == 'T1'
        assert gt.get_tier('MMLU', '85%') == 'T4'

    def test_row_coherent_boundary_takes_modal_tier(self):
        # Qwen3-1.7B is a documented T1 representative: its MMLU 55%+ boundary
        # must resolve to T1 to match its row, not down to T0.
        row = {'MMLU': '55%+', 'GSM8K': '50%+', 'BBH': '20%+',
               'MATH': '12%+', 'GPQA': '30%+', 'HumanEval': '20%+'}
        assert gt._modal_tier(row) == 'T1'
        assert gt.get_tier('MMLU', row['MMLU'], row) == 'T1'

    def test_gap_scores_take_nearest_band(self):
        # Doc assigns no tier to BBH 10-20 or MATH 5-10; nearest band wins.
        # BBH 12 is closer to T0 (0-10) than T1 (20-35) -> T0, which matches
        # Gemma-2-2B being a documented T0 representative.
        assert gt.get_tier('BBH', '12%+') == 'T0'
        assert gt.get_tier('MATH', '6%+') == 'T0'
        # GSM8K 45 sits equidistant between T0 (40) and T1 (50) -> resolves up
        assert gt.get_tier('GSM8K', '45%+') == 'T1'
        # Super-frontier scores above the doc's descriptive ceilings
        assert gt.get_tier('MMLU', '93.3%') == 'T4'
        assert gt.get_tier('HumanEval', '88%') == 'T4'

    def test_gap_scores_are_row_coherent(self):
        row = {'MMLU': '50%+', 'GSM8K': '40%+', 'BBH': '12%+',
               'MATH': '6%+', 'GPQA': '28%+', 'HumanEval': '15%+'}
        assert gt._modal_tier(row) == 'T0'
        assert gt.get_tier('BBH', '12%+', row) == 'T0'
        assert gt.get_tier('MATH', '6%+', row) == 'T0'

    def test_gsm8k_90_boundary_matches_row_tier(self):
        # DeepSeek-V2's row is T3; GSM8K 90%+ must not regress to T2
        row = {'MMLU': '78%+', 'GSM8K': '90%+', 'BBH': '55%+',
               'MATH': '42%+', 'GPQA': '44%+', 'HumanEval': '58%+'}
        assert gt.get_tier('GSM8K', row['GSM8K'], row) == 'T3'
        # Same score without row context resolves upward
        assert gt.get_tier('GSM8K', '90%+') == 'T3'

    def test_bbh_55_boundary_matches_row_tier(self):
        # DeepSeek-V2's row is T3; BBH 55%+ must not regress to T2
        row = {'MMLU': '78%+', 'GSM8K': '90%+', 'BBH': '55%+',
               'MATH': '42%+', 'GPQA': '44%+', 'HumanEval': '58%+'}
        assert gt.get_tier('BBH', row['BBH'], row) == 'T3'

    def test_modal_tier_straightforward(self):
        row = {'MMLU': '68%+', 'GSM8K': '82%+', 'BBH': '42%+',
               'MATH': '30%+', 'GPQA': '38%+', 'HumanEval': '45%+'}
        assert gt._modal_tier(row) == 'T2'


# ---------------------------------------------------------------------------
# Whole-table classification: every score must land in a documented tier
# ---------------------------------------------------------------------------

class TestModelRows:
    def models(self):
        return [r for r in gt.models if any(r[2:-1])]

    @pytest.mark.parametrize('model_row', [r[0] for r in gt.models if any(r[2:-1])])
    def test_every_score_maps_to_a_tier(self, model_row):
        row = next(r for r in gt.models if r[0] == model_row)
        scores = dict(zip(gt.benchmarks, row[2:-1]))
        for benchmark, score in scores.items():
            tier = gt.get_tier(benchmark, score, scores)
            assert tier is not None, f'{model_row} {benchmark}={score} has no tier'
            assert tier in gt.TIER_COLORS

    def test_gpqa_frontier_scores_are_t4(self):
        # The regression that started this: 86.0% and 89.2% were colored T3
        for name, expected in [('Qwen3.6-35B-A3B', 'T4'), ('Qwen3.8-27B', 'T4')]:
            row = next(r for r in gt.models if r[0] == name)
            scores = dict(zip(gt.benchmarks, row[2:-1]))
            assert gt.get_tier('GPQA', scores['GPQA'], scores) == expected

    def test_tier_progression_by_family_size(self):
        """Within the Qwen 3.x ruler, tiers should not regress as models grow."""
        order = ['Qwen3-0.6B', 'Qwen3-1.7B', 'Qwen3-4B', 'Qwen3-8B', 'Qwen3-14B']
        tier_idx = {t: i for i, t in enumerate(gt.TIERS)}
        prev = {b: -1 for b in gt.benchmarks}
        for name in order:
            row = next(r for r in gt.models if r[0] == name)
            scores = dict(zip(gt.benchmarks, row[2:-1]))
            for b in gt.benchmarks:
                cur = tier_idx[gt.get_tier(b, scores[b], scores)]
                assert cur >= prev[b], f'{name} {b} regressed vs smaller model'
                prev[b] = cur


# ---------------------------------------------------------------------------
# HTML generation
# ---------------------------------------------------------------------------

class TestHtml:
    def test_gpqa_frontier_cells_are_blue(self):
        html = gt.build_html()
        for score in ('86.0%', '89.2%'):
            m = re.search(r'<td style="background-color: (#[0-9a-f]+);[^"]*">' + re.escape(score) + '</td>', html)
            assert m, f'cell {score} not found'
            assert m.group(1) == gt.TIER_COLORS['T4']

    def test_row_consistent_colors_in_html(self):
        # DeepSeek-V2's GSM8K/BBH (90%/55%) should be T3 green, not T2 yellow
        html = gt.build_html()
        v2 = html.split('DeepSeek-V2</td>')[1].split('</tr>')[0]
        gsm8k = re.search(r'<td style="background-color: (#[0-9a-f]+);[^"]*">90%\+</td>', v2)
        bbh = re.search(r'<td style="background-color: (#[0-9a-f]+);[^"]*">55%\+</td>', v2)
        assert gsm8k and gsm8k.group(1) == gt.TIER_COLORS['T3']
        assert bbh and bbh.group(1) == gt.TIER_COLORS['T3']

    def test_legend_present(self):
        html = gt.build_html()
        for tier, color in gt.TIER_COLORS.items():
            assert color in html
            assert gt.TIER_NAMES[tier] in html

    def test_written_file_matches_build(self):
        out = PROJECT_ROOT / 'table_html.txt'
        assert out.exists(), 'run generate_table.py to produce table_html.txt'
        assert out.read_text() == gt.build_html()


# ---------------------------------------------------------------------------
# Doc sync: thresholds in this script must match the markdown doc
# ---------------------------------------------------------------------------

class TestDocSync:
    def test_md_documents_updated_gpqa_t4_range(self):
        md = (PROJECT_ROOT / 'llm-reasoning-benchmarks.md').read_text()
        # T4 GPQA band extended to cover frontier scores (85-92%)
        assert re.search(r'\|\s*\*\*T4:.*\|\s*50–92%', md), (
            'llm-reasoning-benchmarks.md T4 GPQA band should cover up to 92%'
        )

    def test_markdown_embed_is_current(self):
        md = (PROJECT_ROOT / 'llm-reasoning-benchmarks.md').read_text()
        start, end = '<!-- GENERATED-TABLE-START -->', '<!-- GENERATED-TABLE-END -->'
        if start not in md or end not in md:
            pytest.skip('embed markers not present in markdown')
        embedded = md.split(start, 1)[1].split(end, 1)[0].strip()
        assert embedded == gt.build_html().strip()
