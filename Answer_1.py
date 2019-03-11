from datetime import datetime as dt
import pytz as py
from pytz import timezone, utc


 
time = dt.utcfromtimestamp(1541962108935000000 // 1000000000).strftime('%Y-%m-%d %H:%M:%S:%f') # Now the value is taken as our local time of UTC
print time
value = timezone('CET')# Using timezone to get CERN local time difference to that of UTC
time = dt.strptime(time, '%Y-%m-%d %H:%M:%S:%f')
time_cern = utc.localize(time, is_dst = None).astimezone(value)
print time_cern
 
