def gcd(x,y):
    z=min(x,y)
    for i in range(1,z+1):
        if((x%i==0) and (y%i==0)):
            hcf=i
    return(hcf)        
m=int(input("Enter the first number:  "))
n=int(input("Enter the second number:  "))
print("HCF is    ",gcd(m,n))

