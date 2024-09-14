import pytest,os,sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from calculator import sumar, restar

def test_sumar():
    assert sumar(2,3)==5
    assert sumar(3,-8)==-5
    assert sumar(-33,-66)==-99

def test_restar():
    assert restar(8,6)==2
    assert restar(-8,3)==-11
    assert restar(-5,-8)==3
