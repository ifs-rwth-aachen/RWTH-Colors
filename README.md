# RWTH Colors

RWTH Color definitions in different formats.
See [here](https://www9.rwth-aachen.de/global/show_document.asp?id=aaaaaaaaaadpbhq) for oringinal color defintions (German only)

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

and then

`cm = ColorManager()`

and the for example: `c=cm.RWTHSchwarz.p(75)` to get RWTH black 75 % version.
The method call by default returns the HEX code of the color