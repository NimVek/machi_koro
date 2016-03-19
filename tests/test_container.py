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
    supply = LimitedSupply(
        [Card.WHEAT_FIELD, Card.CAFE, Card.MINE, Card.STADIUM,
         Card.STATION], 2, 3)
    assert_equals(supply.count(), 13)
    assert_equals(supply.count(CardType.BLUE), 6)
    assert_equals(supply.count(CardType.GREEN), 0)
    assert_equals(supply.count(CardType.RED), 3)
    assert_equals(supply.count(CardType.PURPLE), 2)
    assert_equals(supply.count(CardType.LANDMARK), 2)


def test_limited_supply_remove():
    supply = LimitedSupply(
        [Card.WHEAT_FIELD, Card.CAFE, Card.MINE, Card.STADIUM,
         Card.STATION], 2, 3)
    assert_equals(supply.count(CardType.RED), 3)
    assert_equals(supply.remove(CardType.RED), Card.CAFE)
    assert_equals(supply.count(CardType.RED), 2)
    assert_equals(supply.remove(CardType.RED), Card.CAFE)
    assert_equals(supply.count(CardType.RED), 1)
    assert_equals(supply.remove(CardType.RED), Card.CAFE)
    assert_equals(supply.count(CardType.RED), 0)
    assert_raises(KeyError, supply.remove, CardType.RED)

    assert_equals(supply.count(CardType.BLUE), 6)
    assert_in(supply.remove(CardType.BLUE), [Card.WHEAT_FIELD, Card.MINE])
    assert_equals(supply.count(CardType.BLUE), 5)
    assert_equals(supply.count(Card.STADIUM), 2)
    assert_equals(supply.remove(Card.STADIUM), Card.STADIUM)
    assert_equals(supply.count(Card.STADIUM), 1)

    assert_in(supply.remove(), [Card.WHEAT_FIELD, Card.MINE, Card.STADIUM,
                                Card.STATION])
    assert_equals(
        supply.remove(['&', CardType.BLUE, CardSymbol.GEAR]), Card.MINE)
    assert_raises(KeyError, supply.remove, ['&', CardType.RED,
                                            CardSymbol.GEAR])


def test_limited_supply_add():
    supply = LimitedSupply([Card.WHEAT_FIELD, Card.CAFE, Card.STATION], 2)
    assert_equals(supply.count(), 14)
    supply.add(Card.CAFE)
    assert_equals(supply.count(), 15)
    assert_equals(supply.count(CardType.BLUE), 6)
    supply.add(Card.MINE)
    assert_equals(supply.count(CardType.BLUE), 7)
    assert_raises(AssertionError, supply.add, CardType.PURPLE)


def test_tiles_market_count():
    supply = LimitedSupply()
    assert_equals(supply.count(CardType.BLUE), 30)
    assert_equals(supply.count(CardType.GREEN), 30)
    assert_equals(supply.count(CardType.RED), 12)
    assert_equals(supply.count(CardType.PURPLE), 12)
    assert_equals(supply.count(), 100)
    market = TilesMarket(supply)
    assert_equals(len(market.list()), 14)
    assert_equals(len(market.list(CardType.LANDMARK)), 4)
    assert_equals(len(market.list(CardType.PURPLE)), 2)
    assert_equals(
        len(market.list(['&', ['|', CardType.BLUE, CardType.RED, CardType.GREEN
                               ], ['|', 1, 2, 3, 4, 5, 6]])), 4)
    assert_equals(
        len(market.list(['&', ['|', CardType.BLUE, CardType.RED, CardType.GREEN
                               ], ['|', 7, 8, 9, 10, 11, 12, 13, 14]])), 4)
    assert_equals(
        supply.count(CardType.BLUE) + market.count(CardType.BLUE), 30)
    assert_equals(
        supply.count(CardType.GREEN) + market.count(CardType.GREEN), 30)
    assert_equals(supply.count(CardType.RED) + market.count(CardType.RED), 12)
    assert_equals(
        supply.count(CardType.PURPLE) + market.count(CardType.PURPLE), 12)
    assert_equals(market.count(CardType.LANDMARK), 16)
    assert_equals(
        market.count(CardType.LANDMARK), supply.count(CardType.LANDMARK))


def test_tiles_market_remove():
    supply = LimitedSupply()
    market = TilesMarket(supply)
    for i in range(7):
        assert_equals(
            supply.count(CardType.PURPLE) + market.count(CardType.PURPLE),
            12 - i)
        assert_equals(len(market.list(CardType.PURPLE)), 2)
        assert_in(
            market.remove(CardType.PURPLE), [Card.STADIUM, Card.TV_STATION,
                                             Card.BUSINESS_CENTRE])
        assert_equals(len(market.list(CardType.PURPLE)), 2)
        assert_equals(
            supply.count(CardType.PURPLE) + market.count(CardType.PURPLE),
            12 - i - 1)
    for i in range(4):
        assert_in(
            market.remove(CardType.PURPLE), [Card.STADIUM, Card.TV_STATION,
                                             Card.BUSINESS_CENTRE])
        assert_equals(
            supply.count(CardType.PURPLE) + market.count(CardType.PURPLE),
            5 - i - 1)
    assert_equals(supply.count(CardType.PURPLE), 0)
    assert_equals(len(market.list(CardType.PURPLE)), 1)
    assert_in(
        market.remove(CardType.PURPLE), [Card.STADIUM, Card.TV_STATION,
                                         Card.BUSINESS_CENTRE])
    assert_equals(len(market.list(CardType.PURPLE)), 0)
    assert_equals(market.count(CardType.PURPLE), 0)
    assert_raises(KeyError, supply.remove, CardType.PURPLE)


def test_tiles_market_add():
    supply = LimitedSupply(
        [Card.WHEAT_FIELD, Card.CAFE, Card.STADIUM, Card.TV_STATION,
         Card.BUSINESS_CENTRE, Card.STATION], 2)
    market = TilesMarket(supply)
    assert_equals(len(market.list(CardType.PURPLE)), 2)
    market.add(Card.STADIUM)
    market.add(Card.TV_STATION)
    market.add(Card.BUSINESS_CENTRE)
    assert_equals(len(market.list(CardType.PURPLE)), 3)
    assert_equals(len(market.list(CardType.LANDMARK)), 1)
    assert_equals(market.count(CardType.LANDMARK), 2)
    market.add(Card.RADIO_TOWER)
    assert_equals(len(market.list(CardType.LANDMARK)), 2)
    assert_equals(market.count(CardType.LANDMARK), 3)


def test_tableau_money():
    tableau = Tableau(5)
    assert_equals(tableau.money(), 5)
    assert_equals(tableau.money(-3), 3)
    assert_equals(tableau.money(), 2)
    assert_equals(tableau.money(-4), 2)
    assert_equals(tableau.money(), 0)
    assert_equals(tableau.money(2), -2)
    assert_equals(tableau.money(), 2)
