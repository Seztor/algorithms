f_in = open('input.txt')
f_out = open('output.txt', 'w')
n = int(f_in.readline())
a1, a2 = 0, 1

if n < 0 or n > 10**7:
    print('Error', file=f_out)
    exit(0)


if n == 0: print(a1, file=f_out)
elif n == 1: print(a2, file=f_out)
else:
    for i in range(n-1):
        a1, a2 = a2%10, (a1+a2)%10
    print(a2, file=f_out)

f_in.close()
f_out.close()