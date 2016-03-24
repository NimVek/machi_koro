from nose.tools import *

from machikoro import *
from machikoro.effect import *


def test_not_implemented():
    effect = NotImplementedEffect()
    assert_raises(NotImplementedError, effect, None, None, None)


def test_general_income_base():
    effect = GeneralIncome(1)
    player = RandomPlayer()
    game = Game([player], UnlimitedSupply())
    assert_equal(game.money(player), 3)
    effect(Card.WHEAT_FIELD, player, game)
    assert_equal(game.money(player), 4)
    effect(Card.WHEAT_FIELD, player, game)
    assert_equal(game.money(player), 5)
    effect = GeneralIncome(3)
    effect(Card.WHEAT_FIELD, player, game)
    assert_equal(game.money(player), 8)
    effect(Card.WHEAT_FIELD, player, game)
    assert_equal(game.money(player), 11)


def test_general_income_multiplier():
    effect = GeneralIncome(1, CardSymbol.GRAIN)
    player = RandomPlayer()
    game = Game([player], UnlimitedSupply())
    assert_equal(game.count(player, CardSymbol.GRAIN), 1)
    assert_equal(game.money(player), 3)
    effect(Card.WHEAT_FIELD, player, game)
    assert_equal(game.money(player), 4)
    effect(Card.WHEAT_FIELD, player, game)
    assert_equal(game.money(player), 5)
    effect = GeneralIncome(3, CardSymbol.GRAIN)
    effect(Card.WHEAT_FIELD, player, game)
    assert_equal(game.money(player), 8)
    effect(Card.WHEAT_FIELD, player, game)
    assert_equal(game.money(player), 11)
    game.add(player, Card.WHEAT_FIELD)
    assert_equal(game.count(player, CardSymbol.GRAIN), 2)
    effect(Card.WHEAT_FIELD, player, game)
    assert_equal(game.money(player), 17)
    effect(Card.WHEAT_FIELD, player, game)
    assert_equal(game.money(player), 23)
    game.remove(player, Card.WHEAT_FIELD)
    game.remove(player, Card.WHEAT_FIELD)
    effect(Card.WHEAT_FIELD, player, game)
    assert_equal(game.money(player), 23)


def test_general_income_required():
    effect = GeneralIncome(1, None, Card.STATION)
    player = RandomPlayer()
    game = Game([player], UnlimitedSupply())
    assert_equal(game.money(player), 3)
    effect(Card.WHEAT_FIELD, player, game)
    assert_equal(game.money(player), 3)
    game.add(player, Card.STATION)
    effect(Card.WHEAT_FIELD, player, game)
    assert_equal(game.money(player), 4)


def test_general_income_restaurant():
    effect = GeneralIncome(2)
    player1 = RandomPlayer()
    player2 = RandomPlayer()
    game = Game([player1, player2], UnlimitedSupply())
    assert_equal(game.money(player1), 3)
    assert_equal(game.money(player2), 3)
    effect(Card.CAFE, player1, game)
    assert_equal(game.money(player1), 3)
    assert_equal(game.money(player2), 3)
    effect(Card.CAFE, player2, game)
    assert_equal(game.money(player1), 1)
    assert_equal(game.money(player2), 5)
    effect(Card.CAFE, player2, game)
    assert_equal(game.money(player1), 0)
    assert_equal(game.money(player2), 6)
    effect(Card.CAFE, player2, game)
    assert_equal(game.money(player1), 0)
    assert_equal(game.money(player2), 6)


def test_general_income_mall():
    effect = GeneralIncome(1)
    player = RandomPlayer()
    game = Game([player], UnlimitedSupply())
    assert_equal(game.money(player), 3)
    effect(Card.WHEAT_FIELD, player, game)
    assert_equal(game.money(player), 4)
    effect(Card.BAKERY, player, game)
    assert_equal(game.money(player), 5)
    game.add(player, Card.SHOPPING_MALL)
    effect(Card.WHEAT_FIELD, player, game)
    assert_equal(game.money(player), 6)
    effect(Card.BAKERY, player, game)
    assert_equal(game.money(player), 8)


def test_stadium():
    effect = StadiumEffect()
    player1 = RandomPlayer()
    player2 = RandomPlayer()
    player3 = RandomPlayer()
    game = Game([player1, player2, player3], UnlimitedSupply())
    assert_equal(game.money(player1), 3)
    assert_equal(game.money(player2), 3)
    assert_equal(game.money(player3), 3)
    effect(Card.STADIUM, player1, game)
    assert_equal(game.money(player1), 7)
    assert_equal(game.money(player2), 1)
    assert_equal(game.money(player3), 1)
    effect(Card.STADIUM, player1, game)
    assert_equal(game.money(player1), 9)
    assert_equal(game.money(player2), 0)
    assert_equal(game.money(player3), 0)
    effect(Card.STADIUM, player1, game)
    assert_equal(game.money(player1), 9)
    assert_equal(game.money(player2), 0)
    assert_equal(game.money(player3), 0)


def test_tv_station():
    effect = TVStationEffect()
    player1 = RandomPlayer()
    player2 = RandomPlayer()
    game = Game([player1, player2], UnlimitedSupply())
    assert_equal(game.money(player1), 3)
    assert_equal(game.money(player2), 3)
    effect(Card.TV_STATION, player1, game)
    assert_equal(game.money(player1), 6)
    assert_equal(game.money(player2), 0)
    game.money(player2, 7)
    assert_equal(game.money(player2), 7)
    effect(Card.TV_STATION, player1, game)
    assert_equal(game.money(player1), 11)
    assert_equal(game.money(player2), 2)
