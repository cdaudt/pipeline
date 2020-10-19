import pytest
from examples import sources


@pytest.mark.parametrize(
        "array",
        [
            ['el1', 'el2', 'el3'],
            [],
            ['elemA', 'elemB', ['elemC1', 'elemC2']]
        ]
)
def test_example_arraysource(array):
    c = len(array)
    p = sources.ArraySource(None, array)
    assert p is not None

    assert p.run() == c
