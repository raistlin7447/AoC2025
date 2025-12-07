diagram = [[0 if j == "." else j for j in i] for i in open("day07_input.txt").read().splitlines()]

for r, line in enumerate(diagram[:-1]):
    for c, char in enumerate(line):
        if char == "S":
            char = 1
        if isinstance(char, int) and char > 0:
            if diagram[r+1][c] == "^":
                diagram[r+1][c-1] += char
                diagram[r+1][c+1] += char
            else:
                diagram[r+1][c] += char

print(sum(diagram[-1]))