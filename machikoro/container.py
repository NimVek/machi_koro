#!/usr/bin/env python

from .constant import CardExpansion
from .card import Card

from abc import ABCMeta, abstractmethod
import random

class ContainerInterface(metaclass=ABCMeta):
    @abstractmethod
    def _list(self):
        pass

    def list(self, attributes=None):
        result = self._list()
        if not attributes is None:
            result = [card for card in result if card == attributes]
        return result

    @abstractmethod
    def _count(self, card):
        pass

    def count(self, attributes=None):
        return sum(self._count(x) for x in self.list(attributes))

    def __contains__(self, attributes):
        return self.count(attributes) > 0

    @abstractmethod
    def _remove(self, card):
        pass

    def remove(self, attributes=None):
        count_ = self.count(attributes)
        if count_ > 0:
            index_ = random.randrange(count_)
            for card in self.list(attributes):
                if index_ > self._count(card):
                    index_ -= self._count(card)
                else:
                    return self._remove(card)
        else:
            raise KeyError(attributes)

    @abstractmethod
    def _add(self, card):
        pass

    def add(self, card):
        assert isinstance(card, Card), "card is not a Card: %r" % card
        self._add(card)


class UnlimitedSupply(ContainerInterface):
    def __init__(self,
                 cards=[card for card in Card if card == CardExpansion.BASE]):
        self.cards = cards

    def _list(self):
        return self.cards

    def _count(self, card):
        return 1 if card in self.cards else 0

    def _remove(self, card):
        return card if card in self.cards else None

    def _add(self, card):
        if not card in self.cards:
            self.cards.append(card)
