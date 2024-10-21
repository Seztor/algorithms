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

if __name__ == '__main__':
    # n = int(input())
    # arr_n = [int(i) for i in input().split()]
    # k = int(input())
    # arr_k = [int(i) for i in input().split()]

    # for el in arr_k:
    #     print(bs(arr_n,el), end=' ')

    import random, time, psutil
    n = 10**5
    k = 10**5
    arr_n = sorted([random.randint(1, 100) for _ in range(n)])
    arr_k = [random.randint(1, 100) for _ in range(k)]
    print(f'n={n}, k={k}')
    #print(*arr)
    t_start = time.perf_counter()
    # for el in arr_k:
    #     print(bs(arr_n,el), end=' ')
    # print()
    print(f"Memory used: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
    print('Elapsed time: %s sec' % round(time.perf_counter() - t_start, 5))