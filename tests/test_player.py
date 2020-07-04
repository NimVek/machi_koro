from machikoro.card import Card
from machikoro.player import RandomPlayer
from nose.tools import assert_in, assert_raises


def test_random_player():
    player = RandomPlayer()
    assert_in(
        player.build(None, [Card.STATION, Card.CAFE]), [Card.STATION, Card.CAFE, None]
    )
    assert_in(player.decide(Card.CAFE, None, [True, False]), [True, False])
    assert_raises(NotImplementedError, player.decide, Card.STADIUM, None)
