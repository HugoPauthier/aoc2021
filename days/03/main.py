from part_one import part1
from part_two import part2


def main():
    """Main function"""
    with open('input.txt') as file:
        full_report = file.read().splitlines()

        # print(part1(full_report))  # 4138664
        # print(part2(full_report))  # 4273224
        assert part1(full_report) == 4138664
        assert part2(full_report) == 4273224


main()
