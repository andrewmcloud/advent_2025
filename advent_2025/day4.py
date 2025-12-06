with open("../input/day4.txt", "r") as f:
    g = [x.strip("\n") for x in f.readlines()]

neighbors = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i != 0 or j != 0]

def make_grid(g: list[str]) -> dict[tuple[int, int], int]:
    return {(i, j): 1 if e != "." else 0 for i, r in enumerate(g) for j, e in enumerate(r)}


def rolls_accessed(grid: dict[tuple[int, int], int], neighbors: list[tuple[int, int]], iterations: int = -1):
    coords = set()
    total = 0
    while True:
        total += len(coords)
        for coord in coords:
            grid[coord] = 0

        coords = set()

        for k, v in grid.items():
            if v == 0:
                continue
            neighboring_rolls = sum(grid.get((k[0]+n[0], k[1]+n[1]), 0) for n in neighbors)
            if neighboring_rolls < 4:
                coords.add(k)
        if iterations == 0 or not coords:
            return total
        iterations -= 1


print(f"part 1: {rolls_accessed(make_grid(g), neighbors, 1)}")
print(f"part 2: {rolls_accessed(make_grid(g), neighbors)}")
