import time
import copy
from numpy.random import seed
from numpy.random import randint
import numpy as np
import matplotlib.pyplot as plt
import random

def main():
    elements = list()
    times = list()
    merge_sort_times = list()
    insertion_sort_times = list()
    run_experiment(elements, times, merge_sort_times, insertion_sort_times)
    plt.xlabel('List Length')
    plt.ylabel('Time Complexity')
    plt.xticks(np.arange(100, 2100, 100))
    plt.plot(elements, times, label = 'Custom Sort')
    plt.plot(elements, merge_sort_times, label = 'Merge Sort')
    plt.plot(elements, insertion_sort_times, label = 'Insertion Sort')
    plt.grid()
    plt.legend()
    plt.show()

def run_experiment(elements, custom_algo_times, merge_sort_times, insertion_sort_times):
   for i in range(1, 21):
        a = randint(0, 1000 * i, 100 * i)
        b = copy.deepcopy(a)
        c = copy.deepcopy(a)

        start = time.clock()
        custom_sort(a)
        end = time.clock()

        merge_start = time.clock()
        merge_sort(b)
        merge_end = time.clock()

        insertion_start = time.clock()
        insertion_sort(c)
        insertion_end = time.clock()
        
        elements.append(len(a))
        custom_algo_times.append(end-start)
        merge_sort_times.append(merge_end-merge_start)
        insertion_sort_times.append(insertion_end-insertion_start)

def custom_sort(Data):
    if(len(Data) <= 1000):
        insertion_sort(Data)
    else:
        merge_sort(Data)
    return Data

def insertion_sort(Data):
    length = len(Data)
    for j in range(1, length):
        key = Data[j]
        i=j-1
        while((i>=0) and (Data[i]>key)):
            Data[i+1] = Data[i]
            i=i-1
        Data[i+1] = key
    return Data

def merge_sort(data):
    if len(data)>1:
        mid = len(data)//2
        left_half = data[:mid]
        right_half = data[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k]=left_half[i]
                i = i+1
            else:
                data[k]=right_half[i]
                j=j+1
            k=k+1
        while i < len(left_half):
            data[k]=left_half[i]
            i=i+1
            k=k+1
        while j < len(right_half):
            data[k] = right_half[j]
            j=j+1
            k=k+1

if __name__ == "__main__":
    main()
