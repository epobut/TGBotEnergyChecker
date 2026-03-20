# 🔋 TGBotEnergyChecker

[UA] Простий Python-скрипт для моніторингу наявності електроенергії або інтернету через Telegram-бота.  
[EN] A simple Python script to monitor power or internet availability via a Telegram bot.

---

## ⚡ How it works / Як це працює

### 🇺🇦 Українською

Скрипт постійно пінгує задану IP-адресу або домен.  
Якщо хост перестає відповідати — ви отримуєте сповіщення про вимкнення світла.  
Коли зв'язок повертається — приходить повідомлення про увімкнення.

- Анти-спам: повідомлення тільки після кількох спроб підряд  
- Тихий режим: 23:00–07:00 (налаштовується)  
- Кілька цілей: моніторинг кількох хостів  

### 🇺🇸 English

The script continuously pings a target (IP/domain).  
If it goes offline — you get a "Power Down" alert.  
When it comes back — "Power Up".

- Anti-spam threshold  
- Silent hours (23:00–07:00)  
- Multi-target monitoring  

---

## 🚀 Quick Start

### 1. Clone repo

```bash
git clone https://github.com/your-username/TGBotEnergyChecker.git
cd TGBotEnergyChecker
```

### 2. Install dependencies

```bash
pip install requests ping3
```

### 3. Setup config

```bash
cp config.py.example config.py
```

Edit `config.py`:

```python
BOT_TOKEN = "your_token"
CHAT_ID = "your_chat_id"

TARGETS = [
    {"name": "Home Router", "host": "192.168.1.1"},
    {"name": "Google", "host": "8.8.8.8"}
]
```

### 4. Run

```bash
python main.py
```

---

## 🛠 Tech Info

- Python 3.x  
- Libraries: `requests`, `ping3`  
- State stored in `state.json` (no duplicate alerts after restart)

---

## 📝 GitHub Settings

**Description:**
Telegram bot for monitoring power and internet connectivity with instant alerts.

**Topics:**
```
telegram-bot python monitoring power-monitor ping uptime-checker networking iot
```

---

## 🛡 Disclaimer

For personal use only. No responsibility for missed alerts.
