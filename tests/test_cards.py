from nose.tools import *

from machikoro.constant import CardType, CardSymbol, CardExpansion
from machikoro.card import Card


def test_equal():
    assert_equals(CardType.PRIMARY_INDUSTRY, Card.WHEAT_FIELD)
    assert_not_equals(CardType.SECONDARY_INDUSTRY, Card.WHEAT_FIELD)
