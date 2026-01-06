import os

def init_camera():
    print("[CAMERA] Checking cameras...")
    cams = [d for d in os.listdir("/dev") if "video" in d]

    if not cams:
        print("[CAMERA] No camera detected.")
    else:
        for cam in cams:
            print(f"[CAMERA] Found camera: /dev/{cam}")