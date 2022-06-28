import ctypes
import os
from re import X
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





dif2 = (os.stat('Point.png').st_size)-(os.stat('Point2.png').st_size)
print(dif2)

dif = (os.stat('Dot.png').st_size)-(os.stat('Dot2.png').st_size)
print(dif)