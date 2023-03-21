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
import cv2
import numpy as np


SCREEN_X = win32api.GetSystemMetrics(0)
SCREEN_Y = win32api.GetSystemMetrics(1)


#time.sleep(2)



def dot():
    while 1:
        time.sleep(1)
        im1 = pyautogui.screenshot(region=(1787,301,100,10))
        im1.save(r"C:\Users\mnawe_000\Desktop\Idya\pics\Pic.png")
        img = r"C:\Users\mnawe_000\Desktop\Idya\pics\Pic.png"
        if rgb_of_pixel(img, 0, 0) == (255, 255, 255):
            print("taking pick")
            pic()
            break

def rgb_of_pixel(img_path, x, y):
    im = Image.open(img_path).convert('RGB')
    r, g, b = im.getpixel((x,y))
    a = (r, g, b)
    return a

def pic():
    iml = pyautogui.screenshot(region=(1536,350,50,220))
    iml.save(r"C:\Users\mnawe_000\Desktop\Idya\pics\Text.png")
    main()


def main():
    pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\Tesseract.exe'
    imge = Image.open(r'C:\Users\mnawe_000\Desktop\Idya\pics\Text.png')
    output = pytesseract.image_to_string(imge)
    print(output)
    print("made it to the convert")

    for i in range(output.count("KILLED")):
        iml = pyautogui.screenshot(region=(1639, 525+((i+1)*10), 50, 50))
        iml.save(r"C:\Users\mnawe_000\Desktop\Idya\pics\Crec.png")
        print("loop")
        y = (1639, (525+((i+1)*10)), 50, 50)
        yy = region=(1639, (525+(i*10)), 50, 50)
        if(pyautogui.locateOnScreen(r"C:\Users\mnawe_000\Desktop\Idya\pics\RazePFP.png", yy, grayscale=True, confidence=0.8) != None):
            #(525+((i+1)*10))
            #(1639, 525, 50, 50)
            print("Raze")





dot()