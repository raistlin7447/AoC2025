from functools import cache

devices = {}
for line in open("day11_input.txt"):
    device, outputs = line.split(":")
    devices[device] = outputs.strip().split()

@cache
def count_paths(start, end):
    if start == end:
        return 1
    if start == "out":
        return 0

    return sum(count_paths(child, end) for child in devices[start])

svr_fft = count_paths("svr", "fft")
fft_dac = count_paths("fft", "dac")
dac_out = count_paths("dac", "out")

print(svr_fft * fft_dac * dac_out)
