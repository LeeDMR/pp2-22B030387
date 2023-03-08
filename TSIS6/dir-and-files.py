import os, string
path = 'C:\\Users\leedm\pp2-22B030387\\'
# 1
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nOnly files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll directories and files :")
print([ name for name in os.listdir(path)])

# 2
print('Exist:', os.access('C:\\Users\leedm\pp2-22B030387\\', os.F_OK))
print('Readable:', os.access('C:\\Users\leedm\pp2-22B030387\\', os.R_OK))
print('Writable:', os.access('C:\\Users\leedm\pp2-22B030387\\', os.W_OK))
print('Executable:', os.access('C:\\Users\leedm\pp2-22B030387\\', os.X_OK))

# 3
print("Test a path exists or not:")
path = 'C:\\Users\leedm\pp2-22B030387\\'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))

# 4
with open(r"test.txt", 'r') as fp:
    lines = len(fp.readlines())
    print('Total Number of lines:', lines)

# 5
items = ['Table ', 'Chair ', 'Mirror ', 'Apple ', 'Banana ']
file = open('test.txt','w')
file.writelines(items)
file.close()

# 6
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)

# 7
with open("test.txt") as f:
    with open("out.txt", "w") as f1:
        for line in f:
            f1.write(line)

# 8
path = "somepath"
if (os.path.exists(path)):
    os.remove(path)
else:
    print("Can not delete the file as it doesn't exists")