from datetime import datetime


datetime_row_1 = '2026-4-30 15-32-23'
datetime_row_2 = '25-7-2026 15:34:23'
datetime_row_3 = '7-25-2026 15:32:23'
datetime_row_4 = '7-25-26 3:32:23 PM'
datetime_row_5 = '25-07-2026T15:32:23:123123ZZ'

# datetime_row_3 != '7-25-2026 15:37:23'

datetime_dt_1 = datetime.strptime(datetime_row_1,
                                '%Y-%m-%d %H-%M-%S')
datetime_dt_2 = datetime.strptime(datetime_row_2,
                                '%d-%m-%Y %H:%M:%S')

datetime_dt_3 = datetime.strptime(datetime_row_3,'%m-%d-%Y %H:%M:%S')
datetime_dt_4 = datetime.strptime(datetime_row_4,'%m-%d-%y %I:%M:%S %p')

print(datetime_dt_2 == datetime_dt_1)
print(datetime_dt_3 == datetime_dt_4)
print(datetime_dt_1)
print(type(datetime_row_1))
print(type(datetime_dt_1))

new_str_datetime = datetime_dt_2.strftime('%Y-%m-%d %I-%M-%S ')
print(new_str_datetime)


def datetime_format_converter(str_date:str, format_to_convert:str = '%d-%m-%Y %H:%M:%S',
                              format_we_want_convert:str = '%Y-%m-%dT%H-%M-%S.%fZZZZ'):
    datetime_date = datetime.strptime(str_date, format_to_convert)
    return datetime_date.strftime(format_we_want_convert)

print(datetime_format_converter(datetime_row_2))






