#!/usr/bin/env python


class Game(object):
    CURRENT_PLAYER = 'current'
    MARKET = 'market'
    DICE_GAME = 'game'

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

    def _money(self, player, argument):
        if argument is None:
            return self.tableaus[player].money
        else:
            self.tableaus[player].money = argument

    def money(self, player, argument=None):
        player = self._target(player)
        money = self._money(player)
        if argument is None:
            return money
        argument = max(argument, -money)
        self._money(player, money + argument)
        return argument

    def list(self, target, argument=None):
        return self._container(target).list(argument)

    def count(self, target, argument=None):
        return self._container(target).count(argument)

    def remove(self, target, argument=None):
        return self._container(target).remove(argument)

    def add(self, target, card):
        return self._container(target).add(card)

    def next_turn(self):
        self.dices = {}

    def next_player(self):
        self.players.append(self.players.pop(0))
        self.next_turn()

    def player(self, player=Game.CURRENT_PLAYER):
        result = self._target(target)
        assert isinstance(result, PlayerInterface)
        return result

    def players(self):
        return self._players

    def opponents(self, player=Game.CURRENT_PLAYER):
        player = self.player(player)
        i = self._players.index(player)
        result = self._players[i + 1:] + self._players[:i]
        return list(reversed(result))

    def neighbors(self, player=Game.CURRENT_PLAYER):
        return self.opponents(player)

    def roll_dices(self, target=GAME.DICE_GAME, count=1):
        self.dices[target] = Game.roll(count)

    def get_dices(self, target=GAME.DICE_GAME):
        return self.dices[target]

    def get_pip(self, target):
        return sum(self.get_dices(target))
