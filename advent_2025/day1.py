with open("../input/day1.txt", "r") as f:
    instructions = [l.strip("\n") for l in f.readlines()]


def next_value(value: int, instruction: str) -> (int, int):
    d, v = instruction[0], int(instruction[1:])
    match d:
        case "L":
            move = (value - v) % 100
            zeros = abs((value - v) // 100)
            zeros -= 1 if value == 0 else 0  # don't double count if we start at zero
            zeros += 1 if move == 0 else 0  # include the zero we land on
            return move if move >= 0 else 100 + move, zeros
        case "R":
            move = (value + v) % 100
            zeros = (value + v) // 100
            return move if move < 100 else move - 100, zeros
        case _:
            raise ValueError(f"Invalid direction: {d}")

def count_zeros(instructions: list[str]) -> tuple[int, int]:
    current = 50
    values = []
    zeros = []
    for i in range(len(instructions)):
        v, z = next_value(current, instructions[i])
        values.append(v)
        zeros.append(z)
        current = v
    return values.count(0), sum(zeros)


part1, part2 = count_zeros(instructions)
print(f"part 1: {part1}")
print(f"part 2: {part2}")