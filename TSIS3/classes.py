import math


class String:
    def __init__(self):
        self.str1 = ""

    def getString(self):
        self.str1 = input()

    def printString(self):
        print(self.str1.upper())


str1 = String()
str1.getString()
str1.printString()


class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):

    def __init__(self, length):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length * self.length


class Rectangle(Shape):

    def __init__(self, length, width):
        super().__init__()

        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return self.x, self.y

    def move(self, x, y):
        self.x += x
        self.y += y

    def dist(self, pt):
        dx = pt.x - self.x
        dy = pt.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'

    def deposit(self, dep_amt):
        self.balance += dep_amt
        print('Deposit Accepted')

    def withdraw(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

my_list = []
a = int(input())
for i in range (a):
    my_list.append(input())
filtered_list_iterator = filter(lambda p: is_prime(int(p)), my_list)
filtered_list = list(filtered_list_iterator)
print(filtered_list)