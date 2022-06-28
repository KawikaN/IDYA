import ctypes
import os
import keyboard
import time
import win32gui
import mss
import winsound
import pyautogui
import threading
from interception import  *
import constant
import constants
from constants import *
import mouse
import keyboard
import time
import random
from pytesseract import *
import pyautogui
import keyboard
import time
import pyautogui
from pytesseract import *
import random
import win32api, win32con
from PIL import Image


#errors to fix - does not take new photos every loop



def sound():
    winsound.Beep(700, 200)
    winsound.Beep(100, 10)



def offf():
    winsound.Beep(440, 75)
    winsound.Beep(200, 100)


def rgb_of_pixel(img_path, x, y):
    im = Image.open(img_path).convert('RGB')
    r, g, b = im.getpixel((x,y))
    a = (r, g, b)
    return a

dif = (os.stat('Dot.png').st_size)-(os.stat('Dot2.png').st_size)
dif2 = (os.stat('Point.png').st_size)-(os.stat('Point2.png').st_size)
#finds the differences in the image files


# size checks to see if the difference in the image files are big enough in the middle(indicating that there was movemnet at the crosshair)
# but small enough at the top (indicating the entire screen didnt change)
def size():
    point()
    if(dif < 15 and dif > -15):
        print("no change at crosshair")
        return 1
    elif(dif2 < 100 and dif2 > -100):
        if (dif >15 or dif < -15):
            mouse.click() 
            print("clicked")
        print("change")
        return 2
         

    else:
        #turn off triggerbot
        print("No change Same")
        sound()
        global triggerbot
        triggerbot = not triggerbot
        return 






def point():
    im4 = pyautogui.screenshot(region=(955,100,20,20)) #x, y(from top), width, height(down)
    im4.save(r"C:\Users\mnawe_000\Desktop\Idya\Point2.png")
    img4 = "Point2.png"




def dot2():
    im2 = pyautogui.screenshot(region=(955, 535, 15, 15))
    im2.save(r"C:\Users\mnawe_000\Desktop\Idya\Dot2.png")
    img2 = "Dot2.png"
    size()

def ppp():
    print("ppp")


def trigger():
    while (keyboard.is_pressed("7") != True):
        dot2()
        while (size() == 1):
            dot2()
            time.sleep(2)
        if (size() == 2):
            global triggerbot
            triggerbot = not triggerbot
            
            break
        time.sleep(.5)
    else:
        print("trigger off")
        offf()
        triggerbot = not triggerbot

