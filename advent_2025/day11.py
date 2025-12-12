from collections import defaultdict
from functools import cache

with open("../input/day11.txt") as f:
    lines = f.readlines()

graph = defaultdict(set)
for line in lines:
    parent, children = line.split(": ")
    for child in children.split(" "):
        graph[parent].add(child.strip("\n"))


def find_paths(graph: dict[str, list[str]], start: str, end: str) -> int:
    paths = []
    def search(node, path):
        path = path + [node]
        if node == end:
            paths.append(path)
            return
        for neighbor in graph[node]:
            search(neighbor, path[:])

    search(start, [])
    return len(paths)


def find_paths_contains(graph: dict[str, list[str]], start: str, end: str) -> int:
    @cache
    def search(node: str, dac: bool = False, fft: bool = False) -> int:
        if node == end:
            return 1 if (dac and fft) else 0
        if node == "dac":
            dac = True
        elif node == "fft":
            fft = True

        return sum(search(neighbor, dac, fft) for neighbor in graph[node])
    return search(start)


print(f"part 1: {find_paths(graph, 'you', 'out')}")
print(f"part 2: {find_paths_contains(graph, 'svr', 'out')}")