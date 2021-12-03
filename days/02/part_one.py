test = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]


def part1(course):
    """Part one"""
    horizontal = 0
    depth = 0
    for command in course:
        (move, unit) = command.split()
        if move == "forward":
            horizontal += int(unit)
        elif move == "down":
            depth += int(unit)
        elif move == "up":
            depth -= int(unit)
    return horizontal * depth


assert part1(test) == 150
