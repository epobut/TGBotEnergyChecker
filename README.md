# 🔋 TGBotEnergyChecker

[UA] Простий Python-скрипт для моніторингу наявності електроенергії або інтернету через Telegram бот.
[EN] A simple Python script to monitor power or internet availability via Telegram bot.

---

## ⚡ Як це працює? / How it works?

### 🇺🇦 Українською:
Скрипт постійно пінгує (ping) задану IP-адресу або домен. Якщо хост перестає відповідати — ви отримуєте сповіщення про вимкнення світла. Коли зв'язок повертається — приходить повідомлення про увімкнення.
- **Анти-спам:** Повідомлення надсилається лише після кількох невдалих/вдалих спроб поспіль (налаштовується).
- **Тихий режим:** Можна задати години, коли бот не буде вас турбувати.
- **Кілька цілей:** Моніторинг кількох об'єктів одночасно.

---

### 🇺🇸 English:
The script continuously pings a specified IP address or domain. If the host stops responding, you receive a "Power Down" notification. Once it's back, you get a "Power Up" alert.
- **Anti-spam:** Notifications are sent only after a certain threshold of failed/successful pings (configurable).
- **Silent Hours:** Set a time range when the bot stays quiet.
- **Multi-target:** Monitor several locations or devices at once.

---

## 🚀 Налаштування / Setup

1. Створіть бота через [@BotFather](https://t.me) та отримайте **Token**.
2. Дізнайтеся свій **Chat ID**.
3. Налаштуйте файл `config.py` (або змінні оточення):
   - `TARGETS`: `Name:IP:Interval` (наприклад, `Home:1.2.3.4:60`)
   - `BOT_TOKEN` & `CHAT_ID`
   - `FAIL_THRESHOLD`: скільки пінгів пропустити перед алярмом.

4. **Запуск:**
```bash
pip install requests ping3
python main.py
