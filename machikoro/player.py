#!/usr/bin/env python

import random
from copy import deepcopy

from .card import Card
from .constant import DICE_GAME
from .interface import PlayerInterface
from .rules import Rules


class RandomPlayer(PlayerInterface):
    def build(self, game, cards):
        return random.choice(cards + [None])

    def decide(self, card, game, answers=None):
        if answers:
            return random.choice(answers)
        else:
            raise NotImplementedError(card)


class AdvancedPlayer(RandomPlayer):
    def decide(self, card, game, answers=None):
        if card == Card.STATION:
            for i in range(1, 15):
                test = deepcopy(game)
                test.dices(DICE_GAME, {i})
                Rules.Phase.earn_income(test)
            raise NotImplementedError(card)
        else:
            return super(AdvancedPlayer, self).decide(card, game, answers)
