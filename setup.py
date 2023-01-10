#!/usr/bin/python3

from setuptools import setup
from setuptools import find_packages
from lbh15 import __version__
from lbh15 import __author__

setup(
    name='lbh15',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    author=__author__,
    author_email='daniele.panico@newcleo.com, daniele.tomatis@newcleo.com',
    description='Python implementation of liquid metal properties from '
                'Handbook on Lead-bismuth Eutectic Alloy and Lead Properties, '
                'Materials Compatibility, Thermal-hydraulics and Technologies',
    long_description_content_type='text/x-rst',
    long_description=open('README.rst', 'r').read(),
    license='lgpl v3',
    python_requires='>=3.8.10',
    install_requires=['scipy>=1.8.1', 'numpy>=1.22.3'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

"""
Developers memo:
    - how to upload on PyPI:
        python3 setup.py sdist                     # in project directory
        twine check dist/*                         # check that package is ok
        twine upload --repository testpypi dist/*  # verify upload is successful on test-PyPI (see note below)
        twine upload dist/*                        # upload to PyPI: upload fails if version is already on PyPI

    - how to test package installation from test-pypi:
        - upload the new version of the package but change the package name in setup.py in lbh15_test
        - install the package from test-pypi using the following command:
            pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple lbh15_test
"""