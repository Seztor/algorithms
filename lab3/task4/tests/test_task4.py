from lab3.task4.src.task4 import *
from lab3.utils_lab3 import *

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


@func_mem_and_time
def test_should_testing_task4():
    #given
    s = random.randint(1, 5000)
    p = random.randint(1, 5000)
    arr_seg = []
    for i in range(s):
        st_n = random.randint(-10**8,10**8)
        end_n = st_n + random.randint(0,10**8)
        arr_seg.append((st_n, end_n))
    arr_points = []
    for i in range(p):
        n = random.randint(-25,25)
        arr_points.append(n)
    write_data(PATH_INPUT, (s,p), *arr_seg, arr_points)

    #when
    task4()
    ans, = read_data(PATH_OUTPUT)

    #then
    assert ans == True


if __name__ == '__main__':
    test_should_testing_task4()
