

def task1():
    f = open('input.txt')
    f2 = open('output.txt', 'w')
    n = int(f.readline())
    arr = [int(i) for i in f.readline().split()]

    def ins_sort(arr):
        for j in range(1, len(arr)):
            i = j-1
            k = arr[j]
            while arr[i] > k and i >= 0:
                arr[i+1] = arr[i]
                i = i-1
            arr[i+1] = k
        return arr

    print(*ins_sort(arr), file=f2)

    f.close()
    f2.close()
