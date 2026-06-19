# BlackRock: One Asset, Two Lenses
### An Investment Thesis & Intrinsic Value Assessment

> **Recommendation: HOLD** · Target **$959** · Price **~$1,050** · ~**8%** above fair value
> Accumulate in the high-$900s, where the two lenses converge.

---

## The Argument

The valuation gap reflects a fundamental disagreement about what BlackRock actually is. The interesting question isn't whether the SOTP says $959 or $987—it's whether BlackRock's ecosystem of segments makes it worth more together than apart. See the full intellectual centerpiece: [**What is BlackRock?**](methodology/what_is_blackrock.md)

---
## Overview

Most BlackRock valuations begin with a single assumption: *BlackRock is an asset manager.*

This project starts with a different question: **what if BlackRock is actually two businesses sharing one ticker?**

Using a segment-level sum-of-the-parts (SOTP) framework, geographic equity risk premia, and cash-flow-based valuation, I value BlackRock under two competing lenses:

- **Rate-Sensitive Asset Manager** — a levered claim on the level of global markets → **~$825/share**
- **Platform Compounder** — an ETF utility fused to a software franchise (Aladdin) and private-market cash flows that don't move one-for-one with equities → **~$959/share**

The resulting valuation gap exceeds **$130 per share**. The objective is not to forecast the next quarter; it is to determine which lens better explains the economics of the business — and whether the market is pricing BlackRock appropriately today.

![One Asset, Two Lenses](charts/lens_comparison.png)

## What makes this different

- **A framework, not a number.** The two-lens construction is the spine of the whole analysis; every valuation conclusion flows from it.
- **Segment-level discounting.** Each business is discounted at its own cost of equity rather than one blended rate on consolidated cash flows.
- **Disclosed judgment.** Every place where analyst judgment overrides mechanical source data is itemized, with magnitude and rationale.
- **Stress-tested against reality.** The thesis incorporates BlackRock's March/June 2026 private-credit redemption gating — the first live test of the "durable, infrastructure-like cash flow" claim the bull case depends on.

## Key findings

1. The **evidence leans toward the platform lens.** In the 2022 drawdown, operating income fell ~13% against a ~19% market decline (elasticity ~0.69×) — not the signature of a plain beta machine.
2. **But the market has gone further than the evidence supports.** At ~$1,050 it prices BlackRock above even the optimistic platform valuation.
3. The **private-credit redemption gates** are a real crack in the durability story the premium is paying for, which is why HPS is carried at normalized through-cycle cash flow, not peak.
4. **Net call: HOLD.** The skew is unfavorable above $1,000 (~+9% to the bull vs. ~−21% to the bear).

## Results

| Lens | Fair value / share | vs. ~$1,050 price |
|---|---|---|
| Rate-Sensitive Asset Manager | $825 | −21% |
| **Platform Compounder (base)** | **$959** | **−8.7%** |
| Market-implied (the third lens) | ~$1,050 | — |

![Sum-of-the-Parts waterfall](charts/valuation_waterfall.png)

![Sensitivity](charts/sensitivity_matrix.png)

## Methodology (short version)

Sum-of-the-parts across four segments — iShares & Public Markets, Aladdin Technology, GIP Infrastructure, HPS Private Credit — each valued by Gordon Growth (`V = FCFE × (1+g) / (Ke − g)`) at its own cost of equity, with corporate adjustments (net debt, co-invest drag, platform overlay) applied last. Discount rates use a geographic-mix-weighted equity risk premium (Damodaran). A relative-valuation cross-check (EV/EBIT, EV/Sales vs. peers) and a small growth-vs-P/E regression are used only as directional consistency checks, never as the anchor. Full detail in [`methodology/valuation_framework.md`](methodology/valuation_framework.md).

## Repository structure

```
blackrock-two-lenses/
├── README.md
├── report/
│   ├── On_BLK_Two_Lenses.pdf      # memo (p.1) + core narrative
│   └── On_BLK_Two_Lenses.docx
├── model/
│   └── On_BLK_SOTP_Model.xlsx     # formula-driven SOTP, sensitivity grid, two-lens bridge
├── charts/
│   ├── lens_comparison.png
│   ├── valuation_waterfall.png
│   ├── sensitivity_matrix.png
│   ├── bull_base_bear.png
│   └── catalyst_calendar.png
├── memo/
│   └── IC_Memo.pdf                # one-page investment committee memo
└── methodology/
    └── valuation_framework.md
```

## Data & sources

Market data as of mid-June 2026. BlackRock Q1 2026 results (8-K / press release, April 14, 2026); Federal Reserve H.15 (10Y UST ~4.45%); Damodaran January/April 2026 datasets (betas, multiples, country ERPs). Every figure used in the model is flagged with its source on the **Assumptions** tab of the workbook.

## Limitations

This is an independent academic exercise, not the product of an institutional research desk, and uses only publicly available data. It does not constitute investment advice. The geographic-blended ERP is methodologically defensible but not a sell-side convention. The 2022 elasticity figure is a single-year observation, not a statistical beta. Aladdin scenario probabilities are author judgments.

## About

Built by **W.H. Blackburn**. Framework, model, and writeup are reproducible end-to-end: change an input on the model's SOTP tab and every downstream value — including the sensitivity grid and the two-lens bridge — recomputes.
