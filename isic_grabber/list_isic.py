
from .src import isic
from .src.utils import slugify
import click
import sys

@click.command()
def main():
    """
    Lists all the available dataset in the ISIC Archive (https://www.isic-archive.com)
    :return:
    """
    datasets, _ = isic.get_datasets()
    print("Datasets available from the ISIC archive are: \n")
    for dataset in datasets:
        print("{0}".format(slugify(dataset)))


if __name__ == '__main__':
    sys.exit(main())
