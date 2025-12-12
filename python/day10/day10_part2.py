from scipy.optimize import linprog
import numpy as np

machines = []
for line in open("day10_input.txt").read().splitlines():
    _, *line_buttons, line_joltages = line.split()

    buttons = [[int(i) for i in button[1:-1].split(",")] for button in line_buttons]
    joltage = [int(x) for x in line_joltages[1:-1].split(",")]

    machines.append((buttons, joltage))

total = 0
for buttons, joltage in machines:
    A = np.array([[i in button for i in range(len(joltage))] for button in buttons], int).T
    c = np.ones(len(buttons))
    b = np.asarray(joltage)

    total += linprog(c=c, A_eq=A, b_eq=b, integrality=1).fun

print(int(total))
