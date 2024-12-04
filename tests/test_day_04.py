"""Tests for day 4."""
from day04_ceres_search import part1, part2
from data import aoc24


def test_part1():
    """Test if part1 function returns the expected result."""
    assert part1(aoc24.day4.example_data_file) == aoc24.day4.example_expected_result_part1


def test_part2():
    """Test if part2 function returns the expected result."""
    assert part2(aoc24.day4.example_data_file) == aoc24.day4.example_expected_result_part2
