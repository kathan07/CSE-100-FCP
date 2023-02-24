#Write a Python program to check whether a number is divisible by 5 or not.
n=int(input('ENTER YOUR NUMBER HERE::'))
N=n%5
if N==0:
    print('IT IS DIVISIBLE BY 5')
else:
    print('IT IS NOT DIVISIBLE BY 5')