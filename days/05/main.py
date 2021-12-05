from pathfinder import *


test_vents_lines, test_max_x, test_max_y = prepare_data('test_input.txt')
test_diagram = init_diagram(test_max_x, test_max_y)

vents_lines, max_x, max_y = prepare_data('input.txt')
diagram = init_diagram(max_x, max_y)


def part1(vents_lines, diagram):
    """Part one"""
    for (start, end) in vents_lines:
        (x1, y1) = start
        (x2, y2) = end
        if (x1 == x2) or (y1 == y2):
            update_diagram_lines(diagram, start, end)
    return np.count_nonzero(diagram > 1)


# print(part1(vents_lines, diagram))
assert part1(test_vents_lines, test_diagram.copy()) == 5

# print(part1(vents_lines, diagram.copy()))
assert part1(vents_lines, diagram.copy()) == 5084


def part2(vents_lines, diagram):
    """Part two"""
    for (start, end) in vents_lines:
        (x1, y1) = start
        (x2, y2) = end
        if (x1 == x2) or (y1 == y2):
            update_diagram_lines(diagram, start, end)
        else:
            update_diagram_diag(diagram, start, end)
    return np.count_nonzero(diagram > 1)


# print(part2(vents_lines, diagram.copy()))
assert part2(test_vents_lines, test_diagram.copy()) == 12

# print(part2(vents_lines, diagram.copy()))
assert part2(vents_lines, diagram.copy()) == 17882
