from datetime import datetime, timedelta

my_date = datetime.now()
# 1
y = datetime.now() - timedelta(days=5)
print(y)


# 2
x1 = datetime.now() - timedelta(days=1)
print(x1.strftime("%A"))
x2 = datetime.now()
print(x2.strftime("%A"))
x3 = datetime.now() + timedelta(days=1)
print(x3.strftime("%A"))


# 3
print(my_date.replace(microsecond=0))


# 4
a = datetime(2023, 2, 21, 14, 25, 20)
b = datetime(2022, 1, 16, 5, 23, 50)
c = a - b
minutes = c.days*24*60 + c.seconds/60
print(minutes)