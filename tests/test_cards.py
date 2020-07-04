from machikoro.card import Card
from machikoro.constant import CardExpansion, CardSymbol, CardType


def test_equal():
    assert Card.WHEAT_FIELD == Card.WHEAT_FIELD
    assert Card.WHEAT_FIELD == CardExpansion.BASE
    assert Card.WHEAT_FIELD == CardType.PRIMARY_INDUSTRY
    assert Card.WHEAT_FIELD == CardType.BLUE
    assert Card.WHEAT_FIELD == CardSymbol.GRAIN
    assert Card.WHEAT_FIELD == 1
    assert Card.WHEAT_FIELD == ["|", 1, 2, 3, 4, 5, 6]
    assert Card.WHEAT_FIELD == [
        "&",
        CardExpansion.BASE,
        CardType.BLUE,
        CardSymbol.GRAIN,
    ]


def test_not_equal():
    assert Card.WHEAT_FIELD != Card.STATION
    assert Card.WHEAT_FIELD == ["!", Card.STATION]
    assert Card.WHEAT_FIELD != CardExpansion.SHARP
    assert Card.WHEAT_FIELD == ["!", CardExpansion.SHARP]
    assert Card.WHEAT_FIELD != CardType.RESTAURANT
    assert Card.WHEAT_FIELD == ["!", CardType.RESTAURANT]
    assert Card.WHEAT_FIELD != CardSymbol.LANDMARK
    assert Card.WHEAT_FIELD == ["!", CardSymbol.LANDMARK]
    assert Card.WHEAT_FIELD != 12
    assert Card.WHEAT_FIELD == ["!", 12]
