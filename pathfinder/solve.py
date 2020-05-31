from pathfinder.parse import Parser
from pathfinder.errors import ShortestPathNotFoundError
from pathfinder.utils import read_file, print_map


class ShortestPathFinder:
    @staticmethod
    def find_shortest_path(ocean_map):
        """Finds shortest path from start point to end point in map. Returns a map with path marked in specified format.

        :param ocean_map: map of the ocean in specified format
        :type ocean_map: numpy.ndarray(dtype='U1')

        :return: the map provided as input but with the shortest path marked in specified format
        :rtype: numpy.ndarray(dtype='U1')

        :raises ShortestPathNotFoundError: If shortest path to treasure does not exist
        """


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
            ocean_map = Parser.parse_string_to_map(coordinates_string)
            ocean_map_marked = find_shortest_path(ocean_map)
        except ShortestPathNotFoundError as e:
            raise
        else:
            return print_map(ocean_map_marked)
