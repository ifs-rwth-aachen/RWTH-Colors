from os import listdir
from os.path import isdir, join

import matplotlib.pyplot as plt

import RWTHColors
from . import altair_theme
from .cm import ColorManager
from .utils import read_styles_in_folders

# Similar to https://github.com/garrettj403/SciencePlots/blob/master/scienceplots/__init__.py
# Register the included stylesheet in the matplotlib style library
rwthcolors_path = RWTHColors.__path__[0]
styles_path = join(rwthcolors_path, 'mpl-styles')

# Reads styles in /styles folder and all subfolders
stylesheets = read_styles_in_folders(styles_path)

# Fix namespace changes introduced in matplotlib 3.11
# see issue https://github.com/garrettj403/SciencePlots/issues/163
try:  # matplotlib >= 3.11
    update_nested_dict = plt.style.update_nested_dict  # function obj
    available = plt.style.available  # list shallow-copy
except AttributeError:  # matplotlib < 3.11
    update_nested_dict = plt.style.core.update_nested_dict  # function obj
    available = plt.style.core.available  # list shallow-copy

# Update dictionary of styles - plt.style.library
update_nested_dict(plt.style.library, stylesheets)
# Update `plt.style.available`, copy-paste from:
# https://github.com/matplotlib/matplotlib/blob/a170539a421623bb2967a45a24bb7926e2feb542/lib/matplotlib/style/core.py#L266  # noqa: E501
available[:] = sorted(plt.style.library.keys())

plt.style.use(['rwth'])
