from machikoro.constant import CardExpansion, CardSymbol, CardType
from nose.tools import assert_equals, assert_not_equals


def test_colors():
    assert_equals(CardType.PRIMARY_INDUSTRY, CardType.BLUE)
    assert_equals(CardType.SECONDARY_INDUSTRY, CardType.GREEN)
    assert_equals(CardType.RESTAURANT, CardType.RED)
    assert_equals(CardType.MAJOR_ESTABLISHMENT, CardType.PURPLE)


def test_enum_differs():
    assert_not_equals(CardType.BLUE, CardExpansion.BASE)
    assert_not_equals(CardType.BLUE, CardSymbol.GRAIN)
