import unittest

from lab1.task10.src.task10 import task10
from lab1.utils_lab1 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64

    def test_should_testing_task10(self):
        #given
        data = (6, 'QAZQAZ')
        ans_to_check = 'AQZZQA'

        #when
        string = task10(data)
        time, memory = measure_mem_time(task10, data)

        #then
        self.assertEqual(string, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

if __name__ == '__main__':
    unittest.main()