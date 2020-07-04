import copy

import pytest

from machikoro.card import Card
from machikoro.constant import CardSymbol, CardType
from machikoro.container import LimitedSupply, Tableau, TilesMarket, UnlimitedSupply


def test_unlimited_supply_count():
    supply = UnlimitedSupply([Card.WHEAT_FIELD, Card.CAFE, Card.MINE, Card.BAKERY])
    assert supply.count() == 4
    assert supply.count(CardType.BLUE) == 2
    assert supply.count(CardType.GREEN) == 1
    assert supply.count(CardType.RED) == 1
    assert supply.count(CardType.PURPLE) == 0


def test_unlimited_supply_remove():
    supply = UnlimitedSupply([Card.WHEAT_FIELD, Card.CAFE, Card.MINE, Card.BAKERY])
    assert supply.count(CardType.RED) == 1
    assert supply.remove(CardType.RED) == Card.CAFE
    assert supply.count(CardType.RED) == 1
    assert supply.count(Card.MINE) == 1
    assert supply.remove(Card.MINE) == Card.MINE
    assert supply.count(Card.MINE) == 1
    assert supply.count(CardType.BLUE) == 2
    assert supply.remove(CardType.BLUE) in [Card.WHEAT_FIELD, Card.MINE]
    assert supply.count(CardType.BLUE) == 2
    assert supply.remove() in [Card.WHEAT_FIELD, Card.MINE, Card.CAFE, Card.BAKERY]
    assert supply.remove(["|", CardType.RED, CardType.LANDMARK]) == Card.CAFE
    with pytest.raises(KeyError):
        supply.remove(CardType.PURPLE)


def test_unlimited_supply_add():
    supply = UnlimitedSupply([Card.WHEAT_FIELD, Card.CAFE])
    assert supply.count() == 2
    supply.add(Card.CAFE)
    assert supply.count() == 2
    assert supply.count(CardType.BLUE) == 1
    supply.add(Card.MINE)
    assert supply.count(CardType.BLUE) == 2
    with pytest.raises(AssertionError):
        supply.add(CardType.PURPLE)


def test_limited_supply_count():
    supply = LimitedSupply(
        [Card.WHEAT_FIELD, Card.CAFE, Card.MINE, Card.STADIUM, Card.STATION], 2, 3
    )
    assert supply.count() == 13
    assert supply.count(CardType.BLUE) == 6
    assert supply.count(CardType.GREEN) == 0
    assert supply.count(CardType.RED) == 3
    assert supply.count(CardType.PURPLE) == 2
    assert supply.count(CardType.LANDMARK) == 2


def test_limited_supply_remove():
    supply = LimitedSupply(
        [Card.WHEAT_FIELD, Card.CAFE, Card.MINE, Card.STADIUM, Card.STATION], 2, 3
    )
    assert supply.count(CardType.RED) == 3
    assert supply.remove(CardType.RED) == Card.CAFE
    assert supply.count(CardType.RED) == 2
    assert supply.remove(CardType.RED) == Card.CAFE
    assert supply.count(CardType.RED) == 1
    assert supply.remove(CardType.RED) == Card.CAFE
    assert supply.count(CardType.RED) == 0
    with pytest.raises(KeyError):
        supply.remove(CardType.RED)

    assert supply.count(CardType.BLUE) == 6
    assert supply.remove(CardType.BLUE) in [Card.WHEAT_FIELD, Card.MINE]
    assert supply.count(CardType.BLUE) == 5
    assert supply.count(Card.STADIUM) == 2
    assert supply.remove(Card.STADIUM) == Card.STADIUM
    assert supply.count(Card.STADIUM) == 1

    assert supply.remove() in [Card.WHEAT_FIELD, Card.MINE, Card.STADIUM, Card.STATION]
    assert supply.remove(["&", CardType.BLUE, CardSymbol.GEAR]) == Card.MINE
    with pytest.raises(KeyError):
        supply.remove(["&", CardType.RED, CardSymbol.GEAR])


def test_limited_supply_add():
    supply = LimitedSupply([Card.WHEAT_FIELD, Card.CAFE, Card.STATION], 2)
    assert supply.count() == 14
    supply.add(Card.CAFE)
    assert supply.count() == 15
    assert supply.count(CardType.BLUE) == 6
    supply.add(Card.MINE)
    assert supply.count(CardType.BLUE) == 7
    with pytest.raises(AssertionError):
        supply.add(CardType.PURPLE)


