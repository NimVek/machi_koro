#!/usr/bin/env python

import random

from .container import Tableau
from .interface import PlayerInterface


class Game(object):
    CURRENT_PLAYER = "current"
    MARKET = "market"
    DICE_GAME = "game"

    def __init__(self, players, market):
        self._players = list(players)
        self.tableaus = {}
        for player in self._players:
            self.tableaus[player] = Tableau()
        self.market = market
        self.dices = {}

    def _target(self, argument):
        if argument is None:
            argument = Game.CURRENT_PLAYER
        if type(argument) is str:
            if argument == Game.MARKET:
                return self.market
            elif argument == Game.CURRENT_PLAYER:
                return self._players[0]
        else:
            return argument

    def _container(self, argument):
        result = self._target(argument)
        if isinstance(result, PlayerInterface):
            result = self.tableaus[result]
        return result

    def list(self, target, argument=None):
        return self._container(target).list(argument)

    def count(self, target, argument=None):
        return self._container(target).count(argument)

    def remove(self, target, argument=None):
        return self._container(target).remove(argument)

    def add(self, target, card):
        return self._container(target).add(card)

    def money(self, target, difference=None):
        return self._container(target).money(difference)

    def advance(self, next_player=False):
        if next_player:
            self._players.append(self._players.pop(0))
        self.dices = {}

    def player(self, player=CURRENT_PLAYER):
        result = self._target(player)
        assert isinstance(result, PlayerInterface)
        return result

    def players(self):
        return self._players

    def opponents(self, player=CURRENT_PLAYER):
        player = self.player(player)
        i = self._players.index(player)
        result = self._players[i + 1 :] + self._players[:i]  # noqa: E203
        return list(reversed(result))

    def neighbors(self, player=CURRENT_PLAYER):
        return self.opponents(player)

    @staticmethod
    def __roll(count_):
        return [random.randint(1, 6) for _ in range(count_)]

    def roll(self, target=DICE_GAME, count_=1):
        self.dices[target] = Game.__roll(count_)

    def dice(self, target=DICE_GAME, value=None):
        if value:
            self.dices[target] = value
        else:
            return self.dices[target]

    def pip(self, target=DICE_GAME):
        return sum(self.dice(target))
