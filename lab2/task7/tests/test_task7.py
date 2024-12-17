import random
import unittest

from lab2.task7.src.task7 import task7
from lab2.utils_lab2 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64

    def test_should_testing_task7(self):
        #given
        n = 10**5
        data = (n, [random.randint(-10**2, 10 ** 2) for _ in range(n)])

        #when
        ans1, ans2 = task7(data)
        time, memory = measure_mem_time(task7, data)

        #then
        assert ans1 == ans2
        self.assertEqual(ans1, ans2)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


if __name__ == '__main__':
    unittest.main()