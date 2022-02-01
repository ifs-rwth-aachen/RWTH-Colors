from RWTHColors import ColorManager as cm
from RWTHColors.colors import RWTHRot


def test_color_manager():
    my_cm = cm()

    assert RWTHRot.HEX[100] == my_cm.RWTHRot.p(100)

    my_cm.frmt = "RGB"

    assert RWTHRot.RGB[100] == my_cm.RWTHRot.p(100)

    my_cm.frmt = "HEX"

    assert RWTHRot.HEX[100] == my_cm.RWTHRot.p(100)
