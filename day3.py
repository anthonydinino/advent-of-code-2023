def main():
    f = open("input/day3.txt", "r")
    matrix = []
    digits = []
    partNumbers = []
    for l in [x.rstrip() for x in f]:
        matrix.append(list(l))

    # Record all digit positions
    inDigit = False
    tempDigit = []
    for x, row in enumerate(matrix):
        for y, col in enumerate(row):
            if col.isdigit():
                if inDigit:
                    tempDigit.append([x, y])
                else:
                    inDigit = True
                    tempDigit.append([x, y])
            elif inDigit:
                digits.append(tempDigit)
                tempDigit = []
                inDigit = False

    # Check if digits are part numbers
    for numList in digits:
        if isPartNumber(numList, matrix):
            partNumbers.append(getValue(numList, matrix))
    print(sum(partNumbers))


def isPartNumber(numList, matrix):
    for i in numList:
        for j in getSorroundCoord(i[0], i[1], len(matrix)):
            if isSymbol(matrix[j[0]][j[1]]):
                return True
    return False


def isSymbol(d):
    return d != "." and not d.isdigit()


def getSorroundCoord(x, y, size):
    tempCoord = [
        [x - 1, y - 1],
        [x, y - 1],
        [x + 1, y - 1],
        [x + 1, y],
        [x + 1, y + 1],
        [x, y + 1],
        [x - 1, y + 1],
        [x - 1, y],
    ]
    return [
        c
        for c in tempCoord
        if not (c[0] < 0 or c[1] < 0 or c[0] == size or c[1] == size)
    ]


def getValue(num, matrix):
    return int("".join([matrix[d[0]][d[1]] for d in num]))


if __name__ == "__main__":
    main()
