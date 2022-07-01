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
import trigs
from trigs import * #trigs is a package 
from trigs import difs

dif = (os.stat('Dot.png').st_size)-(os.stat('Dot2.png').st_size)
dif2 = (os.stat('Point.png').st_size)-(os.stat('Point2.png').st_size)

triggerbot = True

while True:
    if(dif < 15 and dif > -15): #if the difference is not big then return 1
        print("no change at crosshair")
    elif(dif2 < 100 and dif2 > -100): #if the difference for dif is big then check if there was change at point
        if (dif >15 or dif < -15): 
            mouse.click() #click to fire if all perameters were met
            print("clicked")
        print("change")
        

    else:
        #turn off triggerbot
        print("No change Same")

