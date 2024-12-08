from lab4.task2.src.task2 import task2
from lab4.utils_lab4 import write_data, func_mem_and_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


@func_mem_and_time
def test_should_testing_task2():
    #given
    data = ["4","+ 1", "+ 10", "-", "-"]

    #when
    st = task2(data)
    ans_to_check = "1\n10"


    #then
    assert st==ans_to_check


if __name__ == '__main__':
  test_should_testing_task2()