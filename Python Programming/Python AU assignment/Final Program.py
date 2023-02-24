#Q1
# Write a Python program to print your ID – Card (Concept to learn: Formatted output)
print('NAME:Kathan Yogesh Thakkar')
print('Roll No.:AU2140040')
print('ADDRESS:Ahmedabad')
print('SEAS')
print('Ahmedabad University')
#OUTPUT
'''NAME:Kathan Yogesh Thakkar
Roll No.:AU2140040
ADDRESS:Ahmedabad
SEAS
Ahmedabad University'''

#Q2
#Write a Python program to input a number and check whether the entered number is even or odd.
a=int(input('ENTER YOUR NUMBER HERE::'))
N=a%2
if N==0:
    print('ITS AN EVEN NUMBER')
else:
    print('IT IS AN ODD NUMBER')
#output
'''ENTER YOUR NUMBER HERE::5
IT IS AN ODD NUMBER'''

#Q3
#Write a Python program to check whether a number is divisible by 5 or not.
a=int(input('ENTER YOUR NUMBER HERE::'))
N=a%5
if N==0:
    print('IT IS DIVISIBLE BY 5')
else:
    print('IT IS NOT DIVISIBLE BY 5')
#output
'''ENTER YOUR NUMBER HERE::6
IT IS NOT DIVISIBLE BY 5'''

#Q4
#Write a Python program to read a month number and print corresponding month name.
n=int(input('ENTER NUMBER OF MONTH'))
B={1:'JANUARY',2:'FEBRUARY',3:'MARCH',4:'APRIL',5:'MAY',6:'JUNE',7:'JULY',8:'AUGUST',9:'SEPTEMBER',10:'OCTOBER',11:'NOVEMBER',12:'DECEMBER'}
print(B.get(n))
#output
'''ENTER NUMBER OF MONTH3
MARCH'''

#Q5
#Write a Python program to find the Square Root of a given number.
import math
n=int(input('ENTER NUMBER HERE'))
K= math.sqrt(n)
print(K)
#Output
'''ENTER NUMBER HERE4
2.0'''

#Q6
#Write a Python program to input angles of a triangle and check whether triangle is valid or not.
n1=int(input('ENTER 1ST ANGLE(in degrees)'))
n2=int(input('ENTER 2ND ANGLE(in degrees)'))
n3=int(input('ENTER 3RD ANGLE(in degrees)'))
b=n1+n2+n3
if b==180:
    print('ABOVE TRIANGLE IS POSSIBLE')
else:
    print('TRIANGLE NOT POSSIBLE')
#Output
'''ENTER 1ST ANGLE(in degrees)30
ENTER 2ND ANGLE(in degrees)90
ENTER 3RD ANGLE(in degrees)60
ABOVE TRIANGLE IS POSSIBLE'''

#Q7
#Write a Python program to calculate the Area of a Triangle.
b=int(input('ENTER BASE LENGTH OF TRIANGLE'))
h=int(input('ENTER HEIGHT OF TRIANGLE'))
C=(b*h)/2
print(C)
#Output
'''ENTER BASE LENGTH OF TRIANGLE5
ENTER HEIGHT OF TRIANGLE6
15.0'''

#Q8
#Make a program that asks the number between 1 and 10. If the number is out of range the program should display “invalid number”.
n=float(input('ENTER NUMBER B/W 1 AND 10'))
if n<=10.0 or n>=1.0:
    print('VALID INPUT')
else:
    print('INVALID NUMBER') 
#Output
'''ENTER NUMBER B/W 1 AND 10
5
VALID INPUT'''

#Q9
#Write a Python program that generates and prints 100 random numbers.
import random
i=1
while i<=100:
    print(random.randint(0,100),end=',')
    i=i+1
#Output
'''26,78,1,37,44,22,100,36,70,50,19,10,45,89,8,90,73,45,79,49,88,37,9,49,77,75,35,28,0,40,89,94,58,43,18,0,29,96,40,11,6,32,82,45,98,73,24,64,12,81,96,10,100,16,87,73,92,84,47,22,94,99,44,42,58,85,41,15,31,27,50,37,40,9,81,65,57,51,58,58,66,32,31,1,9,24,62,37,7,79,45,87,29,18,58,11,77,24,57,82'''

#Q10
#Write a Python program to check whether a person is eligible to vote or not.
a=int(input('ENTER YOUR AGE'))
if a>=18:
    print('YOU ARE ELIGIBLE TO VOTE')
else:
    print('YOU ARE NOT ELIGIBLE TO VOTE')
