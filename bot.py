import os
import time
import json
import requests
from ping3 import ping 
from pathlib import Path
from datetime import datetime

from config import *


STATE_FILE = Path("state.json")


# ================== TELEGRAM ==================
def send_telegram(text: str):
    if not BOT_TOKEN or not CHAT_ID:
        print("Telegram config missing")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    requests.post(url, data=payload, timeout=10)

# ================== PING ==================
def ping_host(host: str, retries: int = 3) -> bool:
    #Возвращает True, если хотя бы один из retries пингов успешен (>0.0)
    for _ in range(retries):
        try:
            result = ping(host, timeout=1)
            if result is not None and result > 0:
                return True
        except Exception:
            pass
        time.sleep(0.2)
    return False

# ================== HELPERS ==================
def is_silent_time():
    if not SILENT_HOURS:
        return False

    start, end = map(int, SILENT_HOURS.split("-"))
    hour = datetime.now().hour

    if start < end:
        return start <= hour < end
    return hour >= start or hour < end

def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {}

def save_state(state):
    STATE_FILE.write_text(json.dumps(state))

def format_message(template, *, name, host, up, tag):
    return template.format(
        tag=tag,
        name=name,
        host=host,
        state="UP" if up else "DOWN"
    )

# ================== TARGETS ==================
def load_targets():
    targets = {}

    if not TARGETS:
        return targets

    for item in TARGETS.split(","):
        if not item:
            continue

        # name:host[:interval]
        parts = item.split(":")
        name = parts[0]
        host = parts[1]
        interval = int(parts[2]) if len(parts) > 2 else INTERVAL_DEFAULT

        tag = os.getenv(f"TARGET_TAG_{name.upper()}", "")

        targets[name] = {
            "name": name,
            "host": host,
            "interval": interval,
            "next_check": 0,
            "last_up": None,
            "fail_count": 0,
            "success_count": 0,
            "tag": tag,
        }

    return targets

# ================ LOGGING =================
def log_status(name, host, up, fail_count, success_count, state_changed):
    status = "UP" if up else "DOWN"
    changed = "⚠️ State changed!" if state_changed else ""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {name} ({host}) - {status} | fail: {fail_count} success: {success_count} {changed}")

# ================== MAIN ==================
def main():
    targets = load_targets()
    state = load_state()

    if not targets:
        send_telegram("⚠️ TARGETS not defined")
        while True:
            time.sleep(60)

    # FIRST MESSAGE (always)
    for name, t in targets.items():
        if name in state:
            t["last_up"] = state[name]
        else:
            up = ping_host(t["host"])
            t["last_up"] = up
            state[name] = up

            msg = format_message(
                ALERT_FIRST,
                name=name,
                host=t["host"],
                up=up,
                tag=t["tag"]
            )
            send_telegram(msg)

    save_state(state)

    # MONITOR LOOP
    while True:
        try:
            now = time.time()

            for name, t in targets.items():
                if now < t["next_check"]:
                    continue

                t["next_check"] = now + t["interval"]
                up = ping_host(t["host"])

                if up:
                    t["success_count"] += 1
                    t["fail_count"] = 0
                else:
                    t["fail_count"] += 1
                    t["success_count"] = 0

                state_changed = False
                state_changed = (
                    up and not t["last_up"] and t["success_count"] >= SUCCESS_THRESHOLD
                ) or (
                    not up and t["last_up"] and t["fail_count"] >= FAIL_THRESHOLD
                )
                log_status(name, t["host"], up, t["fail_count"], t["success_count"], state_changed)

                if state_changed:
                    template = ALERT_ON if up else ALERT_OFF
                    msg = format_message(
                        template,
                        name=name,
                        host=t["host"],
                        up=up,
                        tag=t["tag"]
                    )
                    send_telegram(msg)
                    t["last_up"] = up
                    state[name] = up

            save_state(state)
            time.sleep(1)

        except Exception as e:
            print(f"Error in main loop: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()
