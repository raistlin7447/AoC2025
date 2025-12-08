import itertools
import math

points = [tuple(map(int, i.split(","))) for i in open("day08_input.txt").read().splitlines()]

def distance(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    d = 0.0
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return d

point_distances = []
for point1, point2 in itertools.combinations(points, 2):
    point_distances.append((distance(point1, point2), point1, point2))

point_distances.sort(key=lambda p: p[0])

circuits = []

for distance, point1, point2 in point_distances[:1000]:
    wire = {point1, point2}

    new_circuits = []
    for circuit in circuits:
        if circuit & wire:
            wire.update(circuit)
        else:
            new_circuits.append(circuit)

    new_circuits.append(wire)
    circuits = new_circuits

circuits.sort(key=len, reverse=True)

total = len(circuits[0])
for circuit in circuits[1:3]:
    total *= len(circuit)

print(total)