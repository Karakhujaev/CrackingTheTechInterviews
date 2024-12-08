from binary_search import search_recursion
import pytest

@pytest.mark.parametrize("arr, target, expected", [
    ([1, 2, 3, 4, 5, 7], 3, True),
    ([1, 2, 3, 4, 5, 7], 12, False),
    ([1, 2, 3, 4, 5, 7, 300, 500], 80, True)

])
def test_search_recursion(arr, target, expected):
    got = search_recursion(arr, target)
    assert expected==got, f"{expected=}, {got=}"