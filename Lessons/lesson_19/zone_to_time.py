from datetime import datetime
from zoneinfo import ZoneInfo

# 1. Create a datetime aware of the target zone (e.g., Kyiv)
target_time = datetime(2026, 7, 13, 20, 45, tzinfo=ZoneInfo("Europe/Kyiv"))

# 2. Convert to any other zone
utc_time = target_time.astimezone(ZoneInfo("UTC"))
est_time = target_time.astimezone()
print(target_time.time)
print("Kyiv:", target_time)
print("UTC:", utc_time)
print("New York:", est_time)
ZoneInfo("UTC")

# print( - ZoneInfo("America/New_York") )

