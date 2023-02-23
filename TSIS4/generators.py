# 1
def squares(N):
    for i in range(N):
        yield i**2
for x in squares(5):
    print(x)

# 2
def even(n):
    for i in range(n):
        if(i%2 == 0):
            yield i
n = int(input())
my_list = []
for x in even(n):
    my_list.append(str(x))
print(",".join(my_list))

# 3
def div_by_3_4(n):
    for i in range(n):
        if(i%3==0 and i%4==0):
            yield i
for x in div_by_3_4(100):
    print(x)

# 4
def squares2(a,b):
    for i in range(a,b):
        yield i
for x in squares2(2,7):
    print(x)

# 5
print(" ")
def reverse(n):
    for i in range(n,0,-1):
        yield i
for x in reverse(10):
    print(x)