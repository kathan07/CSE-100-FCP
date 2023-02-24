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
