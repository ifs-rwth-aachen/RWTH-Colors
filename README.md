# RWTH Aachen University - Corporate Design Colors

This repository contains RWTH Aachen University's corporate design color definitions in different formats.
See [here](https://www9.rwth-aachen.de/global/show_document.asp?id=aaaaaaaaaadpbhq) for oringinal color defintions (German only)

## Android Studio
An XML file containing most RWTH colors

## Inkscape
A `.gpl` file for Inkscape. Place in the palette folder of your Inkscape installation. You can find the location in the Inkscape settings under System.

## CSS
.css file containing all RWTH Colors

## LaTeX
.tex file containing all RWTH Colors for use with the xcolor package

## Draw.io
A json file containing all RWTH Colors for use with draw.io

## Python Package
The `rwthcolors` package allows you to integrate RWTH's official color palette into your Python applications, particularly for use with matplotlib.

### Installation

Install `rwthcolors` via pip:

```bash
pip install rwthcolors
```

### Usage

#### Importing RWTHColors

To automatically set the default color cycle to RWTH colors, simply import:

```python
import RWTHColors
```
This will make all matplotlib figures by default use RWTH colors!

Alternatively, apply RWTH colors to your matplotlib plots using:

```python
plt.style.use('rwth')
```

Additional styles include:
- **`rwth-full`**: A color cycle with more colors.
- **`rwth-dark`**: For dark backgrounds. Use it with:
  ```python
  with plt.style.context(['dark_background', 'rwth-dark']):
      # Your plotting code here
  ```

#### Accessing Colors Explicitly

To access colors explicitly, use `ColorManager`:

```python
from RWTHColors import ColorManager
cm = ColorManager()
```

Example to get RWTH black at 75% intensity:

```python
c = cm.RWTHSchwarz.p(75)
```

By default, this returns the HEX code. For RGB codes, instantiate `ColorManager` with:

```python
cm = ColorManager(frmt='RGB')
```

Retrieve colors directly by calling them:

```python
c = cm.RWTHBlau()  # RWTHBlau at 100%
c = cm.RWTHBlau(50)  # RWTHBlau at 50%
```
⚠️ **Warning:** RWTHColors only contains the official RWTH colors at 100 %, 75%, 50 %, 25 % and 10 %. It does not interpolate inbetween values.

Print color values using:

```python
print(RWTHRot.colors('RGB')) # or
print(RWTHRot())
```

When instantiated, `ColorManager` replaces matplotlib's default color cycle with the cycle used in the `rwth` mplstyle.

### Color Palette

Display all RWTH colors with:

```python
cm.plot_color_palette()
```

![Color Palette](Python/rwth-colors/tests/output/palette.png)

### Tips for Enhanced Plots

Enhance your plots by combining `rwthcolors` with the [SciencePlots](https://github.com/garrettj403/SciencePlots) package. Example style combination:

```python
with plt.style.context(['science', 'grid', 'rwth']):
    # Your plotting code here
```

#### Example Plot

```python
import matplotlib.pyplot as plt
import numpy as np
import RWTHColors
import scienceplots

plt.style.use(['science', 'grid', 'rwth'])

x = np.arange(0, 4*np.pi, .01)

fig, ax = plt.subplots(1, 1, figsize=(10, 4))

for a in [1, 2, 3, 4, 5, 6, 7, 8]:
    ax.plot(x, a*np.sin(x), label='$\hat{a}=$' + '${}$'.format(a))
    
ax.legend(loc=1)
ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')

plt.show()
```

This produces:

![Example Plot](Python/rwth-colors/tests/output/plot.png)

### Vega-Altair plots
RWTHColors also provides themes for the plotting library [Vega-Altair](https://altair-viz.github.io/). To activate the themes inlclude the following before using altair:

```python
import altair as alt
import RWTHColors

alt.theme.enable("rwth") # or "rwth-full" or "rwth-dark"
```

The themes `rwth`, `rwth-full` and `rwth-dark`, analog to the matplotlib themes are available. Then you can craete plots as usual, e.g.,:

```python
import altair as alt
import pandas as pd
import RWTHColors

alt.theme.enable("rwth") # or "rwth-full" or "rwth-dark"

source = pd.DataFrame(
{
    "a": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
    "b": [28, 55, 43, 91, 81, 53, 19, 87, 52],
}
)

bar = alt.Chart(source).mark_bar(tooltip=True).encode(x="a:N", y="b:Q").properties(title='Bar Chart')

```

<!-- CONTACT -->
# Disclaimer

This repository is not maintained by RWTH Aachen University's marketing department but a voluntary offer by the Institute of Rail Vehicles.
If you have the color definitions in other formats, feel free to contribute them using a merge request.

<div>  
<a href="">
    <img src="http://www.ifs.rwth-aachen.de/fileadmin/images/rwth_ifs_de_rgb.png" alt="IFS Logo" width="400">
  </a>
</div>

