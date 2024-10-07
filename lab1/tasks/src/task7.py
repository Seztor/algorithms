def task7():
    f = open('input.txt')
    f2 = open('output.txt', 'w')
    n = int(f.readline())
    arr = [(float(item),ind+1) for ind,item in enumerate(f.readline().split())]
    
    for j in range(1, len(arr)):
        i = j-1
        k = arr[j]
        while arr[i][0] > k[0] and i >= 0:
            arr[i+1] = arr[i]
            i = i-1
        arr[i+1] = k

    print(arr[0][1], arr[n//2][1], arr[-1][1], file=f2)

    f.close()
    f2.close()