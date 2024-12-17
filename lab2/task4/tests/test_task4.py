import unittest

from lab2.task4.src.task4 import task4
from lab2.utils_lab2 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64

    def test_should_testing_task4(self):
        #given
        data = (5, [1,5,8,12,13], 5, [8,1,23,1,11])
        ans_to_check = [2,0,-1,0,-1]

        #when
        arr_bs = task4(data)
        time, memory = measure_mem_time(task4, data)

        #then
        self.assertEqual(arr_bs, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

if __name__ == '__main__':
  unittest.main()
