import re

# 1
txt = input('enter a string ')
x = re.findall("a(b*)", txt)
print(x)
if x:
    print('it\'s a match')
else:
    print('no match found')

# 2
txt = input('enter a string ')
x = re.findall("ab{2,3}", txt)
print(x)
if x:
    print('it\'s a match')
else:
    print('no match found')

# 3
txt = input('enter a string ')
x = re.findall("[a-z]+[_]+[a-z]+", txt)
print(x)
if x:
    print('it\'s a match')
else:
    print('no match found')

# 4
txt = input('enter a string ')
x = re.findall("[A-Z]+[a-z]", txt)
print(x)
if x:
    print('it\'s a match')
else:
    print('no match found')

# 5
txt = input('enter a string ')
x = re.findall("a.*(b$)", txt)
print(x)
if x:
    print('it\'s a match')
else:
    print('no match found')

# 6
txt = input('enter a string ')
x = re.sub("[ ,.]", ":", txt)
print(x)

# 7
txt = input('enter a string ')
x = re.split('_', txt)
y = ' '.join(x)
z = y.title()
b = re.sub("\s", "", z)
print(b)

# 8
txt = input('enter a string ')
x = re.split("[A-Z]", txt)
print(x)

# 9
txt = input('enter a string ')
x = re.findall('[A-Z][a-z]*', txt)
y = ' '.join((x))
print(y)

# 10
txt = input('enter a string ')
x = re.findall('[A-Z][a-z]*', txt)
b = ' '.join((x))
y = b.lower()
z = re.sub(' ', '_', y)
print(z)