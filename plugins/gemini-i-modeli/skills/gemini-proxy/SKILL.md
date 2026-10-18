---
name: gemini-proxy
description: Запуск Claude Code на моделях Google Gemini через локальный прокси (Gemini for Claude Code). Используй, когда просят «подключить Gemini к Claude Code», «запустить Claude Code на Gemini», «сэкономить на Claude Code через Gemini», настроить прокси ANTHROPIC_BASE_URL для Gemini или починить его ошибки.
license: WTFPL
compatibility: Нужны компьютер с Python 3.8+, Claude Code CLI и ключ Google AI Studio (GEMINI_API_KEY). Не работает внутри чата claude.ai — только на своём компьютере или сервере.
---

# Gemini for Claude Code — прокси «Claude Code → Gemini»

Небольшой сервер на Python (FastAPI + LiteLLM), который притворяется API Anthropic.
Claude Code отправляет ему запросы как обычно, а прокси переводит их в формат Gemini,
отправляет в Google и возвращает ответ обратно в формате Anthropic — с потоковой выдачей
и вызовами инструментов. В итоге интерфейс остаётся Claude Code, а «мозг» — Gemini.

Все файлы сервера лежат рядом с этим навыком в папке `assets/`:

| Файл | Что это |
|---|---|
| `assets/server.py` | сам прокси (порт 8082 по умолчанию) |
| `assets/requirements.txt` | зависимости Python |
| `assets/.env.example` | шаблон настроек |
| `assets/CLAUDE.md` | инструкции для Gemini, как вести себя внутри Claude Code |

## Когда использовать

- человек хочет работать в Claude Code, но на моделях Gemini (дешевле, бесплатный лимит AI Studio, огромный контекст);
- нужно поднять, перенастроить или починить такой прокси;
- нужно объяснить, как это устроено.

Если же нужно, чтобы **Claude остался главным**, а Gemini только читал большие кодовые базы —
это навык `gemini-bridge`. Если нужен один прокси сразу под много провайдеров
(OpenAI, Grok, DeepSeek, Kimi и др.) — навык `opencodex`.

## Установка (делает Claude по шагам, с согласия человека)

1. **Проверить окружение:** `python3 --version` (нужно 3.8+), `claude --version`.
2. **Скопировать сервер в постоянную папку**, например `~/gemini-proxy`:
   скопировать туда все файлы из `assets/` этого навыка.
3. **Виртуальное окружение и зависимости:**
   ```bash
   cd ~/gemini-proxy
   python3 -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```
4. **Ключ и модели.** `cp .env.example .env`, затем человек сам вписывает ключ в `.env`:
   ```dotenv
   GEMINI_API_KEY="ключ из https://aistudio.google.com/apikey"
   BIG_MODEL="<актуальная Pro-модель>"     # на неё уходят запросы sonnet/opus
   SMALL_MODEL="<актуальная Flash-модель>" # на неё уходят запросы haiku
   HOST="127.0.0.1"
   PORT="8082"
   ```
   - **Ключ не просить в чат.** Пусть человек вставит его в `.env` сам, в своём редакторе.
   - **Обязательно поменять модели.** В шаблоне по умолчанию стоят `gemini-1.5-…` — эти модели
     Google уже отключил, с ними прокси будет падать. Точные названия брать из списка на
     https://ai.google.dev/gemini-api/docs/models (например, семейство `gemini-2.5-pro` /
     `gemini-2.5-flash` или более новые). Прокси принимает любое название из `.env`.
   - `HOST="127.0.0.1"` — чтобы прокси был виден только на этом компьютере. Значение
     `0.0.0.0` из оригинала открывает его всей локальной сети.
5. **Запуск:** `python server.py` (в отдельном окне терминала или как фоновый сервис).
6. **Проверка:** `curl http://127.0.0.1:8082/health` и `curl http://127.0.0.1:8082/test-connection`
   (в этой копии тест использует модель из `SMALL_MODEL`).
7. **Подключить Claude Code:**
   ```bash
   ANTHROPIC_BASE_URL=http://127.0.0.1:8082 claude
   ```
   Для постоянной работы можно сделать алиас, например `alias claude-gemini='ANTHROPIC_BASE_URL=http://127.0.0.1:8082 claude'`.
8. **Подложить `CLAUDE.md`.** Скопировать `assets/CLAUDE.md` в корень проекта (если там уже есть свой
   `CLAUDE.md` — дописать содержимое в конец, а не затирать). В начале сессии полезно попросить:
   «Сначала прочитай CLAUDE.md и следуй ему. Ответь YES, когда прочитаешь».

## Как сопоставляются модели

- в названии запроса есть `haiku` → `SMALL_MODEL`;
- есть `sonnet` или `opus` → `BIG_MODEL`;
- если Claude Code просит модель с названием `gemini-…` или `gemini/…` — она используется как есть.

## Адреса сервера

`POST /v1/messages` — основной; `POST /v1/messages/count_tokens` — подсчёт токенов;
`GET /health` — состояние; `GET /test-connection` — пробный запрос в Gemini; `GET /` — текущие настройки.

## Частые проблемы

| Симптом | Что сделать |
|---|---|
| `model not found` / 404 от Gemini | в `.env` устаревшее название модели — заменить на актуальное |
| ошибки «malformed chunk», обрывы потока | `FORCE_DISABLE_STREAMING=true` в `.env`, перезапустить; или поднять `MAX_STREAMING_RETRIES` |
| 500 от Gemini | временный сбой Google, прокси сам повторяет; проверить `/health` позже |
| таймауты | увеличить `REQUEST_TIMEOUT` |
| 429 / лимиты | закончилась квота AI Studio — смотреть в Google AI Studio / Cloud Console |
| Claude Code ходит в настоящий Anthropic | не задан `ANTHROPIC_BASE_URL` в том же окне, где запущен `claude` |
| инструменты вызываются криво | напомнить Gemini перечитать `CLAUDE.md`; Gemini хуже Claude следует формату инструментов — это ограничение подхода |

Подробные логи: `LOG_LEVEL=DEBUG` в `.env`.

## Честные ограничения

- Качество работы с инструментами и длинными задачами ниже, чем у Claude: это другая модель.
- Запросы уходят в Google по ключу человека; расход и лимиты — по его аккаунту AI Studio.
- Проект сторонний (на основе claude-code-proxy от @1rgs), не от Anthropic и не от Google.
