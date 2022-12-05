import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def tests_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def tests_division_calculate_correctly(self):
        assert self.calc.division(self, 5, 1) == 5

    def tests_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 4, 2) == 2

    def tests_adding_calculate_correctly(self):
        assert self.calc.adding(self, 1, 1) == 2
