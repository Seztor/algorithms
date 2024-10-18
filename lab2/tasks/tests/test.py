import pytest
import task1
import task3
import task4
import task5
import random
import task6

def test_mergesort():
    n = 10**5
    arr = [random.randint(1, 10**9) for _ in range(n)]
    arr_c = arr.copy()
    task1.merge_sort(arr,0,len(arr)-1)
    assert arr == sorted(arr_c)

def test_reverse_num():
    arr = [1,8,2,1,4,7,3,2,3,6]
    task3.merge_sort(arr,0,len(arr)-1)
    assert task3.get_answer() == 17

def test_bs():
    n = 10**5
    arr = sorted(set([random.randint(1, 10**9) for _ in range(n)]))
    el = random.choice(arr)
    assert task4.bs(arr,el) == arr.index(el)

def test_majority():
    arr1 = [2,3,9,2,2]
    arr2 = [1,2,3,4]
    assert task5.majority(arr1,0,len(arr1)-1) == 1
    assert task5.majority(arr2,0,len(arr2)-1) == 0

def test_max_subarray():
    arr = [100,113,110,85,105,102,86,63,81,101,94,106,101,79,94,90,97]
    razn_arr = [j-i for i,j in zip(arr,arr[1:])]
    assert task6.max_subarray(razn_arr,0,len(razn_arr)-1) == (7, 10, 43)
