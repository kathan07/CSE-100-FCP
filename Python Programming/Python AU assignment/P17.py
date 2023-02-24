#Create a converter that will convert a distance in meters to feet and inches.
n=float(input('Enter length in metres:'))
f=n*3.281
r=f%1
i=r*12
print(int(f),' feet and ',i,' inches.')