import pytest
import numpy as np
from pathfinder.solution import *
from pathfinder.errors import ShortestPathNotFoundError


class TestPathFinder:
    input_files = {
        "shortest_path_exists": "./tests/inputs/shortest_path_exists.txt",
        "no_shortest_path": "./tests/inputs/no_shortest_path.txt",
        "invalid_coordinate_at_end": "./tests/inputs/invalid_coordinate_at_end.txt",
        "invalid_coordinate_in_middle": "./tests/inputs/invalid_coordinate_in_middle.txt",
    }

    input_strings = {
        "shortest_path_exists": "x0y0,x0y1,x1y1,x3y2,x2y2",
        "no_shortest_path": "x0y0,x0y1,x1y1,x2y1,x1y2,x3y2,x2y2",
        "invalid_coordinate_at_end": "x4y1,x1y2,x5y2,x4y2x5x1",
        "invalid_coordinate_in_middle": "x4y1,x1y2,x5yy,x4y3",
    }

    maps = {
        "shortest_path_exists": np.array([
            ['S', '.', '.', '.'],
            ['x', 'x', '.', '.'],
            ['.', '.', 'E', 'x']
        ]).transpose(),
        "no_shortest_path": np.array([
            ['S', '.', '.', '.'],
            ['x', 'x', 'x', '.'],
            ['.', 'x', 'E', 'x']
        ]).transpose(),
        "invalid_coordinate_at_end": np.array([
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', 'S', '.'],
            ['.', 'x', '.', '.', '.', 'E'],
            ['.', '.', '.', '.', '.', '.']
        ]).transpose(),
        "invalid_coordinate_in_middle": np.array([
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', 'S', '.'],
            ['.', 'x', '.', '.', '.', '.'],
            ['.', '.', '.', '.', 'E', '.']
        ]).transpose()
    }

    maps_marked = {
        "shortest_path_exists": np.array([
            ['S', 'O', 'O', '.'],
            ['x', 'x', 'O', '.'],
            ['.', '.', 'E', 'x']
        ]).transpose(),
        "no_shortest_path": np.array([
            ['S', '.', '.', '.'],
            ['x', 'x', 'x', '.'],
            ['.', 'x', 'E', 'x']
        ]).transpose(),
        "invalid_coordinate_at_end": np.array([
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', 'S', '.'],
            ['.', 'x', '.', '.', 'O', 'E'],
            ['.', '.', '.', '.', '.', '.']
        ]).transpose(),
        "invalid_coordinate_in_middle": np.array([
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', 'S', '.'],
            ['.', 'x', '.', '.', 'O', '.'],
            ['.', '.', '.', '.', 'E', '.']
        ]).transpose()
    }

    printed_marked_maps = {
        "shortest_path_exists": "SOO.\nxxO.\n..Ex",
        "no_shortest_path": "S...\nxxx.\n.xEx",
        "invalid_coordinate_at_end": "......\n....S.\n.x..OE\n......",
        "invalid_coordinate_in_middle": "......\n....S.\n.x..O.\n....E."
    }

    key_values = [
        "shortest_path_exists",
        "no_shortest_path",
        "invalid_coordinate_at_end",
        "invalid_coordinate_in_middle"
    ]

    # Read File
    def test_read_file(self):
        pass

    def test_read_file_error(self):
        pass

    # Parse String
    def test_parse_string_to_map(self):
        pass

    def test_parse_string_to_map_error(self):
        pass

    # Find Shortest Path
    def test_find_shortest_path(self):
        pass

    def test_find_shortest_path_error(self):
        pass

    # Print Map
    def test_print_map_path(self):
        pass

    # All At Once
    def test_solve_path(self):
        pass

    def test_solve_error(self):
        pass
