a = float(input("Enter your income :\n"))
if a<=500000:
    print("Your income tax is zero")
elif 500000<a<=1000000:
    b = (a-500000)*10/100
    print("Your income tax is",b)
elif a>1000000:
    c = (a-1000000)*20/100 + 500000*10/100
    print("your income taxis ",c)

