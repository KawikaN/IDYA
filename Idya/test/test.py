import ctypes
import os
from re import X
from django.urls import translate_url
import keyboard
import time
import win32api,win32gui
import mss
import PIL.ImageGrab
import PIL.Image
import winsound
import pyautogui
import threading
from interception import  *
from constants import *
from PIL import Image
import PIL
from pytesseract import *
import keyboard
import random
import win32api, win32con
import time
from photos import *


while translate_url:

    def dot2(): #gets and stores image as Dot2
        im2 = pyautogui.screenshot(region=(955, 535, 15, 15))
        im2.save(r"C:\Users\mnawe_000\Desktop\Idya\Dot2.png")
        img2 = "Dot2.png"

    dot2()
    dif = (os.stat('Dot.png').st_size)-(os.stat('Dot2.png').st_size)
    print(dif)

    
    