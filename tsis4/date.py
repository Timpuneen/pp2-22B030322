from datetime import datetime as date
from datetime import timedelta as delta
#1
chichas= date.now()
new_date= chichas-delta(days=5)
print(new_date)
#2
yesterday= chichas-delta(days=1)
tomorrow=chichas+delta(days=1)
print(yesterday)
print(chichas)
print(tomorrow)
#3
print(chichas.replace(microsecond=0))
#4
date1=date(2022,2,14,12,0,0)
date2=date(1999,2,14,0,10,0)
diff=(date1-date2).total_seconds()
print(diff)
