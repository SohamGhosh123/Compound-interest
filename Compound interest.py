def compoundinterest(p,t,r):
    print("Principal:",p)
    print("Time:",t)
    print("Rate of interest:",r)
    amount=p*(pow((1+r)/100,t))
    ci=amount-p
    print("Compound interest is $:",ci)
    return ci
p=float(input("Enter the principal:"))
t=float(input("Enter the time in years:"))
r=float(input("Enter the rate of interest:"))
compoundinterest(p,t,r)