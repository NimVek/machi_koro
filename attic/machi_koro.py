#!/usr/bin/env python3.4

from enum import Enum
import random
import itertools

# mandatory
# multiplier
# base


def general_income(card, owner, table, parameter):
    #    print(card)
    #    print(owner)
    #    print(table)
    #    print(parameter)
    base = parameter['base']
    if parameter.get('multiplier'):
        base *= table.count(owner, parameter.get('multiplier'))
    if table.list(owner, Card.SHOPPING_MALL):
        base += 1
    #    print(table.money(owner))
    if card == CardType.RESTAURANT:
        base = -table.money('current', -base)
    table.money(owner, base)
#    print(table.money(owner))


class AutoNumber(Enum):
    def __new__(self):
        value = len(self.__members__) + 1
        obj = object.__new__(self)
        obj._value_ = value
        return obj


class CardExpansion(AutoNumber):
    BASE = ()
    HARBOUR = ()
    SHARP = ()
    PROMOTION = ()


class CardSymbol(AutoNumber):
    GRAIN = ()
    ANIMAL = ()
    GEAR = ()
    SHOP = ()
    FACTORY = ()
    FRUIT = ()
    CUP = ()
    BOAT = ()
    BRIEFCASE = ()
    LANDMARK = ()


class CardType(AutoNumber):
    PRIMARY_INDUSTRY = ()
    SECONDARY_INDUSTRY = ()
    RESTAURANT = ()
    MAJOR_ESTABLISHMENT = ()
    LANDMARK = ()


class Card(Enum):
    WHEAT_FIELD = (CardExpansion.BASE, CardType.PRIMARY_INDUSTRY,
                   CardSymbol.GRAIN, 1, [1], general_income, {"base": 1})
    RANCH = (CardExpansion.BASE, CardType.PRIMARY_INDUSTRY, CardSymbol.ANIMAL,
             1, [2], general_income, {"base": 1})
    FOREST = (CardExpansion.BASE, CardType.PRIMARY_INDUSTRY, CardSymbol.GEAR,
              3, [5], general_income, {"base": 1})
    MINE = (CardExpansion.BASE, CardType.PRIMARY_INDUSTRY, CardSymbol.GEAR, 6,
            [9], general_income, {"base": 5})
    APPLE_ORCHARD = (CardExpansion.BASE, CardType.PRIMARY_INDUSTRY,
                     CardSymbol.GRAIN, 3, [10], general_income, {"base": 3})
    BAKERY = (CardExpansion.BASE, CardType.SECONDARY_INDUSTRY, CardSymbol.SHOP,
              1, [2, 3], general_income, {"base": 1})
    CONVENIENCE_STORE = (CardExpansion.BASE, CardType.SECONDARY_INDUSTRY,
                         CardSymbol.SHOP, 2, [4], general_income, {"base": 3})
    CHEESE_FACTORY = (CardExpansion.BASE, CardType.SECONDARY_INDUSTRY,
                      CardSymbol.FACTORY, 5, [7], general_income,
                      {"base": 3,
                       "multiplier": CardSymbol.ANIMAL})
    FURNITURE_FACTORY = (CardExpansion.BASE, CardType.SECONDARY_INDUSTRY,
                         CardSymbol.FACTORY, 3, [8], general_income,
                         {"base": 3,
                          "multiplier": CardSymbol.GEAR})
    FRUIT_AND_VEGETABLE_MARKET = (
        CardExpansion.BASE, CardType.SECONDARY_INDUSTRY, CardSymbol.FRUIT, 2,
        [11, 12], general_income, {"base": 2,
                                   "multiplier": CardSymbol.GRAIN})
    CAFE = (CardExpansion.BASE, CardType.RESTAURANT, CardSymbol.CUP, 2, [3],
            general_income, {"base": 1})
    FAMILY_RESTAURANT = (CardExpansion.BASE, CardType.RESTAURANT,
                         CardSymbol.CUP, 3, [9, 10], general_income,
                         {"base": 2})
    STADIUM = (CardExpansion.BASE, CardType.MAJOR_ESTABLISHMENT,
               CardSymbol.LANDMARK, 6, [6])
    TV_STATION = (CardExpansion.BASE, CardType.MAJOR_ESTABLISHMENT,
                  CardSymbol.LANDMARK, 7, [6])
    BUSINESS_CENTRE = (CardExpansion.BASE, CardType.MAJOR_ESTABLISHMENT,
                       CardSymbol.LANDMARK, 8, [6])
    STATION = (CardExpansion.BASE, CardType.LANDMARK, CardSymbol.LANDMARK, 4)
    SHOPPING_MALL = (CardExpansion.BASE, CardType.LANDMARK,
                     CardSymbol.LANDMARK, 10)
    AMUSEMENT_PARK = (CardExpansion.BASE, CardType.LANDMARK,
                      CardSymbol.LANDMARK, 16)
    RADIO_TOWER = (CardExpansion.BASE, CardType.LANDMARK, CardSymbol.LANDMARK,
                   22)
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

    def __init__(self,
                 expansion,
                 type,
                 symbol,
                 cost,
                 pip=None,
                 income=None,
                 parameter=None):
        self.expansion = expansion
        self.type = type
        self.symbol = symbol
        self.cost = cost
        self.pip = pip
        self.income = income
        self.parameter = parameter

    def __eq__(self, other):
        if isinstance(other, CardExpansion):
            return self.expansion == other
        elif isinstance(other, CardType):
            return self.type == other
        elif isinstance(other, CardSymbol):
            return self.symbol == other
        elif isinstance(other, int):
            return self.pip and other in self.pip
        else:
            return other is self

    def __hash__(self):
        return hash(self._name_)


