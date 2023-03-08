import math

# 1
a = math.pi
b = int(input())
radians = (a*b)/180
x = "Output radians: {}"
print(x.format(radians))
print(math.radians(b))

# 2
h = int(input())
a = int(input())
b = int(input())
area = ((a+b)/2)*h
x = "Area of a trapezoid: {}"
print(x.format(area))

# 3
n = int(input())
l = int(input())
ap = l/(2*math.tan(math.radians(180/n)))
area_polygon = ap*l*n/2
x = "The area of the polygon is: {}"
print(x.format(int(area_polygon)))

# 4
a = int(input())
h = int(input())
area_parallelogram = a*h
x = "Area of a parallelogram: {}"
print(x.format(area_parallelogram))
