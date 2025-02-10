import numpy as np
import pytest
import scienceplots
from matplotlib import pyplot as plt

from RWTHColors import ColorManager as cm
from RWTHColors.colors import RWTHRot, RWTHBlau


@pytest.fixture
def col_m():
    return cm()

def test_color_manager():
    my_cm = cm()

    assert RWTHRot.HEX[100] == my_cm.RWTHRot.p(100)

    my_cm.frmt = "RGB"

    assert RWTHRot.RGB[100] == my_cm.RWTHRot.p(100)

    my_cm.frmt = "HEX"

    assert RWTHRot.HEX[100] == my_cm.RWTHRot.p(100)


def test_plot_color_palette():
    my_cm = cm()

    fig, ax = cm.plot_color_palette()

    plt.show()
    fig.savefig("output/palette.png")


def test_matplotlib_context():
    styles = plt.style.available

    with plt.style.context(["rwth"]):
        fig1, ax = plt.subplots()

        x = np.arange(0, 10, 0.1)

        for i in range(10):
            ax.plot(x, i * np.sin(x), label=str(i + 1))

        plt.suptitle('Suptitle')
        ax.set_title('Axes Title')
        ax.set_xlabel('x-Axis')
        ax.set_ylabel('y-Axis')

    with plt.style.context(['science', 'grid', 'rwth', ]):
        fig3, ax = plt.subplots()

        x = np.arange(0, 10, 0.1)

        for i in range(10):
            ax.plot(x, i * np.sin(x), label=str(i + 1))

        plt.suptitle('Suptitle')
        ax.set_title('Axes Title')
        ax.set_xlabel('x-Axis')
        ax.set_ylabel('y-Axis')

    with plt.style.context(["rwth-full"]):
        fig4, ax = plt.subplots()

        ax.plot([0, 1], [0, 1])
        ax.plot([0, 2], [0, 1])
        ax.plot([0, 3], [0, 1])

        plt.suptitle('Suptitle')
        ax.set_title('Axes Title')
        ax.set_xlabel('x-Axis')
        ax.set_ylabel('y-Axis')

    with plt.style.context(["dark_background", "rwth-dark"]):
        fig5, ax = plt.subplots()

        x = np.arange(0, 10, 0.1)

        for i in range(10):
            ax.plot(x, i * np.sin(x), label=str(i + 1))

        plt.suptitle('Suptitle')
        ax.set_title('Axes Title')
        ax.set_xlabel('x-Axis')
        ax.set_ylabel('y-Axis')

    plt.show()
    pass


def test_normalized_rgb():
    my_cm = cm(frmt="NRGB")

    c = my_cm.RWTHBordeaux.p(100)
    assert c == (0.6313725490196078, 0.06274509803921569, 0.20784313725490197)


def test_cmaps():
    my_cm = cm(frmt="NRGB")

    x = np.arange(0, 100, 1)

    fig, ax = plt.subplots(1, 1)

    ax.scatter(x, x, c=x, s=100, cmap="viridis")
    ax.scatter(x + 20, x, c=x, s=100, cmap=my_cm.cmaps["rwth-viridis"])

    plt.show()
    pass


def test_simple_plot():
    x = np.arange(0, 100, 1)

    fig, ax = plt.subplots(1, 1)

    ax.plot(x, np.sin(x))
    ax.plot(x, np.cos(x))

    plt.show()


def test_rwthblau(col_m):
    rwthblau = col_m.RWTHBlau()
    assert rwthblau == RWTHBlau.p(100)