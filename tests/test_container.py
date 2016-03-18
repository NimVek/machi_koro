from nose.tools import *

from machikoro import *


def test_unlimited_supply_count():
    supply = UnlimitedSupply([Card.WHEAT_FIELD, Card.CAFE, Card.MINE,
                              Card.BAKERY])
    assert_equals(supply.count(), 4)
    assert_equals(supply.count(CardType.BLUE), 2)
    assert_equals(supply.count(CardType.GREEN), 1)
    assert_equals(supply.count(CardType.RED), 1)
    assert_equals(supply.count(CardType.PURPLE), 0)


def test_unlimited_supply_remove():
    supply = UnlimitedSupply([Card.WHEAT_FIELD, Card.CAFE, Card.MINE,
                              Card.BAKERY])
    assert_equals(supply.count(CardType.RED), 1)
    assert_equals(supply.remove(CardType.RED), Card.CAFE)
    assert_equals(supply.count(CardType.RED), 1)
    assert_equals(supply.count(Card.MINE), 1)
    assert_equals(supply.remove(Card.MINE), Card.MINE)
    assert_equals(supply.count(Card.MINE), 1)
    assert_equals(supply.count(CardType.BLUE), 2)
    assert_in(supply.remove(CardType.BLUE), [Card.WHEAT_FIELD, Card.MINE])
    assert_equals(supply.count(CardType.BLUE), 2)
    assert_in(supply.remove(), [Card.WHEAT_FIELD, Card.MINE, Card.CAFE,
                                Card.BAKERY])
    assert_equals(
        supply.remove(['|', CardType.RED, CardType.LANDMARK]), Card.CAFE)
    assert_raises(KeyError, supply.remove, CardType.PURPLE)


def test_unlimited_supply_add():
    supply = UnlimitedSupply([Card.WHEAT_FIELD, Card.CAFE])
    assert_equals(supply.count(), 2)
    supply.add(Card.CAFE)
    assert_equals(supply.count(), 2)
    assert_equals(supply.count(CardType.BLUE), 1)
    supply.add(Card.MINE)
    assert_equals(supply.count(CardType.BLUE), 2)
    assert_raises(AssertionError, supply.add, CardType.PURPLE)

def test_limited_supply_count():
    supply = LimitedSupply([Card.WHEAT_FIELD, Card.CAFE, Card.MINE,
                              Card.STADIUM, Card.STATION], 2, 3)
    assert_equals(supply.count(), 13)
    assert_equals(supply.count(CardType.BLUE), 6)
    assert_equals(supply.count(CardType.GREEN), 0)
    assert_equals(supply.count(CardType.RED), 3)
    assert_equals(supply.count(CardType.PURPLE), 2)
    assert_equals(supply.count(CardType.LANDMARK), 2)
