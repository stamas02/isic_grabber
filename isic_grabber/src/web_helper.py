import requests
import os
from tqdm import tqdm
import sys


def get_json(url):
    """
    Gets a json response from the given url.

    :param url: URL.
    :return: the received Json data.
    """
    resp = requests.get(url=url)
    return resp.json()


def get_file(url, output_file, show_progress_bar=True):
    """
    Downloads a file.

    Source: https://github.com/sirbowen78/lab/blob/master/file_handling/dl_file1.py

    :param url: url of the file to be downloaded
    :param output_file: file where the downloaded data is saved.
    :param show_progress_bar: If true progressbar is shown otherwise False
    :return: None
    """

    filesize = int(requests.head(url).headers["Content-Length"])
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    chunk_size = 1024

    with requests.get(url, stream=True) as r, open(output_file, "wb") as f, tqdm(
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
            total=filesize,
            file=sys.stdout,
            disable=not show_progress_bar,
            desc="Downloading file {}".format(os.path.basename(output_file),
                                              )
    ) as progress:
        for chunk in r.iter_content(chunk_size=chunk_size):
            # download the file chunk by chunk
            datasize = f.write(chunk)
            # on each chunk update the progress bar.
            progress.update(datasize)
