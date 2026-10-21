---
version: 2.1
status: Accepted
date: 2026-10-21
owner: AI Platform Team
---

# Blueprint: AI-Assisted Observability Investigator (Russian LLM Edition) v2.1

> **ВНИМАНИЕ:** Полный текст Blueprint вставьте сюда, обернув внешний блок
> в четыре обратные кавычки (````), как описано в комментарии к документу.
> Ниже — краткая структура разделов для навигации.

## Оглавление

1. [Контекст и Problem Statement](#1-контекст-и-problem-statement)
2. [Выбор российских LLM](#2-выбор-российских-llm-матрица-решений)
3. [Целевая архитектура](#3-целевая-архитектура)
4. [Компоненты системы](#4-компоненты-системы)
5. [Триггеры запуска и таймауты](#5-триггеры-запуска-и-таймауты)
6. [Безопасность и комплаенс](#6-безопасность-и-комплаенс)
7. [Метрики успеха](#7-метрики-успеха)
8. [Roadmap](#8-roadmap)
9. [Технологический стек](#9-технологический-стек-российский-контур)
10. [Anti-patterns](#10-anti-patterns)
11. [Definition of Done для MVP](#11-definition-of-done-для-mvp)
12. [Executive Summary](#12-executive-summary-эволюция-v10--v21)

## Связанные артефакты

- [Playbook](../design/playbook-investigation.yaml)
- [Cost Guard](../design/cost-guard.yaml)
- [Langfuse Tool Modes](../design/langfuse-tool-modes.yaml)
- [Golden Set: Tool Calling](../operations/golden-set/tool-calling-25-cases.yaml)
- [Golden Set: Prompt Robustness](../operations/golden-set/prompt-robustness-10-cases.yaml)
- [ADR-001](decisions/ADR-001-russian-llm-stack.md)