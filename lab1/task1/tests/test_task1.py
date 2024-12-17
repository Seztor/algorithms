import random
import unittest

from lab1.task1.src.task1 import task1
from lab1.utils_lab1 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64

    def test_should_testing_task1(self):
        #given
        n = 10
        data = [n, [random.randint(1, 10 ** 3) for _ in range(n)]]
        ans_to_check = sorted(data[1])

        #when
        sorted_arr = task1(data)
        time, memory = measure_mem_time(task1, data)

        #then
        self.assertListEqual(sorted_arr, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

if __name__ == '__main__':
    unittest.main()
