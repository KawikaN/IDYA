import keyboard, pyautogui, mouse, time, win32api

agents = {}# dictionary with agent name and location
# since 2 values per key set the values inside a list []
def findd():
    while True:
        if win32api.GetKeyState(0x01)<0:
            lox = mouse.get_position()[0]
            loy = mouse.get_position()[1]
            return lox, loy
def agent(x, y):
    name = input("What is the name of the agent you want to add \n")
    agents[name] = [x, y]

agent(findd()[0], findd()[1])

print(''.join(agents), "set to ", ''.join(agents.values())) # failes to output just the value but will keys
