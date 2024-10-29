from lab2.task5.src.task5 import *
from lab2.utils_lab2 import *

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

@func_mem_and_time
def test_should_testing_task5_1():
    #given
    n = 5
    arr = [2,3,9,2,2]
    write_data(PATH_INPUT, n, arr)

    #when
    task5()
    is_majority, = read_data(PATH_OUTPUT)

    #then
    assert is_majority == 1


@func_mem_and_time
def test_should_testing_task5_2():
    #given
    n = 4
    arr = [1,2,3,4]
    write_data(PATH_INPUT, n, arr)

    #when
    task5()
    is_majority, = read_data(PATH_OUTPUT)

    #then
    assert is_majority == 0


if __name__ == 'main':
  test_should_testing_task5_1()
  test_should_testing_task5_2()