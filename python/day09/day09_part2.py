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

def ccw(A,B,C):
    return (C[1]-A[1])*(B[0]-A[0]) > (B[1]-A[1])*(C[0]-A[0])

def intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

def get_edges(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    # Normalize so x1 <= x2 and y1 <= y2
    left, right = sorted((x1, x2))
    top, bottom = sorted((y1, y2))

    # Shrink rectangle by 1 on all sides
    left += 1
    right -= 1
    top += 1
    bottom -= 1

    # If the rectangle collapses, return empty list
    if left >= right or top >= bottom:
        return []

    # Build and return edges
    return [
        ((left, top), (right, top)),        # top edge
        ((right, top), (right, bottom)),    # right edge
        ((right, bottom), (left, bottom)),  # bottom edge
        ((left, bottom), (left, top)),      # left edge
    ]

for area, red_tile1, red_tile2 in areas:
    line_crosses = False
    for line_point1, line_point2 in itertools.pairwise(red_tiles + [red_tiles[0]]):
        edges = get_edges(red_tile1, red_tile2)
        if not edges:
            line_crosses = True
            break
        for edge_point1, edge_point2 in edges:
            if intersect(edge_point1, edge_point2, line_point1, line_point2):
                line_crosses = True
                break
        if line_crosses:
            break
    if not line_crosses:
        print(area)
        break
