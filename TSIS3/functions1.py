# 1

def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

# 2


def fahrenheit_to_celcius(fahrenheit):
    celcius = (5 / 9) * (fahrenheit - 32)
    return celcius

# 3


def solve(numheads, numlegs):
    rabbits = 0
    chicks = 0
    if numlegs % 2 != 0:
        print('No solution')
    else:
        rabbits = (numlegs - 2 * numheads)/2
        chicks = numheads - rabbits
    return int(rabbits), int(chicks)


"""""
my_list = list(solve(35, 94))
print("rabbits: " + str(my_list[0]))
print ("chicks: " + str(my_list[1]))
"""""

# 4


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def filter_prime(numbers):
    return list(filter(lambda x: is_prime(int(x)), numbers))


"""
numbers = []
a = int(input())
for i in range(a):
    numbers.append(input())
print(filter_prime(numbers))
"""

# 5

def permutations(remaining, candidate=''):
    if len(remaining) == 0:
        print(candidate)

    for i in range(len(remaining)):
        newCandidate = candidate + remaining[i]
        newRemaining = remaining[0:i] + remaining[i + 1:]

        permutations(newRemaining, newCandidate)

s = 'ABC'
permutations(s)

# 6

def reverse(s):
    return s[::-1]
s = 'Hello'
print(reverse(s))

# 7

def has_33(nums):
    for i in range(len(nums)):
        if nums[i:i+2] == [3,3]:
                return True
    return False
if has_33([1, 3, 1, 3]):
    print('true')
else:
    print ('false')

# 8

def spy_game(nums):
    for x in range(0,len(nums)-2):

        if nums[x] == 0 and nums[x+1] == 0 and nums[x+2]==7:
            return True
    return False

# 9

def volume(radius):
    return float(((int(radius) ** 3) * 4 * 3.14)/3)
print(volume(3))

# 10

def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x

# 11

#ABBA, ABCBA
def IsPalindrome(s):
    return s == s[::-1]

s = "malayalam"
ans = IsPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")

# 12

def histogram(items):
    for n in items:
        output = ''
        times = n
        while(times > 0):
          output += '*'
          times = times - 1
        print(output)