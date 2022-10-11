#phrases, celebration, trade, auto tricks

import time, keyboard, mouse, pyautogui

recorded = keyboard.record(until='esc') # records until press esc
keyboard.play(recorded) # plays back recording