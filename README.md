# 🔋 TGBotEnergyChecker

[UA] Простий Python-скрипт для моніторингу наявності електроенергії або інтернету через Telegram бот.
[EN] A simple Python script to monitor power or internet availability via Telegram bot.

---

## ⚡ Як це працює? / How it works?

### 🇺🇦 Українською:
Скрипт пінгує (ping) задану IP-адресу або домен. Якщо хост не відповідає — ви отримуєте сповіщення про вимкнення світла. Коли зв'язок повертається — приходить повідомлення про увімкнення.

- **Анти-спам:** Повідомлення надсилається лише після кількох невдалих/вдалих спроб поспіль.
- **Тихий режим:** Можна задати години (наприклад, 23-07), коли бот не буде вас турбувати.
- **Кілька об'єктів:** Моніторинг кількох адрес одночасно через одну конфігурацію.

---

### 🇺🇸 English:
The script pings a specified IP address or domain. If the host stops responding, you receive a "Power Down" alert via Telegram. Once connection is restored, you get a "Power Up" notification.

- **Anti-spam:** Alerts are sent only after a configurable threshold of failed/successful pings.
- **Silent Hours:** Set a time range (e.g., 23-07) to disable notifications during the night.
- **Multi-target:** Monitor several devices or locations simultaneously.

---

## 🚀 Швидкий старт / Quick Start

1. **Клонуйте репозиторій:**
   ```bash
   git clone https://github.com
   cd TGBotEnergyChecker
