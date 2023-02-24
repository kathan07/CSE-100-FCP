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
