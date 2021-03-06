#!/usr/bin/env python

from .card import BASEDECK, Card
from .constant import CardSymbol, CardType
from .interface import ContainerInterface


class UnlimitedSupply(ContainerInterface):
    def __init__(self, cards=BASEDECK):
        self.cards = []
        for card in cards:
            self.add(card)

    def _list(self):
        return self.cards

    def _count(self, card):
        return 1 if card in self.cards else 0

    def _remove(self, card):
        return card if card in self.cards else None

    def _add(self, card):
        if card not in self.cards:
            self.cards.append(card)


class LimitedSupply(ContainerInterface):
    def __init__(
        self, cards=BASEDECK, player_count=4, stock_count=6,
    ):
        self.cards = {}
        for card in cards:
            if card == CardSymbol.LANDMARK:
                for _ in range(player_count):
                    self.add(card)
            else:
                for _ in range(stock_count):
                    self.add(card)

    def _list(self):
        return [card for card, count_ in self.cards.items() if count_ > 0]

    def _count(self, card):
        return self.cards.get(card, 0)

    def _remove(self, card):
        self.cards[card] -= 1
        return card

    def _add(self, card):
        self.cards[card] = self.cards.get(card, 0) + 1


class TilesMarket(ContainerInterface):
    def __init__(
        self,
        supply,
        tiles=[
            [2, CardType.MAJOR_ESTABLISHMENT],
            [4, ["|", 1, 2, 3, 4, 5, 6]],
            [4, None],
        ],
    ):
        self.supply = supply
        self.tiles = [x + [LimitedSupply([])] for x in tiles]
        self.__assure_tiles()

    def _list(self):
        result = self.supply.list(CardType.LANDMARK)
        for _, _, tile in self.tiles:
            result.extend(tile._list())
        return result

    def _count(self, card):
        if card == CardType.LANDMARK:
            return self.supply._count(card)
        else:
            for _, _, tile in self.tiles:
                if card in tile:
                    return tile._count(card)

    def _remove(self, card):
        result = None
        if card == CardType.LANDMARK:
            result = self.supply._remove(card)
        else:
            for _, _, tile in self.tiles:
                if card in tile:
                    result = tile._remove(card)
                    break
            self.__assure_tiles()
        return result

    def _add(self, card):
        if card == CardType.LANDMARK:
            self.supply._add(card)
        else:
            for _, selector, tile in self.tiles:
                if not selector or card == selector:
                    tile._add(card)
                    break

    def __assure_tiles(self):
        remains = self.supply.list(["!", CardType.LANDMARK])
        for count_, selector, tile in self.tiles:
            if selector:
                using = [card for card in remains if card == selector]
                remains = [card for card in remains if card not in using]
            else:
                using = remains
                remains = []
            while using and (len(tile._list()) < count_):
                self.add(self.supply.remove(["|"] + list(using)))
                using = self.supply.list(["|"] + list(using))


class Tableau(ContainerInterface):
    __ATTRIBUTE_COUNT = "count"

    def __init__(self, money=3, cards=[Card.WHEAT_FIELD, Card.BAKERY]):
        self._money = money
        self.cards = {}
        for card in cards:
            self.add(card)

    def _list(self):
        return [card for card in self.cards if self._count(card) > 0]

    def _count(self, card):
        return self.cards[card].get(Tableau.__ATTRIBUTE_COUNT, 0)

    def _remove(self, card):
        self.cards[card][Tableau.__ATTRIBUTE_COUNT] -= 1
        return card

    def _add(self, card):
        if card in self.cards:
            self.cards[card][Tableau.__ATTRIBUTE_COUNT] += 1
        else:
            self.cards[card] = {Tableau.__ATTRIBUTE_COUNT: 1}

    def money(self, diff=None):
        if diff is None:
            return self._money
        else:
            diff = max(diff, -self._money)
            self._money += diff
            return -diff
