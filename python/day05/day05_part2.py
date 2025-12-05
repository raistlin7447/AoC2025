ranges, _ = open("day05_input.txt").read().split("\n\n")

ranges = [list(map(int, i.split("-"))) for i in ranges.splitlines()]

new_ranges = []
ranges.sort()

current_low, current_high = ranges[0]
for next_low, next_high in ranges[1:]:
    if next_low > current_high:
        new_ranges.append([current_low, current_high])
        current_low, current_high = next_low, next_high
    else:
        current_high = max(current_high, next_high)
new_ranges.append([current_low, current_high])

total = 0
for low, high in new_ranges:
    total += high - low + 1

print(total)
