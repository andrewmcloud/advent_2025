from collections import defaultdict

with open("../input/day11.txt") as f:
    lines = f.readlines()

graph = defaultdict(set)
for line in lines:
    parent, children = line.split(": ")
    for child in children.split(" "):
        graph[parent].add(child.strip("\n"))


def find_paths(graph, start: str, end: str) -> int:
    paths = []
    def search(node, path):
        path = path + [node]
        if node == end or node not in graph:
            paths.append(path)
            return
        for neighbor in graph[node]:
            search(neighbor, path[:])

    search(start, [])
    return len(paths)


print(f"part 1: {find_paths(graph, 'you', 'out')}")