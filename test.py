import pytest
from _pytest import monkeypatch
from CoffeeMachine import CoffeeMachine


def test_is_coin_enough_false(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1 quarters")
    coffee_machine = CoffeeMachine()
    assert coffee_machine.is_coin_enough("espresso") is False


def test_is_coin_enough_exact_change(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "4 quarters, 5 dimes")
    coffee_machine = CoffeeMachine()
    assert coffee_machine.is_coin_enough("espresso") is True


def test_is_coin_enough_surplus_change(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "4 quarters, 7 dimes")
    coffee_machine = CoffeeMachine()
    assert coffee_machine.is_coin_enough("espresso") is True


def test_is_resources_enough_false(monkeypatch):
    coffee_machine = CoffeeMachine()
    coffee_machine.resources = dict(water=0, milk=0, coffee=0, profit=0)
    assert coffee_machine.is_resources_enough("latte") is False


def test_is_resources_enough_true(monkeypatch):
    coffee_machine = CoffeeMachine()
    coffee_machine.resources = dict(water=300, milk=1200, coffee=240, profit=0)
    assert coffee_machine.is_resources_enough("latte") is True
