from nose.tools import *

from machikoro import *


def test_equal():
    assert_equals(Card.WHEAT_FIELD, Card.WHEAT_FIELD)
    assert_equals(Card.WHEAT_FIELD, CardExpansion.BASE)
    assert_equals(Card.WHEAT_FIELD, CardType.PRIMARY_INDUSTRY)
    assert_equals(Card.WHEAT_FIELD, CardType.BLUE)
    assert_equals(Card.WHEAT_FIELD, CardSymbol.GRAIN)
    assert_equals(Card.WHEAT_FIELD, 1)
    assert_equals(Card.WHEAT_FIELD, ['|', 1, 2, 3, 4, 5, 6])
    assert_equals(Card.WHEAT_FIELD, ['&', CardExpansion.BASE, CardType.BLUE,
                                     CardSymbol.GRAIN])


def test_not_equal():
    assert_not_equals(Card.WHEAT_FIELD, Card.STATION)
    assert_equals(Card.WHEAT_FIELD, ['!', Card.STATION])
    assert_not_equals(Card.WHEAT_FIELD, CardExpansion.SHARP)
    assert_equals(Card.WHEAT_FIELD, ['!', CardExpansion.SHARP])
    assert_not_equals(Card.WHEAT_FIELD, CardType.RESTAURANT)
    assert_equals(Card.WHEAT_FIELD, ['!', CardType.RESTAURANT])
    assert_not_equals(Card.WHEAT_FIELD, CardSymbol.LANDMARK)
    assert_equals(Card.WHEAT_FIELD, ['!', CardSymbol.LANDMARK])
    assert_not_equals(Card.WHEAT_FIELD, 12)
    assert_equals(Card.WHEAT_FIELD, ['!', 12])
