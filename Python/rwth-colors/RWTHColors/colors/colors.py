from abc import ABC, abstractmethod


class Color(ABC):
    frmt = "HEX"

    def __init__(self, frmt: str = "HEX"):
        if frmt not in ["HEX", "RGB", "NRGB"]:
            raise ValueError("frmt must be HEX, NRGB or RGB not %s" % frmt)

        self.frmt = frmt

    @property
    @abstractmethod
    def HEX(self) -> dict:
        pass

    @property
    @abstractmethod
    def RGB(self) -> dict:
        pass

    @classmethod
    def power(cls, p: int = 100, frmt: str = None):
        if not frmt:
            frmt = cls.frmt

        if p not in [10, 25, 50, 75, 100]:
            raise ValueError("Power must be 10, 25, 50, 75 or 100 but not %d" % p)

        if frmt == "HEX":
            return cls.HEX[p]
        elif frmt == "NRGB":
            c = tuple(el / 255 for el in cls.RGB[p])
            return c
        elif frmt == "RGB":
            return cls.RGB[p]
        else:
            raise ValueError("Unsupported frmt %s" % frmt)

    @classmethod
    def p(cls, p: int = 100, frmt: str = None):
        return cls.power(p, frmt)


class RWTHBlau(Color):
    HEX = {100: '#00549F',
           75: '#407FB7',
           50: '#8EBAE5',
           25: '#C7DDF2',
           10: '#E8F1FA'}

    RGB = {100: (0, 84, 159),
           75: (64, 127, 183),
           50: (142, 186, 229),
           25: (199, 221, 242),
           10: (232, 241, 250)}


class RWTHSchwarz(Color):
    HEX = {100: '#000000',
           75: '#646567',
           50: '#9C9E9F',
           25: '#CFD1D2',
           10: '#ECEDED'}

    RGB = {100: (0, 0, 0),
           75: (100, 101, 103),
           50: (156, 158, 159),
           25: (207, 209, 210),
           10: (236, 237, 237)}


class RWTHMagenta(Color):
    HEX = {100: '#E30066',
           75: '#E96088',
           50: '#F19EB1',
           25: '#F9D2DA',
           10: '#FDEEF0'}

    RGB = {100: (227, 0, 102),
           75: (233, 96, 136),
           50: (241, 158, 177),
           25: (249, 210, 218),
           10: (253, 238, 240)}


class RWTHGelb(Color):
    HEX = {100: '#FFED00',
           75: '#FFF055',
           50: '#FFF59B',
           25: '#FFFAD1',
           10: '#FFFDEE'}

    RGB = {100: (255, 237, 0),
           75: (255, 240, 85),
           50: (255, 245, 155),
           25: (255, 250, 209),
           10: (255, 253, 238)}


class RWTHPetrol(Color):
    HEX = {100: '#006165',
           75: '#2D7F83',
           50: '#7DA4A7',
           25: '#BFD0D1',
           10: '#E6ECEC'}

    RGB = {100: (0, 97, 101),
           75: (45, 127, 131),
           50: (125, 164, 167),
           25: (191, 208, 209),
           10: (230, 236, 236)}


class RWTHTuerkis(Color):
    HEX = {100: '#0098A1',
           75: '#00B1B7',
           50: '#89CCCF',
           25: '#CAE7E7',
           10: '#EBF6F6'}

    RGB = {100: (0, 152, 161),
           75: (0, 177, 183),
           50: (137, 204, 207),
           25: (202, 231, 231),
           10: (235, 246, 246)}


class RWTHGruen(Color):
    HEX = {100: '#57AB27',
           75: '#8DC060',
           50: '#B8D698',
           25: '#DDEBCE',
           10: '#F2F7EC'}

    RGB = {100: (87, 171, 39),
           75: (141, 192, 96),
           50: (184, 214, 152),
           25: (221, 235, 206),
           10: (242, 247, 236)}


class RWTHMaiGruen(Color):
    HEX = {100: '#BDCD00',
           75: '#D0D95C',
           50: '#E0E69A',
           25: '#F0F3D0',
           10: '#F9FAED'}

    RGB = {100: (189, 205, 0),
           75: (208, 217, 92),
           50: (224, 230, 154),
           25: (240, 243, 208),
           10: (249, 250, 237)}


class RWTHOrange(Color):
    HEX = {100: '#F6A800',
           75: '#FABE50',
           50: '#FDD48F',
           25: '#FEEAC9',
           10: '#FFF7EA'}

    RGB = {100: (246, 168, 0),
           75: (250, 190, 80),
           50: (253, 212, 143),
           25: (254, 234, 201),
           10: (255, 247, 234)}


class RWTHRot(Color):
    HEX = {100: '#CC071E',
           75: '#D85C41',
           50: '#E69679',
           25: '#F3CDBB',
           10: '#FAEBE3'}

    RGB = {100: (204, 7, 30),
           75: (216, 92, 65),
           50: (230, 150, 121),
           25: (243, 205, 187),
           10: (250, 235, 227)}


class RWTHBordeaux(Color):
    HEX = {100: '#A11035',
           75: '#B65256',
           50: '#CD8B87',
           25: '#E5C5C0',
           10: '#F5E8E5'}

    RGB = {100: (161, 16, 53),
           75: (182, 82, 86),
           50: (205, 139, 135),
           25: (229, 197, 192),
           10: (245, 232, 229)}


class RWTHViolett(Color):
    HEX = {100: '#612158',
           75: '#834E75',
           50: '#A8859E',
           25: '#D2C0CD',
           10: '#EDE5EA'}

    RGB = {100: (97, 33, 88),
           75: (131, 78, 117),
           50: (168, 133, 158),
           25: (210, 192, 205),
           10: (237, 229, 234)}


class RWTHLila(Color):
    HEX = {100: '#7A6FAC',
           75: '#9B91C1',
           50: '#BCB5D7',
           25: '#DEDAEB',
           10: '#F2F0F7'}

    RGB = {100: (122, 111, 172),
           75: (155, 145, 193),
           50: (188, 181, 215),
           25: (222, 218, 235),
           10: (242, 240, 247)}
