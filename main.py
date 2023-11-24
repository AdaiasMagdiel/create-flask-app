import shutil
from core.builder import WORK_DIR
from core.cli import get_args, print_next

if __name__ == '__main__':
    folder = get_args()
    shutil.copytree(WORK_DIR, folder, dirs_exist_ok=True)

    print_next(folder)
