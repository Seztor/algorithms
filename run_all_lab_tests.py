import subprocess
import os


lab_tasks = [1,2,3]


for i in lab_tasks:
    os.chdir(f'lab{i}/')

    print(f'\033[34mTESTS LAB #{i}\033[0m')
    print()
    path_test = f'run_tests_lab{i}.py'
    result = subprocess.run(['python',path_test], capture_output=True, text=True).stdout
    print(result)
    os.chdir(f'..')