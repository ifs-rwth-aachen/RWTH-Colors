# RWTH Colors

RWTH Color definitions in different formats.
See [here](https://www9.rwth-aachen.de/global/show_document.asp?id=aaaaaaaaaadpbhq) for oringinal color defintions (German only)

## Android Studio
An XML file containing most RWTH colors

## CSS
.css file containing all RWTH Colors

## LaTeX
.tex file containing all RWTH Colors for use with the xcolor package

## Python Package
To integrate RWTH's colors into your python application, you can use the rwthcolors package

### Installation

You can install rwthcolors via pip:

`pip install rwthcolors`

### Usage

Simply import RWTHColors via :
`import RWTHColors`

Then you can use:
`plt.style.use('rwth')` to get RWTH colors in your matplotlib plots

Theres also style available called `rwth-full` containing a color cyle with more colors.

If you want to access colors explictly you can also use

`from RWTHColors import ColorManager`

and then instantiate a ColorManager using:

`cm = ColorManager()`

and then for example: `c=cm.RWTHSchwarz.p(75)` to get RWTH black as 75 % version.
The method by default returns the HEX code of the color. If you need RGB codes, you can instantiate
a ColorManager using  ColorManager(frmt='RGB').

If instantiated, the ColorManager furthermore replaces matplotlibs default color cycle with the same cycle used in mplstlye `rwth`.

## Color Palette
`cm.plot_color_palette()` returns a figure showing all RWTH colors

![Color Palette]("Python/rwth-colors/tests/output/palette.png")


## Tip
You can get even more beautiful plots if you use rwthcolors together with the [SciencePlots](https://github.com/garrettj403/SciencePlots) python package.
Then you can use for example:

`with plt.style.context(['science', 'grid', 'rwth']):
	...
`

