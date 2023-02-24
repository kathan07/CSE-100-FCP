#Calculate the area of triangle given its three sides. The formula or algorithm used is: Area = sqrt(s(s – a)(s – b)(s – c)), where s = (a + b + c) / 2 or perimeter / 2 and a, b & c are the sides of triangle.
import math
a=int(input("ENTER SIDE 1"))
b=int(input("ENTER SIDE 2"))
c=int(input("ENTER SIDE 3"))
s=(a+b+c)/2
x=s*(s-a)*(s-b)*(s-c)
area=math.sqrt(x)
print(area)