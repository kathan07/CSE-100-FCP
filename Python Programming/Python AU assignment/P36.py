a = float(input("Enter your electricity units:\n"))
if a<=100:
    print("Your electricity bill is zero")
elif 100<a<=500:
    b = (a-100)*5
    print("Your bill is",b)
elif a>500:
    c = ((a-500)*8) + 400*5
    print("your bill is ",c)

