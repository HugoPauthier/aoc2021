test = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]


def part2(course):
    """Part two"""
    horizontal = 0
    depth = 0
    aim = 0
    for command in course:
        (move, unit) = command.split()
        if move == "forward":
            horizontal += int(unit)
            depth += aim * int(unit)
        elif move == "down":
            aim += int(unit)
        elif move == "up":
            aim -= int(unit)
    return (horizontal * depth)


assert part2(test) == 900