def filter_cards_or(cards, attributes):
    return set.union(*[filter_cards(cards, i) for i in attributes])


def filter_cards_and(cards, attributes):
    return set.intersection(*[filter_cards(cards, i) for i in attributes])


def filter_cards_not(cards, attributes):
    return set(cards) - filter_cards(cards, attributes)


def filter_cards(cards, attributes):
    if isinstance(attributes, Card) or isinstance(
            attributes, CardExpansion) or isinstance(
                attributes, CardExpansion) or isinstance(
                    attributes, CardType) or isinstance(
                        attributes, CardSymbol) or isinstance(attributes, int):
        return set([x for x in cards if x == attributes])
    elif isinstance(attributes, list):
        if attributes[0] == '!':
            return filter_cards_not(cards, attributes[1])
        elif attributes[0] == '&':
            return filter_cards_and(cards, attributes[1:])
        elif attributes[0] == '|':
            return filter_cards_or(cards, attributes[1:])
    elif attributes is None:
        return cards


class Container(object):
    def _list(self):
        raise NotImplementedError("Subclasses should implement this!")

    def list(self, attributes=None):
        return filter_cards(self._list(), attributes)

    def _count(self, card):
        raise NotImplementedError("Subclasses should implement this!")

    def count(self, attributes):
        return sum(self._count(x) for x in self.list(attributes))

    def __contains__(self, attributes):
        return self.count(attributes) > 0

    def _take(self, card):
        raise NotImplementedError("Subclasses should implement this!")

    def take(self, attributes):
        count = self.count(attributes)
        if count > 0:
            index = random.randrange(count)
            for card in self.list(attributes):
                if index > self._count(card):
                    index -= self._count(card)
                else:
                    return self._take(card)
        else:
            return None

    def put(self, card):
        raise NotImplementedError("Subclasses should implement this!")


class UnlimitedSupply(Container):
    def __init__(self, cards=filter_cards(Card, CardExpansion.BASE)):
        self.cards = list(cards)

    def _list(self):
        return self.cards

    def _count(self, card):
        assert isinstance(card, Card)
        return 1 if card in self.cards else 0

    def _take(self, card):
        assert isinstance(card, Card)
        return card if card in self.cards else None

    def put(self, card):
        assert isinstance(card, Card)
        if not card in self.cards:
            self.cards.append(card)


class LimitedSupply(Container):
    def __init__(self,
                 cards=filter_cards(Card, CardExpansion.BASE),
                 player_count=4,
                 stock_count=6):
        self.cards = {}
        for card in cards:
            if card == CardType.LANDMARK:
                self.cards[card] = player_count
            else:
                self.cards[card] = stock_count

    def _list(self):
        #        for card, _count in self.cards.items():
        #            print(str(card) + " " + str(_count))
        #        print([card for card, _count in self.cards.items() if _count > 0])
        return [card for card, _count in self.cards.items() if _count > 0]

    def _count(self, card):
        assert isinstance(card, Card)
        return self.cards.get(card, 0)

    def _take(self, card):
        assert isinstance(card, Card)
        if self._count(card) > 0:
            self.cards[card] -= 1
            return card
        else:
            return None

    def put(self, card):
        assert isinstance(card, Card)
        self.cards[card] = self.cards.get(card, 0) + 1


