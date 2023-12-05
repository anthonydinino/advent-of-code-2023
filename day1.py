f = open("input/day1.txt", "r")


def getNum(s, mode="first"):
    numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    i = 0
    frontChar = -1 if mode == "first" else 0
    while i < len(s):
        x = s[0 : i + 1] if mode == "first" else s[i * -1 if i != 0 else -1 :]
        if x[frontChar].isdigit():
            return x[frontChar]
        for k in numbers.keys():
            if k in x:
                return str(numbers[k])
        i += 1


total = 0
for x in map(lambda x: x.rstrip(), f):
    first, last = (getNum(x), getNum(x, "last"))
    total += int((first or last) + (last or first))

print(total)
