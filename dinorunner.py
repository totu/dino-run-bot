#!/usr/bin/env python3

from cv2 import waitKey, namedWindow, startWindowThread, imshow, resize, cvtColor, COLOR_BGR2GRAY, THRESH_BINARY, threshold
from mss import mss
from PIL.Image import frombytes
from numpy import array
from time import time
from pyautogui import press

def grab(sct, monitor):
    sct_img = sct.grab(monitor)
    img = frombytes('RGB', sct_img.size, sct_img.rgb) 
    img_np = array(img)
    cropped = cvtColor(img_np, COLOR_BGR2GRAY)
    _, cropped = threshold(cropped, 126, 255, THRESH_BINARY)
    return cropped

if __name__ == "__main__":
    sct = mss() 
    # startWindowThread()
    # namedWindow("bot view")
    start = time()
    width = 95
    left = 100
    speed_up = True

    while 1:
        # Get screen shot
        monitor = {"top": 390, "left": left, "width": width, "height": 70}
        cropped = grab(sct, monitor)

        # Reference of empty row
        ref = sum(cropped[-1])

        # Obstacle detection
        cacti_check = sum(cropped[80][40:])
        birb_check = sum(cropped[20][40:])

        # jump over obstacles:
        if cacti_check != ref or birb_check != ref: 
            press("space")
        
        # check if we are speeding up
        if speed_up:

            # every 3 seconds we increase how far we detect objects
            # this compensates for the increasing speed of the game
            current = time()
            if current > start + 3:
                start = current
                width = width + 1
                left = left + 1
                # At this point game should be at max speed 
                if width >= 160:
                    speed_up = False
            
        # imshow("bot view", cropped)
        # if waitKey(1) &0xFF == ord('q'):
        #     break
