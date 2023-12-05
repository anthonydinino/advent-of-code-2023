def main():
    f = open("input/day4.txt", "r")
    scratchcards = {}
    runsCount = 0
    for l in [x.rstrip() for x in f]:
        game = [x.strip() for x in l.split(":")]
        gameNum = int([x for x in game[0].split(" ") if x][1])
        numbers = game[1].strip().split("|")
        winningNumbers = [int(n) for n in numbers[0].split(" ") if n]
        myNumbers = [int(n) for n in numbers[1].split(" ") if n]

        # start playing
        runs = 1 + scratchcards.get(gameNum, 0)
        runsCount += runs
        while runs > 0:
            temp = int(gameNum)
            for n in myNumbers:
                for w in winningNumbers:
                    if n == w:
                        temp += 1
                        scratchcards[temp] = scratchcards.get(temp, 0) + 1
            runs -= 1
    print(runsCount)


if __name__ == "__main__":
    main()
