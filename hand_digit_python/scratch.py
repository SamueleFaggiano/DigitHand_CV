import cv2
import numpy as np

def start():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

def close(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.destroyAllWindows()
        start()

def main_page():
    img = cv2.imread('eye.jpg', 1)
    cv2.imshow('start', img)
    cv2.setMouseCallback('start', close)
    k = cv2.waitKey(0) & 0xFF

if __name__ == '__main__':
    main_page()