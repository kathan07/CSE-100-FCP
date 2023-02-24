#Write a program to find the sum of odd numbers and even numbers from 1 to N. Read value of N from user.
#ODD NUMBERS
N=int(input('ENTER NUMBER'))
n=0
sum=0
while n<N:
    sum=sum+n

    n=n+2
print(sum)
#even number
I=int(input('ENTER NUMBER'))
i=1
summ=0
while i<I:
    summ=summ+i

    i=i+2
print(summ)