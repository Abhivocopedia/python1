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
banks_dict={"ICICI":4,"HDFC":6,"SBI":5,"KOTAK":8,"HSBC":10}
psws=[]
for i,size in list(banks_dict.keys()),list(banks_dict.values()):
    psws.append(otpgen2(i,size))
print(psws)



#print(banks_dict.keys())
#print(banks_dict.values())
#print(banks_dict.items())

#list1=otpgen2(size1,10)
#print(list1)
