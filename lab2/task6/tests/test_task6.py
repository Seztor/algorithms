from lab2.task6.src.task6 import *
from lab2.utils_lab2 import *

@func_mem_and_time
def test_task6():

    arr = [100,113,110,85,105,102,86,63,81,101,94,106,101,79,94,90,97]
    n = len(arr)
    write_data("../txtf/input.txt", n, arr)

    task6()

    arr_ans, = read_data("../txtf/output.txt")
    assert arr_ans == [7, 10, 43]
