#Write a program to enter a number from the user and display the sum of all the digits in the number. [Hint: if user input is 123, display answer 6, which is addition of 1+2+3].
n =input("Enter a number:\n")
a = 0 
sum = 0
while a<len(n):
    sum = sum+int(n[a])
    a+=1
print(sum)