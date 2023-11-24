import sys
from pathlib import Path

usage = """
usage:
    create-flask-app <folder>

    create a flask app inside folder, folder cannot be ..\
"""

nextt = """
App created inside: {folder}
Next:
    cd {folder_name}
    py -m venv .venv
    .venv\\Scripts\\activate
    pip install -r requirements.txt
"""


def print_usage(message: str = ''):
    if message != '':
        print(message)
    print(usage)
    sys.exit(1)


def print_next(folder: Path):
    print(nextt.format(folder=folder, folder_name=folder.name))
    sys.exit(0)


def get_args() -> Path:
    sys.argv.pop(0)

    if len(sys.argv) == 0:
        print_usage(usage)

    folder = sys.argv.pop(0)
    if folder == '..':
        print_usage('ERROR: Can not create a application inside ..')

    folder = Path('.').joinpath(folder)

    if folder.is_file():
        print_usage(f'ERROR: argument {folder} is already a file')

    if folder.is_dir():
        if len(list(folder.iterdir())) > 0:
            print_usage(f'ERROR: folder {folder} is not empty')
    else:
        folder.mkdir()

    return folder.absolute()
