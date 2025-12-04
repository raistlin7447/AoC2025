dial = 50

rotations = [int(r[1:]) if r[0] == "R" else -int(r[1:]) for r in open("day01_input.txt").read().splitlines()]

num_zeros = 0

for i, rotation in enumerate(rotations):
    previous_dial = dial

    # Full Rotations
    num_zeros += abs(rotation) // 100

    # Rotate Dial
    dial += rotation % 100
    if dial < 0:
        dial = 100 + dial
    elif dial > 99:
        dial = dial - 100

    # Count if on zero
    if dial == 0:
        num_zeros += 1

    # Count if moved through zero left
    elif previous_dial != 0 and rotation < 0 and previous_dial - abs(rotation) % 100 < 0:
            num_zeros += 1

    # Count if moved through zero right
    elif previous_dial != 0 and rotation > 0 and previous_dial + rotation % 100 > 99:
            num_zeros += 1

print(num_zeros)

