#Write a Python program to read 3 numbers from user and print the maximum among them. (with conditional operator)
n1=float(input('enter number 1'))
n2=float(input('enter number 2'))
n3=float(input('enter number 3'))
if n1>n2 and n1>n3:
    print(n1)
elif n2>n1 and n2> n3:
    print(n2)
else:
    print(n3)