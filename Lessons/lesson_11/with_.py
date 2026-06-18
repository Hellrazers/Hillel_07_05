# try:
#     file_ = None
#     file_ = open('text.txt', 'r')
#     file_text = file_.read()
#     print(file_text)
# except Exception as e:
#     print(e)
# finally:
#     if file_:
#         file_.close()
# [”1,2,3,4”, ”1,2,3,4,50”, ”qwerty1,2,3”]
import pathlib

from constans import BASE_DIR

with open(f'{BASE_DIR}\\Lessons\\lesson_11\\text.txt', 'r') as file_1:
    text = file_1.read()
    print(text)
