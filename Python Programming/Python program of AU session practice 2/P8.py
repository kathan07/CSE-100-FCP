e = float(input("Enter Your bike cost\n"))
if e>150000:
    t1 = e*15/100
    print("Your road tax is",t1)
elif 50000<e<=150000:
    t2 = e/10
    print("Your road tax is",t2)
elif e<=50000:
    t3 = e*5/100
    print("Your road tax is",t3) 
