#!/usr/bin/env python3

from cv2 import waitKey, namedWindow, startWindowThread, imshow, resize, cvtColor, COLOR_BGR2GRAY, THRESH_BINARY, threshold
from mss import mss
from PIL.Image import frombytes
from numpy import array
from pynput.keyboard import Controller, Key
from time import time, sleep
import pyautogui

def grab(sct, monitor):
    sct_img = sct.grab(monitor)
    img = frombytes('RGB', sct_img.size, sct_img.rgb) 
    img_np = array(img)
    cropped = cvtColor(img_np, COLOR_BGR2GRAY)
    _, cropped = threshold(cropped, 126, 255, THRESH_BINARY)
    return cropped

if __name__ == "__main__":
    sct = mss() 
    monitor = {"top": 390, "left": 92, "width": 35, "height": 70}
    monitor2 = {"top": 390, "left": 92, "width": 500, "height": 70}
    kb = Controller()
    down = Key.down
    space = Key.space
    can_press = True
    # startWindowThread()
    # namedWindow("bot view")

    while True:
        # Get screen shot
        cropped = grab(sct, monitor)
        # full = grab(sct, monitor2)

        # Reference of empty row
        ref = sum(cropped[-1])
        # Obstacle detection
        birb_check = 0
        cacti_check = 0
        # fill = [150 for x in full[0]]
        # fill2 = [255 for x in full[0]]
        for i in range(0, 20, 2):
            birb_check += sum(cropped[8 + i])
            cacti_check += sum(cropped[70 + i])
            # full[8 + i] = fill
            # full[70 + i] = fill2

        # jump over cacti
        if cacti_check != ref: 
            if can_press:
                can_press = False
                print("jump^")
                with kb.pressed(space):
                    sleep(0.10)
                print("jumpv")
                can_press = True

        # duck bird
        elif birb_check != ref:
            print(birb_check, cacti_check)
            if can_press:
                can_press = False
                s = time()
                print("down at %s" % s)
                pyautogui.keyDown("down")
                # with kb.pressed(down):
                #     sleep(2.0)
                sleep(2.0)
                e = time()
                print("up at %s" % s)
                pyautogui.keyUp("down")
                d = e - s 
                print("delta %s" % d)
                can_press = True

        # imshow("bot view", full)
        # if waitKey(1) &0xFF == ord('q'):
        #     break
