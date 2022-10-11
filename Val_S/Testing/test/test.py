
import colorama
from termcolor import cprint, colored
from pyfiglet import Figlet
from pynput.mouse import Controller, Button
from pynput import mouse
import numpy as np

import time
import keyboard
import win32gui
import win32api
import os
import ctypes


class stat():
    def __init__ (self, weight, height):
        self.w = weight
        self.h = height
    def values(self):
        values = (self.w, self.h)
        return values

class person(stat):
    def __init__(self, name):
        self.name = name



def hello():
    print("hello")

p1 = stat(132, 5-2)
print(p1.values())

SCREEN_X = win32api.GetSystemMetrics(0)
print(SCREEN_X)