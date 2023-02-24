#Write a program called ExtractDigits to extract each digit from an int in the reverse order. For example, if the int is 12345, the output shall be "5 4 3 2 1", with a space separating the digits.
#ExtractDigits
a=int(input('ENTER A NUMBER : '))
x=a%10
y=(a%100)//10
z=(a%1000)//100
b=(a%10000)//1000
c=(a%100000)//10000
print(x,' ',y,' ',z,' ',b,' ',c,)