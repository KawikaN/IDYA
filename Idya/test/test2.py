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

def im():
    im4 = pyautogui.screenshot(region=(955, 535, 100, 100)) #x, y(from top), width, height(down)
    im4.save(r"C:\Users\mnawe_000\Desktop\Idya\test\L.png")
    img4 = "L.png"
    print("done")
im()