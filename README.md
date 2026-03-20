🔋 TGBotEnergyChecker
[UA] Простий Python-скрипт для моніторингу наявності електроенергії або інтернету через Telegram бот.
[EN] A simple Python script to monitor power or internet availability via Telegram bot.
⚡ Як це працює? / How it works?
🇺🇦 Українською:
Скрипт постійно пінгує (ping) задану IP-адресу або домен. Якщо хост перестає відповідати — ви отримуєте сповіщення про вимкнення світла. Коли зв'язок повертається — приходить повідомлення про увімкнення.
Анти-спам: Повідомлення надсилається лише після кількох невдалих чи вдалих спроб поспіль.
Тихий режим: Можна задати години (наприклад, 23-07), коли бот не буде вас турбувати.
Кілька цілей: Моніторинг кількох об'єктів одночасно.
🇺🇸 English:
The script continuously pings a specified IP address or domain. If the host stops responding, you receive a "Power Down" alert. Once it's back, you get a "Power Up" notification.
Anti-spam: Notifications are sent only after a certain threshold of failed/successful pings.
Silent Hours: Set a time range when the bot stays quiet (e.g., 23-07).
Multi-target: Monitor several locations or devices at once.
🚀 Швидкий старт / Quick Start
Клонуйте репозиторій:
git clone github.com
cd TGBotEnergyChecker
Встановіть залежності:
pip install requests ping3
Налаштуйте конфіг:
Створіть файл config.py на основі config.py.example та впишіть свої дані (Token, Chat ID, Targets).
Запустіть:
python main.py
🛠 Технічні деталі / Tech Info
Мова: Python 3.x
Бібліотеки: requests, ping3.
Стан: Зберігає останній статус у файл state.json, щоб не дублювати повідомлення після перезавантаження.
📝 GitHub Setup (About & Topics)
Description:
🔋 Telegram bot for power and internet monitoring. Get instant alerts when your home router goes offline or online. Supports silent hours and multi-target tracking.
Topics:
telegram-bot, python, monitoring, power-monitor, connectivity-check, ping, uptime-checker, iot, networking
🛡 Disclaimer
Цей проект створений для особистого використання. Автор не несе відповідальності за будь-які збої або пропущені сповіщення.
