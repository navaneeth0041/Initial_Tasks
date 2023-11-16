from random import *
import time

for i in range(10):
    n1=randint(0,9)
    n2=randint(0,9)
    product=n1*n2
    tries=3
    tm=time.time()
    while time.time()-tm <8 and tries>0:
        ans=int(input(f"Enter tha produt of {n1} x {n2}: "))
        try:
            if ans==product:
                print("The answer is correct!!")
                time.sleep(1)
                break
            else:
                print("Wrong Answer")
                tries-=1
        except ValueError:
            print("Check your input")
    if tries==0:
        print("No more tries..")
    elif time.time()-tm>=8:
        print("Time is up!")