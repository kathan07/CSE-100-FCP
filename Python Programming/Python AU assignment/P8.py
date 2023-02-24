#Make a program that asks the number between 1 and 10. If the number is out of range the program should display “invalid number”.
n=int(input('ENTER NUMBER B/W 1 AND 10\n'))
if n<=10 or n>=1:
    print('VALID INPUT')
else:
    print('INVALID NUMBER') 