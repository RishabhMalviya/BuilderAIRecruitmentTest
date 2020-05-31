import pytest
from pathfinder.utils import read_file, print_map
from pathfinder.tests.testing_data import TestingData


class TestParse:
    # Read File
    @pytest.mark.parametrize('key', TestingData.keys)
    def test_read_file(self, key):
        assert read_file(TestingData.input_files[key]) \
               == TestingData.input_strings[key]

    def test_read_file_error(self):
        with pytest.raises(FileNotFoundError):
            read_file(TestingData.bad_file_path)

    # Print Map
    @pytest.mark.parametrize('key', TestingData.keys)
    def test_print_map_path(self, key):
        assert print_map(TestingData.maps_marked[key]) \
               == TestingData.printed_marked_maps[key]