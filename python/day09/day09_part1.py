import itertools

red_tiles = [list(map(int, i.split(","))) for i in open("day09_input.txt").read().splitlines()]

def area(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    length1 = abs(x1 - x2) + 1
    length2 = abs(y1 - y2) + 1
    return length1 * length2

areas = []
for red_tile1, red_tile2 in itertools.combinations(red_tiles, 2):
    areas.append((area(red_tile1, red_tile2), red_tile1, red_tile2))

areas.sort(reverse=True)

print(areas[0][0])
