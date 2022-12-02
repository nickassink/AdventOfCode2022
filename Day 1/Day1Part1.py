lastInput = False
index = 0
elfs = list()
elfs.append(0)

inputFile = open("Day 1/input.txt", "r")

while not lastInput:
    userInput = inputFile.readline()
    if userInput == '':
        lastInput = True
        break
    elif userInput == '\n':
        index = index + 1
        elfs.append(0)
    else:
        elfs[index] = elfs[index] + int(userInput)

print("The most calories is: " + str(max(elfs)))