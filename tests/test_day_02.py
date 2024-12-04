"""Tests for day 1 - historian hysteria puzzle."""
from day02_rednosed_reports import part1, part2
from data import aoc24


def test_part1():
    """Test if part1 function returns the expected result."""
    assert part1(aoc24.day2.example_data_file) == aoc24.day2.example_expected_result_part1


def test_part2():
    """Test if part2 function returns the expected result."""
    assert part2(aoc24.day2.example_data_file) == aoc24.day2.example_expected_result_part2
