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
        if nums[i] == 3 and nums[i+1] == 3:
                return True
    return False
if has_33([1, 3, 3]):
    print('true')
else:
    print ('false')
