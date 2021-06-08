import pytest
import programs.factorial as pf

def test_fact():
    assert pf.fact(0) == 1

def test_fact():
    assert pf.fact(5) == 120