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

print("The most calories is: " + str(max(elfs)))