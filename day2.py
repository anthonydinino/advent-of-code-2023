def main():
    f = open("input/day2.txt", "r")
    total = 0
    for l in [x.rstrip() for x in f]:
        game = list(map(lambda x: x.strip(), l.split(":")[1].split(";")))
        product = 1
        for x in list(calculateMinGame(game).values()):
            product *= x
        total += product
    print(total)


# e.g game = ["3 green, 15 blue, 14 red", "3 green, 15 blue, 14 red"]
def calculateMinGame(game: list):
    thisGame = {"red": 0, "green": 0, "blue": 0}
    for handful in game:
        for pick in [c.strip().split(" ") for c in handful.split(",")]:
            number, color = int(pick[0]), pick[1]
            if number > thisGame[color]:
                thisGame[color] = number
    return thisGame


if __name__ == "__main__":
    main()
