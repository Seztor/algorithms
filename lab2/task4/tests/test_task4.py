from lab2.task4.src.task4 import *
from lab2.utils_lab2 import *

@func_mem_and_time
def test_task4():
    n = 5
    arr_n = [1,5,8,12,13]
    k = 5
    arr_k = [8,1,23,1,11]
    write_data("../txtf/input.txt", n, arr_n, k, arr_k)

    task4()

    arr_bs, = read_data("../txtf/output.txt")
    assert arr_bs == [2,0,-1,0,-1]
