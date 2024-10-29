from lab2.task1.src.task1 import *
from lab2.utils_lab2 import *

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

@func_mem_and_time
def test_should_testing_task1():
    #given
    n = 10 ** 5
    arr = [random.randint(1, 10 ** 9) for _ in range(n)]
    arr_c = arr.copy()
    write_data(PATH_INPUT, n, arr)

    #when
    task1()
    arr_alr_sorted, = read_data(PATH_OUTPUT)

    #then
    assert arr_alr_sorted == sorted(arr_c)

if __name__ == 'main':
  test_should_testing_task1()