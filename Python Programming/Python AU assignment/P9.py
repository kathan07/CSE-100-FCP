#Write a Python program that generates and prints 100 random numbers.
import random
i=1
while i<=100:
    print(random.randint(0,100),end=',')
    i=i+1