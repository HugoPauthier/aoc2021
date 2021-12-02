from part_one import part1
from part_two import part2

def main():
    """Main function"""
    with open('input.txt') as file:
        full_commands = file.readlines()

        # print(part1(full_commands))  # 2215080
        # print(part2(full_commands))  # 1864715580
        assert part1(full_commands) == 2215080
        assert part2(full_commands) == 1864715580


main()