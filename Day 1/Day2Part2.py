lastInput = False
index = 0

elfs = list()
elfs.append(0)

while not lastInput:
    userInput = input()
    if userInput == 'c':
        lastInput = True
        break
    elif userInput == '':
        index = index + 1
        elfs.append(0)
    else:
        elfs[index] = elfs[index] + int(userInput)

elfs.sort()
elfs.reverse()

TotalTop3 = elfs[0] + elfs[1] + elfs[2]

print("The total of the top 3 elfs is: " + str(TotalTop3))