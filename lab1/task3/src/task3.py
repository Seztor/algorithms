from lab1.utils_lab1 import *

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

def reverse_ins_sort(arr):
    for i in range(len(arr)-1):
        while arr[i] < arr[i+1] and i >= 0:
            arr[i+1], arr[i] = arr[i], arr[i+1]
            i -= 1
    return arr

def task3():
    n, arr = read_data(PATH_INPUT)
    write_data(PATH_OUTPUT, reverse_ins_sort(arr))

if __name__ == 'main':
    task3()
