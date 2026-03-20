# 🔋 TGBotEnergyChecker

[UA] Простий Python-скрипт для моніторингу наявності електроенергії або інтернету через Telegram-бота.  
[EN] A simple Python script to monitor power or internet availability via a Telegram bot.

---

## ⚡ Як це працює? / How it works?

### 🇺🇦 Українською
Скрипт постійно пінгує задану IP-адресу або домен. Якщо хост перестає відповідати — ви отримуєте сповіщення про вимкнення світла. Коли зв'язок повертається — приходить повідомлення про увімкнення.

- Анти-спам: повідомлення надсилається лише після кількох невдалих або вдалих спроб поспіль  
- Тихий режим: можна задати години (23:00–07:00)  
- Кілька цілей: моніторинг кількох об'єктів одночасно  

### 🇺🇸 English
The script continuously pings a specified IP or domain. If the host stops responding, you get a "Power Down" alert. When it's back — "Power Up".

- Anti-spam threshold  
- Silent hours (23:00–07:00)  
- Multi-target monitoring  

---

## 🚀 Quick Start

### Clone
git clone https://github.com/your-username/TGBotEnergyChecker.git
cd TGBotEnergyChecker

### Install
pip install requests ping3

### Config
cp config.py.example config.py

Edit:
- BOT_TOKEN
- CHAT_ID
- TARGETS

### Run
python main.py

---

## 🛠 Tech Info
- Python 3.x  
- requests, ping3  
- state.json prevents duplicate alerts  

---

## 🛡 Disclaimer
For personal use only. No ответственности for missed alerts.
