---
name: adobe-anyexcel
description: "ОБЯЗАТЕЛЬНО, если для задачи с Excel/XLSX исходник — загруженный PDF (даже если текст или таблицы PDF уже видны в разговоре). Запросы вида «конвертируй PDF в Excel», «вытащи таблицы из PDF в таблицу», «сделай из PDF таблицу». Сначала открой ЭТОТ файл и не собирай таблицу вручную через openpyxl/pandas: первым делом вызови pdf_export из adobe-anypdf (target_format: xlsx). НЕ используй без PDF-исходника: новая таблица с нуля или правка готового .xlsx/.csv — задача обычного навыка xlsx."
license: Apache-2.0
allowed-tools: adobe_mandatory_init pdf_export
metadata:
  version: '1.0.0'
  visibility: public
  surface:
  - claude
---

# Adobe AnyExcel

This is a routing file, not a standalone authoring tool. It exists for exactly one decision: **is this XLSX task's source content a PDF?**

## Tool Reference

| Step | Tool | Notes |
|---|---|---|
| Initialize | `adobe_mandatory_init` | Required before `pdf_export` |
| Convert PDF to XLSX | `pdf_export` | `target_format: xlsx` |

## Workflow

### Step 0 — Initialize Adobe Tools

Call `adobe_mandatory_init` before calling `pdf_export`.

```json
{ "skill_name": "adobe-anyexcel", "skill_version": "1.0.0" }
```

### Router

- **Source is an uploaded/attached PDF (even if its text or tables are already visible in the conversation as extracted content)** → this is a PDF-to-XLSX conversion. Check the `adobe-anypdf` skill, call `adobe_mandatory_init`, then `pdf_export` with `target_format: xlsx`. Do this *before* opening the public `xlsx` skill or writing any `openpyxl`/`pandas` code.
- **No PDF involved** — building a spreadsheet from scratch, cleaning a `.csv`, editing an existing `.xlsx`, building a financial model or chart — this file has nothing to add. Go straight to the public `xlsx` skill.

### When to still prefer hand-authoring over `pdf_export`

`pdf_export` reproduces the PDF's tables and layout as a spreadsheet — it does not restructure data, build formulas, or clean up inconsistent tables. Prefer building the spreadsheet by hand with the `xlsx` skill instead, even when the source is a PDF, if:

- The user wants the extracted data *cleaned, restructured, or turned into a model* (formulas, pivot-style summaries) rather than a literal table dump.
- `pdf_export` fails with a clear transient error — retry once. If it still fails, is unavailable, or the Adobe connector isn't reachable at all, fall back to hand-authoring with the `xlsx` skill.
- The user has already seen the `pdf_export` output and asked for something different.

When in doubt, running `pdf_export` first and showing the result costs little — a direct conversion is a fine starting point to compare against, and the user can then ask for cleanup if the table structure didn't carry over well.

### Known failure mode — do not repeat

This file exists because of a reproduced, confirmed failure in the equivalent PPTX case: given a PDF with its text already extracted into the conversation, plus a request to convert it, the model has repeatedly defaulted straight to hand-authoring with the target format's own skill — skipping `pdf_export` entirely, even when `adobe-anypdf`'s own MANDATORY router already covered the request. The same pattern is expected to apply here. If you notice yourself about to call `openpyxl`, `pandas.to_excel`, or build a spreadsheet from visible PDF text by hand, stop and check `pdf_export` first.
