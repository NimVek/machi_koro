#!/usr/bin/env python

import itertools
import random

from copy import deepcopy
from typing import Dict

from .card import Card
from .constant import DICE_GAME, CardSymbol, CardType
from .container import LimitedSupply
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
    def __compute_earnings(self, game):
        result = {}
        for i in range(1, 15):
            tmp = deepcopy(game)
            tmp.dice(DICE_GAME, [i])
            Rules.Phase.earn_income(tmp)
            result[i] = tmp.money(self) - game.money(self)
        return result

    def __compute_outcome(self, game):
        earnings = self.__compute_earnings(game)
        result: Dict[int, float] = {}
        for i in [1, 2]:
            result[i] = 0
            count_ = 0
            for dice in itertools.product([1, 2, 3, 4, 5, 6], repeat=i):
                count_ += 1
                tmp = sum(dice)
                if game.list(self, Card.HARBOUR) and tmp >= 10:
                    """ Add 2 """
                    if earnings[tmp] < earnings[tmp + 2]:
                        tmp += 2
                result[i] += earnings[tmp]
            result[i] /= count_
        if game.list(self, Card.AMUSEMENT_PARK):
            """ Additional Turn """
            result[2] *= 6 / 5
        return result

    def build(self, game, cards):
        if CardType.LANDMARK in cards:
            return CardType.LANDMARK
        else:
            return super(AdvancedPlayer, self).build(game, cards)

    def decide(self, card, game, answers=None):
        if card == Card.STATION:
            """ Dice count """
            outcome = self.__compute_outcome(game)
            return outcome[2] > outcome[1]
        elif card == Card.RADIO_TOWER:
            """ Reroll """
            earning = self.__compute_earnings(game)[game.pip(DICE_GAME)]
            outcome = self.__compute_outcome(game)
            dice_count = len(game.dice(DICE_GAME))
            if dice_count == 2 and game.list(self, Card.AMUSEMENT_PARK):
                if game.dice(DICE_GAME)[0] == game.dice(DICE_GAME)[1]:
                    earning += outcome[dice_count]
            return outcome[dice_count] > earning
        elif card == Card.TV_STATION:
            """ Get 5 bucks from opponent """
            money = -1
            for i in game.opponents(self):
                if game.money(i) > money:
                    money = game.money(i)
                    result = [i]
                elif game.money(i) == money:
                    result.append(i)
            return random.choice(result)
        elif card == Card.BUSINESS_CENTRE:
            tmp = deepcopy(game)
            tmp.market = LimitedSupply([])
            while tmp.count(self, ["!", CardSymbol.LANDMARK]) > 0:
                c = tmp.remove(self, ["!", CardSymbol.LANDMARK])
                tmp.money(self, c.cost)
                tmp.add("market", c)
            while tmp.count("market") > 1:
                c = tmp.remove("market", self.build(tmp, tmp.list("market")))
                tmp.money(self, -c.cost)
                tmp.add(self, c)
            own_card = tmp.list("market")[0]
            tmp.market = LimitedSupply([])
            for i in game.opponents(self):
                for c in tmp.list(i, ["!", CardSymbol.LANDMARK]):
                    for _ in range(tmp.count(i, c)):
                        tmp.add("market", c)
            other_card = self.build(tmp, tmp.list("market"))
            count_ = -1
            for i in game.opponents(self):
                if tmp.count(i, other_card) > count_:
                    count_ = tmp.count(i, other_card)
                    other = [i]
                elif tmp.count(i, other_card) == count_:
                    other.append(i)
            other = random.choice(other)
            other_card = tmp.remove(other, other_card)
            print(own_card, other, other_card)
            return own_card, other, other_card
        else:
            return super(AdvancedPlayer, self).decide(card, game, answers)


class PriorityPlayer(AdvancedPlayer):
    def __init__(self, priority):
        self.priority = priority

    def build(self, game, cards):
        for card in self.priority:
            if card in cards or card is None:
                return card
        return None
