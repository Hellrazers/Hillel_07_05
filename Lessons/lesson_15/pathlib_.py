import pathlib
import os
import sys

from constans import BASE_DIR
path_to_file = pathlib.Path(__file__)
print(type(path_to_file))
print(BASE_DIR.is_dir())
print(path_to_file.is_dir())
print(path_to_file.is_file())
print(path_to_file.suffix == '.csv')
firsst_value , soecon, third = [1, 2, 3]


os_all_files = os.walk(BASE_DIR)
list_ = list(range(1000000))
itrator_ = iter(range(1000000))

print(sys.getsizeof(list_))
print(sys.getsizeof(itrator_))

print(type(os_all_files))
path_to_py_list = []
for item in os_all_files:
    path_dir, dir_name_list, file_name_list = item
    print(item)
    # pass
    # print(dir_name_list)
    # print(dir_name_list)
    # print('-' * 50)
    CONSTANT_DIR = ['.git', '.idea', '.pytest_cache','__pycache__']
    dir_name_list[:] = [k for k in dir_name_list if k not in CONSTANT_DIR]
    # print(file_name_list)
    # for fi
    # print(dir_name_list)
    for file in file_name_list:
        # if   ('.git' not in path_dir) or '.idea'  not in path_dir:
        # print(type(file))
        if file.endswith('.py') and file != '__init__.py':
            file_path = os.path.join(path_dir,file)
            print(pathlib.Path(file))
            path_to_py_list.append(file_path)

for k in path_to_py_list:
    print(k)
# D:\work\Hillel_07_05\Lessons\lesson_1\new_derectoryt\new_file4.py
# D:\work\Hillel_07_05\Lessons\lesson_1\new_derectoryt\new_file4.py

print(type(path_to_py_list[0]))

    # item[1][:] = []

