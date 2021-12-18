"""
    Created by howie.hu at 2021-12-18.
    Description: Logger function for Magic Google
    Changelog: all notable changes to this file will be documented
"""

import logging


def get_logger(name="magic_google"):
    """Logger function for Magic Google

    Args:
        name (str, optional): [description]. Defaults to "magic_google".

    Returns:
        [type]: Logger instance
    """
    logging_format = f"[%(asctime)s] %(levelname)-5s %(name)-{len(name)}s "
    logging_format += "%(message)s"

    logging.basicConfig(
        format=logging_format, level=logging.INFO, datefmt="%Y:%m:%d %H:%M:%S"
    )
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("chardet").setLevel(logging.WARNING)
    logging.getLogger("requests").setLevel(logging.WARNING)
    return logging.getLogger(name)
