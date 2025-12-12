with open("../input/day12.txt") as f:
    lines = f.readlines()

fits_all = 0
for line in lines[30:]:
    size, counts = line.split(": ")
    x, y = [int(x) for x in size.split("x")]
    counts = [int(c) for c in counts.split(" ")]
    fits_all += 1 if x*y >= sum(c*9 for c in counts) else 0


print(f"part 1: {fits_all}")