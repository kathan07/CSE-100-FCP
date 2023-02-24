#Accept a number N from the user and print the first N elements of the Fibonacci series.
n = int(input("Enter number"))
a=0
b=1
print(a,end = " ")
print(b,end = " ")
for i in range(2,n):
    print(a+b,end = " ")
    c=b
    b=a+b
    a=c
    
