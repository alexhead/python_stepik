import datetime

x = input().split()
a = int(x[0])
b = int(x[1])
c = int(x[2])


date_my = datetime.date( a, b, c)
delta = datetime.timedelta(days = int(input()))

now_date = date_my + delta

print(now_date.year, now_date.month, now_date.day)