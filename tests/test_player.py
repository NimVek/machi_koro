import pytest

from machikoro.card import Card
from machikoro.player import RandomPlayer


def test_random_player():
    player = RandomPlayer()
    assert player.build(None, [Card.STATION, Card.CAFE]) in [
        Card.STATION,
        Card.CAFE,
        None,
    ]
    assert player.decide(Card.CAFE, None, [True, False]) in [True, False]
    with pytest.raises(NotImplementedError):
        player.decide(Card.STADIUM, None)
