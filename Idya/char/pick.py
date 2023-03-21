import keyboard, pyautogui, mouse, time, win32api

agents = {}# dictionary with agent name and location
# since 2 values per key set the values inside a list []
def findd():
    while True:
        print("Place your mouse on the cahracter and press h to save the chords of the character \n")
        if (keyboard.is_pressed("h")):#win32api.GetKeyState(0x01)<0:# if click
            lox = mouse.get_position()[0]
            loy = mouse.get_position()[1]
            return lox, loy


def agent(x, y):
    name = input("What is the name of the agent you want to add \n")
    agents[name] = [x, y]
    return agents[name]




findr = (findd()[0], findd()[1])# creates a tuple with the results to be able to be called when printing
agent(findr[0], findr[1])
print(''.join(agents), "set to", *findr)

