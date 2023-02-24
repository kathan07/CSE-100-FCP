#Write a Python program to input a number and check whether the entered number is even or odd.
n=int(input('ENTER YOUR NUMBER HERE::'))
N=n%2
if N==0:
    print('ITS AN EVEN NUMBER')
else:
    print('IT IS AN ODD NUMBER')