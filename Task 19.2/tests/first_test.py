import pytest
from app.calculator import Calculator

class TestCals:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculator_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculator_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_division_calculator_correctly(self):
        assert self.calc.division(self, 2, 2) == 1

    def test_subtraction_calculator_correctly(self):
        assert self.calc.subtraction(self, 2, 2) == 0

    def test_adding_calculator_correctly(self):
        assert self.calc.adding(self, 2, 2) == 4