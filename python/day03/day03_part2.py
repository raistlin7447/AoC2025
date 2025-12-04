banks = open("day03_input.txt").read().splitlines()

total_joltage = 0

num_batteries = 12

for bank in banks:
    joltage = ""
    for i in range(1, num_batteries + 1):
        largest_digit = max(bank[:(-(num_batteries - i)) or None])
        largest_digit_location = bank.index(largest_digit)
        joltage += largest_digit
        bank = bank[largest_digit_location + 1:]

    total_joltage += int(joltage)

print(total_joltage)