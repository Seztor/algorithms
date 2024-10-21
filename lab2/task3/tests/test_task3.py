from lab2.task3.src.task3 import *
from lab2.utils_lab2 import *

@func_mem_and_time
def test_task3():
    n = 10
    arr = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]
    write_data("../txtf/input.txt", n, arr)

    task3()

    num, = read_data("../txtf/output.txt")
    assert num == 17
