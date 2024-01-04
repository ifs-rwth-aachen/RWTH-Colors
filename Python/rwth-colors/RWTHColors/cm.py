import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

from RWTHColors.colors import *
from cycler import cycler


class ColorManager:
    RWTHBlau = RWTHBlau()
    RWTHSchwarz = RWTHSchwarz()
    RWTHMagenta = RWTHMagenta()
    RWTHGelb = RWTHGelb()
    RWTHPetrol = RWTHPetrol()
    RWTHTuerkis = RWTHTuerkis()
    RWTHGruen = RWTHGruen()
    RWTHMaiGruen = RWTHMaiGruen()
    RWTHOrange = RWTHOrange()
    RWTHRot = RWTHRot()
    RWTHBordeaux = RWTHBordeaux()
    RWTHViolett = RWTHViolett()
    RWTHLila = RWTHLila()

    color_list = [RWTHBlau,
                  RWTHPetrol,
                  RWTHTuerkis,
                  RWTHGruen,
                  RWTHMaiGruen,
                  RWTHOrange,
                  RWTHRot,
                  RWTHBordeaux,
                  RWTHViolett,
                  RWTHLila,
                  RWTHSchwarz,
                  RWTHMagenta,
                  RWTHGelb]

    def __init__(self, frmt: str = "HEX", cycle='default'):
        if frmt not in ["HEX", "RGB", "NRGB"]:
            raise ValueError("frmt must be HEX, NRGB or RGB not %s" % frmt)

        self.rwth_color_cycle = cycler(color=[self.RWTHBlau.p(100),
                                              self.RWTHOrange.p(100),
                                              self.RWTHGruen.p(100),
                                              self.RWTHRot.p(100),
                                              self.RWTHViolett.p(100),
                                              self.RWTHBordeaux.p(100),
                                              self.RWTHLila.p(100),
                                              self.RWTHPetrol.p(100),
                                              self.RWTHMaiGruen.p(100),
                                              self.RWTHTuerkis.p(100),
                                              ])

        self.rwth_full_color_cycle = cycler(color=[self.RWTHBlau.p(100),
                                                   self.RWTHOrange.p(100),
                                                   self.RWTHGruen.p(100),
                                                   self.RWTHRot.p(100),
                                                   self.RWTHViolett.p(100),
                                                   self.RWTHBordeaux.p(100),
                                                   self.RWTHLila.p(100),
                                                   self.RWTHPetrol.p(100),
                                                   self.RWTHMaiGruen.p(100),
                                                   self.RWTHTuerkis.p(100),
                                                   self.RWTHBlau.p(75),
                                                   self.RWTHOrange.p(75),
                                                   self.RWTHGruen.p(75),
                                                   self.RWTHRot.p(75),
                                                   self.RWTHViolett.p(75),
                                                   self.RWTHBordeaux.p(75),
                                                   self.RWTHLila.p(75),
                                                   self.RWTHPetrol.p(75),
                                                   self.RWTHMaiGruen.p(75),
                                                   self.RWTHTuerkis.p(75),
                                                   self.RWTHBlau.p(50),
                                                   self.RWTHOrange.p(50),
                                                   self.RWTHGruen.p(50),
                                                   self.RWTHRot.p(50),
                                                   self.RWTHViolett.p(50),
                                                   self.RWTHBordeaux.p(50),
                                                   self.RWTHLila.p(50),
                                                   self.RWTHPetrol.p(50),
                                                   self.RWTHMaiGruen.p(50),
                                                   self.RWTHTuerkis.p(50),
                                                   self.RWTHBlau.p(25),
                                                   self.RWTHOrange.p(25),
                                                   self.RWTHGruen.p(25),
                                                   self.RWTHRot.p(25),
                                                   self.RWTHViolett.p(25),
                                                   self.RWTHBordeaux.p(25),
                                                   self.RWTHLila.p(25),
                                                   self.RWTHPetrol.p(25),
                                                   self.RWTHMaiGruen.p(25),
                                                   self.RWTHTuerkis.p(25),
                                                   self.RWTHBlau.p(10),
                                                   self.RWTHOrange.p(10),
                                                   self.RWTHGruen.p(10),
                                                   self.RWTHRot.p(10),
                                                   self.RWTHViolett.p(10),
                                                   self.RWTHBordeaux.p(10),
                                                   self.RWTHLila.p(10),
                                                   self.RWTHPetrol.p(10),
                                                   self.RWTHMaiGruen.p(10),
                                                   self.RWTHTuerkis.p(10),
                                                   ])

        if cycle == 'default':
            plt.rcParams["axes.prop_cycle"] = self.rwth_color_cycle
        elif cycle == 'full':
            plt.rcParams["axes.prop_cycle"] = self.rwth_full_color_cycle
        else:
            raise ValueError('Unknown cycle setting {}'.format(cycle))

        self.frmt = frmt

        self.cmaps = {'rwth-viridis': LinearSegmentedColormap.from_list('rwth-viridis',
                                                                        [(0, self.RWTHViolett.p(100, 'NRGB')),
                                                                         (0.25, self.RWTHTuerkis.p(100, 'NRGB')),
                                                                         (0.75, self.RWTHMaiGruen.p(100, 'NRGB')),
                                                                         (1, self.RWTHGelb.p(100, 'NRGB'))],
                                                                        N=256)}

    @property
    def frmt(self):
        return self._frmt

    @frmt.setter
    def frmt(self, frmt: str = "HEX"):
        if frmt not in ["HEX", "RGB", "NRGB"]:
            raise ValueError("frmt must be HEX, NRGB or RGB not %s" % frmt)

        self._frmt = frmt

        RWTHBlau.frmt = frmt
        RWTHSchwarz.frmt = frmt
        RWTHMagenta.frmt = frmt
        RWTHGelb.frmt = frmt
        RWTHPetrol.frmt = frmt
        RWTHTuerkis.frmt = frmt
        RWTHGruen.frmt = frmt
        RWTHMaiGruen.frmt = frmt
        RWTHOrange.frmt = frmt
        RWTHRot.frmt = frmt
        RWTHBordeaux.frmt = frmt
        RWTHViolett.frmt = frmt
        RWTHLila.frmt = frmt

    @classmethod
    def plot_color_palette(cls):
        fig, ax = plt.subplots(1, 1, figsize=(5, 5), dpi=300)

        for y, c in enumerate(ColorManager.color_list):
            for x, shade in zip([1, 2, 3, 4, 5], [100, 75, 50, 25, 10]):
                ax.scatter(x, y + 1, c=c.p(shade), s=150)

        ylabels = [c.__class__.__name__ for c in ColorManager.color_list]

        ax.set_xticks([1, 2, 3, 4, 5], ["100 %", "75 %", "50 %", "25 %", "10 %"], rotation=45)
        ax.set_yticks(list(range(1, 14)), ylabels, rotation=45)

        plt.tight_layout()
        return fig, ax
