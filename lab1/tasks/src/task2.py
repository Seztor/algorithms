def task2():
    f = open('input.txt')
    f2 = open('output.txt', 'w')
    n = int(f.readline())
    arr = [int(i) for i in f.readline().split()]


    def ins_sort(arr):
        ind_arr = [-1] * n
        ind_arr[0] = 1
        for j in range(1, len(arr)):
            i = j-1
            k = arr[j]
            while arr[i] > k and i >= 0:
                arr[i+1] = arr[i]
                i = i-1
            arr[i+1] = k
            ind_arr[j] = i+2
        return ind_arr, arr

    arr1, arr2 = ins_sort(arr)

    print(*arr1, file=f2)
    print(*arr2, file=f2)

    f.close()
    f2.close()
