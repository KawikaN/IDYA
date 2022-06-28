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









#get picture of area near crosshair
#if rgb changes then clicks
#if rgb changes eslewhere on the screen then cancel the trigger

SCREEN_X = win32api.GetSystemMetrics(0)
SCREEN_Y = win32api.GetSystemMetrics(1)


triggerbot = False #shoots with movement/enemy 
t2s = False #Speaks out the words since your lazy
vh = False #
bhop = False #hop without thinking
damage = False #reads the damage you dealt for u
character = False #Auto lock that jett
spike = False #do you have enough time to defuse?
autophrase = False #gg's
shortcut = False #tired of typing out the same messages? keybind it
afkbot = False #Free xp? Dont want to be banned while using the bathroom?
loadout = False #might as well let it buy your loadout 4 u too
sing = False #let the bot webscrape for the lyrics to a song and type it in chat

def sound():
    winsound.Beep(700, 200)
    winsound.Beep(100, 10)

def offf():
    winsound.Beep(440, 75)
    winsound.Beep(200, 100)

def onn():
    winsound.Beep(440, 75)
    winsound.Beep(700, 100)

def trigoff():
    offf()
    print("Triggerbot inactive")

def trigon():
    onn()
    print("Triggerbot active")




        


#play sound if triggerbot is active or not




#class Frame
#{
#   cvImage img;
#   uint    idx;
#}

    # also if another area didnt change

#ctrl k c   ctrl k u

# def pic():
#     iml = pyautogui.screenshot(region=(1536,350,44,220))
#     iml.save(r"C:\Users\mnawe_000\Desktop\Idya\Text.png")
#     main()


def main():
    pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\Tesseract.exe'
    imge = Image.open(r'C:\Users\mnawe_000\Desktop\Idya\Text.png')
    output = pytesseract.image_to_string(imge)
    print(output)
    print("made it to the convert")




class CColor:
	Red = '\033[91m'
	Green = '\u001b[32m'
	Yellow = '\u001b[33m'
	Blue = '\u001b[34m'
	Cyan = '\u001b[36m'
	White = '\033[0m'

    

def printgui():
    os.system("cls") 
    Color = CColor()
    print(f"{Color.Yellow}[*]Triggerbot: {Color.Green}{triggerbot}{Color.Yellow} [*]{Color.White}")
    print(f"{Color.Red} - Text2Speach: {Color.Green}{t2s}{Color.Red}{Color.White}")
    print(f"{Color.Red} - Sniper Mode: {Color.Green}{vh}{Color.Red}{Color.White}\r\n")
    print(f"{Color.Yellow}[*]Bhop: {Color.Green}{bhop}{Color.Yellow} [*]{Color.White}")
    print(f"{Color.Yellow}Damage Reader: {Color.Green}{damage}{Color.Yellow} [*]{Color.White}")
    

#call functions here



printgui()










while True:

    if(keyboard.is_pressed("delete")):
        print("Finished !")
        os._exit(1)

    if(keyboard.is_pressed("5")):
        triggerbot = not triggerbot
        print("start")
        if(triggerbot == True):
            onn()
            time.sleep(1)
            im1 = pyautogui.screenshot(region=(955, 535, 15, 15)) #x, y(from top), width, height(down)
            im1.save(r"C:\Users\mnawe_000\Desktop\Idya\Dot.png")
            img = "Dot.png"

            im3 = pyautogui.screenshot(region=(955,100,20,20)) #x, y(from top), width, height(down)
            im3.save(r"C:\Users\mnawe_000\Desktop\Idya\Point.png")
            img3 = "Point.png"

            trigger()
        else:
            
            offf()







