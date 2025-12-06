import operator
from functools import reduce

problems = [[j for j in i] for i in open("day06_input.txt").read().splitlines()]
problems.insert(len(problems) - 1, [" "] * len(problems[0]))
problems = list(zip(*problems))
problems.reverse()
problems = [i.split() for i in "".join(["".join(i) for i in problems]).split(" " * len(problems[0]))]

total = 0
for *numbers, op in problems:
    numbers = list(map(int, numbers))

    op = operator.add if op == "+" else operator.mul
    problem_total = reduce(op, numbers)

    total += problem_total

print(total)