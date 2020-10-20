import pytest
from examples import filters


@pytest.mark.parametrize(
        "minsize, element, ret_none",
        [
            (0, {'word': ''}, False),
            (1, {'word': ''}, True),
            (2, {'word': ''}, True),

            (0, {'word': 'a'}, False),
            (1, {'word': 'a'}, False),
            (2, {'word': 'a'}, True),

            (3, {'word': 'test'}, False),
            (4, {'word': 'test'}, False),
            (5, {'word': 'test'}, True),
        ]
)
def test_example_dropsmallworld(minsize, element, ret_none):
    p = filters.DropSmallWord(None, minsize)
    assert p is not None

    r = p.sink(element)

    if ret_none:
        assert r is None
    else:
        assert r is not None
