def max_subarray(arr, low, high):
    if low == high:
        return (low,high, arr[low])
    else:
        m = (low+high)//2
        lt_low, lt_high, lt_sum = max_subarray(arr,low,m)
        rt_low, rt_high, rt_sum = max_subarray(arr,m+1,high)
        crs_low, crs_high, crs_sum = max_cross_subarray(arr,low,m,high)
        if lt_sum >= rt_sum and lt_sum >= crs_sum:
            return (lt_low, lt_high, lt_sum)
        elif rt_sum >= lt_sum and rt_sum >= crs_sum:
            return (rt_low, rt_high, rt_sum)
        else:
            return (crs_low, crs_high, crs_sum)


def max_cross_subarray(arr, low, m, high):
    lt_sum = rt_sum = float('-inf')
    temp_sum = 0
    for i in range(m, low-1,-1):
        temp_sum += arr[i]
        if temp_sum > lt_sum:
            lt_sum = temp_sum
            mx_lt = i
    
    temp_sum = 0
    for i in range(m+1, high+1):
        temp_sum += arr[i]
        if temp_sum > rt_sum:
            rt_sum = temp_sum
            mx_rt = i
    return (mx_lt, mx_rt, lt_sum + rt_sum)


if __name__ == '__main__':
    arr = [100,113,110,85,105,102,86,63,81,101,94,106,101,79,94,90,97]
    # a2 = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    # n = int(input())
    # arr = [int(i) for i in input().split()]   
    razn_arr = [j-i for i,j in zip(arr,arr[1:])]
    print(razn_arr)
    print(max_subarray(razn_arr, 0, len(razn_arr)-1))


    # import random, time, psutil
    # n = 10**5
    # arr = [random.randint(-10**4, 10**4) for _ in range(n)]
    # print(f'n={n}')
    # #print(*arr)
    # t_start = time.perf_counter()
    # razn_arr = [j-i for i,j in zip(arr,arr[1:])]
    # print(max_subarray(arr,0,len(arr)-1))
    # print(f"Memory used: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
    # print('Elapsed time: %s sec' % round(time.perf_counter() - t_start, 5))