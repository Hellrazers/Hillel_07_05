# Список рядків
row: str = "Це приклад      для заміни у рядку.        заміни приклад заміни  приклад заміни"
new_row:list[str] = row.split()
print(new_row)

new_join: str = '___'.join(new_row[::-1]) # -> str

print(new_join)
print(row.replace(' ', '___'))

print('+++'.join(row)) # -> кожний символ як елемент

print(len(row))
for index, value in enumerate(row):
    print(index, value)

# for k in row


# print(row.split(''))
