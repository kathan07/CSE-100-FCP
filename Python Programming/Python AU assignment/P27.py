#Accept the marks (out of 70) for 3 subjects (Maths, physics, chemistry) from the user and check if the student is eligible for admission based on the following criteria:
#i) Mathematics >= 40, Physics >= 35, Chemistry >= 30
#ii) Total marks of Mathematics + Physics >= 100
a=int(input('ENTER MARKS OF MATHS OUT OF 70 : '))
b=int(input('ENTER MARKS OF PHYSICS OUT OF 70 : '))
c=int(input('ENTER MARKS OF CHEMISTRY OUT OF 70 : '))
if a>70 or b>70 or c>70 or a<0 or b<0 or c<0:
    print('INVALID INPUT')
else:
    if a>=40 and b>=35 and c>=30:
        print('YOU ARE ELIGIBLE FOR ADMISSION')
    elif a+b>=100:
        print('YOU ARE ELIGIBLE FOR ADMISSION')
    else:
        print('YOU ARE NOT ELIGIBLE FOR ADMISSION')
