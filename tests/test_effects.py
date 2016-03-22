from nose.tools import *

from machikoro import *
from machikoro.effect import *


def test_not_implemented():
    effect = NotImplementedEffect()
    assert_raises(NotImplementedError, effect, None, None, None)
