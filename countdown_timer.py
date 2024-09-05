import time

def count():
    t=int(input("Enter time in seconds: "))
    while t:
        min,secs=divmod(t,60)
        timer='{:02d}:{:02d}'.format(min,secs)
        print(timer,end="\r")
        time.sleep(1)
        t-=1
        print("\n")