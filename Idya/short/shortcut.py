from re import X
from tkinter import Y
import keyboard
import time
import mouse
import pyautogui
import win32api, win32con
import winsound
#GET SHORTCUT PHRASES AND BIND THEM TO KEY

phrases = {}

def sound():
    winsound.Beep(700, 200)
    winsound.Beep(100, 10)

def offf():
    winsound.Beep(440, 75)
    winsound.Beep(200, 100)

def ask():
    ques = input("Do you want to add any phrases?   y/n ")

    if(ques == "y" or ques == "Y"):
        run()
        return 1
    elif(ques == "n" or ques == "N"):
        return 2
    else:
        print("please only respond with y(for yes) or n(for no)")
        return 2



class Phrase:
    def __init__(self, name, key):
        self.name = name
        self.key = key

def run():
    n = int(input('Enter amount of phrases you want to add: '))
    d = {}
    for i in range(n):
        name = input('Enter name: ')
        key = input('What key do you want to bind it to?')
        d[name] = Phrase(name, key)
