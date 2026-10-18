---
name: audience-research
description: "Оценка аудитории блогера, инфлюенсера или бренда по открытым данным: сигналы профиля, демография аудитории TikTok, подписчики и подписки, комментарии, география, язык и соответствие тематике. Помогает решить, подходит ли блогер для рекламы и выхода на рынок."
license: MIT
metadata:
  version: '1.0.0'
  author: ScrapeCreators
  homepage: https://scrapecreators.com
  repository: https://github.com/ScrapeCreators/social-media-research-skills
  requires-env: SCRAPECREATORS_API_KEY
---

# Audience Research

## Overview

Evaluate whether a creator or social account reaches the right audience. This skill combines available public profile metrics, TikTok audience demographics, regional signals, follower/following data when available, comments, language, and content topics.

## When to Use

Use this skill when the user asks to:

- check if a creator's audience fits a market
- compare audience fit across creators
- find US-heavy, country-specific, or niche-specific creators
- evaluate sponsorship/influencer opportunities
- understand who appears to engage with an account

## Useful Sources

- `/v1/tiktok/user/audience`
- `/v1/tiktok/profile/region`
- profile endpoints across platforms
- follower/following endpoints where available
- comments on recent posts
- link-in-bio pages and creator shops for niche signals

## Workflow

1. Pull profile and available audience/demographic data.
2. Pull recent content and comments if audience intent matters.
3. Extract region, language, niche, product/category, and community signals.
4. Score audience fit against the user's target market.
5. Label confidence based on the strength of public data.

## Output Format

```markdown
# Audience Research: {creator}

## Fit Summary
- Target market:
- Fit score: High/Medium/Low
- Confidence: High/Medium/Low

## Evidence
| Signal | Evidence | Source |
|---|---|---|

## Audience Notes
- Geography:
- Language:
- Niche/content fit:
- Comment quality:

## Sponsorship Recommendation
- Good fit / Maybe / Poor fit
- Why:
```

## Common Pitfalls

- Do not infer exact demographics from vibes. Use available evidence and label assumptions.
- Do not overpromise audience details for platforms that do not expose them publicly.
- Do not ignore mismatch between creator location and audience location.
