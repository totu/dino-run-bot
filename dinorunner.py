#!/usr/bin/env python3

from cv2 import waitKey, namedWindow, startWindowThread, imshow, resize, cvtColor, COLOR_BGR2GRAY, THRESH_BINARY, threshold
from mss import mss
from PIL.Image import frombytes
from numpy import array
from pyautogui import press, keyDown, keyUp
from time import time, sleep

def grab(sct, monitor):
    sct_img = sct.grab(monitor)
    img = frombytes('RGB', sct_img.size, sct_img.rgb) 
    img_np = array(img)
    cropped = cvtColor(img_np, COLOR_BGR2GRAY)
    _, cropped = threshold(cropped, 126, 255, THRESH_BINARY)
    return cropped

if __name__ == "__main__":
    sct = mss() 
    monitor = {"top": 390, "left": 90, "width": 30, "height": 70}

    startWindowThread()
    namedWindow("bot view")

    while 1:
        # Get screen shot
        cropped = grab(sct, monitor)

        # # cactus detector
        # cacti = sum(cropped[90])
        # cacti2 = sum(cropped[76])
        # cacti3 = sum(cropped[80])
        # bird detector
        birb = sum(cropped[30])
        # store reference of empty space
        ref = sum(cropped[-1])
        
        # fill = [255 for x in cropped[0]]
        cacti_check = 0
        for i in range(0, 20, 2):
            cacti_check += sum(cropped[70 + i])

        # jump over cacti
        if cacti_check != ref: 
            press("space")

        # duck bird
        elif birb != ref:
            start = time()
            while time() - start < 2:
                keyDown('down')
            keyUp("down")


        # imshow("bot view", cropped)
        # if waitKey(1) &0xFF == ord('q'):
        #     break
