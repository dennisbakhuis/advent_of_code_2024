"""Read text file."""
from pathlib import Path
from itertools import groupby


def text_file_to_parts_of_lists(file_path: Path) -> list[str]:
    """
    Read text file and return groups of list with stripped lines.

    Parameters
    ----------
    file_path : Path
        Path to text file.

    Returns
    -------
    list[str]
        List of stripped lines.
    """
    with open(file_path, "r") as f:
        data = [line.strip() for line in f.readlines()]

    split_lists = [list(group) for key, group in groupby(data, key=bool) if key]

    return split_lists
