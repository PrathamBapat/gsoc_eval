from datetime import datetime as dt
import pytz as py
from pytz import timezone, utc


 # The temp_time value comes out to be "1974-11-20 16:16:50"
time = dt.utcfromtimestamp(1541962108935000000 // 1000000000).strftime('%Y-%m-%d %H:%M:%S:%f') # Now the value is taken as our local time of UTC
print time
value = timezone('CET')
time = dt.strptime(time, '%Y-%m-%d %H:%M:%S:%f')
# Using timezone to get CERN local time difference to that of UTC
time_cern = utc.localize(time, is_dst = None).astimezone(value)
print time_cern
 
