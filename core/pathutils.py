import shutil
from pathlib import Path

from core.utils import TEMPLATES_DIR


def is_empty(folder: Path) -> bool:
    return len(list(folder.glob("*"))) == 0


def create_project(folder: Path, forced: bool = False) -> tuple[bool, str]:
    if folder.is_file():
        return True, "The current folder is a file. (?)"

    if not folder.is_dir():
        folder.mkdir()

    if not is_empty(folder) and not forced:
        return (
            True,
            "The current folder is not empty. Use --force if you still wish to create it.",
        )

    shutil.copytree(
        TEMPLATES_DIR.joinpath("simple"), folder, dirs_exist_ok=True
    )
    return False, ""
