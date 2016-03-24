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
