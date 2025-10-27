from RWTHColors import colors as c
import importlib.util

spec = importlib.util.find_spec("altair")


# from RWTHColors/cm.py#rwth_color_cycle
color_order = [
    c.RWTHBlau,
    c.RWTHOrange,
    c.RWTHGruen,
    c.RWTHRot,
    c.RWTHViolett,
    c.RWTHBordeaux,
    c.RWTHLila,
    c.RWTHPetrol,
    c.RWTHMaiGruen,
    c.RWTHTuerkis,
]

# from RWTHColors/mpl-styles/rwth-dark.mplstyle
color_order_dark = [
    "#8EBAE5",
    "#FDD48F",
    "#B8D698",
    "#E69679",
    "#A8859E",
    "#CD8B87",
    "#BCB5D7",
    "#7DA4A7",
    "#E0E69A",
    "#89CCCF",
]

# from https://anthology-of-data.science/posts/altair/better-altair-theme.html


def altair_theme_creator(
    category_palette,
    sequential_palette,
    diverging_palette,
    mark_color="#00549F",
    axis_color="#000000",
    font_color="#000000",
    background_color="#FFFFFF",
    font="arial",
    label_font=None,
    source_font=None,
    grid_color="#DEDDDD",
):
    source_font = source_font or font
    label_font = label_font or font
    return {
        "config": {
            "title": {
                "color": font_color
            },
            "axisX": {
                "domainColor": axis_color,
                "labelFont": font,
                "tickColor": axis_color,
                "titleFont": font,
                "labelColor": font_color,
                "titleColor": font_color
            },
            "axisY": {
                "gridColor": grid_color,
                "labelFont": font,
                "titleFont": font,
                "labelColor": font_color,
                "titleColor": font_color
            },
            "background": background_color,
            "legend": {
                "labelFont": font,
                "titleFont": font,
                "labelColor": font_color,
                "titleColor": font_color
            },
            "range": {
                "category": category_palette,
                "diverging": diverging_palette,
                "ordinal": sequential_palette,
                "ramp": sequential_palette,
                "heatmap": sequential_palette,
            },
            "area": {
                "fill": mark_color,
            },
            "line": {
                "color": mark_color,
                "stroke": mark_color,
            },
            "trail": {
                "color": mark_color,
                "stroke": mark_color,
            },
            "path": {
                "stroke": mark_color,
            },
            "text": {
                "font": source_font,
                "color": mark_color,
            },
            "bar": {
                "fill": mark_color,
            },
        },
    }


if spec is not None:
    import altair as alt

    @alt.theme.register("rwth", enable=False)
    def rwth_theme() -> alt.theme.ThemeConfig:
        return altair_theme_creator(
            category_palette=[c.HEX[100] for c in color_order],
            sequential_palette=list(reversed([v for v in c.RWTHBlau.HEX.values()])),
            diverging_palette=[v for v in c.RWTHRot.HEX.values()]
            + ["white"]
            + list(reversed([v for v in c.RWTHBlau.HEX.values()])),
        )

    @alt.theme.register("rwth-full", enable=False)
    def rwth_theme_full() -> alt.theme.ThemeConfig:
        return altair_theme_creator(
            category_palette=[
                c.HEX[i] for i in [100, 75, 50, 25, 10] for c in color_order
            ],
            sequential_palette=list(reversed([v for v in c.RWTHBlau.HEX.values()])),
            diverging_palette=[v for v in c.RWTHRot.HEX.values()]
            + ["white"]
            + list(reversed([v for v in c.RWTHBlau.HEX.values()])),
        )

    @alt.theme.register("rwth-dark", enable=False)
    def rwth_theme_dark() -> alt.theme.ThemeConfig:
        return altair_theme_creator(
            category_palette=[c for c in color_order_dark],
            sequential_palette=['black']+list(c.RWTHBlau.HEX.values()),
            diverging_palette=[v for v in c.RWTHRot.HEX.values()]
            + ["white"]
            + list(reversed([v for v in c.RWTHBlau.HEX.values()])),
            mark_color=color_order_dark[0],
            axis_color="#FFFFFF",
            background_color="#000000",
            grid_color="#212121",
            font_color="#FFFFFF"
        )
