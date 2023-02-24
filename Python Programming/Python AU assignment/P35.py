a = float(input("Enter your basic salary\n"))
if a<5000:
    DA = a*30/100
else:
    DA = a*45/100
HRF = a*15/100
PF = a*12/100
print("Your gross salary is",a+DA+HRF-PF)
