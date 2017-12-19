import pytest
from minimum_three_mpy import minimum_three_mpy

def test_1():
	assert minimum_three_mpy(1,2,3,4,5,6) == 6
def test_2():
	assert minimum_three_mpy(-1,2,3,4,5,6) == -30
def test_3():
	assert minimum_three_mpy(1,2) == None
def test_4():
	assert minimum_three_mpy("1,2,3,4,5,6") == None