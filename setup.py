# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

version = "0.1.3"

description = "A copy of the ASDL parser used in CPython 3.5."

with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_descr = f.read()

setup(
    name = "asdl",
    version = version,

    description = description,
    long_description = long_descr,
    license = "PSFL",
    url = "https://github.com/fpoli/python-asdl",

    author = "Federico Poli",
    author_email = "federpoli@gmail.com",

    py_modules = ["asdl"],

    extras_require = {
        "dev": [
            "twine",
            "nose",
            "pep8 == 1.4.6"
        ]
    },

    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Compilers",
        "License :: OSI Approved :: Python Software Foundation License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5"
    ]
)
