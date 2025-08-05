import random as rd
def otpgen2(size,qty):
    def otpgen1(size):
        n=size
        lower=10**(n-1)
        upper=10**n-1
        rdn=rd.randint(lower,upper)
        print(rdn)
    for i in range(0,qty,1):
        otpgen1(size)
otpgen2(6,20)
otpgen2(4,40)