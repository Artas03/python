import pytest
import programs.count as pc

def test_count_zeros():
    assert pc.count([0,0,0], 0) == 3

def test_count_string():
    assert pc.count(["a","a","a"], "a") == 3