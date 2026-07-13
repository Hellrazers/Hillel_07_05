# from datetime import datetime, timezone, timedelta
#
# # 1. Create a timezone-aware object for UTC
# utc_now = datetime.now(timezone.utc)
# print(utc_now.tzinfo)
# print(f"UTC Time: {utc_now}")
#
# # 2. Create a custom fixed offset (e.g., UTC+5:30)
# custom_offset = timezone(timedelta(hours=5, minutes=30))
# india_time = datetime.now(custom_offset)
# print(f"India Time (Fixed Offset): {india_time}")
#
# # 3. Create a custom negative offset (e.g., UTC-5:00 for EST)
# est_offset = timezone(timedelta(hours=-5))
# est_time = datetime.now(est_offset)
# print(f"EST Time (Fixed Offset): {est_time}")
