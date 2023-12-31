def main():
    f = open("input/day5.txt", "r")
    seeds = []
    farmMap = []
    maps = []
    insideMap = False
    for i, l in enumerate([x.rstrip() for x in f]):
        if i == 0:
            seeds = [int(n) for n in l.split(":")[1].split(" ") if n]
            continue
        if l and l[0].isalpha():
            insideMap = True
            continue
        m = [int(n) for n in l.split() if n]
        if m:
            farmMap.append(m)
            continue
        if insideMap and not l:
            insideMap = False
            maps.append(farmMap)
            farmMap = []

    # get last map
    maps.append(farmMap)
    farmMap = []

    # navigate through maps to get location
    print(seeds)
    locations = []
    for s in seeds:
        for m in maps:
            s = getMappedValue(s, m)
        locations.append(s)
    print(min(locations))

    # part 2
    newSeeds = {}
    for i in range(0, len(seeds), 2):
        for s in range(seeds[i], seeds[i] + seeds[i + 1]):
            newSeeds[s] = True
    print(newSeeds.keys())

    # navigate through maps to get location
    locations = []
    for s in newSeeds:
        print(f"{s=}", end=" ")
        for m in maps:
            s = getMappedValue(s, m)
        print(s)
        locations.append(s)
    print(min(locations))


def getMappedValue(s, m):
    for dest, source, r in m:
        if s in range(source, source + r):
            return s + dest - source
    return s


if __name__ == "__main__":
    main()
