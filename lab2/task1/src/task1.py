def merge_sort(arr, p, r):
    if p < r:
        q = (p+r)//2
        merge_sort(arr,p,q)
        merge_sort(arr,q+1,r)
        merge(arr, p, q, r)
    
def merge(arr, p, q, r):
    arr1 = arr[p:q+1]
    arr2 = arr[q+1:r+1]
    
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[p+i+j] = arr1[i]
            i += 1
        else:
            arr[p+i+j] = arr2[j]
            j += 1
    
    while i < len(arr1):
        arr[p+i+j] = arr1[i]
        i += 1
    
    while j < len(arr2):
        arr[p+i+j] = arr2[j]
        j += 1
    
    # print(f'p:{p} q:{q} r:{r} | arr1:{arr1} arr2:{arr2} | {arr}' )

from lab2.utils_lab2 import *

def task1():
    n, arr = read_data('../txtf/input.txt')
    merge_sort(arr,0,len(arr)-1)
    write_data("../txtf/output.txt", arr)



        

        