from melhousing.constants.myconstants import constant1, constant2
from melhousing.constants.filepaths import demopath
from melhousing.classes import housingdata as hd


def test_constants():
    assert constant1 == 'constant1 says hello'
    assert constant2 == 123

def test_filepaths():
    assert demopath == 'filepaths.py says hello'

def test_housingdata():
    assert hd.say_hello() == 'housingdata says hello!'

if __name__ == '__main__':
    test_constants()
    test_filepaths()
    test_housingdata()

