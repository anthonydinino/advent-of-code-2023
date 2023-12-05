f = open("input/day1.txt", "r")

total = 0
for x in f:
    test = list(filter(lambda t: t.isdigit(), x))
    test = int(test[0] + test[-1])
    total += test

print(total)

