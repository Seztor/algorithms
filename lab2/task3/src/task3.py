k = 0

def merge_sort(arr, p, r):
    global k
    if p < r:
        q = (p+r)//2
        merge_sort(arr,p,q)
        merge_sort(arr,q+1,r)
        merge(arr, p, q, r)
    
def merge(arr, p, q, r):
    global k
    arr1 = arr[p:q+1]
    arr2 = arr[q+1:r+1]
    
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arr[p+i+j] = arr1[i]
            i += 1
            
        else:
            arr[p+i+j] = arr2[j]
            j += 1
            k += len(arr1)-i
            
    while i < len(arr1):
        arr[p+i+j] = arr1[i]
        i += 1
        k += len(arr2)-j
        
    while j < len(arr2):
        arr[p+i+j] = arr2[j]
        j += 1

def get_answer():
    global k
    return k

if __name__ == '__main__':
    # n = int(input())
    # arr = [int(i) for i in input().split()]
    # k = 0
    # merge_sort(arr,0,n-1)
    # print(k)

    import random, time, psutil
    n = 10**5
    arr = [random.randint(1, 10**2) for _ in range(n)]
    k = 0
    print(f'n={n}')
    #print(*arr)
    t_start = time.perf_counter()
    merge_sort(arr,0,len(arr)-1)
    print(f"Memory used: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
    print('Elapsed time: %s sec' % round(time.perf_counter() - t_start, 5))
    print(k)
    