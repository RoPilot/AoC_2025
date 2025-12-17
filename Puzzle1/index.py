sequence = (open("inputS.txt", "r").read().strip()).split("\n")

def get_dir(instruction):
    #print(instruction)
    if list(instruction[0]) == ["L"]:
        return 0
    else:
        return 1
    
def get_count(instruction):
    listInstruction = list(instruction)
    removeFirst = listInstruction[1:]
    return int("".join(removeFirst))

masterCount = 50
zeroCount = 0
i = 0 

for instruction in sequence:
    i +=1 
    direction = get_dir(instruction)
    count = get_count(instruction)
    #print(direction, count)

    if direction == 0:

        for x in range(count):
            masterCount -= 1
            if masterCount == 0:
                zeroCount += 1
            if masterCount == -1:
                masterCount = 99


    else:
        for x in range(count):
            masterCount += 1
            if masterCount == 100:
                masterCount = 0
                zeroCount += 1

    print(zeroCount)

print("Final Count:", masterCount)