from lab3.task2.src.task2 import task2, create_arr_for_test
from lab3.utils_lab3 import read_data, write_data, func_mem_and_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


@func_mem_and_time
def test_should_testing_task2():
    #given
    n = 10**3
    write_data(PATH_INPUT, n)

    #when
    task2()
    arr, = read_data(PATH_OUTPUT)
    arr2 = create_arr_for_test(n)


    #then
    assert arr==arr2


if __name__ == '__main__':
  test_should_testing_task2()