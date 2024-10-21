from lab1.task1.src.task1 import task1
from lab1.utils_lab1 import *

@func_mem_and_time
def test_task1():
    n = 10
    write_data("../txtf/input.txt", n, [random.randint(1, 10 ** 3) for _ in range(n)])

    task1()

    n, arr = read_data("../txtf/input.txt")
    arr_alr_sorted, = read_data("../txtf/output.txt")
    assert sorted(arr) == arr_alr_sorted


