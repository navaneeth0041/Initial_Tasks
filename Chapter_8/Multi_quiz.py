from random import *
from time import *
import pyinputplus as pyip
n_qns=int(input())
for i in range(n_qns):
    n1=randint(0,9)
    n2=randint(0,9)
    ans=n1*n2

    response=pyip.inputNum(prompt=f'{n1}*{n2}= ',limit=3,timeout=5)
    if ans==response:
        print('Correct')
        sleep(1)
    else:
        print('Wrong!! Try again...')
        
        