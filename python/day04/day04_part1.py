floor = [j for j in [i for i in open("day04_input.txt").read().splitlines()]]

total = 0
for i in range(len(floor)):
    for j in range(len(floor[i])):
        if floor[i][j] == ".":
            continue

        num_neighbors = 0
        for ix, jx in [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]:
            new_i = i + ix
            new_j = j + jx
            if new_i > len(floor) - 1 or new_i < 0 or new_j < 0 or new_j > len(floor[i]) -1:
                continue

            if floor[new_i][new_j] == "@":
                num_neighbors += 1

        if num_neighbors < 4:
            total += 1

print(total)
