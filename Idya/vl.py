#unused for now: ctypes, win32gui, mss, threading, constant, constants, mouse, random, win32con, trigs
try:
    import os, keyboard, time, winsound, pyautogui, keyboard, win32api, trigs
    from interception import  *
    from constants import *
    from pytesseract import *
    from PIL import Image
    from trigs import * #trigs is a package 
    from short import *
    from short.shortcut import Phrase
    from short.shortcut import *
    from lazy.afk import *
except:
    print("There was an error trying to import the required files, check required.txt for the required libraries")

#get picture of area near crosshair
#if rgb changes then clicks
#if rgb changes eslewhere on the screen then cancel the trigger

SCREEN_X = win32api.GetSystemMetrics(0)
SCREEN_Y = win32api.GetSystemMetrics(1)

def sound():
    winsound.Beep(700, 200)
    winsound.Beep(100, 10)

def offf(): #plays off sound
    winsound.Beep(440, 75)
    winsound.Beep(200, 100)

def onn(): #plays on sound
    winsound.Beep(440, 75)
    winsound.Beep(700, 100)

def main():
    pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\Tesseract.exe'
    imge = Image.open(r'C:\Users\mnawe_000\Desktop\Idya\Text.png')
    output = pytesseract.image_to_string(imge)
    print(output)
    print("made it to the convert")

class CColor: #defines the color for the os system output in printgui
	Red = '\033[91m'
	Green = '\u001b[32m'
	Yellow = '\u001b[33m'
	Blue = '\u001b[34m'
	Cyan = '\u001b[36m'
	White = '\033[0m'

def printgui():
    os.system("cls")  #clears the terminal
    #put a thin to say the keybinds
    Color = CColor() 
    print(f"{Color.Yellow}[*]Triggerbot: {Color.Green}{triggerbot}{Color.Yellow} [*]{Color.White}")
    print(f"{Color.Red} - Shortcut: {Color.Green}{t2s}{Color.Red}{Color.White}")
    print(f"{Color.Red} - Sniper Mode: {Color.Green}{vh}{Color.Red}{Color.White}\r\n")
    print(f"{Color.Yellow}[*]Bhop: {Color.Green}{bhop}{Color.Yellow} [*]{Color.White}")
    print(f"{Color.Yellow}Damage Reader: {Color.Green}{damage}{Color.Yellow} [*]{Color.White}") 
    sound()
    #messages that print out when we call this function(printgui)
    
#call functions you want to run here because there is a while loop forever after(will not run after loop)

printgui()

while True: 
    if(keyboard.is_pressed("delete")): #press delete to kill the program5
        print("Finished !")
        os._exit(1)

    if(keyboard.is_pressed("5")): #press 5 to start triggerbot
        triggerbot = True
        print("starting")
        onn()
        im1 = pyautogui.screenshot(region=(955, 535, 15, 15)) #x, y(from top), width, height(down)
        im1.save(r"C:\Users\mnawe_000\Desktop\Idya\Dot.png")

        im3 = pyautogui.screenshot(region=(955,100,20,20)) #x, y(from top), width, height(down)
        im3.save(r"C:\Users\mnawe_000\Desktop\Idya\Point.png")

        trigger() #run trigger function in trig.py file in trigs package
        

        #uses while loop so make sure this is the last thing you want to enable wont be able to access anything else after
    if(keyboard.is_pressed("4")): #press 4 to start shortcut
        shortcut = True
        print("starting")
        onn()
        
        ask()

        if(keyboard.is_pressed("ctrl+4")):
            run() #press ctrl + 4 to add shortcuts
    if(shortcut == True): # in while loop so it will keep checking this
        for name in dict: # iterates throguh dictionary to look at all the keys
            if(keyboard.is_pressed(dict[name])): # if the key is pressed
                print(dict[name], "Pressed")
                keyboard.press_and_release('t') # opens text chat
                keyboard.press_and_release("/") 
                keyboard.press_and_release(ct[name]) # presses the chat u want it in
                keyboard.write(name) # writes the phrase
                keyboard.press_and_release("enter")
                print("Said: ", name)

    if(keyboard.is_pressed("6")):
        afk = True
        print("Starting")
        onn()

        afks()
