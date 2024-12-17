import unittest

from lab1.task7.src.task7 import task7
from lab1.utils_lab1 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64

    def test_should_testing_task7(self):
        #given
        n = 5
        data = (n, [10.00, 8.70, 0.01, 5.00, 3.00])
        ans_to_check = (3,4,1)

        #when
        ans_arr = task7(data)
        time, memory = measure_mem_time(task7, data)

        #then
        self.assertEqual(ans_arr, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

if __name__ == '__main__':
    unittest.main()