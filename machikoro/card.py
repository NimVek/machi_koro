#!/usr/bin/env python

from enum import Enum
from .constant import CardExpansion, CardType, CardSymbol
from .effect import *

class Card(Enum):
# yapf: disable
    WHEAT_FIELD = (
        CardExpansion.BASE, CardType.PRIMARY_INDUSTRY, CardSymbol.GRAIN, 1,
        [1], general_income, {"base": 1})
    RANCH = (
        CardExpansion.BASE, CardType.PRIMARY_INDUSTRY, CardSymbol.ANIMAL, 1,
        [2], general_income, {"base": 1})
    FOREST = (
        CardExpansion.BASE, CardType.PRIMARY_INDUSTRY, CardSymbol.GEAR, 3,
        [5], general_income, {"base": 1})
    MINE = (
        CardExpansion.BASE, CardType.PRIMARY_INDUSTRY, CardSymbol.GEAR, 6,
        [9], general_income, {"base": 5})
    APPLE_ORCHARD = (
        CardExpansion.BASE, CardType.PRIMARY_INDUSTRY, CardSymbol.GRAIN, 3,
        [10], general_income, {"base": 3})
    BAKERY = (
        CardExpansion.BASE, CardType.SECONDARY_INDUSTRY, CardSymbol.SHOP, 1,
        [2, 3], general_income, {"base": 1})
    CONVENIENCE_STORE = (
        CardExpansion.BASE, CardType.SECONDARY_INDUSTRY, CardSymbol.SHOP, 2,
        [4], general_income, {"base": 3})
    CHEESE_FACTORY = (
        CardExpansion.BASE, CardType.SECONDARY_INDUSTRY, CardSymbol.FACTORY, 5,
        [7], general_income, {"base": 3, "multiplier": CardSymbol.ANIMAL})
    FURNITURE_FACTORY = (
        CardExpansion.BASE, CardType.SECONDARY_INDUSTRY, CardSymbol.FACTORY, 3,
        [8], general_income, {"base": 3, "multiplier": CardSymbol.GEAR})
    FRUIT_AND_VEGETABLE_MARKET = (
        CardExpansion.BASE, CardType.SECONDARY_INDUSTRY, CardSymbol.FRUIT, 2,
        [11, 12], general_income, {"base": 2, "multiplier": CardSymbol.GRAIN})
    CAFE = (
        CardExpansion.BASE, CardType.RESTAURANT, CardSymbol.CUP, 2,
        [3], general_income, {"base": 1})
    FAMILY_RESTAURANT = (
        CardExpansion.BASE, CardType.RESTAURANT, CardSymbol.CUP, 3,
        [9, 10], general_income, {"base": 2})
    STADIUM = (
        CardExpansion.BASE, CardType.MAJOR_ESTABLISHMENT, CardSymbol.LANDMARK, 6,
        [6])
    TV_STATION = (
        CardExpansion.BASE, CardType.MAJOR_ESTABLISHMENT, CardSymbol.LANDMARK, 7,
        [6])
    BUSINESS_CENTRE = (
        CardExpansion.BASE, CardType.MAJOR_ESTABLISHMENT, CardSymbol.LANDMARK, 8,
        [6])
    STATION = (
        CardExpansion.BASE, CardType.LANDMARK, CardSymbol.LANDMARK, 4)
    SHOPPING_MALL = (
        CardExpansion.BASE, CardType.LANDMARK, CardSymbol.LANDMARK, 10)
    AMUSEMENT_PARK = (
        CardExpansion.BASE, CardType.LANDMARK, CardSymbol.LANDMARK, 16)
    RADIO_TOWER = (
        CardExpansion.BASE, CardType.LANDMARK, CardSymbol.LANDMARK, 22)
    FLOWER_FIELD = (CardExpansion.HARBOUR, CardType.PRIMARY_INDUSTRY,
                    CardSymbol.GRAIN, 2, [4])
    MACKEREL_FISHING_BOAT = (CardExpansion.HARBOUR, CardType.PRIMARY_INDUSTRY,
                             CardSymbol.BOAT, 2, [8])
    TUNA_FISHING_BOAT = (CardExpansion.HARBOUR, CardType.PRIMARY_INDUSTRY,
                         CardSymbol.BOAT, 5, [12, 13, 14])
    FLOWER_SHOP = (CardExpansion.HARBOUR, CardType.SECONDARY_INDUSTRY,
                   CardSymbol.SHOP, 1, [6])
    FOOD_WAREHOUSE = (CardExpansion.HARBOUR, CardType.SECONDARY_INDUSTRY,
                      CardSymbol.FACTORY, 2, [12, 13])
    SUSHI_BAR = (CardExpansion.HARBOUR, CardType.RESTAURANT, CardSymbol.CUP, 2,
                 [1])
    PIZZA_HUT = (CardExpansion.HARBOUR, CardType.RESTAURANT, CardSymbol.CUP, 1,
                 [7])
    HAMBURGER_SHOP = (CardExpansion.HARBOUR, CardType.RESTAURANT,
                      CardSymbol.CUP, 1, [8])
    PUBLISHER = (CardExpansion.HARBOUR, CardType.MAJOR_ESTABLISHMENT,
                 CardSymbol.LANDMARK, 5, [7])
    TAXATION_OFFICE = (CardExpansion.HARBOUR, CardType.MAJOR_ESTABLISHMENT,
                       CardSymbol.LANDMARK, 4, [8, 9])
    CITY_HALL = (CardExpansion.HARBOUR, CardType.LANDMARK, CardSymbol.LANDMARK,
                 0)
    HARBOUR = (CardExpansion.HARBOUR, CardType.LANDMARK, CardSymbol.LANDMARK,
               2)
    AIRPORT = (CardExpansion.HARBOUR, CardType.LANDMARK, CardSymbol.LANDMARK,
               30)
    CORN_FIELD = (CardExpansion.SHARP, CardType.PRIMARY_INDUSTRY,
                  CardSymbol.GRAIN, 2, [3, 4])
    GRAPE_VINEYARD = (CardExpansion.SHARP, CardType.PRIMARY_INDUSTRY,
                      CardSymbol.GRAIN, 3, [7])
    GENERAL_STORE = (CardExpansion.SHARP, CardType.SECONDARY_INDUSTRY,
                     CardSymbol.SHOP, 0, [2])
    REMODELLING = (CardExpansion.SHARP, CardType.SECONDARY_INDUSTRY,
                   CardSymbol.BRIEFCASE, 2, [4])
    MONEY_LENDING_OFFICE = (CardExpansion.SHARP, CardType.SECONDARY_INDUSTRY,
                            CardSymbol.BRIEFCASE, -5, [5, 6])
    WINERY = (CardExpansion.SHARP, CardType.SECONDARY_INDUSTRY,
              CardSymbol.FACTORY, 3, [9])
    MOVING_COMPANY = (CardExpansion.SHARP, CardType.SECONDARY_INDUSTRY,
                      CardSymbol.BRIEFCASE, 2, [9, 10])
    DRINKS_FACTORY = (CardExpansion.SHARP, CardType.SECONDARY_INDUSTRY,
                      CardSymbol.FACTORY, 5, [11])
    HIGH_CLASS_RESTAURANT = (CardExpansion.SHARP, CardType.RESTAURANT,
                             CardSymbol.CUP, 3, [5])
    PRIVATE_MEMBERS_BAR = (CardExpansion.SHARP, CardType.RESTAURANT,
                           CardSymbol.CUP, 4, [12, 13, 14])
    CLEANING_COMPANY = (CardExpansion.SHARP, CardType.MAJOR_ESTABLISHMENT,
                        CardSymbol.LANDMARK, 4, [8])
    IT_VENTURE = (CardExpansion.SHARP, CardType.MAJOR_ESTABLISHMENT,
                  CardSymbol.LANDMARK, 1, [10])
    PARK = (CardExpansion.SHARP, CardType.MAJOR_ESTABLISHMENT,
            CardSymbol.LANDMARK, 3, [11, 12, 13])
    GAMING_MEGA_STORE = (CardExpansion.PROMOTION, CardType.MAJOR_ESTABLISHMENT,
                         CardSymbol.LANDMARK, 7, [10])
    SANTAS_WORKSHOP = (CardExpansion.PROMOTION, CardType.LANDMARK,
                       CardSymbol.LANDMARK, 0)
# yapf: enable

    def __init__(self,
                 expansion,
                 type,
                 symbol,
                 cost,
                 activation=None,
                 effect=None,
                 parameter=None):
        self.expansion = expansion
        self.type = type
        self.symbol = symbol
        self.cost = cost
        self.activation = activation
        self.effect = effect
        self.parameter = parameter

    def __eq__(self, other):
        if isinstance(other, CardExpansion):
            return self.expansion == other
        elif isinstance(other, CardType):
            return self.type == other
        elif isinstance(other, CardSymbol):
            return self.symbol == other
        elif isinstance(other, int):
            return self.activation and other in self.activation
        else:
            return other is self

    def __hash__(self):
        return hash(self._name_)
