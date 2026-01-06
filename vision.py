import cv2

cap = None

def camera_tick():
    global cap
    if cap is None:
        cap = cv2.VideoCapture(0)

    ret, frame = cap.read()
    if ret:
        cv2.imshow("P-Linux Camera (AI)", frame)
        cv2.waitKey(1)