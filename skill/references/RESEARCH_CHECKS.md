# Research checks

Use the checks that affect the claim. A simple lookup can cite its source and stop. For a consequential comparison, map both methods onto the Handbook's five axes and distinguish the intended setting from the setting actually tested. [Handbook five-axis ontology](https://github.com/sou350121/Trading-Handbook/blob/main/cheat-sheet/ontology.md)

## What the evidence supports

| Evidence | How to use it |
| --- | --- |
| Published research | Cite the original version, table, and protocol when available. Identify preprints and say whether the result came from a lab test, backtest, paper trading, or a live record. |
| Secondary coverage | Attribute the result to the Handbook or other coverage if that is what you read. Mark details pending primary-source verification. |
| Analyst inference | Name the observation and assumption that support the inference. State what additional comparison could change it. |
| Independent replication | Identify the independent team, how it ran or reimplemented the test, and which results and settings were reproduced. An author's code, data bundle, or rerun is useful for reproducibility. |
| Paper trading | Describe the prospective test period, feed, simulated fills, and cost assumptions when available. Claims apply to that simulated setup. |
| Live evidence | Look for actual capital and filled orders, a dated record with scope and size, and realized results and costs. Attribute self-reported and independently verified records separately. |

These distinctions can coexist. A published article may describe a lab test, and a secondary article may report a live result without sharing the underlying records. A workbook can document inputs, assumptions, or calculations. Use index dates to establish timing or coverage. For both, trace investment performance claims to the underlying study or trading record. Mark gaps as *unreported*, *unverified*, or *not found in the sources checked* as appropriate. Absence in the reviewed material leaves the underlying claim open.

## Align the comparison

- **Inputs and timing.** Match markets, universe, liquidity, data vintage, bar frequency, label horizon, holding period, and rebalance interval. Check point-in-time constituents, delistings, corporate actions, availability lags, and when a signal can first trade.
- **Splits and leakage.** Record train, validation, and test dates or walk-forward windows. Check overlapping labels, boundary gaps where needed, how transforms and universe filters were fitted, and whether factor search or tuning reused the test set. For agents, examine retrieval dates and model pretraining knowledge alongside the experiment's time split. Describe uncertainty when training cutoffs or retrieved material are undisclosed.
- **Signals and portfolio results.** Define the kind of information coefficient (IC), its horizon, aggregation, and sign. Compare raw and residual IC on aligned data. State which exposures neutralization removes. Then check the weighting, portfolio constraints, benchmark, and net return, risk, and drawdown measures. Report uncertainty across markets, seeds, or periods where available.
- **Trading frictions.** Use consistent turnover definitions and rebalancing assumptions when comparing gross and net results. Record fees, spread and slippage, borrow fees and availability for shorts, and market impact. Check position size against trading volume, participation, and fill assumptions. Treat linear cost estimates as specific to their model and capacity estimates as conditional on size, liquidity, and impact.
- **Transfer.** Look for evidence that the ordering survives alternative cost and liquidity assumptions, markets, and regimes. State what was tested and where comparison remains weak. Scope conclusions to the protocol and metrics supported by the evidence.

## Worked comparison · R&D-Agent and Alpha101

On the **data modality** axis, FactorBench evaluates both on common tabular price and volume inputs across five equity markets. For **time horizon**, it uses a 20-trading-day forward target and rebalances every 20 trading days. On **learning paradigm**, R&D-Agent uses LLM-assisted research and factor generation, while Alpha101 supplies fixed, human-authored formulas. Their **alpha mechanism** enters through explicit factors in the common portfolio pipeline. On **human–machine collaboration**, the agent automates parts of research within a specified protocol, while researchers define and implement the public formula baseline. Keep the original R&D-Agent paper's settings separate from this benchmark. [FactorBench study, §4.3 and Table 2](https://arxiv.org/html/2610.06947v1) · [R&D-Agent paper](https://arxiv.org/abs/2505.15155) · [101 Formulaic Alphas](https://doi.org/10.1002/wilm.10525)

The Handbook's analysis of FactorBench v1 reports training on 2017–2021, validation on 2022–2023, and out-of-sample testing from January 2024 to October 2025. Its reading of Table 2 gives R&D-Agent a raw IC of 0.0253 and residual IC of 0.0011 after neutralizing five measured styles. Alpha101's residual IC was 0.0237. R&D-Agent had the higher modeled net long–short Sharpe (0.679 versus 0.319) and reported turnover of 7.8×. The two metrics address different questions. Neutralization leaves open unmeasured exposures, and the comparison does not identify the cause of the Sharpe gap. Fixed constituents, linear transaction costs, simplified borrowing, and the test window limit claims about slippage, nonlinear impact, capacity, and other regimes. Report the metric-specific backtest ranking. A universal ranking or pure-alpha claim would require further evidence. [FactorBench study, §4.3 and Table 2](https://arxiv.org/html/2610.06947v1) · [Handbook FactorBench analysis](https://github.com/sou350121/Trading-Handbook/blob/main/foundations/evaluation-benchmarks/factorbench.md)

## Worked interpretation · operational evidence

Vibe-Trading's lab checks concern tool results, provenance, and authorization boundaries. A functioning paper-trading mode or simulated fill supports a claim about the workflow under the stated test. A claim about live investment results requires a separate record of real fills, capital, costs, and outcomes. Report which evidence the source actually provides. [Vibe-Trading preprint](https://arxiv.org/abs/2611.24845v1) · [Handbook Vibe-Trading analysis](https://github.com/sou350121/Trading-Handbook/blob/main/foundations/llm-agentic/vibe-trading.md)
