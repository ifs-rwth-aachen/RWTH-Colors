import matplotlib.pyplot as plt

from RWTHColors.colors import *
from cycler import cycler


class ColorManager:
    def __init__(self, frmt: str = "HEX", cycle='default'):
        if frmt not in ["HEX", "RGB"]:
            raise ValueError("frmt must be HEX or RGB not %s" % frmt)

        self.RWTHBlau = RWTHBlau()
        self.RWTHSchwarz = RWTHSchwarz()
        self.RWTHMagenta = RWTHMagenta()
        self.RWTHGelb = RWTHGelb()
        self.RWTHPetrol = RWTHPetrol()
        self.RWTHTuerkis = RWTHTuerkis()
        self.RWTHGruen = RWTHGruen()
        self.RWTHMaiGruen = RWTHMaiGruen()
        self.RWTHOrange = RWTHOrange()
        self.RWTHRot = RWTHRot()
        self.RWTHBordeaux = RWTHBordeaux()
        self.RWTHViolett = RWTHViolett()
        self.RWTHLila = RWTHLila()

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

    @property
    def frmt(self):
        return self._frmt

    @frmt.setter
    def frmt(self, frmt: str = "HEX"):
        if frmt not in ["HEX", "RGB"]:
            raise ValueError("frmt must be HEX or RGB not %s" % frmt)

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
