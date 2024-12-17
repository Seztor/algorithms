import unittest

from lab2.task3.src.task3 import task3
from lab2.utils_lab2 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64


    def test_should_testing_task3(self):
        #given
        data = (10, [1, 8, 2, 1, 4, 7, 3, 2, 3, 6])
        ans_to_check = 17

        #when
        num = task3(data)
        time, memory = measure_mem_time(task3, data)

        #then
        self.assertEqual(num, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


if __name__ == '__main__':
  unittest.main()