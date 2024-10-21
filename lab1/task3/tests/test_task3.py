from lab1.task3.src.task3 import task3
from lab1.utils_lab1 import *
import random

@func_mem_and_time
def test_task3():
    n = 10
    write_data("../txtf/input.txt", n, [random.randint(1, 10 ** 3) for _ in range(n)])

    task3()

    n, arr = read_data("../txtf/input.txt")
    arr_alr_sorted, = read_data("../txtf/output.txt")
    assert sorted(arr, reverse=True) == arr_alr_sorted