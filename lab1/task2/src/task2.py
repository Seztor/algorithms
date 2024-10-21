from lab1.utils_lab1 import *

def ins_sort_2(arr):
    ind_arr = [-1] * len(arr)
    ind_arr[0] = 1
    for j in range(1, len(arr)):
        i = j - 1
        k = arr[j]
        while arr[i] > k and i >= 0:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = k
        ind_arr[j] = i + 2
    return ind_arr, arr

def task2():
    n, arr = read_data('../txtf/input.txt')
    write_data('../txtf/output.txt', *ins_sort_2(arr))
