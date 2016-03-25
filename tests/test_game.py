from nose.tools import *

from machikoro import *
import copy


def test_game_player():
    player1 = RandomPlayer()
    player2 = RandomPlayer()
    player3 = RandomPlayer()
    player4 = RandomPlayer()
    game = Game([player1, player2, player3, player4], UnlimitedSupply())
    assert_equal(game.player(), player1)
    assert_list_equal(game.players(), [player1, player2, player3, player4])
    assert_list_equal(game.opponents(), [player4, player3, player2])
    assert_list_equal(game.neighbors(), [player4, player3, player2])


def test_game_copy():
    player1 = RandomPlayer()
    player2 = RandomPlayer()
    player3 = RandomPlayer()
    player4 = RandomPlayer()
    game = Game([player1, player2, player3, player4], UnlimitedSupply())
    game2 = copy.deepcopy(game)
    assert_equal(game.money(player1), game2.money(player1))
    assert_equal(game2.player(), player1)
