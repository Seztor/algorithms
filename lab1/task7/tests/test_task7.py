from lab1.task7.src.task7 import task7
from lab1.utils_lab1 import *
import random

@func_mem_and_time
def test_task7():
    n = 5
    arr_to_write = [10.00, 8.70, 0.01, 5.00, 3.00]
    write_data("../txtf/input.txt", n, arr_to_write)

    task7()

    arr_ans, = read_data("../txtf/output.txt")
    assert arr_ans == [3,4,1]