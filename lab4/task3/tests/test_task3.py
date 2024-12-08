from lab4.task3.src.task3 import task3
from lab4.utils_lab4 import write_data, func_mem_and_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


@func_mem_and_time
def test_should_testing_task3():
    #given
    arr_data = ["5","()()","([])","([)]","((]]",")("]

    #when
    ans = task3(arr_data)
    arr_to_check = ["YES","YES","NO","NO","NO"]

    #then
    assert ans == arr_to_check


if __name__ == '__main__':
    test_should_testing_task3()
