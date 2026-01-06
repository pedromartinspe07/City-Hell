import subprocess

def detect_gpu():
    print("[GPU] Detecting GPU...")
    try:
        out = subprocess.check_output(["lspci"]).decode()
        for line in out.splitlines():
            if "VGA" in line or "3D" in line:
                print(f"[GPU] {line}")
    except:
        print("[GPU] Could not detect GPU.")