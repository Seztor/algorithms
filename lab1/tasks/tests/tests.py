import random
from task1 import task1
from task2 import task2
from task3 import task3
from task4 import task4
from task7 import task7
from task10 import task10
import time
import psutil
from string import ascii_uppercase as alph

def load_test_for_tasks_1_2_3(n):
    arr = [random.randint(-10**6,10**6) for i in range(n)]
    f = open('input.txt','w')
    print(len(arr), file=f)
    print(*arr, file=f)
    f.close()

def load_test_for_task_4(n):
    arr = [random.randint(-10**3,10**3) for i in range(n)]
    f = open('input.txt','w')
    print(*arr, file=f)
    print(random.randint(-10**3,10**3), file=f)
    f.close()

def load_test_for_task_7(n):
    arr = list(set(float(f'{random.randint(1,10**6)}.{random.randint(0,99)}') for i in range(n)))
    f = open('input.txt','w')
    print(len(arr), file=f)
    print(*arr, file=f)
    f.close()

def load_test_for_task_10(n):
    st = ''.join(random.choice(alph) for i in range(n))
    f = open('input.txt','w')
    print(len(st), file=f)
    print(st, file=f)
    f.close()


n = 100000
print(f'n={n}')
#Тут функция для загрузки данных в файл#########
load_test_for_task_10(n) 
################################################

t_start = time.perf_counter()

task10()

print(f"Memory used: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
print('Elapsed time: %s sec' % round(time.perf_counter() - t_start, 5))
