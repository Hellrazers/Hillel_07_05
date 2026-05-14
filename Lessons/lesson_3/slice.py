sting_1 = 'TEXT'
print(len(sting_1))
print(len([1,2, 3]))
print([1,2, 3][2])
# print([1,2, 3][4234])

dict_ = {'key': 2}
print(dict_['key'])
print(sting_1[0])

list_validation = [1, 2, 3]
print(f'size of list list_validation: {len(list_validation)}')
for k in range(len(list_validation)):
    print(f'index: {k}, value: {list_validation[k]}')

text_str = ('Послідовність — це впорядкований контейнер елементів, '
            'проіндексованих цілими числами або хешами. Python має '
            'вбудовані типи послідовностей, відомі як рядки (байти або str), кортежі, списки, набори та словники')


print(sting_1[:1:])

# :::  звідки включно |  до котрого елементу не включно | і яка переодичність
text_str[25:80:3]

print(text_str[:-15:1])
print(len('Послідовність — це впорядкований контейнер ел'))

tuple_2 = (1, 2, 3 ,4 ,5)
tuple_3 = tuple_2[1:3]
print(type(tuple_3))
print(id(tuple_2) == id(tuple_3))

print('123123'[-1])
print(min((1, 2, 3 ,4 ,5)))
print(sum((1, 2, 3 ,4 ,5 ,1 )))
int_value = None
for k in (1, 2, 3 ,4 ,5):
    if int_value is None:
        int_value = k
    if int_value > k:
        int_value = k
    else:
        continue
#     int_value += k


set_value  = {1 , 2 , 3 , 4 , 5, 1}
print(sum(tuple(set_value)))
print()
# print(int_value)