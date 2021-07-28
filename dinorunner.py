#!/usr/bin/env python3

from cv2 import waitKey, namedWindow, startWindowThread, imshow, resize, cvtColor, COLOR_BGR2GRAY, THRESH_BINARY, threshold
from mss import mss
from PIL.Image import frombytes
from numpy import array
from pynput.keyboard import Controller, Key
from time import time, sleep
import pyautogui
import keyboard

def grab(sct, monitor):
    sct_img = sct.grab(monitor)
    img = frombytes('RGB', sct_img.size, sct_img.rgb) 
    img_np = array(img)
    cropped = cvtColor(img_np, COLOR_BGR2GRAY)
    _, cropped = threshold(cropped, 126, 255, THRESH_BINARY)
    return cropped

if __name__ == "__main__":
    sct = mss() 
    monitor = {"top": 390, "left": 100, "width": 120, "height": 70}
    # startWindowThread()
    # namedWindow("bot view")

    while 1:
        # Get screen shot
        cropped = grab(sct, monitor)
        # Reference of empty row
        ref = sum(cropped[-1])
        # Obstacle detection
        cacti_check = sum(cropped[80][40:])

        # jump over cacti
        if cacti_check != ref: 
            pyautogui.keyUp("down")
            pyautogui.keyDown("space")
            sleep(0.1)
            pyautogui.keyUp("space")
        else:
            if not keyboard.is_pressed("down"):
                pyautogui.keyDown("down")

        # This requires sudo
        if keyboard.is_pressed("q"):
            break

        # imshow("bot view", cropped)
        # if waitKey(1) &0xFF == ord('q'):
        #     break
