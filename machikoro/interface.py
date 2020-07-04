#!/usr/bin/env python

import random

from abc import ABCMeta, abstractmethod
from enum import Enum

from .constant import CardExpansion, CardSymbol, CardType


class CardInterface(Enum):
    def __init__(self, expansion, type_, symbol, cost, activation, effect):
        self.expansion = expansion
        self.type = type_
        self.symbol = symbol
        self.cost = cost
        self.activation = activation
        self.effect = effect

    def __eq__(self, other):
        if isinstance(other, CardExpansion):
            return self.expansion == other
        elif isinstance(other, CardType):
            return self.type == other
        elif isinstance(other, CardSymbol):
            return self.symbol == other
        elif isinstance(other, list):
            if other[0] == "!":
                return self != other[1]
            elif other[0] == "|":
                return self in other[1:]
            elif other[0] == "&":
                return False not in [self == x for x in other[1:]]
            else:
                return NotImplemented
        elif isinstance(other, int):
            return self.activation and other in self.activation
        else:
            return other is self

    def __hash__(self):
        return hash(self._name_)

    def __copy__(self):
        return self

    def __deepcopy__(self, memo={}):
        memo[id(self)] = self
        return self


class EffectInterface(metaclass=ABCMeta):
    @abstractmethod
    def __call__(self, card, owner, game):
        pass


class ContainerInterface(metaclass=ABCMeta):
    @abstractmethod
    def _list(self):
        pass

    def list(self, attributes=None):
        result = self._list()
        if attributes is not None:
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
        assert isinstance(card, CardInterface), "card is not a Card: %r" % card
        self._add(card)


class PlayerInterface(metaclass=ABCMeta):
    def __copy__(self):
        return self

    def __deepcopy__(self, memo={}):
        memo[id(self)] = self
        return self

    @abstractmethod
    def build(self, game, cards):
        pass

    @abstractmethod
    def decide(self, card, game, answers=None):
        pass
