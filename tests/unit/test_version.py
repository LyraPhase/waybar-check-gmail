import sys

if sys.version_info[:2] >= (3, 8):
    import importlib.metadata as importlib_metadata
else:
    import importlib_metadata


def test_version():
    from waybar_check_gmail import version

    dist = importlib_metadata.distribution("waybar_check_gmail")
    expected = dist.version
    assert version.__version__ == expected
