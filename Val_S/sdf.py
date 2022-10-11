from pytesseract import *
import pyautogui
from PIL import Image
import keyboard
import time
from PIL import ImageGrab
import pyautogui
from pytesseract import *

def pic():
    im1 = pyautogui.screenshot(region=(1787,301,1,1))
    im1.save(r"C:\Users\mnawe_000\Desktop\Val_S\Dot.png")

pic()