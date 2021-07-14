def slugify(text):
    """
    Removes all char from string that can cause problems whe used as a file name.

    :param text: text to be modified.
    :return: modified text
    """
    return "".join(x for x in text if x.isalnum())
