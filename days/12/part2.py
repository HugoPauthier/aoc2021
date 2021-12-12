test_input = ['start-A','start-b','A-c','A-b','b-d','A-end','b-end']

def prepare_data(caves_map):
    res = {'start': []}
    for line in caves_map:
        [entry1, entry2] = line.split('-')
        if entry1 == 'start':
            res['start'].append(entry2)
        elif entry2 == 'start':
            res['start'].append(entry1)
        else:
            if entry1 not in res:
                res[entry1] = [entry2]
            else:
                res[entry1].append(entry2)
            if entry2 not in res:
                res[entry2] = [entry1]
            else:
                res[entry2].append(entry1)
    return res

test_cave_map = prepare_data(test_input)
print(test_cave_map)

def can_visit(visited_caves):
    # print('visited', visited_caves)
    counts = [visited_caves.count(c) for c in visited_caves]
    return all([c < 2 for c in counts])

assert can_visit([]) == True
assert can_visit(['c', 'b']) == True
assert can_visit(['c', 'b', 'c']) == False

def path(caves_map, current_path, visited, all_path):
    if current_path[-1] == 'end':
        return
    for cave in caves_map[current_path[-1]]:
        next_path = current_path.copy()
        next_path.append(cave)
        if cave == 'end':
            print(next_path)
            all_path.append(next_path)
        if can_visit(visited.copy()):
            next_visited = visited.copy()
            if cave.islower():
                next_visited.append(cave)
            path(caves_map, next_path.copy(), next_visited.copy(), all_path)
    return

def part2(caves_map):
    all_path = []
    current_path = ['start']
    path(caves_map, current_path, [], all_path)
    print('\n')
    print(len(all_path))

part2(test_cave_map)
