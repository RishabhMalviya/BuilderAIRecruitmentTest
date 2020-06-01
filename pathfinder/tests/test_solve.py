import pytest
from pathfinder import solve
from pathfinder.tests.testing_data import TestingData
from pathfinder.search import BreadthFirstSearch
from pathfinder.errors import ShortestPathNotFoundError


class TestSolve:
    # Find Shortest Path
    @pytest.mark.parametrize('key', TestingData.good_keys)
    def test_find_shortest_path(self, key):
        ocean_map_ = TestingData.maps[key]
        start_ = TestingData.start_positions[key]
        end_ = TestingData.end_positions[key]

        assert (BreadthFirstSearch(ocean_map_, start_, end_).find_shortest_path()
                == TestingData.maps_marked[key]).all()

    def test_find_shortest_path_error(self):
        with pytest.raises(ShortestPathNotFoundError):
            ocean_map_ = TestingData.maps[TestingData.bad_key]
            start_ = TestingData.start_positions[TestingData.bad_key]
            end_ = TestingData.end_positions[TestingData.bad_key]

            BreadthFirstSearch(ocean_map_, start_, end_).find_shortest_path()

    # End To End
    @pytest.mark.parametrize('key', TestingData.good_keys)
    def test_solve_path(self, key):
        assert solve(TestingData.input_files[key]) \
               == TestingData.printed_marked_maps[key]

    def test_solve_error(self):
        with pytest.raises(ShortestPathNotFoundError):
            solve(TestingData.input_files[TestingData.bad_key])
