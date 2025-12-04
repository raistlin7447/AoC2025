dial = 50

rotations = [int(r[1:]) if r[0] == "R" else -int(r[1:]) for r in open("day01_input.txt").read().splitlines()]

num_zeros = 0

for rotation in rotations:
    dial += rotation % 100
    if dial < 0:
        dial = 100 + dial
    elif dial > 99:
        dial = dial - 100
    if dial == 0:
        num_zeros += 1

print(num_zeros)

