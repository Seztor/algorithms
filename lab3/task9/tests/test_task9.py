from lab3.task9.src.task9 import *
from lab3.utils_lab3 import *

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


@func_mem_and_time
def test_should_testing_task9():
    #given
    test_arr = [11, (4, 4), (-2, -2), (-3, -4), (-1, 3), (2, 3), (-4, 0), (1, 1), (-1, -1), (3, -1), (-4, 2), (-2, 4)]
    write_data(PATH_INPUT, *test_arr)

    #when
    task9()
    ans, = read_data(PATH_OUTPUT)
    ans_to_check = '1.414213'

    #then
    assert ans == ans_to_check


if __name__ == '__main__':
    test_should_testing_task9()