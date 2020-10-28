from math import sqrt, acos, degrees, cos

x1, y1 = 1, 1 # map(int, input("point 1: ").split())
x2, y2 = 4, 2 # map(int, input("point 2: ").split())
x3, y3 = 1, 5 # map(int, input("point 3: ").split())

x2 = x2 - x1 # making the first dot as the origin
y2 = y2 - y1 # making the first dot as the origin

x3 = x3 - x1 # making the first dot as the origin
y3 = y3 - y1 # making the first dot as the origin

x1 = 0 # making the first dot as the origin
y1 = 0 # making the first dot as the origin

dot23 = x2 * x3 + y2 * y3

side1 = magnitude2 = sqrt(x2**2 + y2**2) # length side is same as magnitude
side2 = magnitude3 = sqrt(x3**2 + y3**2) # length side is same as magnitude

angle12 = acos(dot23 / (magnitude2 * magnitude3)) # first angle

side3 = sqrt(side1**2 + side2**2 - (2*side1 *side2 * cos(angle12))) # using law of cosines to the the third side

print(degrees(angle12))
print(side1, side2, side3)
print(magnitude2)
print(magnitude3)