with open("../input/day2.txt", "r") as f:
    pid_ranges = f.read().split(",")


def find_invalid_pids(start: int, end: int) -> list[int]:
    invalid_pids = []
    current = start
    while current <= end:
        str_current = str(current)
        str_len = len(str_current)
        if str_len % 2 == 1:
            # advance to the next number with an even length
            current = int("1" + "0" * str_len)
        else:
            mid = str_len // 2
            if str_current[:mid] == str_current[mid:]:
                invalid_pids.append(current)
            current += 1
    return invalid_pids


def find_repeating_pids(start: int, end: int) -> list[int]:
    invalid_pids = []
    for pid in range(start, end + 1):
        s = str(pid)
        if len(s) == 1:
            continue
        doubled = s + s
        if s in doubled[1:-1]:
            invalid_pids.append(pid)
    return invalid_pids


p1_invalid_pids, p2_invalid_pids = [], []
for pid_range in pid_ranges:
    start, end = pid_range.split("-")
    p1_invalid_pids.extend(find_invalid_pids(int(start), int(end)))
    p2_invalid_pids.extend(find_repeating_pids(int(start), int(end)))
print(f"part 1: {sum(p1_invalid_pids)}")
print(f"part 2: {sum(p2_invalid_pids)}")
