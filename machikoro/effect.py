#!/usr/bin/env python

import machikoro.card

from .constant import CURRENT_PLAYER, CardSymbol, CardType
from .interface import EffectInterface


class NotImplementedEffect(EffectInterface):
    def __call__(self, card, owner, game):
        raise NotImplementedError(card)


class GeneralIncome(EffectInterface):
    def __init__(self, base, multiply=None, required=None):
        self.base = base
        self.multiply = multiply
        self.required = required

    def __call__(self, card, owner, game):
        if not self.required or game.list(owner, self.required):
            value = self.base
            if self.multiply:
                value *= game.count(owner, self.multiply)
            if card in [CardSymbol.CUP, CardSymbol.SHOP] and game.list(
                owner, machikoro.card.Card.SHOPPING_MALL
            ):
                value += 1
            if card == CardType.RED:
                value = game.money(CURRENT_PLAYER, -value)
            game.money(owner, value)


class StadiumEffect(EffectInterface):
    def __call__(self, card, owner, game):
        for other in game.opponents(owner):
            game.money(owner, game.money(other, -2))


class TVStationEffect(EffectInterface):
    def __call__(self, card, owner, game):
        other = owner.decide(card, game, game.opponents(owner))
        game.money(owner, game.money(other, -5))


class BusinessCentreEffect(EffectInterface):
    def __call__(self, card, owner, game):
        own_card, other, other_card = owner.decide(card, game)
        game.add(other, game.remove(owner, own_card))
        game.add(owner, game.remove(other, other_card))
