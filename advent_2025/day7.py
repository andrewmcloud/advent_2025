from functools import cache
with open("../input/day7.txt", "r") as f:
    g = [x.strip("\n") for x in f.readlines()]

def make_grid(g: list[str]) -> dict[tuple[int, int], str]:
    return {(i, j): e for i, r in enumerate(g) for j, e in enumerate(r)}

def find_start(grid: dict[tuple[int, int], str]) -> tuple[int, int]:
    return next(k for k, v in grid.items() if v == "S")

def count_beam_splits(grid: dict[tuple[int, int], str]) -> int:
    to_explore = {find_start(grid),}
    beam_splits = 0
    for i in range(1, len(g)):
        next_explore = set()
        for point in to_explore:
            if grid[point[0]+1, point[1]] == "^":
                next_explore.add((point[0]+1, point[1]-1))
                next_explore.add((point[0]+1, point[1]+1))
                beam_splits += 1
            else:
                next_explore.add((point[0]+1, point[1]))
        to_explore = next_explore
    return beam_splits


def timelines(grid: dict[tuple[int, int], str], start: tuple[int, int]) -> int:
    @cache
    def dfs(location: tuple[int, int]) -> int:
        if location[0] >= len(g):
            return 0  # done
        if grid[location] == "^":
            l = dfs((location[0], location[1]-1))
            r = dfs((location[0], location[1]+1))
            return l + r + 1  # count the split
        return dfs((location[0]+1, location[1]))  # no split, move down
    return dfs(start)

print(f"part 1: {count_beam_splits(make_grid(g))}")
print(f"part 2: {timelines(make_grid(g), find_start(make_grid(g)))}")
