import re
def str_pass(password):
    flag=0
    if len(password)<8:
        flag=0
    elif not re.search(r'[A-Z]',password):
        flag=0
    elif not re.search(r'\d',password):
        flag=0
    elif not re.search(r'[a-z]',password):
        flag=0
    else:
        flag=1

    if flag==1:
        print("Password is strong")
        return True

    else:
        print("Try another password")
        return False
while True:
    password=input("Test your password here: ")
    if str_pass(password):
        break
