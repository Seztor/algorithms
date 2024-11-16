from lab3.task8.src.task8 import task8
from lab3.utils_lab3 import read_data, write_data, func_mem_and_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


@func_mem_and_time
def test_should_testing_task8():
    #given
    test_arr = [(3, 2), (3, 3), (5, -1), (-2, 4)]
    write_data(PATH_INPUT, *test_arr)

    #when

    ans = task8()
    ans_to_check = '[3,3],[-2,4]'


    #then
    assert ans == ans_to_check


if __name__ == '__main__':
    test_should_testing_task8()
