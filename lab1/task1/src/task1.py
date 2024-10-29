from lab1.utils_lab1 import *

def ins_sort(arr):
    for j in range(1, len(arr)):
        i = j-1
        k = arr[j]
        while arr[i] > k and i >= 0:
            arr[i+1] = arr[i]
            i = i-1
        arr[i+1] = k
    return arr

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

def task1():
    n, arr = read_data(PATH_INPUT)
    write_data(PATH_OUTPUT, ins_sort(arr))

if __name__ == 'main':
    task1()



