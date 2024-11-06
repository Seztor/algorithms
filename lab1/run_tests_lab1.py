import os
import subprocess

list_tasks = [1,2,3,4,7,10]

for i in list_tasks:
    os.chdir(f'task{i}/tests/')
    print(f'TEST TASK #{i}')
    path_test = f'test_task{i}.py'
    command = f'pytest --tb=no {path_test}'

    #os.system(command)
    result = subprocess.run(['pytest','--tb=no',path_test], capture_output=True, text=True).stdout
    if 'passed' in result:
        print(f"\033[32m{result}\033[0m")
    else:
        print(f"\033[31m{result}\033[0m")
    print()
    print('#'*85)
    print()
    os.chdir(f'../..')