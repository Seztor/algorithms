import unittest

from lab1.task2.src.task2 import task2
from lab1.utils_lab1 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64

    def test_should_testing_task2(self):
        #given
        n = 10
        data = [n, [1,8,4,2,3,7,5,6,9,0]]
        ans_to_check = ([1,2,2,2,3,5,5,6,9,1],[0,1,2,3,4,5,6,7,8,9])

        #when
        ans_arr = task2(data)
        time, memory = measure_mem_time(task2, data)

        #then
        self.assertEqual(ans_arr, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

if __name__ == '__main__':
    unittest.main()