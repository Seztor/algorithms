import time, sys
from random import randint

tests_1 = [randint(0, 45) for i in range(5)]
tests_2 = [randint(0, 10**7) for i in range(5)]

def fib_1(n):
    a1, a2 = 0, 1

    if n == 0: return a1
    elif n == 1: return a2
    else:
        for i in range(n-1):
            a1, a2 = a2, a1+a2
        return a2
    
def fib_2(n):
    a1, a2 = 0, 1

    if n == 0: return a1
    elif n == 1: return a2
    else:
        for i in range(n-1):
            a1, a2 = a2%10, (a1+a2)%10
        return a2

print('Test 2 task')
for i in range(5):
    t_start = time.perf_counter()
    ans = fib_1(tests_1[i])
    print('TEST INP:',tests_1[i], '| Elapsed time: %s sec' % round(time.perf_counter() - t_start, 8), '| Used memory: %s bytes' % sys.getsizeof(ans))
print()
print('Test 3 task')
for i in range(5):
    t_start = time.perf_counter()
    ans = fib_2(tests_2[i])
    print('TEST INP:',tests_2[i], '| Elapsed time: %s sec' % round(time.perf_counter() - t_start, 5), '| Used memory: %s bytes' % sys.getsizeof(ans))