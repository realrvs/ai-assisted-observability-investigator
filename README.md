# AI Observability Investigator

Read-only ИИ-агент на базе российских LLM для автоматического расследования
инцидентов в LLM-приложениях на основе данных из стека наблюдаемости
(OTel, Loki, Langfuse, Prometheus, Grafana).

## Документация

- [Blueprint v2.1](docs/architecture/blueprint-v2.1.md) — полная архитектура
- [ADR-001: выбор российских LLM](docs/architecture/decisions/ADR-001-russian-llm-stack.md)
- [Playbook расследования](docs/design/playbook-investigation.yaml)
- [Runbook для инженеров](docs/operations/runbook-investigation.md)
- [Roadmap](docs/roadmap/phases.md)

## Статус

Phase 1 — MVP (в разработке)

## Быстрый старт

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# заполнить GIGACHAT_CREDENTIALS, LANGFUSE_KEY и т.д.
```

## Структура

```
docs/         — документация (Blueprint, ADR, runbooks, golden set)
src/          — исходный код агента и tool adapters
evals/        — golden set и скрипты прогона
configs/      — конфигурация моделей
```

## Лицензия

Внутренний проект. См. LICENSE.