from lab1.utils_lab1 import *


def find_equal(arr,v):
    found = []

    for i in range(len(arr)):
        if arr[i] == v:
            found.append(i)

    return found

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

def task4():
    arr, v = read_data(PATH_INPUT)
    found = find_equal(arr,v)
    if len(found) == 0:
        write_data(PATH_OUTPUT, -1)
    else:
        write_data(PATH_OUTPUT, len(found), found)

if __name__ == 'main':
    task4()