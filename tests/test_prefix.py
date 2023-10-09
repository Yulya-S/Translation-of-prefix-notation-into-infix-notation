import pytest
from app import translate_to_infix


class Test_Prefix:
    @pytest.mark.parametrize(
        "text, response",
        [("+ - 13 4 55", "13 + 4 - 55"),
         ("+ 2 * 2 - 2 1", "2 + 2 * 2 - 1"),
         ("+ + 10 20 30", "10 + 20 + 30"),
         ("- - 1 2", "1 - 2"),
         ("/ + 3 10 * + 2 3 - 3 5", "3 / 10 + 2 * 3 + 3 - 5"),
         ("/ + 3 2 hello", None),
         ("/ + 3", "")]
    )
    def test_is_origin(self, text, response):
        assert translate_to_infix(text) == response