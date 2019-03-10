from datetime import datetime as dt
import pytz as py
from pytz import timezone

temp_time = dt.utcfromtimestamp(1541962108935000000 // 1000000000) # The temp_time value comes out to be "1974-11-20 16:16:50"
time = dt(1974, 11, 20, 16, 16, 50, tzinfo=py.utc).strftime('%Y-%m-%d %H:%M:%S %Z%z') # Now the value is taken as our local time of UTC
print time
rn = timezone('Europe/Zurich') # Using timezone to get CERN local time difference to that of UTC
time_cern = dt(1974, 11, 20, 16, 16, 50, tzinfo=py.utc).astimezone(rn).strftime('%Y-%m-%d %H:%M:%S %Z%z')
print time_cern

