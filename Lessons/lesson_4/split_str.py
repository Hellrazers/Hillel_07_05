row = ('Функціявикористовується для розділення рядка на частини на основі '
       'певного роздільника                 та повертає список отриманих частин. Основні варіанти використання split(): використовується використовується')

print(type(row))


row_split = row.split() # перетворює тільки STR в список елементів(list)
print(len(row_split))
print(row_split, sep='\n')
print(type(row_split))
print(row_split[0])
print(  row_split[-3],row_split[-2] ,row_split[-1])
print(type( row_split[-3]),type(row_split[-2]) ,type(row_split[-1]))
print(row_split[-3:])
print(type(row_split[-3:]))
print(type(row_split[-3:][0]))# list[<class 'str'>, <class 'str'>, <class 'str'>]

row_split_space  = row.split(sep=' ')
print(row_split_space)
print(len(row_split_space))

row_split_by_word = row.split(sep='використовується')
print(row_split_by_word)
print(len(row_split_by_word))


row_split_by_word_each_second = row.split(sep='використовується', maxsplit=1)
print(row_split_by_word_each_second)
print(len(row_split_by_word_each_second))

validation_variable = 'u'
counter = 0
new_split_row = row.split() #-> list[<class 'str'>, <class 'str'>, <class 'str'>]
for k in new_split_row: # <class 'str'>

    if k.startswith(validation_variable): # k = <class 'str'>
        print(f'{k} це слово буде починатись з букви "{validation_variable}"')
        counter += 1
if counter == 0:
    print('Nothing to see here')
print(new_split_row[0])
print(row.startswith(new_split_row[0]))