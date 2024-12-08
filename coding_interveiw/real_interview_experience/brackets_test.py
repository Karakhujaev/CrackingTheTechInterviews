from brackets import is_properly
import pytest

def test_is_properly_valid_cases():
    assert is_properly("") == True
    assert is_properly("()") == True
    assert is_properly("()[]{}") == True
    assert is_properly("{[()]}") == True
    assert is_properly("((()))") == True
    assert is_properly("[[[]]]") == True

def test_is_properly_invalid_cases():
    assert is_properly("(") == False
    assert is_properly("}") == False
    assert is_properly("[(])") == False
    assert is_properly("[({)}]") == False
    assert is_properly("[") == False
    assert is_properly("]") == False
    assert is_properly("[)") == False

def test_is_properly_mixed_cases():
    assert is_properly("{[()]}(") == False
    assert is_properly("[{()}") == False
    assert is_properly("({)}") == False
    assert is_properly("[[[()]]") == False

def test_is_properly_complex_cases():
    assert is_properly("{{[[(())]]}}") == True
    assert is_properly("{()}[()]") == True
    assert is_properly("[({})]") == True
    assert is_properly("[({}}") == False

def test_is_properly_edge_cases():
    assert is_properly("}") == False
    assert is_properly("()(") == False
    assert is_properly("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[") == False
