
ranges = [map(int, i.split("-")) for i in open("day02_input.txt").read().split(",")]

bad_id_sum = 0

for start, end in ranges:
    for id in range(start, end+1):
        id_str = str(id)
        i = (id_str + id_str).find(id_str, 1, -1)
        if i != -1:
            bad_id_sum += id

print(bad_id_sum)