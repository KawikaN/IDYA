import pyautogui
import mouse
import keyboard
import time
import win32
import win32api

time.sleep(2)
while(True):
    if(win32api.GetKeyState(0x01)<0):
        print(mouse.get_position())
        time.sleep(0.1)


(1639, 345)
#60
(1639, 405)
#60
(1639, 465)
#60
(1639, 525)
#60-y

#second character(kayo)
(1688, 452) # bottome right
(1639, 453) # bottom left
#49 -x 