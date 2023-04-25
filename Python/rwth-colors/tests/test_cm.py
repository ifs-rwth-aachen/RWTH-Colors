
from matplotlib import pyplot as plt

from RWTHColors import ColorManager as cm
from RWTHColors.colors import RWTHRot


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
    fig.savefig('output/palette.png')

def test_matplotlib_context():
    styles = plt.style.available

    with plt.style.context(['rwth']):
        fig1, ax = plt.subplots()

        ax.plot([0, 1], [0, 1])
        ax.plot([0, 2], [0, 1])
        ax.plot([0, 3], [0, 1])


    with plt.style.context(['rwth-full']):
        fig2, ax = plt.subplots()

        ax.plot([0, 1], [0, 1])
        ax.plot([0, 2], [0, 1])
        ax.plot([0, 3], [0, 1])

    plt.show()
    pass
