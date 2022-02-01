from RWTHColors.colors import *


class ColorManager:
    def __init__(self, frmt: str = "HEX"):
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
