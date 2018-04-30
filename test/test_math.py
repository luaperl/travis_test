import sys

sys.path.insert(0, './')
import pytest
import ngh_func.math as m

@pytest.fixture
def num():
	return -10

@pytest.fixture
def num_list():
	return -1, -2, 3, 4

def test_abs(num):
	assert m.abs(num) == 10

def test_inc(num):
	assert m.inc(num) == -9

def test_sum1(num_list):
	assert m.abs_sum(*num_list) == 10

def test_sum2(num_list):
	assert m.abs_inc_sum(*num_list) == 14
