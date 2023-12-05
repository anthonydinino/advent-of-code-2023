def main():
    f = open("input/day3.txt", "r")
    matrix = []
    for l in [x.rstrip() for x in f]:
        matrix.append(list(l))

    digits = findAllDigits(matrix)

    # Search for gears
    gearPartNumbers = []
    for x, row in enumerate(matrix):
        for y, col in enumerate(row):
            if col == "*":
                gear = calculateGear(x, y, matrix, digits)
                if gear:
                    gearPartNumbers.append(gear)
    print(sum(gearPartNumbers))


# If not a gear return False otherwise returns product of gear part numbers
def calculateGear(x, y, matrix, digits):
    digitIndexes = dict()
    for coord in getSorroundCoord(x, y, len(matrix)):
        for i in range(len(digits)):
            for j in digits[i]:
                if coord == j:
                    digitIndexes[i] = True
    if len(digitIndexes.keys()) == 2:
        # get product of gear's 2 part numbers
        product = 1
        for num in [getValue(digits[i], matrix) for i in digitIndexes.keys()]:
            product *= num
        return product
    else:
        return False


# returns e.g [[[0,1], [0,2]], [[5,6], [5,7]]]
def findAllDigits(matrix):
    digits = []
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
    return digits


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
