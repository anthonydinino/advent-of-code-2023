const fs = require("node:fs");

fs.readFile("./input/day6.txt", "utf-8", (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  [times, distances] = data.split("\n");
  times = parseInput(times);
  distances = parseInput(distances);

  console.log("part1:", calculate(times, distances));
  times = part2Join(times);
  distances = part2Join(distances);
  console.log("part2:", calculate(times, distances));
});

const calculate = (times, distances) => {
  return Array(times.length)
    .fill(0)
    .map((_, i) => {
      return Array(times[i] - 1)
        .fill(0)
        .map((_, j) => {
          j++;
          return distances[i] < (times[i] - j) * j;
        })
        .filter((x) => x).length;
    })
    .reduce((a, c) => a * c);
};

const parseInput = (input) =>
  input
    .split(":")[1]
    .split(" ")
    .filter((t) => t)
    .map((t) => parseInt(t));

const part2Join = (input) => {
  return [parseInt(input.map((t) => t.toString()).join(""))];
};
