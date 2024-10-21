from lab1.task4.src.task4 import task4
from lab1.utils_lab1 import *

@func_mem_and_time
def test_task4():
    write_data("../txtf/input.txt",
               [1,3,4,5,6,4,8,3],4)

    task4()

    cnt, arr = read_data("../txtf/output.txt")
    assert cnt == 2 and arr == [2,5]
