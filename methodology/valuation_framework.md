# Valuation Framework

This note documents the methodology behind *BlackRock: One Asset, Two Lenses*. It is written so a reader can reconstruct every number in the model from public data.

## 1. Why two lenses

A single discount rate applied to consolidated cash flows would misprice BlackRock, because its four businesses have materially different risk and growth profiles. More fundamentally, the right *multiple* for the whole company depends on an unstated prior — whether you believe BlackRock is a cyclical asset manager or a structurally lower-cyclicality platform. Rather than bury that prior, the framework makes it explicit and values the company twice:

- **Rate-Sensitive Asset Manager** — calibrates every input to the view that ~two-thirds of revenue is AUM-linked and therefore market-cyclical. Higher costs of equity, beta near the market, conservative private-market durability. Result: **~$825/share.**
- **Platform Compounder** — credits the lower observed earnings cyclicality, Aladdin's software-like economics, and the private-market diversification. A premium to asset managers, a discount to pure alternatives. Result: **~$906/share.**

The distance between them (~$134/share) is the quantified version of the entire bull/bear debate.

## 2. Sum-of-the-parts construction

Each segment is valued with the Gordon Growth (single-stage perpetuity) model:

```
Segment equity value = FCFE × (1 + g) / (Ke − g)
```

| Segment | FCFE base | g | Ke | Equity value |
|---|---|---|---|---|
| iShares & Public Markets | $5.79B | 3.0% | 8.50% | $108.4B |
| Aladdin Technology (prob-weighted) | ~$0.58B | 8.0% | 11.25% | $19.1B |
| GIP Infrastructure | $0.25B | 5.0% | 10.00% | $5.2B |
| HPS Private Credit | $0.29B | 4.0% | 10.00% | $5.0B |
| **Gross segment sum** | | | | **$137.7B** |

Corporate adjustments are then applied: net debt (−$3.5B), co-invest capital drag (−$3.1B), a +$17.8B iShares operating-leverage overlay, and −$8.2B of terminal-cap corrections on Aladdin and GIP that hold every segment to a terminal rate at or below Rf. The net franchise premium over a mechanical single-stage SOTP is ~$62/share — the *quantified gap between the two lenses.* Strip the overlay and the conservative read lands near the $825 rate-sensitive value.

**Net SOTP (Platform lens) = $140.7B ÷ 155M shares = $906/share.**

## 3. Cost of capital

- **Risk-free rate:** 4.30% (10Y UST, May 2026).
- **Equity risk premium:** 5.40%, built from geographic-mix-weighted country ERPs (Damodaran April 2026) reflecting BlackRock's actual revenue distribution rather than a US-only convention.
- **Segment betas:** Damodaran sector datasets (Investments & Asset Management; Real Estate Operations; Brokerage & IB; Software & Information Services), with disclosed judgmental floors/overlays per segment.
- **Blended firm-level Ke:** 8.92%, operating-income-weighted (75% iShares / 12% Aladdin / 7% HPS / 5% GIP).

Terminal growth is capped at the risk-free rate (Damodaran convention: no firm outgrows the economy in perpetuity).

## 4. Sensitivity

The valuation is most sensitive to two inputs: the **iShares cost of equity** and the **Aladdin probability-weighted FCFE**. Across the credible range of both, fair value spans roughly **$829–$956**, with the central case at $906. The grid is reproduced live on the model's `Sensitivity` tab.

## 5. Relative valuation (cross-check only)

BlackRock trades around 16× EV/EBIT — a premium to the ~11× pure-play asset-manager median and a discount to the ~20× broader I&AM median once alternatives are included. Its ~7× EV/Sales is consistent with a ~44% operating margin (roughly double the peer median). A small growth-vs-P/E regression across listed peers is reported strictly as a directional consistency check; with a tiny sample and BlackRock at the extreme of the growth distribution, it is not treated as an independent valuation anchor.

## 6. Disclosed judgmental overrides

Every place where judgment overrides mechanical source data is itemized in the report's Appendix B (e.g., HPS credit-cycle floor +140bp; iShares operating-leverage overlay; Aladdin switching-cost reduction; iShares regulatory-capital haircut; HPS through-cycle normalization; geographic ERP blend). The overrides cumulatively bias the valuation *downward*; the platform lens reflects an empirically supported recalibration of them, while the rate-sensitive lens applies them at full conservative magnitude.

## 7. Reproducibility

The model is fully formula-driven. Changing any blue input cell on the `SOTP` tab flows through to the segment values, the net target, the `Sensitivity` grid, and the `Two Lenses` bridge. No values are hardcoded downstream of the inputs.
