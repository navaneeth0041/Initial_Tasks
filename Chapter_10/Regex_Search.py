import os
import re
from pathlib import Path
fold_path=input("Enter the path here: ")
if not Path(fold_path).exists():
    print("Check your input again!!!")

else:
    exp=input("Enter the expression to be searched here: ")
    flag=0
    for foldername, subfolders, filenames in os.walk(fold_path):
        for filename in filenames:
            if filename.endswith('txt'):
                op=open(filename,'r')
                rd=op.readlines()
                for j in rd:
                    for k in j.split():
                        if re.search(exp,k,re.I):
                            flag=1
    if flag==1:
        print("Expression found")
    else:
        print("No such expssion")
