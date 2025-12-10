from __future__ import annotations
from itertools import combinations

with open("../input/day9.txt") as f:
    coords = [(int(x), int(y)) for x, y in [r.split(",") for r in f.readlines()]]

class Rectangle:
    def __init__(self, p1: tuple[int, int], p2: tuple[int, int]):
        self.xn = min(p1[0], p2[0])
        self.xx = max(p1[0], p2[0])
        self.yn = min(p1[1], p2[1])
        self.yx = max(p1[1], p2[1])

    def disjoint(self, other: Rectangle) -> bool:
        return (
            self.xn >= other.xx  # right
            or self.xx <= other.xn  # left
            or self.yn >= other.yx  # above
            or self.yx <= other.yn  # below
        )

    def __repr__(self) -> str:
        return f"{self.xn, self.xx, self.yn, self.yx}"

    def area(self) -> int:
        return (self.xx - self.xn + 1) * (self.yx - self.yn + 1)

rectangles = [Rectangle(p1, p2) for p1, p2 in combinations(coords, 2)]
edges = [Rectangle(p1, p2) for p1, p2 in zip(coords, coords[1:] + coords[:1])]

all_areas = [r.area() for r in rectangles]
disjoint_areas = [r.area() for r in rectangles if all(r.disjoint(edge) for edge in edges)]

print(f"part1: {max(all_areas)}")
print(f"part 2: {max(disjoint_areas)}")