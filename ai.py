#!/usr/bin/env python3
# ============================================================
# P-Linux AI Core (Sandbox)
# ============================================================

import json
import time
from voice import listen_voice, speak
from vision import camera_tick

PERM_FILE = "permissions.json"
MEM_FILE = "memory.json"

def load_permissions():
    with open(PERM_FILE) as f:
        return json.load(f)

def load_memory():
    try:
        with open(MEM_FILE) as f:
            return json.load(f)
    except:
        return []

def save_memory(mem):
    with open(MEM_FILE, "w") as f:
        json.dump(mem, f, indent=2)

def main():
    speak("P-Linux AI initialized. Awaiting commands.")

    memory = load_memory()

    while True:
        perms = load_permissions()

        if perms["voice"]:
            text = listen_voice()
            if text:
                speak(f"You said {text}")
                if perms["memory"]:
                    memory.append({"time": time.time(), "text": text})
                    save_memory(memory)

        if perms["camera"]:
            camera_tick()

        time.sleep(0.2)

if __name__ == "__main__":
    main()