import os

def init_input():
    print("[INPUT] Detecting input devices...")
    devices = os.listdir("/dev/input")
    for d in devices:
        if "event" in d:
            print(f"[INPUT] Found device: 