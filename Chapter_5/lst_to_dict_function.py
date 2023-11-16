dragonloot=['gold coin','dagger','gold coin','gold coin','ruby']
inv={'gold coin': 42,'rope':1}

def addtoinventory(dragonloot,inv):
    for i in dragonloot:
        if i in inv:
            inv[i]+=1
        else:
            inv[i]=1
    print("Inventory: ")
    print()
    for i in inv:
        print(str(inv[i]), i)
    sum=0
    for i in inv.values():
        sum+=i
    print("Total number of items: ")

    
addtoinventory(dragonloot,inv)