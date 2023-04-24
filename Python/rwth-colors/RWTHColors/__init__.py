from .cm import ColorManager

from os import listdir
from os.path import isdir, join

import matplotlib.pyplot as plt

import RWTHColors

# Similar to https://github.com/garrettj403/SciencePlots/blob/master/scienceplots/__init__.py
# Register the included stylesheet in the matplotlib style library
rwthcolors_path = RWTHColors.__path__[0]
styles_path = join(rwthcolors_path, 'mpl-styles')

# Reads styles in /styles
stylesheets = plt.style.core.read_style_directory(styles_path)

# Reads styles in /styles subfolders
for path in listdir(styles_path):
    new_data_path = join(styles_path, path)
    if isdir(new_data_path):
        new_stylesheets = plt.style.core.read_style_directory(new_data_path)
        stylesheets.update(new_stylesheets)

# Update dictionary of styles
plt.style.core.update_nested_dict(plt.style.library, stylesheets)
plt.style.core.available[:] = sorted(plt.style.library.keys())
