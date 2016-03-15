
from nose.tools import assert_equals

from machikoro.constant import *

def test_colors():
    assert_equals(CardType.PRIMARY_INDUSTRY, CardType.BLUE)
    assert_equals(CardType.SECONDARY_INDUSTRY, CardType.GREEN)
    assert_equals(CardType.RESTAURANT, CardType.RED)
    assert_equals(CardType.MAJOR_ESTABLISHMENT, CardType.PURPLE)
