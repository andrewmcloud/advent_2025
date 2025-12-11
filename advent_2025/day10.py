import re
from itertools import permutations

with open("../input/day10.txt") as f:
    machines = [line.strip("\n") for line in f.readlines()]

def parse_machine(machine: str) -> tuple[list[int], list[list[int]]]:
    indicator = [0 if x == "." else 1 for x in re.findall(r"[\\.#]+", machine)[0]]
    schematics = [[int(y) for y in x.split(",")] for x in re.findall(r"(?<=\().*?(?=\))", machine)]
    wirings = []
    for schematic in schematics:
        wiring = [0]*len(indicator)
        for s in schematic:
            wiring[s] = 1
        wirings.append(wiring)
    return indicator, wirings


def press_buttons(indicator: list[int], wirings: list[list[int]]) -> int:
    presses = 1
    while True:
        for buttons in permutations(wirings, presses):
            state = [0]*len(indicator)
            for button in buttons:
                state = [x ^ y for x, y in zip(state, button)]
            if state == indicator:
                return presses
        presses += 1


print(sum(press_buttons(*parse_machine(machine)) for machine in machines))
