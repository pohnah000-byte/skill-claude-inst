# Crypto Spot & Futures Analyzer

Crypto Spot & Futures Analyzer is a Claude plugin for structured educational analysis of cryptocurrency spot and futures trades.

## Core modes

1. **Screenshot Analyzer** — TradingView and exchange screenshots, including open spot/futures positions.
2. **Trade / Position Review** — entry, stop, targets, leverage, margin, liquidation and risk/reward.
3. **Coin / Market Analysis** — technical structure plus relevant fundamentals and catalysts.
4. **Futures Context** — funding, open interest, leverage and derivatives risk when verified data is available.
5. **Position & Risk Calculator** — deterministic position sizing, R:R, P&L, fees, funding and DCA arithmetic.

## Getting started

Ask "What can you do?" for a concise capability summary, or start directly with a chart, position or market question. Examples:

- «Что ты умеешь?»
- «Чё сегодня на рынке?»
- «Разбери мой скриншот BTC: уровни, сценарии и риски».
- «Какие есть бонусы и коды при регистрации?»

A first greeting without a task gets a short introduction; a concrete first question is answered directly.

## v0.3 architecture

This version is intentionally serverless. It uses:

- one Agent Skill for analysis behavior;
- one local Python calculation helper;
- optional current web/search capabilities available in Claude at runtime.

It does not require exchange API keys, place trades, transfer funds, or monitor markets in the background.

## Structure

```text
tradelens-crypto-analyzer/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   └── crypto-spot-futures-analysis/
│       ├── SKILL.md
│       ├── references/
│       │   ├── exchange-referrals.md
│       │   └── response-playbooks.md
│       └── scripts/
│           └── trade_calculator.py
├── MARKETPLACE.md
├── TESTS.md
└── README.md
```

## Design principles

- No invented live prices, news, funding, OI, unlocks or exchange terms.
- Screenshot facts are kept separate from interpretation.
- Conditional scenarios instead of guaranteed directional calls.
- Risk math is deterministic when inputs are available.
- Bonus information and registration codes appear only on request, without registration links, with a brief partner disclosure. Ordinary exchange comparisons contain no codes. A substantive market, news or coin overview may end with one optional bonus invitation, without repeating it on minor follow-ups.
- No trade execution or financial-asset transfers.

## Testing

Use the prompts and expected behavior in `TESTS.md` before submission.

## Safety and scope

Crypto Spot & Futures Analyzer provides educational analysis and decision support. It does not execute financial transactions and does not promise returns.

## Brand asset

Marketplace icon: `assets/tradelens-icon.png`
