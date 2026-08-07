import re

first_variable = r'\b[y,Y]\w{1,2}\b'



cur_str = '''
some text 2523 usdt
some text 2525 of usdt
some text 2525 USD


some text 2525 EUR
some text 2525 UA
'''

value_currency = r'\b\d{1,4}\b\w{,3}\s\b[u,U]\w{2,3}'
value_currency_2 = r'(\b\d{1,4}\b)(?:\sof)?\s([u,U]\w{2,3})'
phone_ = 'as (096)-555-55-55 asd asd (096)-555-55-55 asdasdasd '
phone_nb = r'\(0\d{2}\)-\d{3}(?:-\d{2}){2}'


print(re.findall(pattern=phone_nb, string=phone_))


print(re.findall(pattern=value_currency, string=cur_str))

iter_re = re.finditer(pattern=value_currency_2, string=cur_str)

for element in iter_re:
    print(element.group())
    print(element.groups()[0], element.groups()[1])
