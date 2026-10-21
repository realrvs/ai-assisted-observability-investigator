# Следующие шаги

## 1. Заполнить Blueprint

Открыть `docs/architecture/blueprint-v2.1.md` и вставить полный текст Blueprint.
Внешний блок обернуть в **четыре** обратные кавычки (````), внутри — тройные
для примеров кода. Это гарантирует корректный рендеринг в GitHub/GitLab/VS Code.

## 2. Заполнить окружение

Скопировать `.env.example` в `.env` и заполнить реальными ключами:

- `GIGACHAT_CREDENTIALS` — ключ авторизации GigaChat
- `LANGFUSE_PUBLIC_KEY` / `LANGFUSE_SECRET_KEY`
- `GRAFANA_SERVICE_TOKEN`
- `SLACK_BOT_TOKEN` / `SLACK_SIGNING_SECRET`

`.env` не коммитится (см. `.gitignore`).

## 3. Заполнить golden set

В `docs/operations/golden-set/` сейчас только примеры:

- `tool-calling-25-cases.yaml` — 6 из 25 кейсов
- `prompt-robustness-10-cases.yaml` — 4 из 10 кейсов

Дописать остальные вместе с командой, которая знает реальные сценарии.

## 4. Реализовать MVP

Порядок:

1. `src/investigator/tools/circuit_breaker.py` — обертка для всех адаптеров
2. `src/investigator/tools/otel_query.py` — через Grafana datasource proxy
3. `src/investigator/tools/langfuse_tool.py` — summarize + expand_span
4. `src/investigator/agent.py` — ReAct на `langchain-gigachat` bind_tools
5. `src/investigator/delivery/slack_bot.py` — async-ответ
6. `evals/run_golden_set.py` — прогон golden set

## 5. Настроить CI

GitHub Actions / GitLab CI:

- `markdown-lint` для `docs/`
- `run_golden_set.py` — падает, если tool-call accuracy < 85% или injection_resistance < 100%
- `PSScriptAnalyzer` для самого `New-ProjectStructure.ps1`

## 6. Проверить скрипт создания структуры

```powershell
Install-Module PSScriptAnalyzer -Scope CurrentUser -Force
Invoke-ScriptAnalyzer -Path .\New-ProjectStructure.ps1 -Severity Warning, Error
```

Ожидаемый результат: 0 warnings, 0 errors. Если PSScriptAnalyzer ругается на
«unused expression» — значит, в скрипте появился here-string без присваивания.