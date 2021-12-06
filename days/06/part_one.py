test = [3, 4, 3, 1, 2]

def prepare_lists(input_list):
    res = dict.fromkeys([0, 1, 2, 3, 4, 5, 6, 7, 8], 0)
    for n in input_list:
        res[n] = input_list.count(n)
    return res

# print(prepare_lists(test))


def part1(init_fishes, countdown):
    fish_list = init_fishes.copy()
    for d in range(countdown):
        print('Day :', d)
        for i in range(len(fish_list)):
            if fish_list[i] == 0:
                fish_list.append(8)
                fish_list[i] = 7
            fish_list[i] += -1

        # print(fish_list)
    return len(fish_list)

# print(part1(test, 18))
# assert part1(test, 80) == 5934

    

def part2(dict_fishes, countdown):
    for day in range(countdown):
        print(dict_fishes)
        for k, v in dict_fishes.items():
            if k == 0:
                dict_fishes[6] = v
                dict_fishes[0] = 0
                dict_fishes[8] += 1
            else:
                dict_fishes[k-1] = v
    return sum(dict_fishes.values())

dict_test = prepare_lists(test)
print(part2(dict_test, 18))
# print(part2(test, 250))
