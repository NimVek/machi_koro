#!/usr/bin/env python

from abc import ABCMeta, abstractmethod

from .constant import CardSymbol, CardType

#from .card import Card
import machikoro.card


class EffectInterface(metaclass=ABCMeta):
    @abstractmethod
    def __call__(self, card, owner, game):
        pass


class NotImplementedEffect(EffectInterface):
    def __call__(self, card, owner, game):
        raise NotImplementedError(card)


class GeneralIncome(EffectInterface):
    def __init__(self, base, multiply=None, required=None):
        self.base = base
        self.multiply = multiply
        self.required = required

    def __call__(self, card, owner, game):
        if not self.required or game.list(owner, required):
            value = self.base
            if self.multiply:
                value *= game.count(owner, self.multiply)
            if card in [CardSymbol.CUP, CardSymbol.SHOP] and game.list(
                    owner, machikoro.card.Card.SHOPPING_MALL):
                value += 1
            if card == CardType.RED:
                value = game.money(Game.CURRENT_PLAYER, -value)
            game.money(owner, value)
