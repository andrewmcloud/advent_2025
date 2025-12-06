with open("../input/day5.txt", "r") as f:
    ranges, ids = f.read().split("\n\n")

def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    merged = []
    for interval in sorted(intervals, key=lambda x: x[0]):
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
    return merged

range_list = [(int(start), int(end)) for start, end in [r.split("-") for r in ranges.splitlines()]]

print(f"part1: {sum(1 if m[0] <= int(id_) <= m[1] else 0 for m in merge_intervals(range_list) for id_ in ids.splitlines())}")
print(f"part2: {sum(m[1] - m[0] + 1 for m in merge_intervals(range_list))}")