from nose.tools import *

from machikoro.constant import CardType, CardSymbol, CardExpansion
from machikoro.card import Card


def test_equal():
    assert_equals(Card.WHEAT_FIELD, CardExpansion.BASE)
    assert_equals(Card.WHEAT_FIELD, CardType.PRIMARY_INDUSTRY)
    assert_equals(Card.WHEAT_FIELD, CardType.BLUE)
    assert_equals(Card.WHEAT_FIELD, CardSymbol.GRAIN)
    assert_equals(Card.WHEAT_FIELD, 1)
    assert_not_equals(CardType.SECONDARY_INDUSTRY, Card.WHEAT_FIELD)
