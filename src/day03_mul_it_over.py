"""Puzzle 3 solution."""
from pathlib import Path
import re


from data import aoc24
from helpers import text_file_to_string


def part1(data_file: Path) -> int:
    """
    Calculate the safe reports.

    Parameters
    ----------
    data_file : pathlib.Path
        Path to the file containing pairs of integers.
    """
    string = text_file_to_string(data_file)

    pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(pattern, string)

    pattern = r"mul\((\d+),(\d+)\)"
    products = [int(a) * int(b) for a, b in re.findall(pattern, ",".join(matches))]

    return sum(products)


def part2(data_file: Path) -> int:
    """
    Calculate the safe reports.

    Parameters
    ----------
    data_file : pathlib.Path
        Path to the file containing pairs of integers.
    """
    string = text_file_to_string(data_file)

    mul_pattern = r"mul\(\d+,\d+\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don\'t\(\)"

    matches = []
    for pattern in [mul_pattern, do_pattern, dont_pattern]:
        matches += [(match.start(), match.group()) for match in re.finditer(pattern, string)]

    matches = list(sorted(matches, key=lambda x: x[0]))

    products = []
    do_multiply = True
    for match in matches:
        command = match[1]
        if command.startswith("mul(") and do_multiply:
            pattern = r"mul\((\d+),(\d+)\)"
            a, b = re.match(pattern, command).groups()
            products.append(int(a) * int(b))
        elif command.startswith("don"):
            do_multiply = False
        elif command.startswith("do"):
            do_multiply = True

    return sum(products)


print(f"Solution part 1: {part1(aoc24.day3.puzzle_input_file)}")
print(f"Solution part 2: {part2(aoc24.day3.puzzle_input_file)}")
