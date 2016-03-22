#!/usr/bin/env python

from abc import ABCMeta, abstractmethod


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
        pass
