"""Read text file."""
from pathlib import Path


def text_file_to_string(file_path: Path) -> str:
    """
    Read text file and return as string.

    Parameters
    ----------
    file_path : Path
        Path to text file.

    Returns
    -------
    str
        data as string.
    """
    with open(file_path, "r") as f:
        data = f.read().strip()

    return data
