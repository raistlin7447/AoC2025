
ranges = [map(int, i.split("-")) for i in open("day02_input.txt").read().split(",")]

bad_id_sum = 0

for start, end in ranges:
    for id in range(start, end+1):
        id_str = str(id)
        if len(id_str) % 2 != 0:  # Odd number
            continue

        if id_str[:len(id_str) // 2] == id_str[len(id_str) // 2:]:
            bad_id_sum += id

print(bad_id_sum)