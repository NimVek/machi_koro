import copy

from machikoro.container import UnlimitedSupply
from machikoro.game import Game
from machikoro.player import RandomPlayer


def test_game_player():
    player1 = RandomPlayer()
    player2 = RandomPlayer()
    player3 = RandomPlayer()
    player4 = RandomPlayer()
    game = Game([player1, player2, player3, player4], UnlimitedSupply())
    assert game.player() == player1
    assert game.players() == [player1, player2, player3, player4]
    assert game.opponents() == [player4, player3, player2]
    assert game.neighbors() == [player4, player3, player2]


def test_game_copy():
    player1 = RandomPlayer()
    player2 = RandomPlayer()
    player3 = RandomPlayer()
    player4 = RandomPlayer()
    game = Game([player1, player2, player3, player4], UnlimitedSupply())
    game2 = copy.deepcopy(game)
    assert game.money(player1) == game2.money(player1)
    assert game2.player() == player1
