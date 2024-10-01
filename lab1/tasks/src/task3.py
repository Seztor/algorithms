def task3():
    f = open('input.txt')
    f2 = open('output.txt', 'w')
    n = int(f.readline())
    arr = [int(i) for i in f.readline().split()]

    def reverse_ins_sort(arr):
        for i in range(len(arr)-1):
            while arr[i] < arr[i+1] and i >= 0:
                arr[i+1], arr[i] = arr[i], arr[i+1]
                i -= 1
        return arr

    print(*reverse_ins_sort(arr), file=f2)

    f.close()
    f2.close()
