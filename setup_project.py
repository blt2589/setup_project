#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
setup_project.py
Garin Wally; May 2014/May 2016

This script creates a project folder-environment for GIS projects as follows:
<project_name>/
    data/
        raw/
        <project_name>.gdb
    design/
        fonts/
        images/
        rasters/
        vectors/
    maps/
        archive/
        final/
    reports/
    resources/
        tools/
"""

import argparse
import os
from shutil import copy2

# import arcpy  # moved for speed


# =============================================================================
# CLI ARGS

argp = argparse.ArgumentParser(description=__doc__, add_help=True,
                               formatter_class=argparse.RawTextHelpFormatter)
argp.add_argument("-n", action="store", dest="name",
                  help="Name of new project folder.")
argp.add_argument("--gdb", action="store_true", default=False,
                  dest="make_gdb", help="Option to make a gdb on setup.")
argp.add_argument("--cart", action="store_true", default=False,
                  dest="make_cart",
                  help="Option to make cartographic resource folders.")
# TODO: For now, we assume user has $ cd'd into the desired base directory

args = argp.parse_args()

if args.make_gdb:
    import arcpy

# =============================================================================
# FUNCTIONS


def make_gdb(gdb_name):
    # if no project exists, place gdb in cwd
    # if it does, place in DATA/
    # process: make gdb in C:/temp and copy to cwd
    copy2(None, None)
    pass


def main(dest_folder):
    # <project>/
    os.mkdir(dest_folder)
    # DATA/
    #   RAWDATA/
    os.makedirs(os.path.join(dest_folder, "data", "raw"))
    #       TODO: make scratch gdb here? / use C:/temp?
    #   MISC/
    os.mkdir(os.path.join(dest_folder, "data", "misc"))
    #   GDB/
    # TODO: if args.make_gdb: make_gdb(dest_folder)

    # MAPS/
    #   archive/
    os.makedirs(os.path.join(dest_folder, "maps", "archive"))
    #   FINAL/
    os.mkdir(os.path.join(dest_folder, "maps", "final"))

    if args.make_cart:
        # DESIGN/
        #   FONTS/
        os.makedirs(os.path.join(dest_folder, "design", "fonts"))
        #   IMAGES/
        os.mkdir(os.path.join(dest_folder, "design", "images"))
        #   RASTERS/
        os.mkdir(os.path.join(dest_folder, "design", "rasters"))
        #   VECTORS/
        os.mkdir(os.path.join(dest_folder, "design", "vectors"))

    # REPORTS/
    os.mkdir(os.path.join(dest_folder, "reports"))

    # RESOURCES/
    #   TOOLS/
    os.makedirs(os.path.join(dest_folder, "resources", "tools"))

    return


# =============================================================================
# RUN IT

if __name__ == "__main__":
    if not args.name:
        args.name = "new_project"

    new_proj = os.path.join(os.getcwd(), args.name)

    main(new_proj)
