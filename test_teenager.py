import random
import sys

from teenager import is_teenager

def test_age_between_0_to_12_are_not_teenager():
    assert is_teenager(random.randint(0, 12)) == False
    
def test_age_between_20_to_max_integer_are_not_teenager():
    assert is_teenager(random.randint(20, sys.maxsize)) == False
     
def test_age_between_13_to_19_are_teenagers():
    assert is_teenager(13)==True
    assert is_teenager(14)==True
    assert is_teenager(15)==True
    assert is_teenager(16)==True
    assert is_teenager(17)==True
    assert is_teenager(18)==True
    assert is_teenager(19)==True
