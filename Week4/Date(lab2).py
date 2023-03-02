import datetime
x = datetime.timedelta(days=1)
today = datetime.datetime.now()
yesterday = today - x
tomorrow = today + x
print(yesterday,today,tomorrow)