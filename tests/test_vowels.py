import pytest
import programs.vowels as pv

def test_vowels():
    assert pv.vowels("Hello World!") == 3