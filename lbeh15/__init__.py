import os


basepath = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(basepath, 'VERSION')) as version_file:
    __version__ = version_file.read().strip()
