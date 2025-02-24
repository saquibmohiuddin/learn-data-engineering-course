from datetime import datetime, timedelta
import time

# generating datetime now
datetime_now = datetime.now()
print(datetime_now)

# modify datetime now minus 1 hour
datetime_now_minus_hour = datetime_now - timedelta(hours=1)
print(datetime_now_minus_hour)

# delete decimal from timestamp
datetime_now_minus_hour_reformatted = datetime_now_minus_hour.replace(microsecond=0)
print(datetime_now_minus_hour_reformatted)

datetime_now_minus_hour_reformatted = datetime_now_minus_hour.strftime("%Y-%m-%d %H:%M:%S")
print(datetime_now_minus_hour_reformatted)

# converting datetime to epoch using timestamp
epoch = int(datetime_now.timestamp())
print(epoch)

# converting epoch to custom datetime format
ts_from_epoch = datetime.fromtimestamp(epoch)
print(ts_from_epoch)

ts_from_epoch = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch))
print(ts_from_epoch)