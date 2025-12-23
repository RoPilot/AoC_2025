location = (open("inputS.txt", "r").read().strip()).split("\n")

totalCount = 0
fakeRows = []

# First pass: build the grid once without seeding an empty row.
for row in range(len(location)):
    basket = list(location[row])

    if row == 0:
        upperBasket = ["."] * len(basket)
        lowerBasket = list(location[row + 1])
    elif row == len(location) - 1:
        upperBasket = list(location[row - 1])
        lowerBasket = ["."] * len(basket)
    else:
        upperBasket = list(location[row - 1])
        lowerBasket = list(location[row + 1])

    # Pad copies for neighbor checking without growing stored rows.
    paddedUpper = ["."] + upperBasket + ["."]
    paddedBasket = ["."] + basket + ["."]
    paddedLower = ["."] + lowerBasket + ["."]

    tempFakeRow = []
    for i in range(len(basket)):
        rowCount = 0
        if basket[i] == ".":
            tempFakeRow.append(".")
        else:
            idx = i + 1  # account for padding offset
            if paddedUpper[idx] == "@":
                rowCount += 1
            if paddedUpper[idx + 1] == "@":
                rowCount += 1
            if paddedUpper[idx - 1] == "@":
                rowCount += 1
            if paddedBasket[idx + 1] == "@":
                rowCount += 1
            if paddedBasket[idx - 1] == "@":
                rowCount += 1
            if paddedLower[idx + 1] == "@":
                rowCount += 1
            if paddedLower[idx - 1] == "@":
                rowCount += 1
            if paddedLower[idx] == "@":
                rowCount += 1

            if rowCount < 4:
                tempFakeRow.append(".")
                totalCount += 1
            else:
                tempFakeRow.append("@")

    fakeRows.append(tempFakeRow)

for x in fakeRows:
    print("".join(x))

print("--------------------------------- SECOND RUN ---------------------------------")

# Repeatedly remove until a pass makes no changes.
while True:
    removedOneThisPass = False
    newFakeRows = []

    for row in range(len(fakeRows)):
        basket = list(fakeRows[row])

        if row == 0:
            upperBasket = ["."] * len(basket)
            lowerBasket = list(fakeRows[row + 1]) if row + 1 < len(fakeRows) else ["."] * len(basket)
        elif row == len(fakeRows) - 1:
            upperBasket = list(fakeRows[row - 1])
            lowerBasket = ["."] * len(basket)
        else:
            upperBasket = list(fakeRows[row - 1])
            lowerBasket = list(fakeRows[row + 1])

        paddedUpper = ["."] + upperBasket + ["."]
        paddedBasket = ["."] + basket + ["."]
        paddedLower = ["."] + lowerBasket + ["."]

        tempFakeRow = []
        for i in range(len(basket)):
            rowCount = 0
            if basket[i] == ".":
                tempFakeRow.append(".")
            else:
                idx = i + 1
                if paddedUpper[idx] == "@":
                    rowCount += 1
                if paddedUpper[idx + 1] == "@":
                    rowCount += 1
                if paddedUpper[idx - 1] == "@":
                    rowCount += 1
                if paddedBasket[idx + 1] == "@":
                    rowCount += 1
                if paddedBasket[idx - 1] == "@":
                    rowCount += 1
                if paddedLower[idx + 1] == "@":
                    rowCount += 1
                if paddedLower[idx - 1] == "@":
                    rowCount += 1
                if paddedLower[idx] == "@":
                    rowCount += 1

                if rowCount < 4:
                    tempFakeRow.append(".")
                    totalCount += 1
                    removedOneThisPass = True
                else:
                    tempFakeRow.append("@")
        newFakeRows.append(tempFakeRow)

    fakeRows = newFakeRows

    for x in fakeRows:
        print("".join(x))

    if not removedOneThisPass:
        break

for x in fakeRows:
    print("".join(x))

print("Total safe spots:", totalCount)
