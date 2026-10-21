# Changelog

Все заметные изменения документа и кода фиксируются здесь.
Формат: [Keep a Changelog](https://keepachangelog.com/ru/1.1.0/).

## [Unreleased]

## [2.1] - 2026-10-21
### Added
- Golden Set для валидации tool calling на fallback-модели (25 кейсов, §11.1)
- Golden Set Prompt Robustness (10 кейсов, §11.2)
- Подраздел Prompt Robustness для защиты от инъекций через недоверенные данные

### Changed
- Уточнены таймауты и async-поведение Delivery Layer с учетом latency российских API (§5)
- Исправлены фактические параметры GigaChat 3.5 Reasoning: контекст 262K, формат GCML, принудительный `<think>` (§2.1, §4.2.1)

## [2.0] - 2026-10-15
### Changed
- Полный переход на российские LLM: GigaChat 3.5 Reasoning (primary), GigaChat-2-Max (fallback), T-lite-it-2.1 (summarizer)
- Добавлены комплаенс-требования (реестр ПО, self-host)

## [1.1] - 2026-10-10
### Added
- OTel-центричный доступ к данным (§3.1)
- Span Summarization & Filtering в LangfuseTool (§3.2)
- Circuit Breaker & Graceful Degradation (§3.5)
- Cost Guard & Token Budget (§3.6)

## [1.0] - 2026-10-01
### Added
- Первая версия Blueprint: AI-Assisted Observability Investigator