# Roadmap

## Phase 1 — MVP (5–7 недель)

- [ ] `OTelQueryTool` через Grafana datasource proxy
- [ ] `LangfuseTool` со span summarization (T-lite-it-2.1)
- [ ] ReAct-агент на GigaChat-2-Max
- [ ] Circuit Breaker
- [ ] Slack `/investigate` с async-ответом
- [ ] PII-маскирование
- [ ] Golden set tool calling (25 кейсов) на GigaChat-2-Max: >85%

**Success:** один инцидент <7 мин, partial mode работает.

## Phase 2 — Production (7–9 недель)

- [ ] Миграция на GigaChat 3.5 Reasoning (когда API станет доступен)
- [ ] Auto-triage по Grafana Alerting (T-lite-it-2.1 для классификации)
- [ ] Playbook RAG с embeddings
- [ ] Cost Guard
- [ ] Self-host fallback (T-lite-it-2.1)

**Success:** >50% P1-алертов триажатся автоматически.

## Phase 3 — Advanced (8–12 недель)

- [ ] ML-детектор аномалий
- [ ] Memory прошлых инцидентов
- [ ] Multi-agent (Planner + Retrieval + Validator)
- [ ] LLM-as-a-judge на GigaChat 3.5 Reasoning

**Success:** >65% precision, >75% coverage.