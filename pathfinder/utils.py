import numpy as np
from os import linesep

def read_file(file_path):
    """Reads in the file at file_path. Reads all lines from file and returns a single string with no newlines

    :param file_path: the path (relative to the working directory) to input file containing encoded map
    :type file_path: str

    :return: all lines from file as a single string with no newlines
    :rtype: str

    :raises FileNotFoundError: if file does note exist
    """

    try:
        with open(file_path, 'r') as f:
            data_text = f.readlines()
            data_text = [text.rstrip() for text in data_text]
            whole_text = ("".join(data_text))
    except FileNotFoundError as e:
        raise
    else:
        return whole_text


def print_map(ocean_map):
    """Parses the input map. Returns a string displaying the map in human-readable format

    :param ocean_map: the map to be printed
    :type ocean_map: numpy.ndarray(dtype='U1')

    :return: A string representing the map in human readable format
    :rtype: str
    """

    s = ""

    for y in range(ocean_map.shape[1]):
        for x in range(ocean_map.shape[0]):
            s += ocean_map[x][y]
        s += linesep

    s = s.rstrip()

    return s
