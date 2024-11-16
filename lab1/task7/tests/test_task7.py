from lab1.task7.src.task7 import task7
from lab1.utils_lab1 import read_data,write_data,func_mem_and_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

@func_mem_and_time
def test_should_testing_task7():
    #given
    n = 5
    arr_to_write = [10.00, 8.70, 0.01, 5.00, 3.00]
    write_data(PATH_INPUT, n, arr_to_write)

    #when
    task7()
    arr_ans, = read_data(PATH_OUTPUT)

    #then
    assert arr_ans == [3,4,1]

if __name__ == '__main__':
    test_should_testing_task7()