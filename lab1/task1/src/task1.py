from lab1.utils_lab1 import *

def task1():
    n, arr = read_data('../txtf/input.txt')
    write_data('../txtf/output.txt', ins_sort(arr))

def ins_sort(arr):
    for j in range(1, len(arr)):
        i = j-1
        k = arr[j]
        while arr[i] > k and i >= 0:
            arr[i+1] = arr[i]
            i = i-1
        arr[i+1] = k
    return arr

