def otpgen1(size):

    import random as rd
    n=size
    lower=10**(n-1)
    upper=10**n-1
    rdn=rd.randint(lower,upper)
    print(rdn)
for i in range(0,20,1):
    otpgen1(6)






