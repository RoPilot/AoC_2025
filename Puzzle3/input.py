totalBatteries = (open("inputS.txt", "r").read().strip()).split("\n")

sumJolts = 0

for battery in totalBatteries:
    openBattery = list(battery)

    # openBattery = [1, 0, 0, 8, 9, 1, 1]
    maximumJoltA = 0 # Initial Value

    presentHighestValue = 0

    for master in range(0, len(openBattery)):
        #print("-------------------")

        leftVal = openBattery[master]

        for child in range(master + 1, len(openBattery)):

            #print(f"Master Index: {master}, Child Index: {child}")
            rightVal = openBattery[child]

            computedValue = int(str(leftVal) + str(rightVal))
            #print(f"Computed Value: {computedValue}")

            #print(f"computedValue {computedValue} > presentHighestValue {presentHighestValue}?")
            if computedValue > presentHighestValue:
                presentHighestValue = computedValue
    
    sumJolts += presentHighestValue


print(f"Total jolts: {sumJolts}")
