"""Class holding the data for the game."""
from pathlib import Path


_BASE_PATH = Path(__file__).parent.parent / "src/data_files"


class aoc24:
    """Advent of Code 2024 data."""

    class day1:
        """Day 1 data."""

        puzzle_input_file = _BASE_PATH / "day_01_puzzle_input.txt"
        example_data_file = _BASE_PATH / "day_01_example_input.txt"
        example_expected_result_part1 = 11
        example_expected_result_part2 = 31

    class day2:
        """Day 2 data."""

        puzzle_input_file = _BASE_PATH / "day_02_puzzle_input.txt"
        example_data_file = _BASE_PATH / "day_02_example_input.txt"
        example_expected_result_part1 = 2
        example_expected_result_part2 = 4

    class day3:
        """Day 3 data."""

        puzzle_input_file = _BASE_PATH / "day_03_puzzle_input.txt"
        example_data_file_1 = _BASE_PATH / "day_03_example_input_1.txt"
        example_data_file_2 = _BASE_PATH / "day_03_example_input_2.txt"
        example_expected_result_part1 = 161
        example_expected_result_part2 = 48

    class day4:
        """Day 4 data."""

        puzzle_input_file = _BASE_PATH / "day_04_puzzle_input.txt"
        example_data_file = _BASE_PATH / "day_04_example_input.txt"
        example_expected_result_part1 = 18
        example_expected_result_part2 = 9
