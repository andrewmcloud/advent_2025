from collections import defaultdict, deque
from dataclasses import dataclass
from math import prod

with open("../input/day8.txt", "r") as f:
    lines = f.readlines()

@dataclass
class Point:
    x: int
    y: int
    z: int

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def distance(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2

points = [Point(*map(int, line.split(","))) for line in lines]

points_to_distances = {}
for i in range(len(points)):
    for j in range(i+1, len(points)):
        points_to_distances[(points[i], points[j])] = points[i].distance(points[j])

sorted_distances = sorted(points_to_distances.values())
distances_to_points = {v: k for k, v in points_to_distances.items()}

def bfs(points: list[Point], graph: dict[Point, set[Point]]) -> list[set[Point]]:
    visited = set()
    circuits = []
    for point in points:
        if point in visited:
            continue

        circuit = set()
        queue = deque([point])
        visited.add(point)

        while queue:
            current = queue.popleft()
            circuit.add(current)
            for connection in graph[current]:
                if connection not in visited:
                    queue.append(connection)
                    visited.add(connection)

        circuits.append(circuit)
    return circuits

def part1(pts: list[Point], connections: int = 1000) -> int:
    graph = defaultdict(set)
    for d in sorted_distances[:connections]:
        p1, p2 = distances_to_points[d]
        graph[p1].add(p2)
        graph[p2].add(p1)
    circuits = bfs(pts, graph)
    circuits.sort(key=len, reverse=True)
    return prod(len(circuit) for circuit in circuits[:3])


def part2(pts: list[Point]) -> int:
    graph = defaultdict(set)
    for i, d in enumerate(sorted_distances):
        p1, p2 = distances_to_points[d]
        graph[p1].add(p2)
        graph[p2].add(p1)
        circuits = bfs(pts, graph)
        circuits.sort(key=len, reverse=True)
        if len(circuits[0]) == len(pts):
            return p1.x * p2.x
    raise ValueError("No solution found")


print(f"part 1: {part1(points)}")
print(f"part 2: {part2(points)}")