#Output
'''ENTER YOUR AGE16
YOU ARE NOT ELIGIBLE TO VOTE'''

#Q11
#Write a Python program to Generate and print a Random Number.
import random
print(random.randint(0,1000))
#Output
'''475'''

#Q12
#Write a Python program to Convert Celsius to Fahrenheit.
c=int(input('ENTER TEMPERATURE IN CELCIUS'))
f=(c*9/5)+32
print(f)
#Output
'''ENTER TEMPERATURE IN CELCIUS32
89.6'''

#Q14
#Write a Python program to print the sum of first 10 numbers.
sum=0
i=1
while i<=10:
    sum=i+sum
    i=i+1
print(sum)
#Output
'''55'''

#Q15
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
#Output
'''enter number 12
enter number 23
enter number 34
4.0'''

#Q16
#Write a program to find the sum of odd numbers and even numbers from 1 to N. Read value of N from user.
#even NUMBERS
N=int(input('ENTER NUMBER'))
n=0
sum=0
while n<N:
    sum=sum+n

    n=n+2
print(sum)
#odd number
I=int(input('ENTER NUMBER'))
i=1
summ=0
while i<I:
    summ=summ+i

    i=i+2
print(summ)
#Output
'''ENTER NUMBER10
20
ENTER NUMBER10
25'''

#Q17
#Create a converter that will convert a distance in meters to feet and inches.
m=float(input('Enter length in metres:'))
f=m*3.281
r=f%1
i=r*12
print(int(f),' feet and ',i,' inches.')
#Output
'''Enter length in metres:5
16  feet and  4.860000000000014  inches.'''

#Q18
#Write a Python program to read a character from the user and check whether it is a vowel (aeiou) or consonant.
n=input('Enter an alphabet')
if ord(n)==97 or ord(n)==101  or ord(n)==105  or ord(n)==111  or ord(n)==117  or ord(n)==65 or ord(n)==69 or ord(n)==73 or ord(n)==79 or ord(n)==85:
    print('ITS A VOWEL')
else:
    print('ITS A CONSONANT')
#Output
'''Enter an alphabet a
ITS A VOWEL'''

#Q19
#Write a program to check whether a character is uppercase or lowercase alphabet.
n=input('Enter an alphabet')
if ord(n)>=97 and ord(n)<=122:
    print('IT IS A LOWER CASE ALPHABET')
elif ord(n)>=65 and ord(n)<=90:
    print('IT IS AN UPPER CASE ALPHABET')
else:
    print('IT IS NOT AN ALPHABET')
#Output
'''Enter an alphabetA
IT IS AN UPPER CASE ALPHABET'''

#Q20
#Write a program to accept two numbers and one mathematical operator. Calculate and display appropriate answer as shown below:
#Write a program to accept two numbers and one mathematical operator. Calculate and display appropriate answer as shown below:
a=int(input('enter number 1::'))
o = str(input('enter math operator::'))
b=int(input('enter number 2::'))
if o =="+":
    print(a,o,b,"=",a+b)
elif o =="*":
    print(a,o,b,"=",a*b)
elif o =="/":
    print(a,o,b,"=",a/b)
elif o =="-":
    print(a,o,b,"=",a-b)
#Output
'''enter number 1::2
enter math operator::+
enter number 2::3
2 + 3 = 5'''

#Q22
#Accept a year from the user and check whether it is leap year or not.
y = int(input('ENTER AN YEAR : '))
if y%400==0:
    print(y,"is a leap year")

elif y%4==0 and not y%100==0:
    print(y,"is a leap year")

else:
    print(y,"is not a leap ")
     
#Output
'''ENTER AN YEAR : 2004
IT IS A LEAPYEAR :)'''

#Q21
#Write a program to enter a number from the user and display the sum of all the digits in the number. [Hint: if user input is 123, display answer 6, which is addition of 1+2+3].
n =input("Enter a number:\n")
a = 0 
sum = 0
while a<len(n):
    sum = sum+int(n[a])
    a+=1
print(sum)
#Output
'''ENTER A NUMBER::234
9'''

#Q23
#Write a program called ExtractDigits to extract each digit from an int in the reverse order. For example, if the int is 12345, the output shall be "5 4 3 2 1", with a space separating the digits.
#ExtractDigits
a=int(input('ENTER A NUMBER : '))
x=a%10
y=(a%100)//10
z=(a%1000)//100
b=(a%10000)//1000
c=(a%100000)//10000
print(x,' ',y,' ',z,' ',b,' ',c,)
#Output
'''ENTER A NUMBER : 12345
5   4   3   2   1'''

