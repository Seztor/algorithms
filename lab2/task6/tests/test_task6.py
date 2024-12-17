import unittest

from lab2.task6.src.task6 import task6
from lab2.utils_lab2 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64

    def test_should_testing_task6(self):
        #given
        arr = [100,113,110,85,105,102,86,63,81,101,94,106,101,79,94,90,97]
        data = (len(arr), arr)
        ans_to_check = (7, 10, 43)

        #when
        arr_ans = task6(data)
        time, memory = measure_mem_time(task6, data)

        #then
        self.assertEqual(arr_ans, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


if __name__ == '__main__':
  unittest.main()
