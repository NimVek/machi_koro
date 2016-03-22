from nose.tools import *

from machikoro import *


def test_random_game():
    player = RandomPlayer()
    game = Game([player], LimitedSupply([card
                                         for card in Card
                                         if card == CardExpansion.BASE and card
                                         != CardType.PURPLE]))
    assert_equal(Rules.evaluate(game), player)