def test_tiles_market_count():
    supply = LimitedSupply()
    assert supply.count(CardType.BLUE) == 30
    assert supply.count(CardType.GREEN) == 30
    assert supply.count(CardType.RED) == 12
    assert supply.count(CardType.PURPLE) == 12
    assert supply.count() == 100
    market = TilesMarket(supply)
    assert len(market.list()) == 14
    assert len(market.list(CardType.LANDMARK)) == 4
    assert len(market.list(CardType.PURPLE)) == 2
    assert (
        len(
            market.list(
                [
                    "&",
                    ["|", CardType.BLUE, CardType.RED, CardType.GREEN],
                    ["|", 1, 2, 3, 4, 5, 6],
                ]
            )
        )
        == 4
    )
    assert (
        len(
            market.list(
                [
                    "&",
                    ["|", CardType.BLUE, CardType.RED, CardType.GREEN],
                    ["|", 7, 8, 9, 10, 11, 12, 13, 14],
                ]
            )
        )
        == 4
    )
    assert supply.count(CardType.BLUE) + market.count(CardType.BLUE) == 30
    assert supply.count(CardType.GREEN) + market.count(CardType.GREEN) == 30
    assert supply.count(CardType.RED) + market.count(CardType.RED) == 12
    assert supply.count(CardType.PURPLE) + market.count(CardType.PURPLE) == 12
    assert market.count(CardType.LANDMARK) == 16
    assert market.count(CardType.LANDMARK) == supply.count(CardType.LANDMARK)


def test_tiles_market_remove():
    supply = LimitedSupply()
    market = TilesMarket(supply)
    for i in range(7):
        assert supply.count(CardType.PURPLE) + market.count(CardType.PURPLE) == 12 - i
        assert len(market.list(CardType.PURPLE)) == 2
        assert market.remove(CardType.PURPLE) in [
            Card.STADIUM,
            Card.TV_STATION,
            Card.BUSINESS_CENTRE,
        ]
        assert len(market.list(CardType.PURPLE)) == 2
        assert (
            supply.count(CardType.PURPLE) + market.count(CardType.PURPLE) == 12 - i - 1
        )
    for i in range(4):
        assert market.remove(CardType.PURPLE) in [
            Card.STADIUM,
            Card.TV_STATION,
            Card.BUSINESS_CENTRE,
        ]
        assert (
            supply.count(CardType.PURPLE) + market.count(CardType.PURPLE) == 5 - i - 1
        )
    assert supply.count(CardType.PURPLE) == 0
    assert len(market.list(CardType.PURPLE)) == 1
    assert market.remove(CardType.PURPLE) in [
        Card.STADIUM,
        Card.TV_STATION,
        Card.BUSINESS_CENTRE,
    ]
    assert len(market.list(CardType.PURPLE)) == 0
    assert market.count(CardType.PURPLE) == 0
    with pytest.raises(KeyError):
        supply.remove(CardType.PURPLE)


def test_tiles_market_add():
    supply = LimitedSupply(
        [
            Card.WHEAT_FIELD,
            Card.CAFE,
            Card.STADIUM,
            Card.TV_STATION,
            Card.BUSINESS_CENTRE,
            Card.STATION,
        ],
        2,
    )
    market = TilesMarket(supply)
    assert len(market.list(CardType.PURPLE)) == 2
    market.add(Card.STADIUM)
    market.add(Card.TV_STATION)
    market.add(Card.BUSINESS_CENTRE)
    assert len(market.list(CardType.PURPLE)) == 3
    assert len(market.list(CardType.LANDMARK)) == 1
    assert market.count(CardType.LANDMARK) == 2
    market.add(Card.RADIO_TOWER)
    assert len(market.list(CardType.LANDMARK)) == 2
    assert market.count(CardType.LANDMARK) == 3


def test_tableau_money():
    tableau = Tableau(5)
    assert tableau.money() == 5
    assert tableau.money(-3) == 3
    assert tableau.money() == 2
    assert tableau.money(-4) == 2
    assert tableau.money() == 0
    assert tableau.money(2) == -2
    assert tableau.money() == 2


def test_tableau_copy():
    tableau = Tableau(2, [Card.WHEAT_FIELD, Card.WHEAT_FIELD])
    assert tableau.money() == 2
    assert tableau.count(Card.WHEAT_FIELD) == 2
    tableau2 = copy.deepcopy(tableau)
    assert tableau.money() == tableau2.money()
    assert tableau.count(Card.WHEAT_FIELD) == tableau2.count(Card.WHEAT_FIELD)
    tableau2.money(12)
    assert tableau2.money() == 14
    tableau2.remove(Card.WHEAT_FIELD)
    assert tableau2.count(Card.WHEAT_FIELD) == 1
    assert tableau.money() == 2
    assert tableau.count(Card.WHEAT_FIELD) == 2
    assert tableau.money() != tableau2.money()
    assert tableau.count(Card.WHEAT_FIELD) != tableau2.count(Card.WHEAT_FIELD)
