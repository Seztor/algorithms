from lab2.task5.src.task5 import *
from lab2.utils_lab2 import *

@func_mem_and_time
def test_task5_1():
    n = 5
    arr = [2,3,9,2,2]
    write_data("../txtf/input.txt", n, arr)

    task5()

    is_majority, = read_data("../txtf/output.txt")
    assert is_majority == 1


@func_mem_and_time
def test_task5_2():
    n = 4
    arr = [1,2,3,4]
    write_data("../txtf/input.txt", n, arr)

    task5()

    is_majority, = read_data("../txtf/output.txt")
    assert is_majority == 0