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
from a import * 
import trigs.tring


from damage.dmg import translate

# take a picture  of the textchat where they said the song
# can put in a name to only get the song from a specific person
# picture of textchat will only read so much characters
#https://music.youtube.com/ 

def msc():
    if(input("Do you want to only allow a specific person to enter a song? (y or n)\n") == "y"):
        person = input("What is the name of the person you want to get songs from?")

        if(keyboard.is_pressed('ctrl+3')): # press ctrl + 3
            trigs.poin(955,100,20,20) # screenshot of chat
            chats = translate('\chat.png') # saves screen shot to C\:.... \chat.png
            if(':' in chats):
                #person.find(':')
                #for i in range(person[person.find(':'), person.find(' ')]):
                y = 1
                while(True):
                    #pick = person.find(':') came back after a while and im not sure if person was right so leaving it here just incase it was n i get lost again
                    pick = chats.find(':')
                    if(chats[pick+y] == " "):
                        break
                    new_song = (new_song + chats[pick+y])
                    y = y+1
                return new_song
            

# agent_dict[player["CharacterID"].lower()]    name of player in https://github.com/zayKenyon/VALORANT-rank-yoinker/blob/main/main.py

        print(new_song)
        #song(new_song)  # runs the function of  searching for the song

        
        #take a picture of the text