class TilesMarket(Container):
    def __init__(self,
                 supply,
                 tiles=[[2, CardType.MAJOR_ESTABLISHMENT],
                        [4, ['|', 1, 2, 3, 4, 5, 6]], [4, None]]):
        self.supply = supply
        self.tiles = [x + [LimitedSupply([])] for x in tiles]
        self.__assure_tiles()

    def _list(self):
        result = self.supply.list(CardType.LANDMARK)
        for tile in self.tiles:
            result = result.union(set(tile[2]._list()))
        return result

    def _count(self, card):
        if card == CardType.LANDMARK:
            return self.supply._count(card)
        else:
            for tile in self.tiles:
                if len(filter_cards([card], tile[1])) > 0:
                    return tile[2]._count(card)
                    break
        return 0

    def _take(self, card):
        result = None
        if card == CardType.LANDMARK:
            result = self.supply._take(card)
        else:
            for tile in self.tiles:
                if len(filter_cards([card], tile[1])) > 0:
                    result = tile[2]._take(card)
                    break
#            print(result)
            self.__assure_tiles()
        return result

    def put(self, card):
        if card == CardType.LANDMARK:
            self.supply.put(card)
        else:
            for tile in self.tiles:
                if len(filter_cards([card], tile[1])) > 0:
                    tile[2].put(card)
                    break

    def __assure_tiles(self):
        remains = self.supply.list(['!', CardType.LANDMARK])
        for tile in self.tiles:
            #            print("tile")
            #            print(remains)
            using = filter_cards(remains, tile[1])
            #            a = len(using)
            #            b = len(remains)
            remains = remains - using
            #            print(using)
            #            print(remains)
            #            print(str(len(remains)) + " + " + str(len(using)) + " == " + str(b))
            #            print(len(using))
            #            assert (len(remains) + len(using) == b)
            #            if using:
            #                print(using)
            #                using = self.supply.list(['|'] + list(using))
            #                print(using)
            #                assert using
            while using and (len(tile[2]._list()) < tile[0]):
                #                print("Using")
                #                print(using)
                #                print(self.supply.count(['|'] + list(using)))
                #                print(self.supply.list(['|'] + list(using)))
                #                t = self.supply.take(['|'] + list(using))
                #                print(t)
                #                self.put(t)
                self.put(self.supply.take(['|'] + list(using)))
                using = self.supply.list(['|'] + list(using))
#            remains -= using


class Tableau(Container):
    def __init__(self, money=3, cards=[Card.WHEAT_FIELD, Card.BAKERY]):
        self.money = money
        self.cards = {}
        for card in cards:
            self.put(card)

    def _list(self):
        return [card for card in self.cards if self._count(card) > 0]

    def _count(self, card):
        if card in self.cards:
            return self.cards[card].get('count', 0)
        else:
            return 0

    def _take(self, card):
        if self._count(card) > 0:
            self.cards[card]['count'] -= 1
            return card
        else:
            return None

    def put(self, card):
        if card in self.cards:
            self.cards[card]['count'] += 1
        else:
            self.cards[card] = {'count': 1}


class PlayerInterface(object):
    def build(self, table, cards):
        raise NotImplementedError("Subclasses should implement this!")

    def decide(self, card, table, answers):
        raise NotImplementedError("Subclasses should implement this!")


class RandomPlayer(PlayerInterface):
    def build(self, table, cards):
        return random.choice(cards + [None])

    def decide(self, card, table, answers=None):
        if answers:
            return random.choice(answers)
        else:
            print("ERROR: " + str(card))
            return super(RandomPlayer, self).decide(card, table, answers)


