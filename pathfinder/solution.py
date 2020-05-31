import numpy as np
from pathfinder.errors import ShortestPathNotFoundError


def parse_string_to_map(coordinates_string):
    """Parses the contents of the comma-separated string of coordinates. Returns a map of the ocean.

    :param coordinates_string: string of comma-separated coordinates encoding the map
    :type coordinates_string: str

    :return: a map of the ocean spanned by starting point (top left) and end point (bottom right)
    :rtype: numpy.ndarray(dtype='U1')
    """


def parse_file_to_map(file_location):
    """Parses the contents of the input file. Returns a map of the ocean.

    :param file_location: path (relative to working directory) to input file
    :type file_location: str

    :return: a map of the ocean spanned by starting point (top left) and end point (bottom right)
    :rtype: numpy.ndarray(dtype='U1')
    """


def find_shortest_path(ocean_map):
    """Finds shortest path from start point to treasure in map. Returns a map with path marked in specified format.

    :param ocean_map: map of the ocean in specified format
    :type ocean_map: numpy.ndarray(dtype='U1')

    :return: the map provided as input but with the shortest path marked in specified format
    :rtype: numpy.ndarray(dtype='U1')

    :raises ShortestPathNotFoundError: If shortest path to treasure does not exist
    """
