tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
def printtable(tableData):
    colwidth=[]
    for i in range(len(tableData)):
        for j in tableData[i]:
            colwidth.append(len(j))
        maxi=max(colwidth)
    for k in range(len(tableData[i])):
        for l in tableData:
            print(l[k].rjust(maxi),end=" ")
        print()
printtable(tableData)