class BaseSimplePlayer(RandomPlayer):
    def __init__(self, order):
        self.order = order

    def __get_available(self, table):
        result = []
        for card in table.list('market'):
            if card != CardSymbol.LANDMARK or not table.list(self, card):
                result.append(card)
        return result

    def evaluate(self, table, cards, step):
        if step[0] == '!':
            return self.evaluate_assure(table, cards, step[1:])
        elif step[0] == '*' or isinstance(step[0], int):
            maxcount = step[0] if isinstance(step[0], int) else 100
            return self.evaluate_count(table, cards, maxcount, step[1:])
        elif isinstance(step[0], list):
            if len(step) > 2:
                return self.evaluate_if(table, cards, step[0], step[1],
                                        step[2])
            else:
                return self.evaluate_if(table, cards, step[0], step[1])
        else:
            return None

    def evaluate_if(self, table, cards, _if, _then, _else=None):
        if self.evaluate_list(table, self.__get_available(table), _if) == None:
            return self.evaluate_list(table, cards, _then)
        else:
            if _else:
                return self.evaluate_list(table, cards, _else)
            else:
                return None

    def evaluate_count(self, table, cards, maxcount, order):
        mincount = maxcount
        result = []
        for item in order:
            tmp_cards = filter_cards(cards, item)
            if tmp_cards:
                tmp = table.count(self, item)
                if tmp < maxcount:
                    if tmp < mincount:
                        mincount = tmp
                        result = []
                    if tmp == mincount:
                        result = result + list(tmp_cards)
        if result:
            #            print(result)
            return random.choice(result)
        else:
            return None

    def evaluate_assure(self, table, cards, order):
        supply = self.evaluate_list(table, cards, order)
        if supply == None:
            if self.evaluate_list(table, self.__get_available(table),
                                  order) != None:
                return False
        return supply

    def evaluate_list(self, table, cards, orders):
        result = None
        for step in orders:
            #            print(step)
            result = self.evaluate(table, cards, step)
            #            print(result)
            if result != None:
                return result
            if result == False:
                return None
                break
        return None

    def build(self, table, cards):
        result = None
        for step in self.order:
            #            print(step)
            result = self.evaluate(table, cards, step)
            #            print(result)
            if result != None:
                return result
            if result == False:
                return None
                break
        return None

    def decide(self, card, table, answers=None):
        if card == Card.STATION:
            return False
        elif card == Card.RADIO_TOWER:
            return False
        else:
            print("ERROR: " + str(card))
            return super(BaseSimplePlayer, self).decide(card, table, answers)


class Simple_ConvenienceStore(BaseSimplePlayer):
    def __init__(self):
        super(Simple_ConvenienceStore, self).__init__(
            [['!', ['*', Card.CONVENIENCE_STORE]],
             ['*', Card.BAKERY],
             ['!', [1, Card.SHOPPING_MALL]],
             ['*', Card.RADIO_TOWER],
             ['*', Card.AMUSEMENT_PARK],
             ['*', Card.STATION]]) # yapf: disable

class Simple_JasonConvenienceStore(BaseSimplePlayer):
    def __init__(self):
        super(Simple_JasonConvenienceStore, self).__init__(
            [['*', Card.SHOPPING_MALL],
             ['*', Card.CONVENIENCE_STORE],
             ['*', Card.RADIO_TOWER],
             ['*', Card.AMUSEMENT_PARK],
             ['*', Card.STATION],
             ['*', Card.WHEAT_FIELD],
             ['*', Card.RANCH]]) # yapf: disable

class Simple_Bakery(BaseSimplePlayer):
    def __init__(self):
        super(Simple_Bakery, self).__init__(
            [['*', Card.BAKERY],
             ['!', [1, Card.SHOPPING_MALL]],
             ['*', Card.RADIO_TOWER],
             ['*', Card.AMUSEMENT_PARK],
             ['*', Card.STATION]]) # yapf: disable

class Simple_Blues(BaseSimplePlayer):
    def __init__(self):
        super(Simple_Blues, self).__init__(
            [['*', Card.SHOPPING_MALL],
             ['*', Card.RADIO_TOWER],
             ['*', Card.AMUSEMENT_PARK],
             ['*', Card.STATION],
             ['*', Card.WHEAT_FIELD],
             ['*', Card.RANCH],
             ['*', Card.FOREST]]) # yapf: disable

class Simple_BluesPlusRed(BaseSimplePlayer):
    def __init__(self):
        super(Simple_BluesPlusRed, self).__init__(
            [['*', Card.SHOPPING_MALL],
             ['*', Card.RADIO_TOWER],
             ['*', Card.AMUSEMENT_PARK],
             ['*', Card.STATION],
             ['*', Card.CAFE],
             ['*', Card.WHEAT_FIELD],
             ['*', Card.RANCH],
             ['*', Card.FOREST]]) # yapf: disable

class Simple_OneDieSpectrum(BaseSimplePlayer):
    def __init__(self):
        super(Simple_OneDieSpectrum, self).__init__(
            [['*', Card.SHOPPING_MALL],
             ['*', Card.RADIO_TOWER],
             ['*', Card.AMUSEMENT_PARK],
             ['*', Card.STATION],
             ['*'] + list(filter_cards(Card, ['&', CardExpansion.BASE,
                                                   ['!', CardSymbol.LANDMARK],
                                                   ['|', 1, 2, 3, 4, 5, 6]]))]) # yapf: disable

