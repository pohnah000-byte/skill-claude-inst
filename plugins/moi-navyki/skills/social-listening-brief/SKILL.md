---
name: social-listening-brief
description: "Мониторинг соцсетей: что люди говорят о бренде, человеке, продукте, теме или нише на открытых площадках. Выдаёт темы со ссылками на источники, оговорки по настроению, заметные посты и рекомендации. Используй, когда спрашивают «что пишут про…», «какая репутация у…»."
license: MIT
metadata:
  version: '1.0.0'
  author: ScrapeCreators
  homepage: https://scrapecreators.com
  repository: https://github.com/ScrapeCreators/social-media-research-skills
  requires-env: SCRAPECREATORS_API_KEY
---

# Social Listening Brief

## Overview

Research what people are saying publicly across social platforms. This is useful for brand monitoring, category research, product feedback, reputation checks, and understanding recent conversations.

## When to Use

Use this skill when the user asks:

- what are people saying about X?
- monitor this brand/topic/category
- find complaints or praise about a product
- summarize recent social discussion
- compare sentiment across Reddit, TikTok, YouTube, LinkedIn, Instagram, or Threads

## Useful Sources

- Reddit search, subreddit search, posts, comments
- TikTok search top/keyword/hashtag and comments
- YouTube search, transcripts, comments
- Instagram reels search and hashtag search
- LinkedIn post search
- Threads search
- Google search when platform search is not enough

## Workflow

1. Define topic, aliases, competitor names, and date window.
2. Search multiple relevant sources, not every source blindly.
3. Keep URLs, dates, platform, engagement metrics, and exact quotes.
4. Cluster conversations into themes.
5. Separate positive, negative, neutral, and mixed signals.
6. Highlight representative examples and action items.

## Output Format

```markdown
# Social Listening Brief: {topic}

## Executive Summary
- Main takeaway:
- Conversation volume: Low/Medium/High
- Sentiment: Positive/Neutral/Negative/Mixed
- Confidence: High/Medium/Low

## Top Themes
| Theme | Sentiment | Evidence | Representative quote/source |
|---|---|---|---|

## Notable Posts
- [source](url) — why it matters

## Risks / Opportunities
- ...

## Recommended Actions
1. ...
```

## Common Pitfalls

- Do not pretend this is exhaustive social monitoring. It is public-data research.
- Do not average sentiment across very different communities without caveats.
- Do not use engagement as a proxy for truth.
