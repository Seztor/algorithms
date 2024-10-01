def task7():
    f = open('input.txt')
    f2 = open('output.txt', 'w')
    n = int(f.readline())
    arr = [(float(item),ind+1) for ind,item in enumerate(f.readline().split())]

    arr.sort()

    print(arr[0][1], arr[n//2][1], arr[-1][1], file=f2)

    f.close()
    f2.close()