def find_k_closest_points(points, k):
    points = sorted([[a,b,find_dist(a,b)] for a,b in points], key=lambda x:x[2])
    points = points[:k]
    ans = ''
    for i in range(len(points)-1):
        a, b, c = points[i]
        ans += f'[{a},{b}],'
    a, b, c = points[-1]
    ans += f'[{a},{b}]'
    return ans

def find_dist(dot1, dot2):
    return (dot1 ** 2 + dot2 ** 2) ** 0.5

from lab3.utils_lab3 import read_data, write_data, open_reading, close_reading, read_data_by_line

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

def task8():
    open_reading(PATH_INPUT)
    n, k = read_data_by_line(PATH_INPUT)
    arr_dots = []
    for _ in range(n):
        a, b = read_data_by_line(PATH_INPUT)
        arr_dots.append((a, b))
    close_reading(PATH_INPUT)

    ans = find_k_closest_points(arr_dots, k)

    write_data(PATH_OUTPUT, ans)

if __name__ == '__main__':
    task8()

