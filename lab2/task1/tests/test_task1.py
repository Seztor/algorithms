from lab2.task1.src.task1 import *
from lab2.utils_lab2 import *

@func_mem_and_time
def test_task1():
    n = 10 ** 5
    arr = [random.randint(1, 10 ** 9) for _ in range(n)]
    arr_c = arr.copy()
    write_data("../txtf/input.txt", n, arr)

    task1()

    arr_alr_sorted, = read_data("../txtf/output.txt")
    assert arr_alr_sorted == sorted(arr_c)
