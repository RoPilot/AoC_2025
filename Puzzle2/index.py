from sympy import li


ranges = (open("inputS.txt", "r").read().strip()).split(",")

def split_number(n, parts):
    s = str(n)
    if len(s) % parts != 0:
        return None
    length = len(s) // parts
    return [int(s[i:i + length]) for i in range(0, len(s), length)]

def checkValidity(num):

    splitNum = list(str(num))

    for i in range(2, int(len(splitNum)) + 1):

        
        equalNumber = split_number(num, i)

        if not equalNumber is None:

            res = all(x == equalNumber[0] for x in equalNumber)
            if res:
                return True


invalidNumCount = []

for r in ranges:
    r1, r2 = r.split("-")
    
    for i in range(int(r1), int(r2) + 1):
        if checkValidity(i):
            invalidNumCount.append(i)

print(invalidNumCount)
print(f"Total invalid numbers: {sum(invalidNumCount)}")