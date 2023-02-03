"""
Usage:
    python setup_ates.py --wd /mnt/Storage/Workspace/ATES/caic --aoi chihuahua_gulch

"""

import argparse
import os


# =============================================================================
def custom_usage_message():
    return """Do the thing."""


def process_options():
    parser = argparse.ArgumentParser(usage=custom_usage_message())
    parser.add_argument("--wd", action="store",
                        help="Path to place project folder.")
    parser.add_argument("--aoi", action="store", default="",
                        help="Name of Avalanche Center or AoI if center has multiple AoIs (use underscores instead of spaces).")

    return parser.parse_args()


# =============================================================================


def ates_project(args):
    wd = args.wd
    aoi = args.aoi

    os.makedirs(os.path.join(wd, aoi, "aoi"))
    os.makedirs(os.path.join(wd, aoi, "clips"))
    os.makedirs(os.path.join(wd, aoi, "deliverables"))
    os.makedirs(os.path.join(wd, aoi, "flow_py"))
    os.makedirs(os.path.join(wd, aoi, "inputdata"))
    os.makedirs(os.path.join(wd, aoi, "PRA"))


# =============================================================================
# RUN IT

if __name__ == "__main__":
    args = process_options()
    ates_project(args)
