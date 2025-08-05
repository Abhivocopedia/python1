def otpgen1(size):

    import random as rd
    n=size
    lower=10**(n-1)
    upper=10**n-1
    rdn=rd.randint(lower,upper)
    print(rdn)
otpgen1(6)
otpgen1(8)