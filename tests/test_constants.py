from machikoro.constant import CardExpansion, CardSymbol, CardType


def test_colors():
    assert CardType.PRIMARY_INDUSTRY == CardType.BLUE
    assert CardType.SECONDARY_INDUSTRY == CardType.GREEN
    assert CardType.RESTAURANT == CardType.RED
    assert CardType.MAJOR_ESTABLISHMENT == CardType.PURPLE


def test_enum_differs():
    assert CardType.BLUE != CardExpansion.BASE
    assert CardType.BLUE != CardSymbol.GRAIN
