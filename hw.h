!/usr/bin/env python3
# ============================================================
# P-Linux Hardware Manager
# Versão: 0.1
# ============================================================

from audio import init_audio
from video import init_video
from input import init_input
from camera import init_camera
from gpu import detect_gpu
import time

def log(msg):
    print(f"[P-LINUX-HW] {msg}")

def main():
    log("Initializing hardware services...")

    detect_gpu()
    init_audio()
    init_video()
    init_input()
    init_camera()

    log("All hardware services initialized.")
    while True:
        time.sleep(5)

if __name__ == "__main__":
    main()