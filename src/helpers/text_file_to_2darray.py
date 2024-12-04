"""Read text file."""
from pathlib import Path


def text_file_to_2darray(file_path: Path) -> list[list[str]]:
    """
    Read text file and return list of stripped lines.

    Parameters
    ----------
    file_path : Path
        Path to text file.

    Returns
    -------
    list[list[str]]
        List of stripped lines.
    """
    with open(file_path, "r") as f:
        data = [
            list(line.strip())
            for line in f.readlines()
            if line
        ]

    return data
