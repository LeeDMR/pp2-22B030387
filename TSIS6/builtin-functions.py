# 1
my_list = [5, 3, 6, 3, 6]
total = 1
for x in my_list:
    total *= x
print(total)

# 2
my_string = input()
up = 0
low = 0
for i in my_string:
    if(i.isupper()):
        up += 1
    else:
        low += 1
print(up)
print(low)

# 3
def isPalindrome(s):
    rev = ''.join(reversed(s))
    if (s == rev):
        return True
    return False

s = "abba"
ans = isPalindrome(s)

if (ans):
    print("Yes")
else:
    print("No")

# 4
import math
import time as t


def square_with_delay(num, time):
    t.sleep(time/1000)
    return math.sqrt(num)


num = int(input())
time = int(input())
print(square_with_delay(num,time))

# 5
my_tuple = (True, True, True)
if(all(my_tuple)):
    print("True")
else:
    print("False")