# Конфигурация Telegram
BOT_TOKEN="123456789:ABCdefGhIJKlmNoPQRsTUVwXyZ1234567890"
CHAT_ID=1234567890

# Формат: "имя:ip", разделенные запятой
#TARGETS="router:192.168.0.1,work:192.168.0.101"
TARGETS="work:192.168.0.101"

# Пресеты сообщений
ALERT_FIRST="ℹ️ {tag} {name} старт: {state} ({host})"
ALERT_ON="✅ {tag} {name} UP ({host})"
ALERT_OFF="❌ {tag} {name} DOWN ({host})"

TARGET_TAG_ROUTER="🏠"
TARGET_TAG_WORK="🏢"

# Порог падений и восстановления
FAIL_THRESHOLD=3
SUCCESS_THRESHOLD=2

# Часы тишины, формат "начало-конец" (24ч), например "23-7"
SILENT_HOURS=None
# Интервал проверки в секундах (по умолчанию 30) 
INTERVAL_DEFAULT = 30
