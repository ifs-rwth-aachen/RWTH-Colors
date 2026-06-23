import os

import matplotlib.pyplot as plt


def read_styles_in_folders(root_path):
    """
    Based on: https://github.com/garrettj403/SciencePlots/blob/master/src/scienceplots/styles_discovery.py
    Reads all stylesheets in the given path and its subfolders.

    Parameters
    ----------
    root_path : str
        Path to the root folder containing the stylesheets and other subfolders
        with stylesheets.

    Returns
    -------
    stylesheets : dict
        Dictionary of stylesheets in the form of {style_name: rcParams}.
        Should be compatible with matplotlib's plt.style.library dictionary.
    """
    # Fix namespace changes introduced in matplotlib 3.11
    # see issue https://github.com/garrettj403/SciencePlots/issues/163
    try:  # matplotlib >= 3.11
        read_style_directory = plt.style.read_style_directory  # function obj
    except AttributeError:  # matplotlib < 3.11
        read_style_directory = plt.style.core.read_style_directory  # function obj

    stylesheets = {}  # plt.style.library is a dictionary
    for folder, _, _ in os.walk(root_path):
        new_stylesheets = read_style_directory(folder)
        stylesheets.update(new_stylesheets)
    return stylesheets