#Q24
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
#Output
'''Enter number6
0 1 1 2 3 5'''

#Q25
#Calculate the area of triangle given its three sides. The formula or algorithm used is: Area = sqrt(s(s – a)(s – b)(s – c)), where s = (a + b + c) / 2 or perimeter / 2 and a, b & c are the sides of triangle.
import math
a=int(input("ENTER SIDE 1"))
b=int(input("ENTER SIDE 2"))
c=int(input("ENTER SIDE 3"))
s=(a+b+c)/2
x=s*(s-a)*(s-b)*(s-c)
area=math.sqrt(x)
print(area)
#Output
'''ENTER SIDE 13
ENTER SIDE 24
ENTER SIDE 35
6.0'''

#Q26
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
#Output
'''ENTER MARKS OF 1ST SUBJECT OUT OF 150 : 100
ENTER MARKS OF 2ND SUBJECT OUT OF 150 : 120
ENTER MARKS OF 3RD SUBJECT OUT OF 150 : 135
DISTINCTION'''

#Q27
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
#Output
'''ENTER MARKS OF MATHS OUT OF 70 : 35
ENTER MARKS OF PHYSICS OUT OF 70 : 40
ENTER MARKS OF CHEMISTRY OUT OF 70 : 60
YOU ARE NOT ELIGIBLE FOR ADMISSION'''

#Q28
'''Considering three numbers provided by the user as length of sides of a triangle, first check, if
the values are valid for representing the sides of a triangle (i.e. whether a triangle can be
drawn using the given values). If the lengths of sides are valid, print the type of the triangle.
Hint: The sum of lengths of any two sides of a triangle is always greater than the length of
the third side. A triangle with all three sides having same length is known as an “Equilateral”
triangle. A triangle is called an “Isosceles” triangle if only two sides have equal lengths. If all
the sides of a triangle have different lengths, then it is called a “Scalene” triangle'''
a=int(input('ENTER LENGTH OF SIDE 1 : '))
b=int(input('ENTER LENGTH OF SIDE 2 : '))
c=int(input('ENTER LENGTH OF SIDE 3 : '))
if a+b<=c or b+c<=a or a+c<=b:
    print('INVALID SIDES INPUT')
elif a==b and a==c:
    print('EQUILATERAL TRIANGLE')
elif a==b and a!=c:
    print('ISOSCELES TRIANGLE')
else:
    print('SCALENE TRIANGLE')
#Output
'''ENTER LENGTH OF SIDE 1 : 3
ENTER LENGTH OF SIDE 2 : 4
ENTER LENGTH OF SIDE 3 : 5
SCALENE TRIANGLE'''

#Q29
#A. 1, 2, 3, 4 ........ 100
for i in range(1,101):
    if i<100:
        print(i,end=',')
    else:
        print(i,end='\n')
print("\n")
#B. 100, 99, 98.......1
i=100
while i<=100 and i>0:
    if i>0:
        print(i,end=',')
        i-=1
    else:
        print(i,end='\n')
print("\n")
#C. 1, 3, 5, 7........99
a=1
while a<100:
    print(a,end=' ')
    a=a+2
print("\n")
#D. 2, 4, 8, 16, 32, 64
b=2
while b<100:
    print(b,end=' ')
    b=b+2
#Output
'''1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100


100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82,81,80,79,78,77,76,75,74,73,72,71,70,69,68,67,66,65,64,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49,48,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,

1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99

2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98'''

#Q31
'''. Calculate income tax for the given income by following the given rules:
Income Rate (in %)
upto Rs 5,00,000 0%
upto Rs 10,00,000 10% (of income above 5,00,000)
above Rs 10,00,000 20% (of income above 10,00,000)
Expected Output:
Enter your income (Rs): 600000
Income tax payable by you (Rs) = 10000/-
'''
a = float(input("Enter your income :\n"))
if a<=500000:
    print("Your income tax is zero")
elif 500000<a<=1000000:
    b = (a-500000)*10/100
    print("Your income tax is",b)
elif a>1000000:
    c = (a-1000000)*20/100 + 500000*10/100
    print("your income taxis ",c)
#Output
'''Enter your income :
600000 
Your income tax is 10000.0'''

#Q32
''' Print multiplication table of a number entered by the user. Validate that the number must
be between 1 and 20. Example, if number=5, then print output as
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
………..
5 X 10 = 50'''
num = int(input("Enter number between 1 to 20\n"))
n=1
while n<=10:
    print(num,"X",n,"=",num*n)
    n=n+1
