#Write a Python program to input angles of a triangle and check whether triangle is valid or not.
n1=int(input('ENTER 1ST ANGLE(in degrees)'))
n2=int(input('ENTER 2ND ANGLE(in degrees)'))
n3=int(input('ENTER 3RD ANGLE(in degrees)'))
a=n1+n2+n3
if a==180:
    print('ABOVE TRIANGLE IS POSSIBLE')
else:
    print('TRIANGLE NOT POSSIBLE')