class Simple_FurnitureFactory(BaseSimplePlayer):
    def __init__(self):
        super(Simple_FurnitureFactory, self).__init__(
            [['*', Card.STATION],
             ['*', Card.AMUSEMENT_PARK],
             ['*', Card.RADIO_TOWER],
             ['*', Card.SHOPPING_MALL],
             [3, Card.FOREST],
             [[['*', Card.STATION]],[[3, Card.FURNITURE_FACTORY, Card.MINE]]]]) # yapf: disable

    def decide(self, card, table, answers=None):
        if card == Card.STATION:
            return True
        else:
            return super(Simple_FurnitureFactory, self).decide(card, table,
                                                               answers)


class Simple_Null(BaseSimplePlayer):
    def __init__(self):
        super(Simple_Null, self).__init__(
            [['*', Card.RADIO_TOWER],
             ['*', Card.AMUSEMENT_PARK],
             ['*', Card.SHOPPING_MALL],
             ['*', Card.STATION]]) # yapf: disable

class Simple_CheeseFactory(BaseSimplePlayer):
    def __init__(self):
        super(Simple_CheeseFactory, self).__init__(
            [['*', Card.STATION],
             ['*', Card.AMUSEMENT_PARK],
             ['*', Card.RADIO_TOWER],
             ['*', Card.SHOPPING_MALL],
             ['*', Card.RANCH],
             [[['*', Card.STATION]],[['*', Card.CHEESE_FACTORY]]]]) # yapf: disable

    def decide(self, card, table, answers=None):
        if card == Card.STATION:
            return True
        else:
            return super(Simple_CheeseFactory, self).decide(card, table,
                                                            answers)


class Simple_FruitAndVegetableMarket(BaseSimplePlayer):
    def __init__(self):
        super(Simple_FruitAndVegetableMarket, self).__init__(
            [['*', Card.STATION],
             ['*', Card.AMUSEMENT_PARK],
             ['*', Card.RADIO_TOWER],
             ['*', Card.SHOPPING_MALL],
             ['*', Card.WHEAT_FIELD],
             [[['*', Card.STATION]],[['*', Card.APPLE_ORCHARD, Card.FRUIT_AND_VEGETABLE_MARKET]]]]) # yapf: disable

    def decide(self, card, table, answers=None):
        if card == Card.STATION:
            return True if table.list(
                self, Card.FRUIT_AND_VEGETABLE_MARKET) else False
        else:
            return super(Simple_FruitAndVegetableMarket, self).decide(
                card, table, answers)


class Simple_Random(BaseSimplePlayer):
    def __init__(self):
        super(Simple_Random, self).__init__(
            [['*', Card.STATION],
             ['*', Card.AMUSEMENT_PARK],
             ['*', Card.RADIO_TOWER],
             ['*', Card.SHOPPING_MALL],
             ['*', ['!', CardSymbol.LANDMARK]]]) # yapf: disable

    def decide(self, card, table, answers=None):
        if card == Card.STATION:
            return True
        else:
            return super(Simple_Random, self).decide(card, table, answers)


class BaseAdvancePlayer(RandomPlayer):
    pass


class Advance_PriorityList(BaseAdvancePlayer):
    def __init__(self, priority):
        self.priority = priority

    def build(self, table, cards):
        for card in self.priority:
            if card in cards or card is None:
                return card
        return None


class TableInterface(object):
    def _target(self, argument=None):
        raise NotImplementedError("Subclasses should implement this!")

#    def _container(self, argument = None):
#        raise NotImplementedError("Subclasses should implement this!")

    def _money(self, player, argument=None):
        raise NotImplementedError("Subclasses should implement this!")

    def money(self, player, argument=None):
        player = self._target(player)
        money = self._money(player)
        if argument is None:
            return money
        argument = max(argument, -money)
        self._money(player, money + argument)
        return argument

    def list(self, target, argument=None):
        raise NotImplementedError("Subclasses should implement this!")

    def take(self, target, argument=None):
        raise NotImplementedError("Subclasses should implement this!")

    def put(self, target, card):
        raise NotImplementedError("Subclasses should implement this!")


