import random
import sys

from cart import cartCal


def test_cart_between_0_to_499_adds_50():
    cart = random.randint(0, 499)
    assert cartCal(cart) == cart + 50


def test_cart_between_500_to_max_integer_stays_same():
    cart = random.randint(500, sys.maxsize)
    assert cartCal(cart) == cart


def test_cart_exactly_500():
    assert cartCal(500) == 500