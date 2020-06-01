"""
This module contains the solution and the test cases for the given problem statement

...

SubModules
-----------
parse.py
    contains methods for parsing input, calculating shortest path, and printing output
errors.py
    defines error types that are raised by modules/methods in this package
"""

from .utils import read_file, print_map
from .errors import ShortestPathNotFoundError
from .parse import Parser
from .search import BreadthFirstSearch


def solve(file_path):
    """Takes as input a file containing an encoded map.

    Returns a human-readable string representing the map with the shortest path marked on it.

    :param file_path: the path (relative to the working directory) to input file containing encoded map
    :type file_path: str

    :return: the map with the shortest path marked in specified format
    :rtype: str

    :raises ShortestPathNotFoundError: if shortest path to treasure does not exist
    :raises FileNotFoundError: if no file exists at location specified by file_path
    """

    try:
        coordinates_string = read_file(file_path)
    except FileNotFoundError as e:
        raise
    else:
        try:
            ocean_map, S, E = Parser.parse_string_to_map(coordinates_string)
            ocean_map_marked = BreadthFirstSearch(ocean_map, S, E).find_shortest_path()
        except ShortestPathNotFoundError as e:
            raise
        else:
            return print_map(ocean_map_marked)
