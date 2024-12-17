import unittest

from lab1.task4.src.task4 import task4
from lab1.utils_lab1 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64

    def test_should_testing_task4(self):
        #given
        data = ([1,3,4,5,6,4,8,3],4)
        ans_to_check = (2, [2,5])

        #when
        ans_arr = task4(data)
        time, memory = measure_mem_time(task4, data)

        #then
        self.assertEqual(ans_arr, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

if __name__ == '__main__':
    unittest.main()