import math
x = math.pi/4
val = math.sin(x)**2 + math.cos(x)**2
print val

v = 3 #m/s
t = 1 #sec
a = 2 #m/s**2
s = ((v * t) + ((1.0/2.0) * a * (t**2)))
print s, "meters"

a = float(input("Enter the first number"))
b = float(input("Enter the second number"))
e1 = ((a+b)**2)
e2 = (a**2)+(2*a*b)+(b**2)
if e1 == e2:
    print "The equations are equal & verified."
else:
    print "The equations are not equal & not verified."
