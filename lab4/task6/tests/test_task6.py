from lab4.task6.src.task6 import task6
from lab4.utils_lab4 import write_data,func_mem_and_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


@func_mem_and_time
def test_should_testing_task6():
    #given
    test_arr = ["7", "+ 1", "?", "+ 10", "?", "-", "?", "-"]

    #when
    ans = task6(test_arr)
    ans_to_check = [1,1,10]

    #then
    assert ans == ans_to_check


if __name__ == '__main__':
    test_should_testing_task6()