class Table(TableInterface):
    def __init__(self, players, market):
        self.players = list(players)
        self.tableaus = {}
        for player in players:
            self.tableaus[player] = Tableau()
        self.market = market
        self.dices = {}

    def _target(self, argument=None):
        if argument is None:
            argument = 'current'
        if type(argument) is str:
            if argument == 'market':
                return self.market
            elif argument == 'current':
                return self.players[0]
        else:
            return argument

    def _container(self, argument=None):
        result = self._target(argument)
        if isinstance(result, PlayerInterface):
            result = self.tableaus[result]
        return result

    def _money(self, player, argument=None):
        if argument is None:
            return self.tableaus[player].money
        else:
            self.tableaus[player].money = argument

    def list(self, target, argument=None):
        return self._container(target).list(argument)

    def count(self, target, argument):
        return self._container(target).count(argument)

    def take(self, target, argument=None):
        return self._container(target).take(argument)

    def put(self, target, card):
        return self._container(target).put(card)

    def player(self, target):
        return self._target(target)

    def next_turn(self):
        self.dices = {}

    def next_player(self):
        self.players.append(self.players.pop(0))
        self.next_turn()

    def get_players(self):
        return self.players

    def get_opponents(self, target=None):
        target = self._target(target)
        i = self.players.index(target)
        result = self.players[i + 1:] + self.players[:i]
        return list(reversed(result))

    def roll_dices(self, target='game', count=1):
        self.dices[target] = Game.roll(count)

    def get_dices(self, target='game'):
        return self.dices[target]

    def get_pip(self, target):
        return sum(self.get_dices(target))


class Game(object):
    @staticmethod
    def roll(count=1):
        return [random.randint(1, 6) for _ in range(count)]

    class Rule(object):
        @staticmethod
        def ask_player(card, table, answers):
            result = table.player('current').decide(card, table, answers)
            assert result in answers
            return result

    class Phase(object):
        @staticmethod
        def roll_dice(table):
            dice = 1
            if table.list('current', Card.STATION):
                # dice count 1 or 2
                if Game.Rule.ask_player(Card.STATION, table, [True, False]):
                    dice = 2
            table.roll_dices('game', dice)
            if table.list('current', Card.RADIO_TOWER):
                # Re-Roll
                if Game.Rule.ask_player(Card.RADIO_TOWER, table, [True,
                                                                  False]):
                    table.roll_dices('game', dice)
            if table.list('current',
                          Card.HARBOUR) and table.get_pip('game') >= 10:
                # Add 2?
                if Game.Rule.ask_player(Card.HARBOUR, table, [True, False]):
                    table.get_dices('game').append(2)

        @staticmethod
        def __earn_income(table, owner, card_type):
            for card in table.list(owner, ['&', card_type,
                                           table.get_pip('game')]):
                if card.income:
                    for _ in range(table.count(owner, card)):
                        if card.parameter:
                            card.income(card, owner, table, card.parameter)
                        else:
                            card.income(card, owner, table)
                else:
                    print("ERROR: " + str(card))

        @staticmethod
        def earn_income(table):
            #            table.money('current', 10)
            # red (nachbarn) counterclock
            for player in table.get_opponents('current'):
                Game.Phase.__earn_income(table, player, CardType.RESTAURANT)
    # green (player)
            Game.Phase.__earn_income(table, table.player('current'),
                                     CardType.SECONDARY_INDUSTRY)
            # blue (player + nachbarn)
            Game.Phase.__earn_income(table, table.player('current'),
                                     CardType.PRIMARY_INDUSTRY)
            for player in table.get_opponents('current'):
                Game.Phase.__earn_income(table, player,
                                         CardType.PRIMARY_INDUSTRY)
        # purple (player)
        #            Game.Phase.__earn_income(table, table.player('current'),
        #                                     CardType.MAJOR_ESTABLISHMENT)

        @staticmethod
        def construction(table):
            if table.list('current',
                          Card.CITY_HALL) and table.money('current') == 0:
                table.money('current', 1)

            buildable = []
            for card in table.list('market'):
                if card.cost <= table.money('current'):
                    if card != CardSymbol.LANDMARK or not table.list('current',
                                                                     card):
                        buildable.append(card)

            build = table.player('current').build(table, buildable)
            if build:
                build = filter_cards(buildable, build)
            if build:
                build = table.take('market', ['|'] + list(build))
                #                print("CONSTRUCTION: " + str(type(table.player('current'))) +
                #                      " " + str(build))
                table.money('current', -build.cost)
                table.put('current', build)

            if table.list('current', Card.AIRPORT) and build is None:
                table.money('current', 10)

    @staticmethod
    def won(table):
        result = True
        for card in table.list('market', CardType.LANDMARK):
            result = result and table.list('current', card)
        return result

    @staticmethod
    def run(table):
        i = 0
        while True:
            i += 1
            if i == 1000:
                break

            Game.Phase.roll_dice(table)

            #            print(table.money('current'))
            Game.Phase.earn_income(table)
            #            print(self.tableaus[player].list())
            #            print(table.money('current'))

            Game.Phase.construction(table)

            #            print(table.list('current', CardType.LANDMARK))

            if Game.won(table):
                #                print(i)
                return table.player('current')

            pip = table.get_dices('game')
            if table.list(
                    'current',
                    Card.AMUSEMENT_PARK) and len(pip) > 2 and pip[0] == pip[
                        1]:
                table.next_turn()
            else:
                table.next_player()


