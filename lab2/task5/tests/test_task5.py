import unittest

from lab2.task5.src.task5 import task5
from lab2.utils_lab2 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64

    def test_should_testing_task5_1(self):
        #given
        data = (5, [2,3,9,2,2])
        ans_to_check = 1

        #when
        is_majority = task5(data)
        time, memory = measure_mem_time(task5, data)

        #then
        self.assertEqual(is_majority, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task5_2(self):
        #given
        data = (4, [1,2,3,4])
        ans_to_check = 0

        #when
        is_majority = task5(data)
        time, memory = measure_mem_time(task5, data)

        #then
        self.assertEqual(is_majority, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


if __name__ == '__main__':
    unittest.main()