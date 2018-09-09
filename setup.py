"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages


# get __version__ from _version.py
#exec(open('pytorch_server/_version.py').read())
from pytorch_server._version import __version__

# Get the long description from the relevant file
#with open('DESCRIPTION.rst') as f:
#    long_description = f.read()
long_description = 'WRITE ME!'


setup(
    # Application name:
    name="pytorch_server",

    # Version number (initial):
    version=__version__,

    # Application author details:
    author="lundy bernard",
    author_email="lundy.bernard@gmail.com",

    license='MIT',

    # Packages
    #packages=["pytorch_server"],
    packages=find_packages(),

    # entry points, to generate executables in python/bin/
    entry_points={
        "console_scripts":
            ['pytorch_server = pytorch_cli:PytorchCLI']
    },

    # Include additional files into the package
    # WARNING not a distutils option
    #include_package_data=True,

    # Details
    url="none exists yet",

    #
    # license="LICENSE.txt",
    description="utilities for automating ipcenter tasks",

    long_description=long_description,

    # Dependent packages (distributions)
    install_requires=[
        'flask',
    ],
)