all_players = [RandomPlayer(), Simple_ConvenienceStore(),
               Simple_JasonConvenienceStore(), Simple_Bakery(), Simple_Blues(),
               Simple_BluesPlusRed(), Simple_OneDieSpectrum(),
               Simple_FurnitureFactory(), Simple_Null(),
               Simple_CheeseFactory(), Simple_FruitAndVegetableMarket(),
               Simple_Random()]

all_players = [Simple_ConvenienceStore(), Simple_JasonConvenienceStore(),
               Simple_Bakery(), Simple_Blues(), Simple_BluesPlusRed(),
               Simple_OneDieSpectrum(), Simple_CheeseFactory(),
               Simple_FruitAndVegetableMarket()]


def original_test():
    players = [RandomPlayer(), Simple_ConvenienceStore(),
               Simple_JasonConvenienceStore(), Simple_Bakery(), Simple_Blues(),
               Simple_BluesPlusRed(), Simple_OneDieSpectrum(),
               Simple_FurnitureFactory(), Simple_Null(),
               Simple_CheeseFactory(), Simple_FruitAndVegetableMarket(),
               Simple_Random()]

    counts = {}

    for player in players:
        counts[str(type(player))] = 0

    for team in itertools.combinations(players, 4):
        table = Table(team,
                      LimitedSupply(player_count=len(team),
                                    stock_count=6))
        winner = Game.run(table)
#        print("WINNER: " + str(type(winner)))

from deap import base
from deap import creator
from deap import tools
from deap import algorithms
import numpy

oversicht = list(filter_cards(Card, CardExpansion.BASE)) + [None]

#oversicht = list(filter_cards(Card, CardExpansion.BASE))


def eval_player(individual):
    #    return random.choice(range(4)),
    cards = [oversicht[i] for i in individual]
    for i in reversed(cards):
        if i is None:
            break
        if i == CardType.LANDMARK:
            return 0,
    player = Advance_PriorityList(cards)

    result = 0
    for team1 in itertools.combinations(all_players, 3):
        for i in range(10):
            team = [player] + list(team1)
            table = Table(team,
                          LimitedSupply(player_count=len(team),
                                        stock_count=6))
            winner = Game.run(table)
            if winner == player:
                result += 1
            print("WINNER: " + str(type(winner)))
    return result,


creator.create("FitnessMax", base.Fitness, weights=(1.0, ))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("cards", random.sample, range(len(oversicht)), len(oversicht))
toolbox.register("individual", tools.initIterate, creator.Individual,
                 toolbox.cards)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", eval_player)
toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=2.0 / len(oversicht))
toolbox.register("select", tools.selTournament, tournsize=3)

pop = toolbox.population(n=100)
hof = tools.ParetoFront()
hof = tools.HallOfFame(10)

stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("Avg", numpy.mean)
stats.register("Std", numpy.std)
stats.register("Min", numpy.min)
stats.register("Max", numpy.max)

algorithms.eaSimple(pop,
                    toolbox,
                    cxpb=0.5,
                    mutpb=0.2,
                    ngen=0,
                    stats=stats,
                    halloffame=hof,
                    verbose=True)

#print(stats)
for coun in range(100):

    print("population = [" + ",\n          ".join(["[ " + ", ".join([str(
        oversicht[i]) for i in indi]) + " ]" for indi in pop]) + "]")
    print("Hall of Fame")
    for indi in hof:
        print(indi.fitness)
        need = []
        for x in [oversicht[i] for i in indi]:
            if x is None:
                break
            need.append(x)
        print("[ " + ", ".join([str(i) for i in need]) + " ]")
    algorithms.eaSimple(pop,
                        toolbox,
                        cxpb=0.5,
                        mutpb=0.2,
                        ngen=1,
                        stats=stats,
                        halloffame=hof,
                        verbose=True)

print("population = [" + ",\n          ".join(["[ " + ", ".join([str(oversicht[
    i]) for i in indi]) + " ]" for indi in pop]) + "]")
print("Hall of Fame")
for indi in hof:
    print(indi.fitness)
    need = []
    for x in [oversicht[i] for i in indi]:
        if x is None:
            break
        need.append(x)
    print("[ " + ", ".join([str(i) for i in need]) + " ]")

