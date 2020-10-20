import pytest
from examples import filters
import imageio
import hashlib

@pytest.mark.parametrize(
        "newsize, element, sha",
        [
            ((120, 120), {
                'image_id': 1,
                'image': imageio.imread('examples/pics/1.jpg', pilmode='RGB'),
                'name': 'pics/1.jpg'
            }, '3427b61c59ef0f762446a271c7a29b4b26f2915f0d42678a5a02a1e0a72364ad'),

            ((512, 512), {
                'image_id': 1,
                'image': imageio.imread('examples/pics/2.jpg', pilmode='RGB'),
                'name': 'pics/2.jpg'
            }, '53d6d2436f063b26fb81c1965b9483612a8a6d0255c3bdc5800f902f012811ec'),
        ]
)
def test_example_resizeimage(newsize, element, sha):
    r = filters.ResizeImage(None, newsize)
    assert r is not None

    u = r.sink(element)

    assert u is not None
    assert 'resized-image' in u

    d = hashlib.sha256(u['resized-image']).hexdigest()
    assert d == sha
