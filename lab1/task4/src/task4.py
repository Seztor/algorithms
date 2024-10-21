from lab1.utils_lab1 import *

def task4():
    arr, v = read_data('../txtf/input.txt')

    found = []

    for i in range(len(arr)):
        if arr[i] == v:
            found.append(i)

    if len(found) == 0:
        write_data("../txtf/output.txt", -1)
    else:
        write_data("../txtf/output.txt", len(found), found)