#print(hof)
quit()
print(toolbox.individual())
indi = toolbox.individual()
for i in range(1):
    team = [RandomPlayer(), RandomPlayer(), RandomPlayer(),
            Advance_PriorityList(indi)]
    team = [RandomPlayer(), Advance_PriorityList(indi)]
    table = Table(team, LimitedSupply(player_count=len(team), stock_count=6))
    winner = Game.run(table)
    print("WINNER: " + str(type(winner)))

#print([Card.WHEAT_FIELD])
#print([CardType.BLUE])
#quit()
#print(Card.WHEAT_FIELD == 2)
#print(Card.WHEAT_FIELD == CardExpansion.BASE)
#print(Card.WHEAT_FIELD == CardSymbol.LANDMARK)

#print(random.randrange(1))
#print(random.randrange(0))
#te = UnlimitedSupply()
#tes = LimitedSupply(player_count=1, stock_count=2)
#m = TilesMarket(tes)
#t = Tableau()
#print(t.list())
#print(Card.WHEAT_FIELD in m)
#print(Card.PARK in m)

#player = RandomPlayer()
#print(player.build([]))

#print([random.randint(1, 6) for _ in range(2)])
#table = Table(
#    [RandomPlayer(), Simple_ConvenienceStore(), Simple_JasonConvenienceStore(),
#     Simple_Bakery()], m)
#table = Table(
#    [Simple_OneDieSpectrum(), Simple_ConvenienceStore(),
#     Simple_JasonConvenienceStore(), Simple_Bakery()], m)

#table = Table([Simple_Random()], tes)
#table = Table([Simple_ConvenienceStore()], m)
#print(table.get_opponents())
#print(table.money('current'))
#print(table.money('current',-5))
#print(table.money('current'))
#table.roll_dices('game', 2)
#print(table.get_dices('game'))
#table.get_dices('game').append(2)
#print(table.get_dices('game'))
#print(table.count('market'))
#quit()
#e = Engine()
#winner = Game.run(table)
#print("WINNER: " + str(type(winner)))
#quit()
#print(tes.list())
#print(tes.count(Card))
#print(tes.count(CardExpansion.BASE))
#print(tes.count(CardExpansion.HARBOUR))
#print(tes.count(CardExpansion.SHARP))
#print(tes.count(CardExpansion.PROMOTION))
#print(tes.count(CardSymbol.LANDMARK))
#print(tes.count(Card.WHEAT_FIELD))
#print(tes.take(Card.WHEAT_FIELD))
#print(tes.take(CardSymbol.LANDMARK))
#for i in range(100):
#    print(tes.take(CardExpansion.BASE))
#print(tes.take(CardExpansion.BASE))
#print(tes.take(CardExpansion.BASE))
#print(tes.take(CardExpansion.BASE))
#print(tes.take(Card.WHEAT_FIELD))
#print(tes.take(Card.WHEAT_FIELD))
#      4       "cardType": "Bakery",
#      2       "cardType": "Boat",
#      2       "cardType": "Business",
#      7       "cardType": "Cafe",
#      1       "cardType": "Cattle",
#      1       "cardType": "Company",
#      5       "cardType": "Factory",
#      4       "cardType": "Field",
#      1       "cardType": "Fruit",
#      2       "cardType": "Gear",
#     16       "cardType": "Landmark",
#      1       "cardType": "Secondary Industry",

# <anzahl><wichtig>
# anzahl 0 - x oder *
# wichtig = oder +

# *= # Kaufe alle 
# 0+ # kaufe wenn möglich ?
# 1+ # kaufe so das du mindestens eine hast
#   # kaufe maximal x

# *!
# *
# 1!
# 1
#class BaseSimplePlayer(RandomPlayer):
#class Simple_ConvenienceStore(BaseSimplePlayer):
#class Simple_JasonConvenienceStore(BaseSimplePlayer):
#class Simple_Bakery(BaseSimplePlayer):
#class Simple_Blues(BaseSimplePlayer):
#class Simple_BluesPlusRed(BaseSimplePlayer):
#class Simple_OneDieSpectrum(BaseSimplePlayer):
#class Simple_FurnitureFactory(BaseSimplePlayer):
#class Simple_Null(BaseSimplePlayer):
#class Simple_CheeseFactory(BaseSimplePlayer):
#class Simple_FruitAndVegetableMarket(BaseSimplePlayer):
#class Simple_Random(BaseSimplePlayer):
