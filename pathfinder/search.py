import numpy as np
from pathfinder.parse import Parser
from pathfinder.errors import ShortestPathNotFoundError
from pathfinder.utils import read_file, print_map


class BreadthFirstSearch:
    """Encapsulates all steps for marking shortest path on maps

    ...

    Args
    ------
        ocean_map_ (np.ndarray(dtype='U1')): map with start, end, and reefs marked on it. Path is not marked on it yet.
        start_ (list [x_start, y_start]): starting coordinates
        end_ (list [x_end, y_end]): end coordinates

    Methods
    --------
        find_shortest_path():
            finds the shortest path from start to end and marks it on the map. Returns the marked map.
    """

    x_change = [0, 1, 0, -1]
    y_change = [1, 0, -1, 0]

    def __init__(self, ocean_map_, start_, end_):
        self.ocean_map = ocean_map_
        self.x_max = self.ocean_map.shape[0]
        self.y_max = self.ocean_map.shape[1]

        self.start = start_
        self.end = end_

        self.parent_cells = np.full((self.x_max, self.y_max), None, dtype='O')
        self.visited_cells = np.full((self.x_max, self.y_max), False, dtype='?')
        self.visited_cells_queue = []

    def __update_valid_neighbours(self, current_cell):
        curr_x = current_cell[0]
        curr_y = current_cell[1]

        neighbours = []

        for i in range(len(BreadthFirstSearch.x_change)):
            new_x = curr_x + BreadthFirstSearch.x_change[i]
            new_y = curr_y + BreadthFirstSearch.y_change[i]

            if 0 <= new_x < self.x_max and 0 <= new_y < self.y_max:
                if not self.visited_cells[new_x][new_y] and not self.ocean_map[new_x][new_y] == 'x':
                    self.visited_cells[new_x][new_y] = True
                    self.parent_cells[new_x][new_y] = current_cell
                    self.visited_cells_queue.append([new_x, new_y])
                    neighbours.append([new_x, new_y])

        return neighbours

    def __mark_shortest_path(self):
        curr_parent_cell = self.parent_cells[self.end[0]][self.end[1]]

        while not curr_parent_cell == self.start:
            self.ocean_map[curr_parent_cell[0]][curr_parent_cell[1]] = 'O'
            curr_parent_cell = self.parent_cells[curr_parent_cell[0]][curr_parent_cell[1]]

    def find_shortest_path(self):
        """Finds shortest path from start point to end point in map. Returns a map with path marked in specified format.

        Uses a modified version of Dijkstra's Algorithm.

        :return: map with shortest path marked in specified format
        :rtype: numpy.ndarray(dtype='U1')

        :raises ShortestPathNotFoundError: If shortest path to treasure does not exist
        """

        reached_end = False
        self.visited_cells[self.start[0]][self.start[1]] = True
        self.visited_cells_queue.append(self.start)
        curr_queue_index = 0

        while curr_queue_index < len(self.visited_cells_queue):
            current_cell = self.visited_cells_queue[curr_queue_index]
            self.__update_valid_neighbours(current_cell)

            if self.visited_cells[self.end[0]][self.end[1]]:
                reached_end = True
                break
            else:
                curr_queue_index += 1

        if not reached_end:
            raise ShortestPathNotFoundError("No valid path to treasure.")
        else:
            self.__mark_shortest_path()
            return self.ocean_map
