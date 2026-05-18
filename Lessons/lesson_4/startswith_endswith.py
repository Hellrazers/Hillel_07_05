row = 'Методи .startswith() та .endswith() використовуються для перевірки того, чи рядок починається або закінчується певною підстрічкою.    '


print(row.startswith('Методи .startswith() та'))
print(row.endswith('або закінчується певною підстрічкою.'))


new_row = row.split()
print(new_row[-1])
print(row.endswith(new_row[-1]))