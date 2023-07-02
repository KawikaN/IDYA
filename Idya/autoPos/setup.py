#auto setup (only with keybaord tho), positioning, automative movements

import time, keyboard, mouse, pyautogui

recorded = keyboard.record(until='esc') # records until press esc
keyboard.play(recorded) # plays back recording

