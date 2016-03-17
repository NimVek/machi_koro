#!/usr/bin/env python

from abc import ABCMeta, abstractmethod
from .card import Card


class ContainerInterface(metaclass=ABCMeta):
    @abstractmethod
    def _list(self):
        pass

    def list(self, attributes=None):
        return [card for card in self._list() if card == attribute]

    @abstractmethod
    def _count(self, card):
        pass

    def count(self, attributes):
        return sum(self._count(x) for x in self.list(attributes))

    def __contains__(self, attributes):
        return self.count(attributes) > 0

    @abstractmethod
    def _remove(self, card):
        pass

    def remove(self, attributes):
        count = self.count(attributes)
        if count > 0:
            index = random.randrange(count)
            for card in self.list(attributes):
                if index > self._count(card):
                    index -= self._count(card)
                else:
                    return self._remove(card)
        else:
            raise KeyError(attributes)

    @abstractmethod
    def _add(self, card):
        pass

    def add(self, card):
        assert isinstance(self, Card), "card is not an Card: %r" % card
        self._add(card)
