import numpy as np
from pathfinder.errors import ShortestPathNotFoundError


class Parser:
    """Encapsulates all utility functions to parse strings/files into maps

    ...

    Methods
    --------
    parse_string_to_map(coordinates_string):
        Parses the contents of the comma-separated string of coordinates into a ocean map.
    """

    @staticmethod
    def __convert_coords_list_to_numpy_array(coords_list):
        """Converts coordinates list into an ocean map

        :param coords_list:
        :type coords_list: list [[x1,y1],[x2,y2]...[xn,yn]]

        :return: ocean map as a numpy array
        :rtype: numpy.ndarray(dtype='U1')
        """
        map_x_size = max([coord[0] for coord in coords_list])
        map_y_size = max([coord[1] for coord in coords_list])

        ocean_map = np.full((map_x_size, map_y_size), '.', dtype='U1')

        for coord in coords_list[1:-1]:
            ocean_map[coord[0]][coord[1]] = 'x'
        ocean_map[coords_list[0][0]][coords_list[0][1]] = 'S'
        ocean_map[coords_list[-1][0]][coords_list[-1][1]] = 'E'

        return ocean_map

    @staticmethod
    def __extract_x_y(coord_string):
        """Parses individual coordinate strings. Returns [x,y] if string is valid, otherwise None

        :param coord_string: a string expected to be of the form `x<number>y<number>`
        :type coord_string: str

        :return: the `x` and `y` coordinates as a list of size 2
        :rtype: list [x,y] or None
        """

        coord = []
        x = None
        y = None

        try:
            x = int(coord_string.split("y")[0].split("x")[1])
            y = int(coord_string.split("y")[1])
        except Exception as e:
            return None

        coord.append(x)
        coord.append(y)

        return coord

    @staticmethod
    def parse_string_to_map(coordinates_string):
        """Parses the contents of the comma-separated string of coordinates into map of the ocean.

        :param coordinates_string: string of comma-separated coordinates encoding the map
        :type coordinates_string: str

        :return: a map of the ocean spanned by starting point (top left) and end point (bottom right)
        :rtype: numpy.ndarray(dtype='U1')

        :raises ShortestPathNotFoundError: If there are not enough valid coordinates in the input string
        """

        coords_list = [
            Parser.__extract_x_y(coord_string)
            for coord_string in coordinates_string.split(",")
        ]
        coords_list = [coord for coord in coords_list if coord is not None]
        if len(coords_list) < 2:
            raise ShortestPathNotFoundError("Not enough valid points in input string to specify Start and End.")

        return Parser.__convert_coords_list_to_numpy_array(coords_list)
