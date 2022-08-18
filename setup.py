#!/usr/bin/python3

from setuptools import setup
import lbh15

with open('README.rst') as readme_file:
    long_description = readme_file.read()

setup(
    name='lbh15',
    version=lbh15.__version__,
    packages=['lbh15'],
    include_package_data=True,
    author=lbh15.__author__,
    author_email='daniele.panico@newcleo.com, daniele.tomatis@newcleo.com',
    description='Python implementation of liquid metal properties from '
                'Handbook on Lead-bismuth Eutectic Alloy and Lead Properties, '
                'Materials Compatibility, Thermal-hydraulics and Technologies',
    long_description=long_description,
    license="lgpl v3",
    python_requires='>=3.8.10',
    install_requires=["scipy>=1.8.1"],
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
