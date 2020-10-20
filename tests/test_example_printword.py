import pytest
from examples import filters


@pytest.mark.parametrize(
        "element",
        [
            {'word': ''},
            {'word': 'a'},
            {'word': 'test'},
        ]
)
def test_example_printworld(element):
    p = filters.PrintWord(None)
    assert p is not None

    r = p.sink(element)
    assert r is not None
