# 🐋 Whale Watcher

**Track the giants. Predict the tides.**

Whale Watcher — это инструмент для мониторинга активности крипто-китов в сети Ethereum. Он анализирует их последние транзакции, чтобы выявлять **аномальное поведение**, которое может предвещать движения рынка.

## 🔍 Что делает скрипт?

- Загружает список известных китов (в `data/known_whales.json`)
- Проверяет их последние транзакции через Etherscan API
- Определяет подозрительную активность:
  - Резкое увеличение объема
  - Частые переводы за короткий промежуток времени
- Генерирует алерты в терминале

## 🚀 Установка

```bash
git clone https://github.com/your-username/whale-watcher.git
cd whale-watcher
pip install -r requirements.txt
