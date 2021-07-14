from . import web_helper

DATASET_INFO_URL = "https://isic-archive.com/api/v1/dataset"
IMAGE_LIST_ULR = "https://isic-archive.com/api/v1/image?limit={0}&offset={1}&sort=name&sortdir=1&detail=true"
IMAGE_HIST_URL = "https://isic-archive.com/api/v1/image/histogram"
IMAGE_DOWNLOAD_URL = "https://isic-archive.com/api/v1/image/{0}/download"


def get_datasets():
    """
    Grabs the list of available datasets in the ISIC archive.

    :return: names and ids of the available datasets in the ISIC Archive.
    """
    datasets = web_helper.get_json(DATASET_INFO_URL)
    names = [d["name"] for d in datasets]
    ids = [d["_id"] for d in datasets]
    return names, ids


def get_image_meta(offset=0, batch_size=10000):
    """
    A generator. Grabs image metadata from the ISIC archive.

    :param offset: start getting image data from this offest.
    :param batch_size: Number of images returned by the ISIC API per request.
    :return: image metadata in json string.
    """
    meta_batch = web_helper.get_json(IMAGE_LIST_ULR.format(batch_size, offset))
    while len(meta_batch) > 0:
        for meta in meta_batch:
            yield meta
        offset += batch_size
        meta_batch = web_helper.get_json(IMAGE_LIST_ULR.format(batch_size, offset))


def get_image_count(dataset_id=None):
    """
    Gets the image count in the ISIC archive

    :param dataset_id: optional. When defined the returned image count relates only to the defined dataset.
    :return: Image count.
    """

    img_hist = web_helper.get_json(IMAGE_HIST_URL)
    if dataset_id is None:
        return img_hist['__passedFilters__'][0]['count']
    else:
        for dataset in img_hist['meta.datasetId']:
            if dataset["label"] == dataset_id:
                return dataset["count"]
        raise ValueError("Invalid dataset ID {0}".format(dataset_id))
    return total


def download_image(id, output_file):
    """
    Downloads an image file from the ISIC Archive

    :param id: id of the image to be downloaded.
    :param output_file: file where the downloaded data is saved.
    :return: None
    """
    web_helper.get_file(IMAGE_DOWNLOAD_URL.format(id), output_file, show_progress_bar=False)