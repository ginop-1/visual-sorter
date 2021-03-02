from constant import *
from time import time, sleep


def selection_sort(self):
    for i in range(len(self.data)):
        for j in range(len(self.data)):
            if self.stop: return
            if self.data[i] < self.data[j]:
                self.data[i], self.data[j] = self.data[j], self.data[i]
                self.Draw([lightGreen if x == i or x ==
                           j else rectBlue for x in range(len(self.data))])
                sleep(self.speedScale.get())


def bubble_sort(self):
    for i in range(len(self.data)):
        for j in range(len(self.data)-1):
            if self.stop: return
            if self.data[j] > self.data[j+1]:
                self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
                self.Draw([lightGreen if x == j or x == j +
                           1 else rectBlue for x in range(len(self.data))])
                sleep(self.speedScale.get())


def insertion_sort(self):
    for i in range(len(self.data)):
        for j in range(i+1, len(self.data)):
            if self.stop: return
            if self.data[j] < self.data[i]:
                self.data[j], self.data[i] = self.data[i], self.data[j]
                self.Draw([lightGreen if x == j or x ==
                           i else rectBlue for x in range(len(self.data))])
                sleep(self.speedScale.get())

# quick_sort


def quick_sort(self, arr, low, high):
    def partition(self, arr, low, high):
        i = (low-1)
        pivot = arr[high]

        for j in range(low, high):
            if self.stop: return -1
            if arr[j] <= pivot:
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
                self.Draw(get_color(int(self.sizeEntry.get()), j, high, i))
                sleep(self.speedScale.get())

        arr[i+1], arr[high] = arr[high], arr[i+1]
        self.Draw(get_color(int(self.sizeEntry.get()), i+1, high))
        return (i+1)
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(self, arr, low, high)
        if pi == -1: return
        quick_sort(self, arr, low, pi-1)
        quick_sort(self, arr, pi+1, high)


def get_color(len, iterable=None, pivot=None, low=None):
    color = []
    for i in range(0, len):
        # print("get_color " + str(i))
        if i == iterable:
            color.append(lightGreen)
        elif i == pivot:
            color.append(white)
        elif i == low:
            color.append(yellow)
        else:
            color.append(rectBlue)
    return color
