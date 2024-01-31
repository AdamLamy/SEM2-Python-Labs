def formatList(list):
    for i in range (0, len(list)):
        list[i][0] = str(list[i][0]) + " Miles"
        list[i][1] = "£" + str(list[i][1])
    return list

#main
#fileName = str(input("Enter name of file: "))
fileName = "week27\Tiny.txt"
file = open(fileName, 'r')
list = []
for line in file:
    list.append(line.split(','))
file.close()

newList = formatList(list)
for i in range (0, len(newList)):
    print(newList[i][0], newList[i][1])
