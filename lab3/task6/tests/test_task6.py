from lab3.task6.src.task6 import task6
from lab3.utils_lab3 import read_data, write_data,func_mem_and_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


@func_mem_and_time
def test_should_testing_task6():
    #given
    test_arr = [(4,4), (7,1,4,9), (2,7,8,11)]
    write_data(PATH_INPUT, *test_arr)

    #when
    task6()
    ans, = read_data(PATH_OUTPUT)
    ans_to_check = 51

    #then
    assert ans == ans_to_check


if __name__ == '__main__':
    test_should_testing_task6()
