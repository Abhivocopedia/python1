import random as rd
bank=input("Enter the name of bank")
def otpgen2(size,qty):
    otps=[]
    def otpgen1(size):
        lower=10**(size-1)
        upper=10**size-1
        rdn=rd.randint(lower,upper)
        otps.append(rdn)
        
    for i in range(0,qty,1):
        otpgen1(size)
    return otps
if bank=="ICICI":
    size1=4
elif bank=="HDFC":
    size1=6
else:
    size1=5
list1=otpgen2(size1,10)
print(list1)
