from part_one import part1


def main():
    """Main function"""
    with open('input.txt') as file:
        full_report = file.read().splitlines()

        print(part1(full_report))  # 4138664
        # print(part2(full_commands))  #
        assert part1(full_report) == 4138664
        # assert part2(full_commands) ==


main()
