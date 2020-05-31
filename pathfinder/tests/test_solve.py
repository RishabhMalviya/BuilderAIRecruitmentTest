import pytest
import numpy as np
from pathfinder.tests.static_values import StaticValues
from pathfinder.solve import ShortestPathFinder, solve
from pathfinder.errors import ShortestPathNotFoundError


class TestSolve:
    # Find Shortest Path
    @pytest.mark.parametrize('key', StaticValues.good_keys)
    def test_find_shortest_path(self, key):
        assert (ShortestPathFinder.find_shortest_path(StaticValues.maps[key])
                == StaticValues.maps_marked[key]).all()

    def test_find_shortest_path_error(self):
        with pytest.raises(ShortestPathNotFoundError):
            ShortestPathFinder.find_shortest_path(StaticValues.maps[StaticValues.bad_key])

    # All At Once
    @pytest.mark.parametrize('key', StaticValues.good_keys)
    def test_solve_path(self, key):
        assert solve(StaticValues.input_files[key]) \
               == StaticValues.printed_marked_maps[key]

    def test_solve_error(self):
        with pytest.raises(ShortestPathNotFoundError):
            solve(StaticValues.input_files[StaticValues.bad_key])