#output
'''Enter number between 1 to 20
8
8 X 1 = 8
8 X 2 = 16
8 X 3 = 24
8 X 4 = 32
8 X 5 = 40
8 X 6 = 48
8 X 7 = 56
8 X 8 = 64
8 X 9 = 72
8 X 10 = 80'''

#Q33
'''. An equation of the form
is known as the quadratic equation. The values of x that satisfy the equation are known as
the roots of the equation. A quadratic equation has two roots which are given by the following
two formula
𝑟𝑜𝑜𝑡1 =
−𝑏 − √𝑏
2 − 4𝑎𝑐
2𝑎
𝑟𝑜𝑜𝑡2 =
−𝑏+ √𝑏2−4𝑎𝑐
2𝑎
Write a program that requests the user to input the values of a, b, and c and outputs root1
and root2'''
a = int(input("Enter value:\n"))
b = int(input("Enter value:\n"))
c = int(input("Enter value:\n"))
root1 = (-b-(b**2 - 4*a*c))/2*a
root2 =(-b+(b**2 - 4*a*c))/2*a
print("First root",root1)
print("Second root",root2)
#Output
'''Enter value:
1
Enter value:
2
Enter value:
1
First root -1.0
Second root -1.0'''

#Q34
'''. Write a program to accept the cost price of a bike and display the total price of bike
including road tax to be paid according to the following criteria :
 Cost price (in Rs) Tax
 > 150000 10 %
 > 50000 and <= 150000 08%
 <= 50000 04%'''
e = float(input("Enter Your bike cost\n"))
if e>150000:
    t1 = e*10/100
    print("Your road tax is",t1)
    print("Your final cost is:",e+t1)
elif 50000<e<=150000:
    t2 = e*8/100
    print("Your road tax is",t2)
    print("Your final cost is:",e+t2)
elif e<=50000:
    t3 = e*4/100
    print("Your road tax is",t3)
    print("Your final tax is:",e+t3) 
#Output
'''Enter Your bike cost
54000
Your road tax is 4320.0
Your final cost is: 58320.0'''

#Q35
'''Accept the basic salary of an employee from the user, and calculate the gross salary using :
Gross Salary = Basic Salary + DA + HRA – PF
DA = 30% of Basic Salary If Basic Salary < 5000 otherwise DA = 45% of the Basic Salary.
HRA = 15% of Basic Salary.
PF = 12% of Basic Salary.'''
a = float(input("Enter your basic salary\n"))
if a<5000:
    DA = a*30/100
else:
    DA = a*45/100
HRF = a*15/100
PF = a*12/100
print("Your gross salary is",a+DA+HRF-PF)
#output
'''Enter your basic salary
6000
Your gross salary is 8880.0'''

#Q36
'''Write a program to calculate the electricity bill (accept the number of electricity units used
from user) using following details:
 Units Price/unit
Up to 100 units No charge
After 100 units Rs 5 per unit
After 500 units Rs 8 per unit'''
a = float(input("Enter your electricity units:\n"))
if a<=100:
    print("Your electricity bill is zero")
elif 100<a<=500:
    b = (a-100)*5
    print("Your bill is",b)
elif a>500:
    c = ((a-500)*8) + 400*5
    print("your bill is ",c)
#Output
'''Enter your electricity units:
300
Your bill is 1000.0'''

#Q13
#Write a Python program to make a Simple Calculator.
a = float(input("Enter first number\n"))
b = float(input("Enter second number\n"))
print("For Addition:e\n For Subtraction:f\n For Multiplication:g\n For division:h\n")
c = input()
if c=='e':
    print(a+b)
elif c=='f':
    print(a-b)
elif c=='g':
    print(a*b)
elif c=='h':
    print(a/b)
#Output
'''Enter first number
10
Enter second number
5
For Addition:e
 For Subtraction:f
 For Multiplication:g
 For division:h

g
50.0'''

#Q30
# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern of alphabets
def alphapat(n):
	
	# initializing value corresponding to 'A'
	# ASCII value
	num = 65

	# outer loop to handle number of rows
	# 5 in this case
	for i in range(0, n):
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# explicitely converting to char
			ch = chr(num)
		
			# printing char value
			print(ch, end=" ")
	
		# incrementing number
		num = num + 1
	
		# ending line after each row
		print("\r")

# Driver Code
n = 5
alphapat(n)
#Output
'''A 
   B B 
   C C C 
   D D D D 
   E E E E E''' 







    

    


















