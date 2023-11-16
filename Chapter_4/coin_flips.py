from random import *
n_streaks=0
for k in range(10000):
    lst=[]
    for i  in range(100):
        turn=randint(0,1)
        if turn==0:
            lst.append('T')
        else:
            lst.append('H')
    for j in range(len(lst)-6):
        if lst[j]==lst[j+1]==lst[j+2]==lst[j+3]==lst[j+4]==lst[j+5]!=lst[j+6]:
            n_streaks+=1

print(n_streaks/(10000))