
import os
import click
from .src import isic
import pandas as pd
from pandas import json_normalize
from tqdm import tqdm
from .src.utils import slugify
from pyfiglet import Figlet
import sys


root_dir = os.path.dirname(os.path.realpath(__file__))
cache_file = os.path.join(root_dir, "data", "cache.csv")


def update_cache():
    """
    Updates the cache file that contains the image list with metadata
    :return: None
    """
    total = isic.get_image_count()
    df = pd.DataFrame()
    for meta in tqdm(isic.get_image_meta(), total=total, desc="Updating image list cache", unit="img"):
        _meta = json_normalize(meta)
        # File name and directory will be named after dataset.name.
        # Make it file system friendly. e.g. remove chars like /
        # Todo: This append stuff is painfully slow... Do something about it
        _meta["dataset.name"] = slugify(_meta["dataset.name"][0])
        df = df.append(_meta, ignore_index=True)
    df.to_csv(cache_file, index=False)


def download_dataset(dataset, destination):
    """
    Downloads images from the ISIC archive by dataset.

    :param dataset: dataset to be downloaded.
    :param destination: folder where the dataset is saved.
    :return: None
    """

    # Get images belonging to the requested dataset from cache
    cache_df = pd.read_csv(cache_file)
    df = cache_df.loc[cache_df['dataset.name'] == dataset]
    assert (df.shape[0] > 0), "Dataset {0} does not exist".format(dataset)

    # Create metadata for dataset that includes the file image paths
    print("Preprocessing metadata.")
    files = []
    for _, row in df.iterrows():

        if type(row["meta.clinical.diagnosis"]) == str:
            path = os.path.join(row["dataset.name"], slugify(row["meta.clinical.diagnosis"]))
        elif type(row["meta.clinical.diagnosis"]) == str:
            path = os.path.join(row["dataset.name"], slugify(row["meta.clinical.benign_malignant"]))
        else:
            path = os.path.join(row["dataset.name"], "unknown")

        files.append(os.path.join(path, "{}.jpg".format(row["_id"])))
    df["file"] = files
    df.to_csv(os.path.join(destination, "{0}.csv".format(dataset)), index=False)

    # Download images
    print("Downloading images from dataset: {}".format(dataset))
    for _, row in tqdm(df.iterrows(), total=df.shape[0], desc="Downloading images", unit="img"):
        isic.download_image(row["_id"], os.path.join(destination,row["file"]))


@click.command()
@click.argument('dataset')
@click.option('--destination', '-d', help='The destination folder where the dataset is saved')
@click.option('--force-update', '-f', is_flag=True, help="Forces the image list to be updated.")
def main(dataset, destination, force_update):
    """
    ISIC archive grabber.

    :param dataset: The name of the dataset to be downloaded.
    :param destination: Path to the folder the dataset is to be downloaded.
    :param force_update: If True, updates the image list from the ISIC website.
    :return: None
    """

    f = Figlet(font='slant')
    print(f.renderText('ISIC Grabber'))

    if force_update or not os.path.exists(cache_file):
        print("Updating cache file! It only happens at first use or when forced!")
        print("It will take a while though... (about 1 hour)")
        update_cache()

    print("Downloading {0} dataset".format(dataset))
    download_dataset(dataset,destination)


if __name__ == '__main__':
    sys.exit(main())
