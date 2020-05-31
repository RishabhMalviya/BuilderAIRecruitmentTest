import pytest
from pathfinder.utils import read_file, print_map
from pathfinder.tests.static_values import StaticValues


class TestParse:
    # Read File
    @pytest.mark.parametrize('key', StaticValues.keys)
    def test_read_file(self, key):
        assert read_file(StaticValues.input_files[key]) \
               == StaticValues.input_strings[key]

    def test_read_file_error(self):
        with pytest.raises(FileNotFoundError):
            read_file(StaticValues.bad_file_path)

    # Print Map
    @pytest.mark.parametrize('key', StaticValues.keys)
    def test_print_map_path(self, key):
        assert print_map(StaticValues.maps_marked[key]) \
               == StaticValues.printed_marked_maps[key]