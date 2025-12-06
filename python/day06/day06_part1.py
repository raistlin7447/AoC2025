import operator
from functools import reduce

problems = [i.split() for i in open("day06_input.txt").read().splitlines()]
problems = list(zip(*problems))

total = 0
for *numbers, op in problems:
    numbers = list(map(int, numbers))

    op = operator.add if op == "+" else operator.mul
    problem_total = reduce(op, numbers)

    total += problem_total

print(total)