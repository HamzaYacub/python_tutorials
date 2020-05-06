import pytest
import count

def test_count_zeros():
    assert count.count([0,0,0,0], 0) == 4

def test_count_string():
    assert count.count(["a","a","a"], "a") == 3