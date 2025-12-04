banks = open("day03_input.txt").read().splitlines()

total_joltage = 0

for bank in banks:
    largest_digit = max(bank[:-1])
    largest_digit_location = bank.index(largest_digit)
    largest_next_digit = max(bank[largest_digit_location + 1:])

    joltage = int(largest_digit + largest_next_digit)
    total_joltage += joltage

print(total_joltage)