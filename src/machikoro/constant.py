#!/usr/bin/env python
"""
This module contains the constants
"""

from enum import Enum


CURRENT_PLAYER = "current"
DICE_GAME = "game"


class CardExpansion(Enum):
    """Defining the Expansion"""

    BASE = 1
    HARBOUR = 2
    SHARP = 3
    PROMOTION = 4


class CardType(Enum):
    """Defining the Establishment type"""

    PRIMARY_INDUSTRY = BLUE = 1
    SECONDARY_INDUSTRY = GREEN = 2
    RESTAURANT = RED = 3
    MAJOR_ESTABLISHMENT = PURPLE = 4
    LANDMARK = 5


class CardSymbol(Enum):
    """Defining the Establishment symbol"""

    GRAIN = 1
    ANIMAL = 2
    GEAR = 3
    SHOP = 4
    FACTORY = 5
    FRUIT = 6
    CUP = 7
    BOAT = 8
    BRIEFCASE = 9
    LANDMARK = 10
