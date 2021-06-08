import pytest
import programs.squares as ps

def test_squares():
    assert ps.list_of_squares(8) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8:64}
    