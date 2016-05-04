#!C:\Anaconda\python.exe
# -*- coding: utf-8 -*-

import sys
from setuptools import setup


if len(sys.argv) == 1:
    sys.argv.append("install")


with open("README.rst") as f:
    readme = f.read()

with open("LICENSE.txt") as f:
    license = f.read()

setup(
    name="GIS Project Setup Utility",
    version="0.1.1",
    description="Creates a new GIS project folder and subfolders",
    long_description=readme,
    author="Garin Wally",
    author_email="garwall101@gmail.com",
    url=None,
    license=license,
    scripts=["setup_project.py"]
    )
