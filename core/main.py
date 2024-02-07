from argparse import ArgumentParser
from pathlib import Path

from core.pathutils import create_project

parser = ArgumentParser(description="Start a Flask project with a template")

parser.add_argument(
    "--init",
    help="Initializa a Flask app in the current directory.",
    action="store_true",
)

parser.add_argument(
    "name", help="A folder will be created with the given name.", nargs="?"
)

parser.add_argument(
    "--routes",
    help="Routes to be included. The options are: site, api",
    nargs="+"
)

parser.add_argument(
    "--force",
    help="Force an action. Be careful",
    action="store_true",
)


def main():
    args = parser.parse_args()

    ACTUAL_DIR = (
        Path(".").resolve()
        if args.init else Path(".").joinpath(args.name).resolve()
    )

    error, message = create_project(ACTUAL_DIR, args.init, args.force)

    if not error:
        print("App started successfully.")
        exit(0)
    else:
        print(f"Error: {message}")
        exit(1)

    print(args)
