import os
dir1="virus"
if not os.path.exists(dir1):
     os.mkdir(dir1)
     os.chdir(dir1)
for i in range(1,1111,1):
     os.mkdir("Devil"+str(i))