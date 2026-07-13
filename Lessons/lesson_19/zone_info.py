from datetime import datetime
import zoneinfo

zone_info = zoneinfo.available_timezones()


#zoneinfo.ZoneInfo('asdasd)
# zo
for zone in zone_info:
    print(zone)
    # if zone.startswith('Eu') and zone.endswith('v'):
    #     print(zone)


str_time_zone = 'Europe/Kyiv'

from zoneinfo import ZoneInfo

ZoneInfo('Europe/Kyiv')

datetime_now = datetime.now().replace(tzinfo=ZoneInfo('Europe/Kyiv'))

# datetime_now = datetime_now
print(datetime_now)
print(datetime_now.astimezone(ZoneInfo("CET")))

print(datetime_now.tzinfo)
datetime_now_2 = datetime_now.replace(tzinfo=ZoneInfo('UTC'))
utc_now = datetime_now.astimezone(ZoneInfo('UTC'))
print(utc_now - datetime_now)
print(datetime_now_2)
print(datetime_now_2 - utc_now)
# datetime_now = datetime.now().replace(tzinfo=3)

print(datetime_now.astimezone(ZoneInfo('Indian/Mahe')))
print(datetime_now.tzinfo)


# print()

