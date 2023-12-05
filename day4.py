def main():
    f = open("input/day4.txt", "r")
    scoreTotal = []
    for l in [x.rstrip() for x in f]:
        numbers = [x.strip() for x in l.split(":")[1].strip().split("|")]
        winningNumbers = [int(n) for n in numbers[0].split(" ") if n]
        myNumbers = [int(n) for n in numbers[1].split(" ") if n]
        matches = 0
        for n in myNumbers:
            for w in winningNumbers:
                if n == w:
                    matches += 1
        scoreTotal.append(calculateScore(matches))
    print(sum(scoreTotal))


def calculateScore(matches):
    if matches < 1:
        return 0
    else:
        score = 1
        for i in range(1, matches):
            score *= 2
        return score


if __name__ == "__main__":
    main()
