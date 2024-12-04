"""Puzzle 1 solution."""
from pathlib import Path

from data import aoc24
from helpers import text_file_to_lines



def part1(data_file: Path) -> int:
    """
    Compute the sum of distances between paired numbers in a data file.

    Each line in the file contains a pair of integers, separated by a space.
    The function sorts the first and second elements of each pair independently,
    computes the differences between corresponding elements, and returns their sum.

    Parameters
    ----------
    data_file : pathlib.Path
        Path to the file containing pairs of integers.

    Returns
    -------
    int
        The sum of distances between corresponding sorted pairs.

    Examples
    --------
    Given a file with the following content:

        1 3
        2 4
        5 7

    The sorted left column is [1, 2, 5], and the sorted right column is [3, 4, 7].
    The function computes distances (3-1, 4-2, 7-5) and returns their sum, 6.
    """
    lines = text_file_to_lines(data_file)

    left, right = zip(*(map(int, line.split()) for line in lines), strict=True)
    distance = (abs(y - x) for x, y in zip(sorted(left), sorted(right), strict=True))

    return sum(distance)


def part2(data_file: Path) -> int:
    """
    Compute the sum of similarity scores of paired numbers in a data file.

    Parameters
    ----------
    data_file : pathlib.Path
        Path to the file containing pairs of integers.

    Returns
    -------
    int
        The sum of similarity scores of the numbers.
    """
    lines = text_file_to_lines(data_file)

    left, right = zip(*(map(int, line.split()) for line in lines), strict=True)

    right_list = list(right)

    similarity = (x * right_list.count(x) for x in left)

    return sum(similarity)


print(f"Solution part 1: {part1(aoc24.day1.puzzle_input_file)}")
print(f"Solution part 2: {part2(aoc24.day1.puzzle_input_file)}")
