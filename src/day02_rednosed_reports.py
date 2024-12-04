"""Puzzle 2 solution."""
from pathlib import Path

from data import aoc24
from helpers import text_file_to_lines


def check_level_rules(levels: list[int], problem_dampener: bool=False) -> bool:
    """
    Check for level rules.

    Rules to check:
    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.

    Parameters
    ----------
    levels : list[int]
        List of levels.

    Returns
    -------
    bool
        True if the levels follow the rules, False otherwise
    """
    if len(levels) < 2:
        return True

    n_levels_minus_1 = len(levels) - 1

    is_increasing = sum(levels[i] < levels[i + 1] for i in range(n_levels_minus_1))
    is_decreasing = sum(levels[i] > levels[i + 1] for i in range(n_levels_minus_1))
    is_within_values = sum(1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(n_levels_minus_1))

    if not (is_increasing ==  n_levels_minus_1 or is_decreasing == n_levels_minus_1):
        safe_without_damper = False
    else:
        safe_without_damper = is_within_values == n_levels_minus_1

    if not problem_dampener or safe_without_damper:
        return safe_without_damper

    # Problem dampener
    for i in range(n_levels_minus_1 + 1):
        new_levels = levels.copy()
        new_levels.pop(i)
        if check_level_rules(new_levels):
            return True

    return False


def part1(data_file: Path) -> int:
    """
    Calculate the safe reports.

    Parameters
    ----------
    data_file : pathlib.Path
        Path to the file containing pairs of integers.
    """
    lines = text_file_to_lines(data_file)

    safe_reports = [
        check_level_rules(list(int(x) for x in line.split()))
        for line in lines
    ]

    return sum(safe_reports)


def part2(data_file: Path) -> int:
    """
    Calculate the safe reports using the problem damper.

    Parameters
    ----------
    data_file : pathlib.Path
        Path to the file containing pairs of integers.
    """
    lines = text_file_to_lines(data_file)

    safe_reports = [
        check_level_rules(list(int(x) for x in line.split()), problem_dampener=True)
        for line in lines
    ]

    return sum(safe_reports)


print(f"Solution part 1: {part1(aoc24.day2.puzzle_input_file)}")
print(f"Solution part 2: {part2(aoc24.day2.puzzle_input_file)}")
