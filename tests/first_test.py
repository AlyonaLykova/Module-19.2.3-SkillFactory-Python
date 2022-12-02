import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(2, 2)

    def test_division_calculate_correctly(self):
        assert self.calc.division(9, 3)

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(9, 4)

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(5, 5)