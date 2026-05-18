row = ('Строки є незмінними, що означає, що після створення рядка ви не можете '
       'змінити його вміст без створення нового рядка (або перезапису вмісту змнної).')

print(row[25:]) # з 25 включно [start:] і до останнього
print(row[:25]) #з 0 елмента(перша літера) до 25 не включно [:stop]
print(row[::5]) # кожне 5 значення [::step] (якщо залишаєм пусте, то по дефолту буде 1 або кожний елмент)

print(row[::-1])

print(row[-25:])

print(row)


new_row = row[:25]
print( 'Довжина нашої змінної:',len(new_row))
print(new_row + ' новий рядок')
print(new_row[15])
print(new_row[-1])

print('виводим new_row[len(new_row) - 1]: ', new_row[len(new_row) - 1])

# for k in new_row:
#     print(k)
#
#
#
# print(len(row))
# print(len(new_row))
#
#
# print('-' * 123)
# print('123' + ' ' +'456')
#

list_numv = [1 , 2 , 4, 5] # index [0, 1 ,2 ,3....]
# len
print(len(list_numv))
print(list_numv[:2])

