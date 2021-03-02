from random import randint, seed, shuffle
import tkinter as tk
import tkinter.ttk as ttk
from constant import *
from algos import *


def Generate(self):
    self.data.clear()
    self.rectangles.clear()
    min_value = int(self.minEntry.get())
    max_value = int(self.maxEntry.get())
    size = int(self.sizeEntry.get())
    for i in range(size):
        self.data.append(randint(min_value, max_value))
    shuffle(self.data)
    self.Draw([rectBlue for x in range(len(self.data))], generate_flag=True)


def Start(self):
    self.stop = False
    if (self.algorithm_menu.get() == 'SELECTION'):
        selection_sort(self)
    elif (self.algorithm_menu.get() == 'BUBBLE'):
        bubble_sort(self)
    elif (self.algorithm_menu.get() == 'INSERTION'):
        insertion_sort(self)
    elif (self.algorithm_menu.get() == 'QUICKSORT'):
        quick_sort(self, self.data, 0, len(self.data)-1)
    self.Draw([lightGreen for x in range(len(self.data))], generate_flag=True)
