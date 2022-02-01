from RWTHColors.colors import RWTHRot


def test_rwthrot():
    assert '#CC071E' == RWTHRot.HEX[100]

    assert '#CC071E' == RWTHRot.p(100)
    assert '#CC071E' == RWTHRot.power(100)

    RWTHRot.frmt = "RGB"

    assert (204, 7, 30) == RWTHRot.p(100)
    assert (204, 7, 30) == RWTHRot.power(100)
