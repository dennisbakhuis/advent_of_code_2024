"""Read text file."""
from pathlib import Path


def text_file_to_lines(file_path: Path) -> list[str]:
    """
    Read text file and return list of stripped lines.

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
        data = [
            line.strip()
            for line in f.readlines()
            if line
        ]

    return data
