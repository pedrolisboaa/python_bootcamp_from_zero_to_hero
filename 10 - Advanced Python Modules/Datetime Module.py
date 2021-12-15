import datetime
from datetime import datetime, date
#
# mytime = datetime.time(13, 54)
# print(mytime.hour)
# print(mytime.minute)
# print(mytime)

# today = datetime.date.today()
# print(today)

mydatetime = datetime(1992, 9, 15, 20, 30, 45)
print(mydatetime)
teste = mydatetime.replace(year=1991, month=10)
print(teste)

# date
date1 = datetime.now()
date2 = datetime(1992, 9, 15)
print((date1 - date2) / 365)