import os, sys, time

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

value = True
while (value):
    os.system("scrape.py")
    print("Data will refresh in:")
    countdown(int(10))
    
