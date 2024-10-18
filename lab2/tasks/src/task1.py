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

if __name__ == '__main__':
    #n = int(input())
    #arr = [int(i) for i in input().split()]
    import random, time, psutil
    n = 5
    arr = [random.randint(1, 10**2) for _ in range(n)]
    
    print(f'n={n}')
    print(*arr)
    t_start = time.perf_counter()
    merge_sort(arr,0,len(arr)-1)
    print(f"Memory used: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
    print('Elapsed time: %s sec' % round(time.perf_counter() - t_start, 5))
    print(*arr)




        

        