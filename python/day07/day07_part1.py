diagram = [list(i) for i in open("day07_input.txt").read().splitlines()]

total_splits = 0
for r, line in enumerate(diagram[:-1]):
    for c, char in enumerate(line):
        if char == "S" or char == "|":
            if diagram[r+1][c] == "^":
                total_splits += 1
                diagram[r+1][c-1] = "|"
                diagram[r+1][c+1] = "|"
            else:
                diagram[r+1][c] = "|"

print(total_splits)