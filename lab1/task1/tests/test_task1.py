from lab1.task1.src.task1 import task1
from lab1.utils_lab1 import *

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

@func_mem_and_time
def test_should_testing_task1():
    #given
    n = 10
    write_data(PATH_INPUT, n, [random.randint(1, 10 ** 3) for _ in range(n)])

    #when
    task1()
    n, arr = read_data(PATH_INPUT)
    arr_alr_sorted, = read_data(PATH_OUTPUT)

    #then
    assert sorted(arr) == arr_alr_sorted

if __name__ == 'main':
    test_should_testing_task1()
