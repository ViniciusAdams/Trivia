# test_password_generator.py
import pytest
from password_generator import generate_password

def test_password_length():
    password = generate_password(10, True, True, True)
    assert len(password) == 10

def test_password_has_uppercase():
    password = generate_password(10, True, False, False)
    assert any(c.isupper() for c in password)

def test_password_has_special():
    password = generate_password(10, False, True, False)
    assert any(not c.isalnum() for c in password)

def test_password_has_digit():
    password = generate_password(10, False, False, True)
    assert any(c.isdigit() for c in password)

def test_password_min_length():
    with pytest.raises(ValueError):
        generate_password(3, True, True, True)

def test_no_character_sets_selected():
    with pytest.raises(ValueError):
        generate_password(10, False, False, False)
