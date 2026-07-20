import pathlib


BASE_DIR: pathlib.Path = pathlib.Path(__file__).parent
DATA_DIR: pathlib.Path = BASE_DIR.joinpath('data')
DATA_DIR_2 = BASE_DIR / 'data'
LESSONS_12_DIR = BASE_DIR.joinpath('Lessons', 'lesson_11')
#
# print(DATA_DIR)
# print(DATA_DIR_2)
