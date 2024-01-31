def printList(distCost):
    for pair in distCost:
        stringFormatted = str (pair[0])+" Miles, "+"£ "+str (pair [1])
        print(stringFormatted)

fileName = input("Enter a file name: ")
infline = open( fileName )
table = []
recNum = 0
for line in infline :
    table.append(line.split(','))
    table[recNum][0]=int(table[recNum][0])
    table[recNum][1]=float(table[recNum][1])
    recNum+=1

infline.close()
printList(table) 
