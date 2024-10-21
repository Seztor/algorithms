def bs(arr, key):
    lt = -1
    rt = len(arr)
    while rt - lt > 1:
        m = (rt+lt) // 2
        if key > arr[m]:
            lt = m
        else:
            rt = m

    if rt < len(arr) and arr[rt] == key:
        return rt
    else:
        return -1


from lab2.utils_lab2 import *

def task4():
    n, arr_n, k, arr_k = read_data('../txtf/input.txt')
    ans_arr = [bs(arr_n,el) for el in arr_k]
    write_data("../txtf/output.txt", ans_arr)

