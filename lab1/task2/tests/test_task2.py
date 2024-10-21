from lab1.task2.src.task2 import task2
from lab1.utils_lab1 import *

@func_mem_and_time
def test_task2():
    n = 10
    arr = [1,8,4,2,3,7,5,6,9,0]
    write_data("../txtf/input.txt", n, arr)

    task2()

    n, arr = read_data("../txtf/input.txt")
    arr1, arr2 = read_data("../txtf/output.txt")
    assert arr1 == [1,2,2,2,3,5,5,6,9,1] and arr2 == [0,1,2,3,4,5,6,7,8,9]
