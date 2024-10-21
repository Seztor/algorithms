def majority(arr, lt, rt):
    if lt == rt:
        return arr[lt]
    
    m = (lt+rt) // 2

    lt_item = majority(arr, lt, m)
    rt_item = majority(arr, m+1, rt)

    cnt_lt_item = arr[lt:m+1].count(lt_item)
    cnt_rt_item = arr[m+1:rt+1].count(rt_item)

    #print(f'lt:{lt} m:{m} rt:{rt} | {lt_item}:{cnt_lt_item} - {rt_item}:{cnt_rt_item}' )

    if lt == 0 and rt == len(arr)-1:
        full_arr_lt_cnt = arr.count(lt_item)
        full_arr_rt_cnt = arr.count(rt_item)
        if lt_item != rt_item:
            if max(full_arr_lt_cnt, full_arr_rt_cnt) > len(arr)//2:
                return 1
            else:
                return 0
        else:
            return int(full_arr_lt_cnt > len(arr)//2)
    else:
        if cnt_lt_item >= cnt_rt_item:
            return lt_item
        else:
            return rt_item


from lab2.utils_lab2 import *

def task5():
    n, arr = read_data('../txtf/input.txt')
    is_majority = majority(arr, 0, len(arr) - 1)
    write_data("../txtf/output.txt", is_majority)


