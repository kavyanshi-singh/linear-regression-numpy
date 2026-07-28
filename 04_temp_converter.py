temp=float(input("What's the temperature? "))
unit=input("Enter the unit(C/F)- ")

if unit=="C":
    c=(temp-32)*(5/9)
    print(f"{c} Degree Fahreniet")
elif unit=="F":
    f=(temp*9/5)+32
    print(f"{f} Degree Celsius")
else:
    print("Not valid")



