import pytest
from examples import sources
from contextlib import ExitStack as does_not_raise


@pytest.mark.parametrize(
        "files, limit, raises",
        [
            ([], -1, does_not_raise()),
            ([], 0, does_not_raise()),
            ([], 1, pytest.raises(IndexError)),

            (['examples/pics/1.jpg'], -1, does_not_raise()),
            (['examples/pics/1.jpg', 'examples/pics/2.jpg'], -1, does_not_raise()),
            (['examples/pics/1.jpg', 'examples/pics/2.jpg'], 0, does_not_raise()),
            (['examples/pics/1.jpg', 'examples/pics/2.jpg'], 1, does_not_raise()),
            (['examples/pics/1.jpg', 'examples/pics/2.jpg'], 2, does_not_raise()),
            (['examples/pics/1.jpg', 'examples/pics/2.jpg'], 3, pytest.raises(IndexError)),
        ]
)
def test_example_picturesource(files, limit, raises):
    if limit == -1:
        count = len(files)
    else:
        count = limit
    with raises:
        p = sources.PictureSource(None, files, limit=limit)
        assert p is not None

        assert p.run() == count
