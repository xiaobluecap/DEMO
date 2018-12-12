from datetime import  datetime
now=datetime.now()
print(now)
now1=now.timestamp()
print(now1)
now2=datetime.fromtimestamp(now1)
print(now2)
now3=datetime.utcfromtimestamp(now1)
print(now3)
now4=now.strftime('%A,%B,%D')
print(now4)
from datetime import timedelta
now5=now+timedelta(days=5)
print(now5)