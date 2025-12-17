#write a function to split a number like 232323 into n equal parts
ranges = (open("input.txt", "r").read().strip()).split(",")

def split_number(n, parts):
    s = str(n)
    if len(s) % parts != 0:
        return None
    length = len(s) // parts
    return [int(s[i:i + length]) for i in range(0, len(s), length)]


print(split_number(232323, 5))