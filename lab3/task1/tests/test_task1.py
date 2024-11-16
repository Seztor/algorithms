from lab3.task1.src.task1 import task1
from lab3.utils_lab3 import read_data, write_data, func_mem_and_time
import random

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

@func_mem_and_time
def test_should_testing_task1():
    #given
    n = 10 ** 5
    arr = [random.randint(1, 30) for _ in range(n)]
    arr_c = sorted(arr.copy())
    write_data(PATH_INPUT, n, arr)

    #when
    task1()
    arr_alr_sorted, = read_data(PATH_OUTPUT)

    #then
    assert arr_alr_sorted == arr_c

if __name__ == '__main__':
  test_should_testing_task1()