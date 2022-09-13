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
    long_description_content_type='text/plain',
    long_description=open('README.rst', 'r').read(),
    license='lgpl v3',
    python_requires='>=3.8.10',
    install_requires=['scipy>=1.8.1'],
    classifiers=[
        "Development Status :: 4 - Beta",
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
