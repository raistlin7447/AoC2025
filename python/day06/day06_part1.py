import operator

problems = [i.split() for i in open("day06_input.txt").read().splitlines()]
problems = list(zip(*problems))

total = 0
for *numbers, op in problems:
    numbers = list(map(int, numbers))
    if op == "+":
        op = operator.add
    elif op == "*":
        op = operator.mul

    problem_total = numbers[0]
    for number in numbers[1:]:
        problem_total = op(problem_total, number)

    total += problem_total

print(total)