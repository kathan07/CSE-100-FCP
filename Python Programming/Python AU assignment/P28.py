'''Considering three numbers provided by the user as length of sides of a triangle, first check, if
the values are valid for representing the sides of a triangle (i.e. whether a triangle can be
drawn using the given values). If the lengths of sides are valid, print the type of the triangle.
Hint: The sum of lengths of any two sides of a triangle is always greater than the length of
the third side. A triangle with all three sides having same length is known as an “Equilateral”
triangle. A triangle is called an “Isosceles” triangle if only two sides have equal lengths. If all
the sides of a triangle have different lengths, then it is called a “Scalene” triangle'''
a=int(input('ENTER LENGTH OF SIDE 1 : '))
b=int(input('ENTER LENGTH OF SIDE 2 : '))
c=int(input('ENTER LENGTH OF SIDE 3 : '))
if a+b<=c or b+c<=a or a+c<=b:
    print('INVALID SIDES INPUT')
elif a==b and a==c:
    print('EQUILATERAL TRIANGLE')
elif a==b and a!=c:
    print('ISOSCELES TRIANGLE')
else:
    print('SCALENE TRIANGLE')