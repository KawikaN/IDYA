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
from PIL import *
import winsound
import pyautogui  as pg
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
import mouse
import cv2
import numpy as np
import pyautogui
import json
import time
msg = "\\"
print("tjis " + msg)
# print("This is a \ msg")

# s = "Kawika"
# print(s.find("a"))


# name = "\hi.png"
# #print("." + name)
# im4 = pyautogui.screenshot(region=(955,100,20,20)) #x, y(from top), width, height(down)
# im4.save(r'C:\Users\mnawe_000\Desktop\Idya\pics' + name)
# Image.open(r'C:\Users\mnawe_000\Desktop\Idya\pics' + name)


# time.sleep(2)
# im2 = pyautogui.screenshot(region=(1850, 67, 2, 2))
# im2.save(r"C:\Users\mnawe_000\Desktop\Idya\pics\Dot2.png")
#1851, 68

# filename = "test"
# new_title = "test"
# extension = "png"
# folder_to_track = 'C:\Users\mnawe_000\Desktop\Idya\pics'
# new_name = folder_to_track + "/" + str(new_title + "." + extension)
# os.rename(folder_to_track + "/" + filename, new_name)

# iz = "Dot2"
# def dot2(name, pic): #gets and stores image as Dot2
#     name = pyautogui.screenshot(region=(955, 535, 15, 15))
#     return name.save(r"C:\Users\mnawe_000\Desktop\Idya\pics\ "+iz+" .png")

# dot2(img2, dc)
# testing = "word"
# letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# if testing[0].lower() in letters:
#     print("is")




# for i in range(5):
#     if(i == 2):
#         break
#     print('hi')

# im = cv2.imread('Text.png')

# # Define lower and upper limits of our blue
# BlueMin = np.array([90,  200, 200],np.uint8)
# BlueMax = np.array([100, 255, 255],np.uint8)

# # Go to HSV colourspace and get mask of blue pixels
# HSV  = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
# mask = cv2.inRange(HSV, BlueMin, BlueMax)

# # Make all pixels in mask white
# im[mask>0] = [255,255,255]
# cv2.imwrite('Text.png', im)


# # Try dilating (enlarging) mask with 3x3 structuring element
# SE   = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
# mask = cv2.dilate(mask, kernel, iterations=1)

# # Make all pixels in mask white
# im[mask>0] = [255,255,255]
# cv2.imwrite('Text.png', im)






# print('--'.join(agents))


# dict = {}

# name = "kawika"
# age = 5
# height = 5.5


# dict[name] = [age, height]

# print(dict)

#ctrl k c to comment    ctrl k u to uncomment

# while True:
#     if win32api.GetKeyState(0x01)<0:# if mouse is pressed
#         print('h')
#     print('j')
#     time.sleep(0.5)


# l = 3
# for k in l:
#     print("hi")



# print(mouse.get_position()[0])



# pos = pg.position()[0]

# print(pos)




#while True:

    # def dot2(): #gets and stores image as Dot2
    #     im2 = pyautogui.screenshot(region=(955, 535, 15, 15))
    #     im2.save(r"C:\Users\mnawe_000\Desktop\Idya\Dot2.png")
    #     img2 = "Dot2.png"

    # dot2()
    # dif = (os.stat('Dot.png').st_size)-(os.stat('Dot2.png').st_size)
    # print(dif)



# def c1():
#     print("1")
# def c2():
#     print("2")
# def c3():
#     print("3")
# def c4():
#     print("4")
# def c5():
#     print("hi")

# def gc():
#     g = "c"+str(random.randrange(1, 5))
#     t = str(g.replace(" ",""))
#     print()
#     l = globals()[t]()
#     return l

# for i in range(random.randint(0, 5)):
#     gc()

# start = time.time()

# for i in range(1):
#     keyboard.press('ctrl')


# end = time.time()

# total = end-start
# print(total)