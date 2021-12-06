test = [3, 4, 3, 1, 2]


def prepare_lists(input_list):
    res = dict.fromkeys([0, 1, 2, 3, 4, 5, 6, 7, 8], 0)
    for n in input_list:
        res[n] = input_list.count(n)
    return res

# print(prepare_lists(test))


def part1(init_fishes, countdown):
    fish_list = init_fishes.copy()
    for day in range(countdown):
        for i in range(len(fish_list)):
            if fish_list[i] == 0:
                fish_list.append(8)
                fish_list[i] = 7
            fish_list[i] += -1
        # print(fish_list)
    return len(fish_list)


def part2(dict_fishes, countdown):
    for day in range(countdown):
        day_dict = dict.fromkeys([0, 1, 2, 3, 4, 5, 6, 7, 8], 0)
        fishes0 = dict_fishes[0]
        day_dict[8] = fishes0
        day_dict[6] = fishes0
        for k in dict_fishes.keys():
            if k != 0:
                if k == 7:
                    day_dict[6] = dict_fishes[k] + day_dict[6]
                else:
                    day_dict[k-1] = dict_fishes[k]
        dict_fishes = day_dict
        # print('end   day:', day + 1, '=>', dict_fishes)
    return sum(dict_fishes.values())
