import math 
a = float(input())
b= float(input())
c = math.sqrt(a*a+b*b)
angle = math.atan(b/a)*180/math.pi
print("the angle, in degrees is",angle)
print("the hypotenuse is",c)