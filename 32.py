import random as rd
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
list1=otpgen2(4,10)
print(list1)
