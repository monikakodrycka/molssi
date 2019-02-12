"""
Unit and regression test for the molssi_devops_2019 package.
"""

# Import package, test suite, and other packages as needed
import molssi_devops_2019 as md
import pytest
import sys


@pytest.mark.skip
def test_mean():
    num_list = [1, 2, 3, 4, 5]
    observed = md.mean(num_list)
    expected = 3

    assert observed == expected 


def test_mean_type_error():
    test_variable = ['this is a string']
	
    with pytest.raises(TypeError):
        md.mean(test_variable)

def test_zero_length():
    test_list = []
    
    with pytest.raises(ZeroDivisionError):
        md.mean(test_list)
	 
