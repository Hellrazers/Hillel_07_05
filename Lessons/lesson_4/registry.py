row = 'ASDASD'

print(row.isupper())

row_digiht = '1233123' # -> int

print(row_digiht.isdigit())


row_title = "Hello World фів"
print(row_title.istitle())

row_title_split = row_title.split()
counter = 0
for item in row_title_split:
    if item.istitle():
        counter += 1
if counter > 1:
    print('в реченні більше 2 слів з великої літери')
else:
    print('програма відпрацювала корректно')



print(row_title.upper())
row_validattion_1 = "hello world фів"
row_validattion_2 = "Hello World фів"
print(row_validattion_1 == row_validattion_2)

print(row_validattion_1.lower() == row_validattion_2.lower())

print(row_validattion_1.upper() == row_validattion_2.upper())



print()