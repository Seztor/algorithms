from lab4.task7.src.task7 import task7
from lab4.utils_lab4 import read_data, write_data,func_mem_and_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


@func_mem_and_time
def test_should_testing_task9():
    #given
    test_arr = [8,(2,7,3,1,5,2,6,2),4]
    write_data(PATH_INPUT, *test_arr)

    #when
    ans = task7()
    ans_to_check = [7,7,5,6,6]

    #then
    assert ans == ans_to_check


if __name__ == '__main__':
    test_should_testing_task9()
