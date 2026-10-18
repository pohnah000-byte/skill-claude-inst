---
name: gemini-bridge
description: Мост Claude Code ↔ Gemini — хук, который отдаёт чтение и анализ больших кодовых баз (много файлов, сотни тысяч токенов) в Gemini CLI, а Claude остаётся главным. Используй, когда просят «подключить Gemini для больших проектов», «чтобы Claude не упирался в контекст», установить, настроить, проверить или удалить Claude-Gemini Bridge.
license: MIT
compatibility: Нужны компьютер с macOS или Linux (bash 4+), Claude Code CLI, Gemini CLI (команда gemini) и jq. Не работает внутри чата claude.ai — только на своём компьютере.
---

# Claude-Gemini Bridge — Gemini как «читалка» для Claude Code

Это хук `PreToolUse` для Claude Code. Каждый раз, когда Claude собирается вызвать
`Read`, `Grep`, `Glob` или `Task`, хук смотрит, сколько файлов и текста будет затронуто.
Если объём большой, хук сам отправляет эти файлы в **Gemini CLI**, получает от него
сжатый анализ и отдаёт Claude готовый результат вместо сырых файлов. Маленькие задачи
идут как обычно, без Gemini.

Итог: Claude продолжает рассуждать и писать код, а «прочитать 40 файлов и рассказать,
что в них» делает Gemini с его огромным окном контекста.

Все скрипты лежат рядом с навыком в папке `bridge/`:

| Путь | Что это |
|---|---|
| `bridge/install.sh` | интерактивный установщик (прописывает хук в `~/.claude/settings.json`, делает резервную копию) |
| `bridge/uninstall.sh` | удаление хука и возврат настроек |
| `bridge/hooks/gemini-bridge.sh` | сам хук |
| `bridge/hooks/lib/` | разбор путей `@`, JSON, вызов Gemini, кэш, логи |
| `bridge/hooks/config/debug.conf` | все настройки и пороги |
| `bridge/test/test-runner.sh`, `bridge/test/manual-test.sh` | автотесты и интерактивная проверка |
| `bridge/docs/TROUBLESHOOTING.md` | подробная диагностика (англ.) |

## Когда использовать

- Claude Code упирается в контекст на больших проектах;
- нужно «проанализировать весь проект / все файлы *.py / найти уязвимости во всей папке»;
- установить, настроить пороги, проверить, что Gemini реально вызывается, или удалить мост.

Если нужно, чтобы **вся** работа Claude Code шла на Gemini — это навык `gemini-proxy`.

## Когда Gemini подключается (по умолчанию)

- объём больше ~50 000 токенов (~200 КБ) — `CLAUDE_TOKEN_LIMIT`;
- задача `Task` затрагивает 3 и больше файлов — `MIN_FILES_FOR_GEMINI`;
- но не больше 10 МБ и 800 000 токенов — `MAX_TOTAL_SIZE_FOR_GEMINI`, `GEMINI_TOKEN_LIMIT`;
- файлы `*.secret|*.key|*.env|*.password|*.token|*.pem|*.p12` никогда не отправляются — `GEMINI_EXCLUDE_PATTERNS`.

Ответы кэшируются на час (`GEMINI_CACHE_TTL`), между вызовами пауза 1 с (`GEMINI_RATE_LIMIT`).

## Установка (Claude ведёт по шагам, с согласия человека)

1. **Проверить зависимости:** `claude --version`, `gemini --version`, `jq --version`, `bash --version`.
   - Gemini CLI: `npm install -g @google/gemini-cli`, затем один раз запустить `gemini` и войти
     (Google-аккаунт или ключ `GEMINI_API_KEY`). Проверка: `echo test | gemini -p "Скажи привет"`.
   - jq: `brew install jq` (macOS) или `sudo apt install jq` (Linux).
2. **Скопировать папку `bridge/` в постоянное место**, например `~/claude-gemini-bridge`
   (хук будет ссылаться на этот путь, переносить потом нельзя). `chmod +x` на все `*.sh`.
3. **Запустить установщик.** `install.sh` задаёт вопросы (`read -p`), поэтому его должен запустить
   сам человек в своём терминале: `cd ~/claude-gemini-bridge && ./install.sh`.
   Если интерактивный запуск невозможен — ручная установка: добавить в `~/.claude/settings.json`
   (сохранив существующие хуки, сначала сделав копию файла):
   ```json
   {
     "hooks": {
       "PreToolUse": [{
         "matcher": "Read|Grep|Glob|Task|Agent",
         "hooks": [{ "type": "command", "command": "/полный/путь/claude-gemini-bridge/hooks/gemini-bridge.sh" }]
       }]
     }
   }
   ```
   и создать папки: `mkdir -p cache/gemini logs/debug debug/captured` внутри моста.
   `Agent` добавлен в matcher потому, что в новых версиях Claude Code инструмент подагентов
   называется `Agent`, а не `Task`.
4. **Перезапустить Claude Code** — хуки читаются только при старте.
5. **Проверить:** `~/claude-gemini-bridge/test/test-runner.sh`.

## Проверить, что Gemini реально вызывается

```bash
tail -f ~/claude-gemini-bridge/logs/debug/$(date +%Y%m%d).log | grep -i gemini
```
Признаки вызова: `Delegating to Gemini`, `Gemini call successful (…s, N files)`.
Без вызова Gemini: `Continuing with normal tool execution`.

Режим без реальных запросов (видно только решение): `DRY_RUN=true` в `hooks/config/debug.conf`.
Максимум логов: `DEBUG_LEVEL=3`.

## Настройка под проект

Любой параметр из `debug.conf` можно переопределить переменной окружения перед запуском `claude`:
```bash
export MIN_FILES_FOR_GEMINI=5      # подключать Gemini реже
export CLAUDE_TOKEN_LIMIT=30000    # подключать раньше
export GEMINI_TIMEOUT=60           # дать Gemini больше времени
claude
```

## Удаление

`~/claude-gemini-bridge/uninstall.sh` (интерактивно — запускает человек) или вручную убрать
блок хука из `~/.claude/settings.json` и перезапустить Claude Code.

## Частые проблемы

| Симптом | Что сделать |
|---|---|
| Gemini никогда не вызывается | Claude Code не перезапущен; путь в `settings.json` неверный; нет прав на запуск (`chmod +x`) |
| «Gemini CLI not found» | установить `@google/gemini-cli`, проверить, что `gemini` есть в `PATH` |
| ошибки авторизации Gemini | заново войти в `gemini` или задать `GEMINI_API_KEY` |
| устаревшие ответы | очистить `cache/gemini/` |
| хук тормозит работу | поднять пороги или увеличить `GEMINI_RATE_LIMIT`/уменьшить `GEMINI_MAX_FILES` |

## Важно сказать человеку

- Содержимое файлов проекта уходит в Google через его аккаунт Gemini. Для чужого или
  конфиденциального кода нужно его согласие; список исключений можно расширить в `GEMINI_EXCLUDE_PATTERNS`.
- Хук использует старый формат ответа (`{"decision": "approve" | "block"}`); если новая версия
  Claude Code перестанет его понимать, хук просто перестанет срабатывать — смотреть логи.
- Проект сторонний, не от Anthropic и не от Google.
