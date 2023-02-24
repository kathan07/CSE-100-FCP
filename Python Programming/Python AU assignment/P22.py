#Accept a year from the user and check whether it is leap year or not.
y = int(input('ENTER AN YEAR : '))
if y%4==0 and not y%100==0:
        print(y,"is a leap year")
elif y%400==0:
    print(y,"is a leap year")
else:
    print(y,"is not a leap ")