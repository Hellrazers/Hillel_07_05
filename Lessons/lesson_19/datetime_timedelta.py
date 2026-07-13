



from datetime import datetime, timedelta



date_now = datetime.now()
print(date_now)
print(date_now.tzinfo)

date_now = date_now.replace(day=30, month=6)
print(date_now)

date_now_2  = datetime.now()
print(date_now_2)


print(date_now_2 - timedelta(hours=5, days=1456 + (6 *30 + 3)))


date_old_3  = date_now.replace(day=date_now_2.day, month=1)
print(date_old_3)
print(date_now_2 - date_old_3)

# int_123 = 123
# int_123 = 12