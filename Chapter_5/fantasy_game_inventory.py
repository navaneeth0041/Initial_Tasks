dict={"arrow":12,"gold coin":42, "rope":1,"torch":6,"dagger":1}
def displayInventory(dict):
    print("Inventory: ")
    print()
    for i in dict:
        print(str(dict[i]), i)
    sum=0
    for i in dict.values():
        sum+=i
    print("Total number of items: ",sum)


    
displayInventory(dict)