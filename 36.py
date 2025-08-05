import time
with open('python1/englishlevel1.txt', 'r') as file:
    L1 = [line.strip() for line in file]

interval = 3
for item in L1:
    print(item)
    time.sleep(interval)
