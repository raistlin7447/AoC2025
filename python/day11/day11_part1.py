devices = {}
for line in open("day11_input.txt"):
    device, outputs = line.split(":")
    devices[device] = outputs.strip().split()

def count_paths(start, end):
    if start == end:
        return 1

    return sum(count_paths(child, end) for child in devices[start])

print(count_paths("you", "out"))
