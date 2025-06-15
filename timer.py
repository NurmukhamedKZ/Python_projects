import time

num = int(input("enter the time in seconds:"))
for i in range(num,0,-1):
    seconds = i % 60
    minutes = i % 3600 // 60
    hours = i %86400 // 3600
    print(f"{hours:>02}:{minutes:>02}:{seconds:>02}")
    time.sleep(0.0001)

