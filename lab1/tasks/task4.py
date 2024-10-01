def task4():
    f = open('input.txt')
    f2 = open('output.txt', 'w')
    arr = [int(i) for i in f.readline().split()]
    v = int(f.readline())

    finded = []

    for i in range(len(arr)):
        if arr[i] == v:
            finded.append(i)

    if len(finded) == 0:
        print(-1, file=f2)
    else:
        print(len(finded), file=f2)
        print(*finded, file=f2)

    f.close()
    f2.close()