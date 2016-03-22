#!/usr/bin/env python

from .game import Game
from .card import Card
from .constant import CardType, CardSymbol

#from .constant import CardExpansion, CardType, CardSymbol


class Rules(object):
    class Phase(object):
        @staticmethod
        def __ask_player(card, game, answers):
            result = game.player(Game.CURRENT_PLAYER).decide(card, game,
                                                             answers)
            assert result in answers
            return result

        @staticmethod
        def roll_dice(game):
            dice_count = 1
            if game.list(Game.CURRENT_PLAYER, Card.STATION):
                # dice count 1 or 2
                if Rules.Phase.__ask_player(Card.STATION, game, [True, False]):
                    dice_count = 2
            game.roll(Game.DICE_GAME, dice_count)
            if game.list(Game.CURRENT_PLAYER, Card.RADIO_TOWER):
                # Re-Roll
                if Rules.Phase.__ask_player(Card.RADIO_TOWER, game, [True,
                                                                     False]):
                    game.roll(Game.DICE_GAME, dice_count)
            if game.list(Game.CURRENT_PLAYER,
                         Card.HARBOUR) and game.pip(Game.DICE_GAME) >= 10:
                # Add 2?
                if Rules.Phase.__ask_player(Card.HARBOUR, game, [True, False]):
                    game.dice(Game.DICE_GAME).append(2)

        @staticmethod
        def __earn_income(game, owner, card_type):
            for card in game.list(owner, ['&', card_type,
                                          game.pip(Game.DICE_GAME)]):
                for _ in range(game.count(owner, card)):
                    print(card.effect)
                    card.effect(card, owner, game)

        @staticmethod
        def earn_income(game):
            game.money(Game.CURRENT_PLAYER, 10)
            """ red (neighbors) counterclock """
            for player in game.neighbors(Game.CURRENT_PLAYER):
                Rules.Phase.__earn_income(game, player, CardType.RESTAURANT)
            """ green (player) """
            Rules.Phase.__earn_income(game, game.player(Game.CURRENT_PLAYER),
                                      CardType.SECONDARY_INDUSTRY)
            """ blue (player + neighbors) """
            Rules.Phase.__earn_income(game, game.player(Game.CURRENT_PLAYER),
                                      CardType.PRIMARY_INDUSTRY)
            for player in game.neighbors(Game.CURRENT_PLAYER):
                Rules.Phase.__earn_income(game, player,
                                          CardType.PRIMARY_INDUSTRY)
            """ purple (player) """
            Rules.Phase.__earn_income(game, game.player(Game.CURRENT_PLAYER),
                                      CardType.MAJOR_ESTABLISHMENT)

        @staticmethod
        def construction(game):
            if game.list(
                    Game.CURRENT_PLAYER,
                    Card.CITY_HALL) and game.money(Game.CURRENT_PLAYER) == 0:
                game.money(Game.CURRENT_PLAYER, 1)

            buildable = []
            for card in game.list(Game.MARKET):
                if card.cost <= game.money(Game.CURRENT_PLAYER):
                    if card != CardSymbol.LANDMARK or not game.list(
                            Game.CURRENT_PLAYER, card):
                        buildable.append(card)

            build = game.player(Game.CURRENT_PLAYER).build(game, buildable)
            if build:
                build = [card for card in buildable if card == build]
            if build:
                build = game.remove(Game.MARKET, ['|'] + list(build))
                game.money(Game.CURRENT_PLAYER, -build.cost)
                game.add(Game.CURRENT_PLAYER, build)

            if game.list(Game.CURRENT_PLAYER, Card.AIRPORT) and build is None:
                game.money(Game.CURRENT_PLAYER, 10)

    @staticmethod
    def won(game):
        result = True
        for card in game.list(Game.MARKET, CardType.LANDMARK):
            result = result and game.list(Game.CURRENT_PLAYER, card)
        return result

    @staticmethod
    def evaluate(game):
        while True:

            Rules.Phase.roll_dice(game)

            Rules.Phase.earn_income(game)

            Rules.Phase.construction(game)

            if Rules.won(game):
                return game.player(Game.CURRENT_PLAYER)

            dice = game.dice(Game.DICE_GAME)
            if game.list(
                    Game.CURRENT_PLAYER,
                    Card.AMUSEMENT_PARK) and len(dice) > 1 and dice[0] == dice[
                        1]:
                game.advance(False)
            else:
                game.advance(True)
