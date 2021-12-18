"""
    Created by howie.hu at 2021-12-18.
    Description: Collection of commonly used functions
    Changelog: all notable changes to this file will be documented
"""


def get_data(file_path):
    """Read data from file and output data in list format

    Args:
        file_path ([str]): file path
    """
    text_list = []
    with open(file_path, encoding="utf-8") as fp:
        for line in fp:
            line = line.replace("\n", "").strip()
            if line:
                text_list.append(line)
    return text_list
