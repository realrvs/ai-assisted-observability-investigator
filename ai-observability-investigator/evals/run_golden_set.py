"""Запуск golden set для tool calling и prompt robustness.

TODO: реализовать согласно Blueprint §11.
- Загружает YAML из docs/operations/golden-set/
- Прогоняет через langchain-gigachat bind_tools
- Сохраняет результаты в evals/results/
- Exit code 1, если порог не достигнут
"""