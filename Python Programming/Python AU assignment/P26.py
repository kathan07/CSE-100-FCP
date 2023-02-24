#Write a program that take input of 3 subjects marks out of 150. Count the percentage. Print the Grade/Class based on following conditions:
#For 70% or more than 70% display DISTINCTION.
#For percentage between 60 and 69 display FIRST CLASS.
#For percentage between 50 and 59 display SECOND CLASS.
#For percentage between 40 and 49 display PASS CLASS.
#For percentage less than 40 display FAIL.
a=int(input('ENTER MARKS OF 1ST SUBJECT OUT OF 150 : '))
b=int(input('ENTER MARKS OF 2ND SUBJECT OUT OF 150 : '))
c=int(input('ENTER MARKS OF 3RD SUBJECT OUT OF 150 : '))
if a>150 or b>150 or c>150 or a<0 or b<0 or c<0:
    print('INVALID INPUT')
else:
    per=((a+b+c)*100)/450
    if per>=70:
        print('DISTINCTION')
    elif per>=60 and per<=69:
        print('FIRST CLASS')
    elif per>=50 and per<=59:
        print('SECOND CLASS')
    elif per>=40 and per<=49:
        print('PASS CLASS')
    elif per<40 and per>=0:
        print('FAIL')
    else :
        print('INVALID INPUT')