#Write a program to check whether a character is uppercase or lowercase alphabet.
n=input('Enter an alphabet')
if ord(n)>=97 and ord(n)<=122:
    print('IT IS A LOWER CASE ALPHABET')
elif ord(n)>=65 and ord(n)<=90:
    print('IT IS AN UPPER CASE ALPHABET')
else:
    print('IT IS NOT AN ALPHABET')