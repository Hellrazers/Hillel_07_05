import sys
import pathlib

from utils.new_file import get_passangers

# def get_passangers():
#     return 'New fuc'
#



print(get_passangers())



print(*sys.path)
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
print(str(pathlib.Path(__file__).parent.parent.parent))



from unit_tests import MyTestCasePositive
