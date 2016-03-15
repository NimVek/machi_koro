#!/usr/bin/env python

"""
This module contains the constants
"""

from enum import Enum

class CardType(Enum):
    """Defining the Establishment type"""
    PRIMARY_INDUSTRY = BLUE = 1
    SECONDARY_INDUSTRY = GREEN = 2
    RESTAURANT = RED = 3
    MAJOR_ESTABLISHMENT = PURPLE = 4
    LANDMARK = 5
