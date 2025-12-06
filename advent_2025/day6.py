import re
import math

with open("../input/day6.txt", "r") as f:
    lines = [line.strip("\n") for line in f.readlines()]

num_string, operators = lines[:-1], lines[-1]
operators = re.findall(r"[\+\*]", operators)

def part1(num_string: list[str], operators: str) -> int:
    numbers = [[int(n) for n in re.findall(r"\d+", l)] for l in num_string]
    total = 0
    for i, op in enumerate(operators):
        match op:
            case "+": total += sum(n[i] for n in numbers)
            case "*": total += math.prod(n[i] for n in numbers)
    return total

def part2(num_string: list[str], operators: str) -> int:
    numbers = [n[::-1] for n in num_string]
    operators = operators[::-1]
    total = 0
    op_index = 0
    nums = []
    for i in range(len(numbers[0])):
        x = "".join(number[i] for number in numbers).strip()
        if x:
            nums.append(int(x))
        if not x or i == len(numbers[0]) - 1:
            match operators[op_index]:
                case "+": total += sum(n for n in nums)
                case "*": total += math.prod(n for n in nums)
            nums = []
            op_index += 1
    return total

print(f"part 1: {part1(num_string, operators)}")
print(f"part 2: {part2(num_string, operators)}")
