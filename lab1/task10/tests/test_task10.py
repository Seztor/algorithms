from lab1.task10.src.task10 import task10
from lab1.utils_lab1 import *

@func_mem_and_time
def test_task10():
    write_data("../txtf/input.txt",
               6, 'QAZQAZ')

    task10()

    string, = read_data("../txtf/output.txt")
    assert string == 'AQZZQA'
