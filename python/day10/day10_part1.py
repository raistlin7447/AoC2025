from collections import deque

machines = []
for line in open("day10_input.txt").read().splitlines():
    line_lights, *line_buttons, _ = line.split()

    lights = int(line_lights[1:-1][::-1].replace("#", "1").replace(".", "0"), 2)

    buttons = []
    for button in line_buttons:
        bitmask = 0
        for i in button[1:-1].split(","):
            bitmask = bitmask | 1 << int(i)
        buttons.append(bitmask)

    machines.append((lights, buttons))

def num_presses(lights: int, buttons: list[int]) -> int | None:
    seen = {0}
    queue = deque([0])
    count = 0

    while queue:
        for _ in range(len(queue)):
            status = queue.popleft()

            if status == lights:
                return count

            for button in buttons:
                nxt = status ^ button
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)

        count += 1

    return None


total = 0
for lights, buttons in machines:
    presses = num_presses(lights, buttons)
    if presses is not None:
        total += presses

print(total)