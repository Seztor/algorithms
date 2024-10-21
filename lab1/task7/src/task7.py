from lab1.utils_lab1 import *

def task7():
    n, arr = read_data('../txtf/input.txt', arr_num_type=float)
    arr = [(item,ind+1) for ind,item in enumerate(arr)]
    
    for j in range(1, len(arr)):
        i = j-1
        k = arr[j]
        while arr[i][0] > k[0] and i >= 0:
            arr[i+1] = arr[i]
            i = i-1
        arr[i+1] = k

    write_data("../txtf/output.txt", (arr[0][1], arr[n//2][1], arr[-1][1]))
