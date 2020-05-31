import pytest
import numpy as np
from pathfinder.parse import Parser
from pathfinder.errors import ShortestPathNotFoundError
from pathfinder.tests.static_values import StaticValues


class TestParse:
    # Parse String
    @pytest.mark.parametrize('key', StaticValues.keys)
    def test_parse_string_to_map(self, key):
        assert (Parser.parse_string_to_map(StaticValues.input_strings[key])
                == StaticValues.maps[key]).all()

    def test_parse_string_to_map_error(self):
        with pytest.raises(ShortestPathNotFoundError):
            Parser.parse_string_to_map(StaticValues.bad_input_string)