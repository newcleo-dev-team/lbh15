#!/usr/bin/python3

from setuptools import setup
import os


with open(os.path.join("lbeh15", "VERSION")) as version_file:
    __version__ = version_file.read().strip()

with open(os.path.join("lbeh15", "AUTHOR")) as author_file:
    __author__ = author_file.read().strip()

with open(os.path.join("docs", "files", "README.rst")) as readme_file:
    long_description = readme_file.read()

setup(
    name='lbeh15',
    version=__version__,
    packages=['lbeh15'],
    include_package_data=True,
    author=__author__,
    author_email='daniele.panico@newcleo.com, daniele.tomatis@newcleo.it',
    description='Python implementation of liquid metal properties from Handbook'
                'on Lead-bismuth Eutectic Alloy and Lead Properties, Materials Compatibility,'
                ' Thermal-hydraulics and Technologies',
    long_description=long_description,
    license="gpl v3",
    python_requires='>=3.*',
    install_requires=["scipy>=1.8.1"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Nuclear Industry",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)