import sys

if sys.version_info[:2] >= (3, 8):
    import importlib.metadata as importlib_metadata
else:
    import importlib_metadata


__version__ = importlib_metadata.version(__name__.split(".", 1)[0])
__distribution__ = importlib_metadata.distribution(__name__.split(".", 1)[0])
PROGRAM_NAME: str = __distribution__.name
