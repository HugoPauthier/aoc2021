from part_one import part1
from part_two import part2


def main():
    """Main function"""
    with open('input.txt') as file:
        full_report = file.readlines()
        int_full_report = [int(i) for i in full_report]

        print(part1(int_full_report))  # 1446
        print(part2(int_full_report))  # 1486
        assert part1(int_full_report) == 1446
        assert part2(int_full_report) == 1486


main()
