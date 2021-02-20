from time       import sleep
from constant   import *

def selection_sort(arrValues, draw, time):
    for i in range(len(arrValues)):
        for j in range(len(arrValues)):
            if arrValues[i] < arrValues[j]:
                arrValues[i], arrValues[j] = arrValues[j], arrValues[i]
                draw(arrValues, [lightGreen if x==i or x==j else rectBlue for x in range(len(arrValues))])
                sleep(time)
    draw(arrValues, [lightGreen for x in range(len(arrValues))])

def bubble_sort(arrValues, draw, time):
    for i in range(len(arrValues)):
        for j in range(len(arrValues)-1):
                if arrValues[j] > arrValues[j+1]:
                    arrValues[j], arrValues[j+1] = arrValues[j+1], arrValues[j]
                    draw(arrValues, [lightGreen if x==j or x==j+1 else rectBlue for x in range(len(arrValues))])
                    sleep(time)
    draw(arrValues, [lightGreen for x in range(len(arrValues))])

def insertion_sort(arrValues, draw, time):
    for i in range(len(arrValues)):
        for j in range(i+1,len(arrValues)):
                if arrValues[j] < arrValues[i]:
                    arrValues[j], arrValues[i] = arrValues[i], arrValues[j]
                    draw(arrValues, [lightGreen if x==j or x==i else rectBlue for x in range(len(arrValues))])
                    sleep(time)
    draw(arrValues, [lightGreen for x in range(len(arrValues))])