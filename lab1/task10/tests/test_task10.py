from lab1.task10.src.task10 import task10
from lab1.utils_lab1 import *

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

@func_mem_and_time
def test_should_testing_task10():
    #given
    write_data(PATH_INPUT,
               6, 'QAZQAZ')

    #when
    task10()
    string, = read_data(PATH_OUTPUT)

    #then
    assert string == 'AQZZQA'

if __name__ == 'main':
    test_should_testing_task10()