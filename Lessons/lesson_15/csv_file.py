import csv

data = [
    ['Name','Is Married', 'Age','Phone Number', 'City'],
    ['John', True, 30, '+380','New York'],
    ['Alice',True, 25, '+380', 'Los Angeles'],
    ['Bob',True, 35, '+380', 'Chicago']
]

# Відкриття CSV-файлу для запису
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, )
    for row in data:
        writer.writerow(row )
    # writer.writerows(data)



with open('output.csv', newline='') as csvfile:
    reader = list(csv.reader(csvfile, ))
    # reader_2 = csv.reader(csvfile)
    # print(type(reader_2))
    # print(reader)

column_name_list = reader[0]
row_values_list = reader[1:]


for row in row_values_list:
    int(row[2]) >= 30
print(column_name_list)
print(row_values_list)
all_data_dict = [dict(zip(column_name_list, row)) for row in row_values_list]
print(all_data_dict)

for data in all_data_dict:
    if int(data['Age']) >= 30:
        print(f'My name is {data["Name"]} and my age is {data["Age"]}.')