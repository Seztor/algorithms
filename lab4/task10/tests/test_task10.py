from lab4.task10.src.task10 import task10
from lab4.utils_lab4 import write_data, func_mem_and_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


@func_mem_and_time
def test_should_testing_task8_1():
    #given
    test_arr = ["5","13 0 100", "14 0 0 ", "14 1 0", "14 2 3", "14 3 0"]

    #when
    ans = task10(test_arr)
    ans_to_check = ["13 10","14 10","14 1","14 20","14 3"]

    #then
    assert ans == ans_to_check


def test_should_testing_task8_2():
    #given
    test_arr = ["8","10 0 0","11 0 0","11 1 1","12 2 0","12 3 3","13 4 3","13 5 6","13 24 0"]

    #when
    ans = task10(test_arr)
    ans_to_check = ['10 10', '11 10', '11 20', '12 12', '12 22', '13 14', '13 24', '13 34']

    #then
    assert ans == ans_to_check

if __name__ == '__main__':
    test_should_testing_task8_1()
    test_should_testing_task8_2()
