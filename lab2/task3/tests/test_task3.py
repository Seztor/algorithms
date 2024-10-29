from lab2.task3.src.task3 import *
from lab2.utils_lab2 import *

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

@func_mem_and_time
def test_should_testing_task3():
    #given
    n = 10
    arr = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]
    write_data(PATH_INPUT, n, arr)

    #when
    task3()
    num, = read_data(PATH_OUTPUT)

    #then
    assert num == 17


if __name__ == 'main':
  test_should_testing_task3()