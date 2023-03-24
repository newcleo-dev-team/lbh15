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
Developers memo for release:
    1. Update package information (on master):
        - Change version in lbh15/__init__.py
        - Change date in lbh15/__init__.py
        - Change date in README.rst

    2. Test the package build and install on test-pypi:
        a. Change the name of the package in setup.py in 'lbh15-test'
        b. python3 setup.py sdist                     # in project directory
        c. twine check dist/*                         # check that package is ok
        d. twine upload --repository testpypi dist/*  # verify upload is successful on test-PyPI
        e. crete a python3 virtual enviroment and verify the correct package installation form test-pypi:
            python3 -m venv venv_install
            source venv_install/bn/activate
            pip3 install wheel
            pip3 install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple lbh15-test
            cd tests/
            <execute tests>
        f. If every thing is ok change back the package name in 'lbh15'
        
    3. Create tag (on master):
        a. git tag v<version>
        b. git push <origin_name> <tag_name>
        c. git diff --stat=200 <previous_tag> <tag_name> > log.diff.<tag_name>
        d. You should see the tag on github page as well. Then on github do:
            - https://github.com/newcleo-dev-team/lbh15/releases
            - Click on "Draft a new release"
            - Choose the tag
            - Insert the title name as "Release v<version>"
            - In the description write:
                Changelog between v<previous varsion> and v<version>

                ```
                < content of  log.diff.<tag_name> >
                ```

    4. Upload the package on PyPI:
        a. repeat step 2.b and 2.c
        b. twine upload dist/*             
"""