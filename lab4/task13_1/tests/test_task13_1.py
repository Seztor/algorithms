from lab4.task13_1.src.task13_1 import task13_1
from lab4.utils_lab4 import write_data, func_mem_and_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


@func_mem_and_time
def test_should_testing_task13_1():
    #given
    test_arr = ["8","+ 1","?","+ 10","?","+ 12","?","-","?"]
    write_data(PATH_INPUT, *test_arr)

    #when

    ans = task13_1()
    ans_to_check = ["1","1 10","1 10 12","1 10"]

    #then
    assert ans == ans_to_check


if __name__ == '__main__':
    test_should_testing_task13_1()

