from pytesseract import *
import pyautogui
from PIL import Image
import keyboard
import time
from PIL import ImageGrab
import pyautogui
from pytesseract import *
import random
import win32api, win32con


SCREEN_X = win32api.GetSystemMetrics(0)
SCREEN_Y = win32api.GetSystemMetrics(1)


time.sleep(5)
print("hell")

def rgb_of_pixel(img_path, x, y):
    im = Image.open(img_path).convert('RGB')
    r, g, b = im.getpixel((x,y))
    a = (r, g, b)
    return a


def dot():
    while 1:
        time.sleep(1)
        im1 = pyautogui.screenshot(region=(1787,301,100,10))
        im1.save(r"C:\Users\mnawe_000\Desktop\Val_S\Dot.png")
        img = "Dot.png"
        if rgb_of_pixel(img, 0, 0) == (255, 255, 255):
            pic()


def pic():
    iml = pyautogui.screenshot(region=(1536,350,44,220))
    iml.save(r"C:\Users\mnawe_000\Desktop\Val_S\Text.png")
    main()



def main():
    pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\Tesseract.exe'
    imge = Image.open(r'C:\Users\mnawe_000\Desktop\Val_S\Text.png')
    output = pytesseract.image_to_string(imge)
    print(output)
    print("made it to the convert")




dot()