import pytest
import numpy as np
from pathfinder.parse import Parser
from pathfinder.errors import ShortestPathNotFoundError
from pathfinder.tests.testing_data import TestingData


class TestParse:
    # Parse String
    @pytest.mark.parametrize('key', TestingData.keys)
    def test_parse_string_to_map(self, key):
        np.testing.assert_array_equal(
            Parser.parse_string_to_map(TestingData.input_strings[key])[0],
            TestingData.maps[key]
        )

    def test_parse_string_to_map_error(self):
        with pytest.raises(ShortestPathNotFoundError):
            Parser.parse_string_to_map(TestingData.bad_input_string)
