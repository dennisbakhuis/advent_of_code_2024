"""Puzzle 4 solution."""
from pathlib import Path

import numpy as np

from data import aoc24
from helpers import text_file_to_2darray


def part1(data_file: Path) -> int:
    """
    Find XMAS in text.

    Parameters
    ----------
    data_file : pathlib.Path
        Path to the file containing pairs of integers.
    """
    list_2d = text_file_to_2darray(data_file)

    word = np.array(["X", "M", "A", "S"])

    array = np.array(list_2d)
    padded_array = np.pad(array, 3, constant_values=".")
    word_start_locations = np.argwhere(padded_array == "X")

    count = 0
    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]

    for x, y in word_start_locations:
        for dx, dy in directions:
            slice = [
                padded_array[x + i * dx, y + i * dy]
                for i in range(4)
            ]
            if np.array_equal(slice, word):
                count += 1

    return count


def part2(data_file: Path) -> int:
    """
    Find XMAS in text.

    Parameters
    ----------
    data_file : pathlib.Path
        Path to the file containing pairs of integers.
    """
    list_2d = text_file_to_2darray(data_file)
    array = np.array(list_2d)

    count = 0
    for x in range(array.shape[0] - 2):
        for y in range(array.shape[1] - 2):
            letters = array[x, y] + array[x][y+2] + array[x+1][y+1] + array[x+2][y] + array[x+2][y+2]

            if letters in ["MSAMS", "SMASM", "SSAMM", "MMASS"]:
                count += 1


    return count


print(f"Solution part 1: {part1(aoc24.day4.puzzle_input_file)}")
print(f"Solution part 2: {part2(aoc24.day4.puzzle_input_file)}")
