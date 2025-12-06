with open("../input/day3.txt", "r") as f:
    banks = [l.strip() for l in f.readlines()]

def find_max_joltage(bank: str, length: int) -> int:
    bank = [int(x) for x in bank]
    max_joltage = ""
    start = 0
    for end in range(length-1, -1, -1):
        search_slice = bank[start:-end] if end > 0 else bank[start:]
        x = max(search_slice)
        start += search_slice.index(x) + 1
        max_joltage += str(x)
    return int(max_joltage)


part1 = sum(find_max_joltage(bank, 2) for bank in banks)
part2 = sum(find_max_joltage(bank, 12) for bank in banks)
print(f"part 1: {part1}")
print(f"part 2: {part2}")