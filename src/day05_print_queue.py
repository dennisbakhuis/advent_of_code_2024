"""Puzzle 5 solution."""
from pathlib import Path

from data import aoc24
from helpers import text_file_to_parts_of_lists


def check_rule_violation(
    update: list[int],
    rule: tuple[int, int],
) -> tuple[bool, int, int]:
    """
    Check if update violates rule.

    Parameters
    ----------
    update : tuple[int,]
        Tuple of n integers.
    rule : tuple[int, int]
        Pair of integers.

    Returns
    -------
    tuple[bool, int, int]
        True if update violates rule, False otherwise. If True, also return indices of the rule.
    """
    if rule[0] in update:
        # check before rule
        right_ix = update.index(rule[0])
        for left_ix in range(update.index(rule[0]), 0, -1):
            if update[left_ix] == rule[1]:
                return (True, left_ix, right_ix)
    if rule[1] in update:
        # check after rule
        left_ix = update.index(rule[1])
        for right_ix in range(update.index(rule[1]), len(update)):
            if update[right_ix] == rule[0]:
                return (True, left_ix, right_ix)

    return (False, -1, -1)


def check_update_violates_rules(update: list[int], rules: list[tuple[int, int]]) -> bool:
    """
    Check if update violates any rule.

    Parameters
    ----------
    update : tuple[int,]
        Tuple of n integers.
    rules : list[tuple[int, int]]
        List of pairs of integers.

    Returns
    -------
    bool
        True if update violates any rule, False otherwise.
    """
    for rule in rules:
        violates, _, _ = check_rule_violation(update, rule)
        if violates:
            return True

    return False

def part1(data_file: Path) -> int:
    """
    Find middle pages of correct updates.

    Parameters
    ----------
    data_file : pathlib.Path
        Path to the file containing pairs of integers.
    """
    rules_raw, updates_raw = text_file_to_parts_of_lists(data_file)

    rules = [
        tuple(map(int, rule.split("|")))
        for rule in rules_raw
    ]

    updates = [
        list(map(int, update.split(",")))
        for update in updates_raw
    ]

    correct_updates = []
    for update in updates:
        if not check_update_violates_rules(update, rules):
            correct_updates.append(update)

    middle_page_numbers = [pages[len(pages) // 2] for pages in correct_updates]

    return sum(middle_page_numbers)


def part2(data_file: Path) -> int:
    """
    Find middle pages of correct updates.

    Parameters
    ----------
    data_file : pathlib.Path
        Path to the file containing pairs of integers.
    """
    rules_raw, updates_raw = text_file_to_parts_of_lists(data_file)

    rules = [
        tuple(map(int, rule.split("|")))
        for rule in rules_raw
    ]

    updates = [
        tuple(map(int, update.split(",")))
        for update in updates_raw
    ]

    incorrect_updates = []
    for update in updates:
        if check_update_violates_rules(update, rules):
            incorrect_updates.append(update)

    fixed_updates = []
    for update in incorrect_updates:
        current_update = list(update)

        applicable_rules = [
            rule
            for rule in rules
            if rule[0] in update and rule[1] in update
        ]

        while check_update_violates_rules(current_update, applicable_rules):
            for rule in applicable_rules:
                violates, left_ix, right_ix = check_rule_violation(current_update, rule)
                if violates:
                    current_update[left_ix], current_update[right_ix] = current_update[right_ix], current_update[left_ix]

        fixed_updates.append(current_update)

    middle_page_numbers = [pages[len(pages) // 2] for pages in fixed_updates]

    return sum(middle_page_numbers)


print(f"Solution part 1: {part1(aoc24.day5.puzzle_input_file)}")
print(f"Solution part 2: {part2(aoc24.day5.puzzle_input_file)}")
