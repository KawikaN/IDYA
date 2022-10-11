from re import X
from tkinter import Y
import keyboard
import time
import mouse
import pyautogui
import win32api, win32con
import winsound

#GET SHORTCUT PHRASES AND BIND THEM TO KEY




phrases = {} # store phrases so that even if they add later we can still look for old key presses
ct = {} #store name and chat to see which chat they want it typed in
dict = {} # save name and key to know what key to look for



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
        ask() # 2 lazy to make new funct for ques
        return 2
        


def find(name, key):
    chat = input('What chat do you want it typed in? (a = all) (t = team)')
    if(chat != "a" and chat != "t"): # if they dont put in a or t run again(recursion)
        find(name, key)
    ct[name] = chat # state that name will = chat in ct dictionary

    return chat


def run(): # run the questions
    n = int(input('Enter amount of phrases you want to add: '))
    for i in range(n): # loop # of phrases they want to add
        name = input('Enter phrase(name): ')
        key = input('What key do you want to bind it to?')
        find(name, key)
        dict[name] = key
        





# class Phrase:
#     def __init__(self, name, key): #everytime we create a object(instance) than things within run
#         self.name = name
#         self.key = key
#         print("Waiting for key presses(press backspace to stop)")
#         while(keyboard.is_pressed("backspace") != True): #press backspace to stop the loop
#             if(keyboard.is_pressed(self.key)): #could not find a way for it to run 1 check then skip an iteration and run the main loop in the main(vl.py) file
#                 print(self.name)
#                 continue
#         print("Done with phrases")

