"""
Author: Sergi Mas-Pujol
Last update: 13/11/2022

Utilities to clean Jupyter Notebooks
"""

import os


def clean_notebooks(notebooks_dir):
    """ Clean outputs and metadate """
    if not os.path.isdir(notebooks_dir):
        raise ValueError(f"{notebooks_dir} is not a valis directory")
    for subdir, _, files in os.walk(notebooks_dir):
        for file in files:
            origin_file = os.path.join(subdir, file)
            print(origin_file)
            os.system('nbstripout ' + origin_file)
