from constant import *
from time import time, sleep


def selection_sort(self):
    for i in range(len(self.data)):
        for j in range(len(self.data)):
            if self.data[i] < self.data[j]:
                self.data[i], self.data[j] = self.data[j], self.data[i]
                self.Draw([lightGreen if x == i or x ==
                           j else rectBlue for x in range(len(self.data))])
                sleep(self.speedScale.get())
    self.Draw([lightGreen for x in range(len(self.data))])


def bubble_sort(self):
    for i in range(len(self.data)):
        for j in range(len(self.data)-1):
            if self.data[j] > self.data[j+1]:
                self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
                self.Draw([lightGreen if x == j or x == j +
                           1 else rectBlue for x in range(len(self.data))])
                sleep(self.speedScale.get())
    self.Draw([lightGreen for x in range(len(self.data))])


def insertion_sort(self):
    for i in range(len(self.data)):
        for j in range(i+1, len(self.data)):
            if self.data[j] < self.data[i]:
                self.data[j], self.data[i] = self.data[i], self.data[j]
                self.Draw([lightGreen if x == j or x ==
                           i else rectBlue for x in range(len(self.data))])
                sleep(self.speedScale.get())
    self.Draw([lightGreen for x in range(len(self.data))])
