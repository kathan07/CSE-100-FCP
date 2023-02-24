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




