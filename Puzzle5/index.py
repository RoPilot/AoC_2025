inventory = (open("inputS.txt", "r").read().strip()).split("\n")

freshRanges = []
idChecks = []

for item in inventory:
    if "-" in list(item):
        freshRanges.append(item)
    else:
        idChecks.append(item)

validIDs = []

idChecks.remove("")

for _range in freshRanges:
    start, end = _range.split("-")
    start = int(start)
    end = int(end)
    
    for i in range(start, end + 1):
        print(i)
        validIDs.append(i)
    
    print(f"Range {start}-{end} complete. {len(idChecks)} IDs remaining.")




#print(validIDs)
print(len(set(validIDs)))