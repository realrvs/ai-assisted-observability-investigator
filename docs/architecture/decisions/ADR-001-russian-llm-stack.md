# ADR-001: Выбор российских LLM для AI Investigator

- **Статус:** Accepted
- **Дата:** 2026-10-21
- **Контекст:** Blueprint v2.0+ требует работы в российском правовом и инфраструктурном контуре.

## Контекст

Агенту нужна reasoning-модель с поддержкой tool calling для ReAct-оркестрации,
а также легкая модель для summarize и триажа. Зарубежные LLM (GPT-4o, Claude)
недоступны по комплаенс-требованиям.

## Рассмотренные варианты

| Модель | Tool calling | Лицензия | API | Реестр ПО |
|---|---|---|---|---|
| GigaChat 3.5 Reasoning | ✅ (GCML) | MIT | Обещан, не открыт | ✅ |
| GigaChat-2-Max | ✅ | Проприетарная | ✅ доступен | ✅ |
| Alice AI Foundation LLM | ❓ не подтвержден | Apache 2.0 | Yandex Cloud | ❌ |
| YandexGPT | ❌ (bind_tools не реализован) | Проприетарная | ✅ | ✅ |
| T-lite-it-2.1 | ✅ (ruBFCL 56.5) | Открытая | Self-host | ❓ |

## Решение

- **Primary reasoning:** GigaChat 3.5 Reasoning (когда API откроется).
- **Fallback reasoning:** GigaChat-2-Max (Phase 1).
- **Summarizer / триаж:** T-lite-it-2.1 (self-host, 8B).
- **Embeddings:** GigaChat / YandexGPT embeddings.

## Последствия

**Положительные:**
- Соответствие реестру ПО (GigaChat).
- Возможность self-host для PII-тенантов (MIT у 3.5 Reasoning, открытая у T-lite).
- Tool calling подтвержден у GigaChat и T-lite.

**Отрицательные:**
- Зависимость от сроков открытия API GigaChat 3.5 Reasoning.
- Формат tool calls GCML (не OpenAI-совместимый) — требуется golden set.
- GigaChat 3.5 Reasoning принудительно «думает» (`<think>`), нельзя использовать для latency-критичных задач.

**Митигация:**
- Phase 1 на GigaChat-2-Max с golden set >85%.
- T-lite-it-2.1 для summarize/триажа.
- Golden set Prompt Robustness (10 кейсов, порог 100%).