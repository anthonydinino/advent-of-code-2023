def main():
    f = open("input/day2.txt", "r")
    p = {"red": 12, "green": 13, "blue": 14}
    total = 0
    for l in [x.rstrip() for x in f]:
        id = int(l.split(":")[0].split(" ")[1])
        game = list(map(lambda x: x.strip(), l.split(":")[1].split(";")))
        if not isGamePossible(game, p):
            continue
        else:
            total += id
    print(total)


# e.g game = ["3 green, 15 blue, 14 red", "3 green, 15 blue, 14 red"]
# e.g possible = {"red": 12, "green": 13, "blue": 14}
def isGamePossible(game: list, p: dict):
    for handful in game:
        for pick in [c.strip().split(" ") for c in handful.split(",")]:
            number, color = int(pick[0]), pick[1]
            if number > p[color]:
                return False
    return True


if __name__ == "__main__":
    main()
