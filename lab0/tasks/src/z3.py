import sys
import time

t_start = time.perf_counter()
f_in = open('input.txt')
f_out = open('output.txt', 'w')
a, b = map(int, f_in.readline().split())

if abs(a) > 10**9 or abs(b) > 10**9:
    print('Error', file=f_out)
    exit(0)

print(a + b, file=f_out)

print('Elapsed time: %s sec' % round(time.perf_counter() - t_start, 5), file=f_out)
print('Used memory: %s bytes' % sys.getsizeof(a + b**2), file=f_out)

f_in.close()
f_out.close()