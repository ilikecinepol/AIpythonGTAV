import numpy as np
import cv2
from mss import mss
import keyboard

bounding_box = {'top': 30, 'left': 0, 'width': 800, 'height': 600}

sct = mss()
for t in range(5, 0, -1):
    print(t)
ww

while True:
    sct_img = sct.grab(bounding_box)
    cv2.imshow('screen', np.array(sct_img))
    keyboard.press('w')
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
