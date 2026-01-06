!/usr/bin/env python3
# ============================================================
# P-Linux Init System (User Space)
# Versão: 0.1
# ============================================================

import os
import time
import json
import subprocess
from datetime import datetime

CONFIG_FILE = "config.json"

def log(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {msg}"
    print(line)
    try:
        with open("/var/log/p-linux-init.log", "a") as f:
            f.write(line + "\n")
    except:
        pass

def load_config():
    with open(CONFIG_FILE) as f:
        return json.load(f)

def start_service(name):
    log(f"Starting service: {name}")

    if name == "udev":
        subprocess.call(["udevadm", "trigger"])
    elif name == "network":
        subprocess.call(["nmcli", "networking", "on"])
    elif name == "audio":
        subprocess.call(["pipewire"])
    elif name == "video":
        log("Video handled by kernel + Mesa")
    elif name == "input":
        log("Input devices managed by evdev")
    else:
        log(f"Unknown service: {name}")

def main():
    log("P-Linux init starting...")
    cfg = load_config()

    for svc in cfg["services"]:
        start_service(svc)
        time.sleep(cfg["boot_delay"])

    log("P-Linux init completed successfully.")

if __name__ == "__main__":
    main()