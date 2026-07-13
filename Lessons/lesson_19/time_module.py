import datetime
import time
import zoneinfo

# from datetime import datetime,date, da

time_stm_now = time.time()

# time.sleep(3)
# print(time.time() - time_stm_now )

# print(time.tm_e.tm_year)
time.localtime()
current_time = time.localtime()
print(current_time)
print(f'{current_time.tm_year}-{current_time.tm_mon}-{current_time.tm_mday}')
# print(datetime.datetime.fromtimestamp(time_stm_now))
# print(datetime.fromtimestamp(time_stm_now))



zone_info = zoneinfo.available_timezones()


# #zoneinfo.ZoneInfo('asdasd)
# # zo
# for zone in zone_info:
#     print(type(zone))
#     # if zone.startswith('Eu') and zone.endswith('v'):
#     #     print(zone)

str_zone = "Asia/Macau"
date_1 = datetime.datetime.now(zoneinfo.ZoneInfo('Europe/Kyiv'))
date_1_2 = date_1.astimezone(tz=zoneinfo.ZoneInfo(str_zone))
print(date_1)

print(date_1_2)

date_2_1 = datetime.datetime.now().replace(tzinfo=zoneinfo.ZoneInfo(str_zone))
print(date_2_1)
print( date_1 - date_2_1)


date_2 = datetime.datetime.now(tz=zoneinfo.ZoneInfo('UTC')) # теперенішній час але в ЮТС


print( date_2 )
# print(date_2 == date_1)



# print())