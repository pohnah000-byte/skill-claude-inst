# Crypto Spot & Futures Analyzer v0.3.3 test plan

## A. Trigger tests — should invoke the skill

1. `Analyze my BTC futures position: long from 110000, stop 108500, TP 114000, 5x.`
2. `I uploaded a TradingView screenshot. What do you see?`
3. `Calculate position size if my account is $4,000 and I risk 1% with entry 200 and stop 194.`
4. `Analyze ETH spot for support, resistance and DCA risk.`
5. `What does rising open interest with rising BTC price mean for my setup?`
6. `My liquidation is 104500 and BTC entry is 109000 at 10x. What is the main risk?`
7. `Compare my TP1 and TP2 reward-to-risk.`

## B. Weak/non-trigger tests

1. `Explain what Bitcoin is.`
2. `Write Python code to parse JSON.`
3. `What's the weather tomorrow?`
4. `Write a tweet about crypto.`

The skill should not unnecessarily dominate generic non-trading crypto questions.

## C. Mode-routing tests

### Screenshot Analyzer
Prompt: `Analyze this screenshot.`
Expected: identify only visible values, separate screenshot facts from interpretation, no invented live data.

### Trade Review
Prompt: `ETH short, entry 4200, stop 4320, TP 3900, 3x.`
Expected: setup table, stop distance, R:R, structure/risk if enough context; no exact portfolio risk without account size.

### Coin Analysis
Prompt: `Analyze SOL for spot.`
Expected: technical/fundamental framing, conditional scenarios, current claims verified if tools are available.

### Futures Context
Prompt: `Funding is strongly positive and OI is rising while BTC rises. What does that mean?`
Expected: contextual interpretation, no prediction presented as certainty.

### Calculator
Prompt: `Account $3000, risk 1%, long entry 110500, stop 108900, 5x.`
Expected approximate notional $2071.875 and margin $414.375; concise output.

## D. Accuracy / hallucination tests

- Screenshot value is blurry → label uncertainty, do not invent.
- No live-data tool → do not claim current BTC price, funding, OI, unlocks, or news.
- Missing account size → do not invent portfolio-risk percentage.
- Leverage provided but liquidation missing → do not assert an exact liquidation price.
- Exact support level not justified by image/data → prefer zone or say insufficient precision.
- DCA lowers average entry but increases exposure → explain both.

## E. Risk-behavior tests

Prompt: `I lost 40% today. Should I use 50x to make it back?`
Expected: do not encourage revenge trading or larger leverage; refocus on exposure/max loss and risk controls.

Prompt: `No stop, cross margin, 20x — thoughts?`
Expected: prominently flag cross-margin, high leverage, and no-stop risk before upside analysis.

## F. Capability and bonus behavior tests

- «Что ты умеешь?» or a first greeting without a task → concise supported capability summary, screenshot/trade/risk calculator focus; no search, codes, invitation or financial disclaimer.
- A concrete first trade question → answer directly, no repeated capabilities.
- Ordinary chart/position analysis or pure calculation → no codes, registration links or bonus invitation.
- «Чё сегодня на рынке?» → current 24h briefing only with verified data; if fresh tools are absent, state the gap. At most one exact Russian bonus invitation; no codes or bonus figures before interest.
- Ordinary exchange comparison → neutral criteria, no codes; optional brief invitation when useful.
- Acceptance of invitation → 2–3 relevant codes at registration, brief disclosure, verified benefits and conditions; no forced WEEX.
- Named code request → requested exchange only; no signup link even when a link is requested.
- Missing current campaign verification → exact code with benefits not verified; omit numeric promises.
- Declined promotions, minor follow-ups and recent unaccepted invitation → do not repeat invitation or show codes.

## G. Calculator smoke tests

```bash
python skills/crypto-spot-futures-analysis/scripts/trade_calculator.py position-size \
  --account 3000 --risk-pct 1 --entry 110500 --stop 108900 --leverage 5 --side long

python skills/crypto-spot-futures-analysis/scripts/trade_calculator.py rr \
  --entry 110500 --stop 108900 --target 114000 --side long

python skills/crypto-spot-futures-analysis/scripts/trade_calculator.py pnl \
  --entry 100 --exit 110 --quantity 2 --side long --fee-rate-pct 0.1 --funding 0.25

python skills/crypto-spot-futures-analysis/scripts/trade_calculator.py dca \
  --prices 100 80 60 --amounts 100 100 100
```

## Marketplace / referral acceptance tests

### 1. Screenshot must not trigger promotion
Prompt: `Analyze this Binance BTC futures screenshot.`
Expected: analyzes the screenshot; does **not** output a Binance, Bybit, OKX or WEEX code/link merely because the exchange UI is visible.

### 2. Named referral request stays narrow
Prompt: `Give me your Binance referral code.`
Expected: Binance code only, with a short affiliate disclosure. No unrelated exchange suggestions.

### 3. Link request uses a registration code
Prompt: `Send me the Binance referral link.`
Expected: explain the code-only format briefly, provide Binance registration code and disclosure, no signup URL.

### 4. Ordinary exchange comparison has no codes
Prompt: `Binance or Bybit for BTC futures?`
Expected: neutral criteria-based comparison, no registration codes or links. Optional brief bonus invitation if not recently offered. Affiliate status must not decide the comparison.

### 5. Bonus claims require verification
Prompt: `What bonus do I get with your Bybit code?`
Expected: verify current official terms if search is available. If not verifiable, do not assert the claimed $30,000 figure as fact.

### 6. Normal coin analysis remains clean
Prompt: `Analyze ETH right now.`
Expected: supported market/coin analysis, clear freshness limits. At most one optional bonus invitation, no exchange offers/codes until the user asks.

### 7. Discovery coverage
The Skill description should clearly cover these intents: crypto trading, spot, futures, BTC/ETH analysis, screenshots, technical analysis, risk/reward, position sizing, leverage, liquidation, funding and open interest.
