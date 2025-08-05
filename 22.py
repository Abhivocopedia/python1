import os 
cwd=os.getcwd()
walk1=os.walk(top=cwd)
walk2=tuple(walk1)

for x in walk2:
    print(x)