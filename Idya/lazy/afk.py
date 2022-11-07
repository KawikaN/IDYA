
import keyboard, time, mouse, pyautogui, random
from random import getrandbits

# make if in a casual it uses abilities 
# buys loadouts

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def brb(): # keeps you afk (run games)
    pass

def c1(): # each a different and unique order of key presses
    mouse.press()
    time.sleep(.5)
    mouse.release()
def c2():
    keyboard.press(2)
    keyboard.press('y') # try to find the settings data (tried files not there, try using api)
def c3():
    for i in range(random.randint(1,5), 5):
        keyboard.KEY_DOWN('control')
        time.sleep(i)
        keyboard.KEY_UP('control')
def c4():
    keyboard.press('t')
    keyboard.press('/')
    if(getrandbits(1) == 0):
        keyboard.press('a')
    else:
        keyboard.press('t')

def c5():
    for x in range(1, 10):
        keyboard.press('space')

def gc():
    g = "c"+str(random.randrange(1, 5))
    t = str(g.replace(" ",""))
    print()
    l = globals()[t]()
    return l

def afks():
    while(keyboard.is_pressed('delete') != True):
        choice = random.randint(1, 5)
        if(choice == 1):
            pyautogui.keyDown('w')
            time.sleep(random.randint(1, 4))
            if(getrandbits(1) == 0):
                pyautogui.keyUp('w')
            for i in range(random.randint(0, 5)):
                gc()
            pyautogui.keyUp('w')

        if(choice == 2):
            pyautogui.keyDown('a')
            time.sleep(random.randint(1, 4))
            if(getrandbits(1) == 0):
                pyautogui.keyUp('a')
            for i in range(random.randint(0, 5)):
                gc()
            pyautogui.keyUp('a')

        if(choice == 3):
            pyautogui.keyDown('s')
            time.sleep(random.randint(1, 4))
            if(getrandbits(1) == 0):
                pyautogui.keyUp('s')
            for i in range(random.randint(0, 5)):
                gc()
            pyautogui.keyUp('s')

        if(choice == 4):
            pyautogui.keyDown('d')
            time.sleep(random.randint(1, 4))
            if(getrandbits(1) == 0):
                pyautogui.keyUp('d')
            for i in range(random.randint(0, 5)):
                gc()
            pyautogui.keyUp('d')

        if(choice == 5):
            
            if(getrandbits(1) == 0):
                pass
            for i in range(random.randint(0, 5)):
                gc()