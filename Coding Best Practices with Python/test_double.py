import pytest
from double import double

def test_double():
    assert double(2.) == 4

def test_raises():
	with pytest.raises(TypeError):
		double('2')