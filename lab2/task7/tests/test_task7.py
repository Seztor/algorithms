from lab2.task7.src.task7 import *
from lab2.utils_lab2 import *

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

@func_mem_and_time
def test_should_testing_task7():
    #given
    n = 10**5
    arr = [random.randint(-10**2, 10 ** 2) for _ in range(n)]
    write_data(PATH_INPUT, n, arr)

    #when
    task7()
    ans1, ans2 = read_data(PATH_OUTPUT)

    #then
    assert ans1 == ans2


if __name__ == '__main__':
    test_should_testing_task7()