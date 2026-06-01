

str_ = 'hello world'
# print(type(str_) is str)
# print(type(str_) is object)
#
#
#
# print(isinstance(str_, str))
# print(isinstance(str_, object))
#
# print(str.mro())
#
#
# print(int.mro())
# print( bool.mro())
# # 1 - True | 0 -False
#
# print(isinstance(True, int))
# print(type(True) is int)
#
#
#
# if type(str_) is str:
#     print(True)
#
if isinstance(str_, bool): # -> True|False
    print(True)
else:
    print(False)