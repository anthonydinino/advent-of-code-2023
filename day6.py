def main():
    f = open("input/day6.txt", "r")
    times = []
    distances = []
    for l in [x.rstrip() for x in f]:
        if "Time" in l:
            times = [int(x) for x in l.split()[1:]]
        elif "Distance" in l:
            distances = [int(x) for x in l.split()[1:]]

    res = []
    ans = []
    for i in range(len(times)):
        for j in range(1, times[i]):
            if getDistance(j, times[i]) > distances[i]:
                ans.append(j)
        res.append(len(ans))
        ans = []
    print(getProd(res))


def getDistance(time, target):
    d = time
    for i in range(target - time):
        d += time
    return d - time


def getProd(l):
    prod = 1
    for n in l:
        prod *= n
    return prod


if __name__ == "__main__":
    main()
