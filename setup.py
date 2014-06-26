#!/usr/bin/env python

from setuptools import setup

setup(
    name = "RPiShift",
    version = "0.2.0",
    author = "Kyle J. Kneitinger",
    author_email = "kylejkneitinger@gmail.com",
    description = ("A module for interfacing a 595 shift register with the Raspberry Pi"),
    license = "GPLv2",
    keywords = "raspberry pi 595 shift register electronics",
    url = "http://github.com/kneitinger/RPiShift",
    packages=['RPiShift'],
    long_description = (""),
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Other Environment",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
