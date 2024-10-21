from lab1.utils_lab1 import *

def task3():
    n, arr = read_data('../txtf/input.txt')
    write_data('../txtf/output.txt', reverse_ins_sort(arr))

def reverse_ins_sort(arr):
    for i in range(len(arr)-1):
        while arr[i] < arr[i+1] and i >= 0:
            arr[i+1], arr[i] = arr[i], arr[i+1]
            i -= 1
    return arr