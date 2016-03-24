#!/usr/bin/env python

from abc import ABCMeta, abstractmethod
import random


class PlayerInterface(metaclass=ABCMeta):
    @abstractmethod
    def build(self, game, cards):
        pass

    @abstractmethod
    def decide(self, card, game, answers=None):
        pass


class RandomPlayer(PlayerInterface):
    def build(self, game, cards):
        return random.choice(cards + [None])

    def decide(self, card, game, answers=None):
        if answers:
            return random.choice(answers)
        else:
            raise NotImplementedError(card)

#class AdvancePlayer(RandomPlayer):
#    def decide(self, card, game, answers=None):
#	if card == Card.
