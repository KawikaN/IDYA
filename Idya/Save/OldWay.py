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
import shutil
#errors to fix -  import file

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
def rgb_of_pixel(img_path, x, y):
    im = Image.open(img_path).convert('RGB')
    r, g, b = im.getpixel((x,y))
    a = (r, g, b)
    return a #useless to me for the time being(grabs rgb values of any given pixle)




def dot2(): #gets and stores image as Dot2
    im2 = pyautogui.screenshot(region=(955, 535, 15, 15))
    im2.save(r"C:\Users\mnawe_000\Desktop\Idya\Dot2.png")

# size checks to see if the difference in the image files are big enough in the middle(indicating that there was movemnet at the crosshair)
# but small enough at the top (indicating the entire screen didnt change)
def size():
    point()
    dif = (os.stat('Dot.png').st_size)-(os.stat('Dot2.png').st_size)#defined here because I can...
    dif2 = (os.stat('Point.png').st_size)-(os.stat('Point2.png').st_size)
    print(dif)
    print(dif2)
                #dot between 0-15 or -15-0
    if(dif < 15 and dif >= 0 or dif > -15 and dif <= 0): #if the difference is not big then return 1
        return 1
                #point between 0-100 or -100-0
    elif(dif2 < 100 and dif2 >= 0 or dif2 > -100 and dif2 <= 0): #if the difference for dif is big then check if there was change at point
        if (dif >15 or dif < -15): 
            mouse.click() #click to fire if all perameters were met
        return 2
    else:
        #turn off triggerbot
        sound()
        global triggerbot
        triggerbot = False

def point():
    im4 = pyautogui.screenshot(region=(955,100,20,20)) #x, y(from top), width, height(down)
    im4.save(r"C:\Users\mnawe_000\Desktop\Idya\Point2.png")
    #gets and stores image as Point2

def shot():
    os.remove(r"C:\Users\mnawe_000\Desktop\Idya\Dot.png", dir_fd=None)
    os.remove(r"C:\Users\mnawe_000\Desktop\Idya\Dot2.png", dir_fd=None)
    os.remove(r"C:\Users\mnawe_000\Desktop\Idya\Point.png", dir_fd=None)
    os.remove(r"C:\Users\mnawe_000\Desktop\Idya\Point2.png", dir_fd=None)

def trigger():  
    dot2()
    while (size() == 1): #if the size function returns 1 run dot again and keep looping
        if(keyboard.is_pressed("ctrl+f") == True): # if ctrl+f is pressed -> breaks
            print("trigger off") 
            offf()
            global triggerbot
            triggerbot = False
            shot()
            break
        dot2()
    if (size() == 2): #if the size function returns 2 then kill the loop cause it fired
        triggerbot = False
        shot()
