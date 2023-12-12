import click
import os


def find_py_files(directory):
    py_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root, file))
    return py_files


@click.command()
@click.argument(
    "path",
    nargs=1,
    type=click.Path(exists=True, file_okay=False, dir_okay=True, readable=True),
    is_eager=True,
    metavar="path ...",
)
def main(path):
    print(find_py_files(path))


if __name__ == "__main__":
    main()
