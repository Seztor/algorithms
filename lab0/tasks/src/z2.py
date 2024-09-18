
import time
import sys


a, b = map(int, input().split())

t_start = time.perf_counter()

while abs(a) > 10**9 or abs(b) > 10**9:
    print('Error data, write again')
    a, b = map(int, input().split())

print(a + b**2)

print('Elapsed time: %s sec' % round(time.perf_counter() - t_start, 5))
print('Used memory: %s bytes' % sys.getsizeof(a + b**2))