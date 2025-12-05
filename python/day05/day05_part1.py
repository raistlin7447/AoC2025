ranges, ingredients = open("day05_input.txt").read().split("\n\n")

ranges = [list(map(int, i.split("-"))) for i in ranges.splitlines()]
ingredients = map(int, ingredients.splitlines())

num_fresh = 0
for ingredient in ingredients:
    for low, high in ranges:
        if low <= ingredient <= high:
            num_fresh += 1
            break

print(num_fresh)