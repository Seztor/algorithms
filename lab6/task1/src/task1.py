from lab6.utils_lab6 import write_data, open_reading, read_data_by_line, close_reading

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


class Set:
    def __init__(self):
        self.mn = set()

    def add(self, item):
        if item not in self.mn:
            self.mn.add(item)

    def pop(self, item):
        if item in self.mn:
            self.mn.remove(item)

    def check(self, item):
        return item in self.mn


def task1(data_to_write=None):
    if not data_to_write is None:
        write_data(PATH_INPUT, *data_to_write)

    open_reading(PATH_INPUT)

    n = read_data_by_line(PATH_INPUT, int)
    mn = Set()
    ans_arr = []
    for i in range(n):
        temp_list = read_data_by_line(PATH_INPUT, str, True)
        if temp_list[0] == "A":
            mn.add(int(temp_list[1]))
        elif temp_list[0] == "D":
            mn.pop(int(temp_list[1]))
        else:
            if mn.check(int(temp_list[1])):
                ans_arr.append("Y")
            else:
                ans_arr.append("N")

    close_reading(PATH_INPUT)


    write_data(PATH_OUTPUT, ans_arr)
    return ans_arr


if __name__ == '__main__':
    task1()


