import keyboard, pyautogui, mouse, time, win32, win32api

#on - ask if they want to add a loadout. yes - ask name. no - wait for key press. say how to turn on
#after name - run look. set cords to name. 
x = 0
#ask if want to add .get key that opens close menue and after key clicks run it check for click 

#detect start of round and buy loadout


menue = "b"
on = False

def con():
    while(True):
        askon = input(str("Do you want IDYA to auto buy your loadout?\n"))
        if(askon == "y"):
            on = True
        elif(askon == "n"):
            on = False
            break
        else:
            print('Invalid input: only enter "y" for yes and "n" for no')
        if(x == 4):
            print("Failed entry 5 times. Please press 7 to rerun the loadout feature")
            on = False
            print("Press ")
            break
        x = x+1

def cl():
    while(True):
        askk = input(str("Do you want to add a loadout?\n (y = yes n = no)\n"))
        if(askk == "y"):
            load()
        elif(askk == "n"):
            break
        else:
            print('Invalid input: only enter "y" for yes and "n" for no')
        if(x == 4):
            print("Failed entry 5 times. Please press 7 to rerun the loadout feature")
            loadout = False
            break
        x = x+1

press = 0
test = 0

def load():
    while(True):
        lox = []
        loy = []
        if(keyboard.is_pressed("l")):#press L to check
            print("Watching you buy")
            while(True):
                if(keyboard.is_pressed(menue)):
                    while(True):
                        if win32api.GetKeyState(0x01)<0:# if click
                            pos = mouse.get_position()[0]
                            lox.append(pos)
                            pos = mouse.get_position()[1]
                            loy.append(pos)
                            press = press+1
                        if(keyboard.is_pressed(menue)):
                            return lox, loy, press

#if they open the menue then buy the shit
def chlo(x, y, p):#if on then run through each index of lo(position of mouse) and click to buy loadout
    if(on == True):
        #dissable mouse and menue key for now
        keyboard.press_and_release(menue)
        for k in range(p):
            mouse.move(x[k], y[y])
            mouse.click()
        keyboard.press_and_release(menue)
        print("bought")



# use mouse.get_position() when u press a button to find the position of mouse on the buy loadout screen