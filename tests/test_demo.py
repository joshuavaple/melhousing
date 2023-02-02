import melhousing
from melhousing.constants.myconstants import constant1, constant2
from melhousing.constants.filepaths import demopath
from melhousing.classes import housingdata as hd


def test_constants():
    assert constant1 != None
    assert constant2 != None

def test_filepaths():
    assert demopath != None

def test_housingdata():
    # output = hd.say_hello() 
    # expected = None
    assert hd.say_hello() != None

