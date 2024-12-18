from lab5.utils_lab5 import write_data, read_data

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


def get_swap_arr(data):
    global ans_swap
    ans_swap = []

    for i in range(len(data) // 2 - 1, -1, -1):
        recursion(i, len(data), data)

    return ans_swap


def recursion(ind, n, data):
    global ans_swap
    min_index = ind
    left = 2 * ind + 1
    right = 2 * ind + 2

    if left < n and data[left] < data[min_index]:
        min_index = left

    if right < n and data[right] < data[min_index]:
        min_index = right

    if ind != min_index:
        data[ind], data[min_index] = data[min_index], data[ind]
        ans_swap.append((ind, min_index))
        recursion(min_index, n, data)





def task4(data_to_write=None):
    if not data_to_write is None:
        write_data(PATH_INPUT, *data_to_write)

    n, arr = read_data(PATH_INPUT)
    arr_ans = get_swap_arr(arr)


    write_data(PATH_OUTPUT, len(arr_ans), *arr_ans)
    return len(arr_ans), *arr_ans


if __name__ == '__main__':
    task4()


